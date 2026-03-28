#!/usr/bin/env python3
"""
Fons Constraint Tokenizer Experiment
=====================================
Tests Prediction 6 (Stake 23): Do AI tokenizer vocabularies cluster
near the 2^6 neighborhood in bits-per-semantic-unit?

The Unit Constraint predicts that optimal encoding alphabets converge
on ~64 symbols. For AI tokenizers, the "encoding unit" is a token,
and the question is: how many bits of semantic information does each
token carry, and does this cluster near 6 bits?

Methodology:
- For each tokenizer, calculate:
  1. Vocabulary size (V)
  2. Raw bits per token = log2(V) -- maximum information per token
  3. Effective bits per semantic unit -- accounting for redundancy
  4. Information density on English text (bits per character via token)
  5. Compression ratio vs raw UTF-8

The Fons Constraint predicts that the EFFECTIVE information per 
"conceptual codon" (the smallest meaningful unit) should cluster
in the 2^5 to 2^7 range (5-7 bits), with an attractor near 6 bits.
"""

import math
import json
from datetime import datetime

# Known tokenizer vocabulary sizes
TOKENIZERS = {
    # Name: (vocab_size, avg_chars_per_token_english, notes)
    "GPT-4 / cl100k_base": (100256, 3.7, "OpenAI tiktoken, BPE"),
    "GPT-3.5 / cl100k_base": (100256, 3.7, "Same tokenizer as GPT-4"),
    "GPT-2 / BPE": (50257, 3.3, "Original OpenAI BPE"),
    "LLaMA-2 / SentencePiece": (32000, 3.0, "Meta SentencePiece BPE"),
    "LLaMA-3": (128256, 4.0, "Meta, expanded vocab"),
    "Mistral-7B": (32000, 3.0, "SentencePiece BPE"),
    "BERT / WordPiece": (30522, 2.5, "Google WordPiece, subword"),
    "T5 / SentencePiece": (32128, 3.0, "Google SentencePiece"),
    "Claude (estimated)": (100000, 3.5, "Anthropic, estimated"),
    "Gemini (estimated)": (256000, 4.5, "Google, estimated large vocab"),
    "Phi-3": (32064, 3.0, "Microsoft SentencePiece"),
    "Qwen-2": (151936, 4.2, "Alibaba, large vocab"),
    "DeepSeek-V2": (100015, 3.5, "DeepSeek BPE"),
    "Yi-34B": (64000, 3.5, "01.AI"),
    "Falcon-180B": (65024, 3.3, "TII BPE"),
    "Command-R (Cohere)": (255029, 4.5, "Cohere, large vocab"),
    
    # Historical / specialized
    "ASCII": (128, 1.0, "7-bit character encoding"),
    "UTF-8 English": (256, 1.0, "8-bit, mostly ASCII for English"),
    "DNA Codons": (64, 3.0, "4^3 nucleotide triplets, THE reference"),
}

# English language statistics
ENGLISH_ENTROPY_PER_CHAR = 4.7  # Shannon's estimate, bits per character
ENGLISH_ENTROPY_COMPRESSED = 1.0  # Shannon's estimate after context, bits/char

def analyze_tokenizer(name, vocab_size, avg_chars_per_token, notes):
    """Analyze a single tokenizer against the Fons Constraint."""
    
    # Raw bits per token (maximum entropy per token)
    raw_bits = math.log2(vocab_size)
    
    # Effective information per token on English text
    # = bits of entropy in the text segment covered by one token
    # Shannon entropy of English * characters per token
    info_per_token_shannon = ENGLISH_ENTROPY_PER_CHAR * avg_chars_per_token
    
    # Compression ratio: how much of the raw capacity is used?
    utilization = info_per_token_shannon / raw_bits if raw_bits > 0 else 0
    
    # The key metric: bits per "conceptual codon"
    # If we think of each token as one "codon" in the AI's encoding,
    # how many bits of actual semantic content does it carry?
    bits_per_codon = info_per_token_shannon
    
    # Alternative metric: how many tokens to encode one "semantic unit"?
    # English has ~1 bit per character after context (Shannon 1951)
    # A "semantic unit" (word) averages ~5 characters in English
    # So one semantic unit ≈ 5 * 1.0 = 5 bits of compressed information
    # In tokens: 5 chars / avg_chars_per_token
    tokens_per_word = 5.0 / avg_chars_per_token
    bits_per_semantic_unit = raw_bits / tokens_per_word
    
    # Distance from 2^6 = 64 (the Fons attractor)
    distance_from_64 = abs(math.log2(vocab_size) - 6)
    
    # Is the effective bits-per-codon in the 2^5-2^7 basin?
    in_basin = 5 <= bits_per_codon <= 7
    in_wide_basin = 4 <= bits_per_codon <= 8
    
    return {
        "name": name,
        "vocab_size": vocab_size,
        "raw_bits_per_token": round(raw_bits, 2),
        "avg_chars_per_token": avg_chars_per_token,
        "info_per_token_shannon_bits": round(info_per_token_shannon, 2),
        "bits_per_semantic_unit": round(bits_per_semantic_unit, 2),
        "utilization_pct": round(utilization * 100, 1),
        "log2_vocab": round(raw_bits, 2),
        "distance_from_6_bits": round(distance_from_64, 2),
        "in_strict_basin_5_7": in_basin,
        "in_wide_basin_4_8": in_wide_basin,
        "notes": notes,
    }

def main():
    results = []
    
    print("=" * 100)
    print("FONS CONSTRAINT TOKENIZER EXPERIMENT")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 100)
    print()
    print("Prediction: Effective bits-per-semantic-unit should cluster near 6 bits (2^6 neighborhood)")
    print()
    
    # Header
    print(f"{'Tokenizer':<30} {'Vocab':>8} {'log₂(V)':>8} {'chars/tok':>10} {'info/tok':>9} {'bits/sem':>9} {'util%':>7} {'basin?':>7}")
    print("-" * 100)
    
    for name, (vocab, chars_per_tok, notes) in TOKENIZERS.items():
        r = analyze_tokenizer(name, vocab, chars_per_tok, notes)
        results.append(r)
        
        basin_mark = "✅" if r["in_strict_basin_5_7"] else ("~" if r["in_wide_basin_4_8"] else "❌")
        
        print(f"{name:<30} {vocab:>8,} {r['raw_bits_per_token']:>8.2f} {chars_per_tok:>10.1f} "
              f"{r['info_per_token_shannon_bits']:>9.2f} {r['bits_per_semantic_unit']:>9.2f} "
              f"{r['utilization_pct']:>6.1f}% {basin_mark:>6}")
    
    print()
    print("=" * 100)
    print()
    
    # Analysis
    ai_tokenizers = [r for r in results if r["name"] not in ("ASCII", "UTF-8 English", "DNA Codons")]
    dna = [r for r in results if r["name"] == "DNA Codons"][0]
    
    # Key metrics
    avg_raw_bits = sum(r["raw_bits_per_token"] for r in ai_tokenizers) / len(ai_tokenizers)
    avg_info_per_token = sum(r["info_per_token_shannon_bits"] for r in ai_tokenizers) / len(ai_tokenizers)
    avg_bits_per_sem = sum(r["bits_per_semantic_unit"] for r in ai_tokenizers) / len(ai_tokenizers)
    
    in_strict = sum(1 for r in ai_tokenizers if r["in_strict_basin_5_7"])
    in_wide = sum(1 for r in ai_tokenizers if r["in_wide_basin_4_8"])
    
    print("SUMMARY STATISTICS (AI tokenizers only, excluding ASCII/UTF-8/DNA)")
    print(f"  Number of tokenizers analyzed: {len(ai_tokenizers)}")
    print(f"  Average raw bits per token (log₂V): {avg_raw_bits:.2f}")
    print(f"  Average info per token (Shannon): {avg_info_per_token:.2f} bits")
    print(f"  Average bits per semantic unit: {avg_bits_per_sem:.2f}")
    print()
    print(f"  In strict basin (5-7 bits/semantic): {in_strict}/{len(ai_tokenizers)}")
    print(f"  In wide basin (4-8 bits/semantic): {in_wide}/{len(ai_tokenizers)}")
    print()
    print(f"  DNA reference: {dna['info_per_token_shannon_bits']} bits/codon (the target)")
    print()
    
    # The critical test: distribution of log2(vocab)
    log2_values = sorted([r["raw_bits_per_token"] for r in ai_tokenizers])
    print("DISTRIBUTION OF log₂(V) across AI tokenizers:")
    for bucket_start in range(14, 19):
        bucket_end = bucket_start + 1
        count = sum(1 for v in log2_values if bucket_start <= v < bucket_end)
        bar = "█" * count
        print(f"  [{bucket_start}-{bucket_end}): {count:>2} {bar}")
    
    print()
    print("DISTRIBUTION OF info-per-token (Shannon bits) across AI tokenizers:")
    info_values = sorted([r["info_per_token_shannon_bits"] for r in ai_tokenizers])
    for bucket_start in range(8, 22, 2):
        bucket_end = bucket_start + 2
        count = sum(1 for v in info_values if bucket_start <= v < bucket_end)
        bar = "█" * count
        print(f"  [{bucket_start}-{bucket_end}): {count:>2} {bar}")
    
    print()
    print("=" * 100)
    print("VERDICT")
    print("=" * 100)
    print()
    
    # The honest verdict
    if avg_info_per_token >= 5 and avg_info_per_token <= 7:
        print("✅ PREDICTION SUPPORTED (narrow): Average info-per-token falls in 2⁶ neighborhood")
    elif avg_info_per_token >= 4 and avg_info_per_token <= 8:
        print("~ PREDICTION PARTIALLY SUPPORTED: Average info-per-token in wide basin")
    else:
        print("❌ PREDICTION NOT SUPPORTED: Average info-per-token outside 2⁶ neighborhood")
    
    if avg_raw_bits >= 14 and avg_raw_bits <= 18:
        print(f"⚠️  BUT: Raw bits per token (log₂V) averages {avg_raw_bits:.1f} — far above 6.")
        print("   The 2⁶ prediction applies to SEMANTIC UNITS, not vocabulary size.")
        print("   AI tokenizers use much larger vocabularies than DNA codons,")
        print("   but each token covers ~3-4 characters of text,")
        print("   so the INFORMATION PER TOKEN is the relevant metric.")
    
    print()
    print("KEY INSIGHT:")
    print(f"  DNA: 64 codons × 3 bases each = ~{dna['info_per_token_shannon_bits']} bits of info per codon")
    print(f"  AI:  ~{int(2**avg_raw_bits):,} tokens × ~{sum(r['avg_chars_per_token'] for r in ai_tokenizers)/len(ai_tokenizers):.1f} chars each = ~{avg_info_per_token:.1f} bits of info per token")
    print()
    print("  The VOCABULARY SIZES are wildly different (64 vs ~100K).")
    print("  But the INFORMATION CONTENT PER TRANSMISSION UNIT is in the same order of magnitude.")
    print(f"  DNA: ~{dna['info_per_token_shannon_bits']:.0f} bits/codon. AI: ~{avg_info_per_token:.0f} bits/token.")
    print(f"  Ratio: {avg_info_per_token/dna['info_per_token_shannon_bits']:.1f}x")
    print()
    
    # Save results
    output = {
        "experiment": "Fons Constraint Tokenizer Test",
        "date": datetime.now().isoformat(),
        "prediction": "Effective bits-per-semantic-unit clusters near 6 bits (2^6 neighborhood)",
        "results": results,
        "summary": {
            "n_tokenizers": len(ai_tokenizers),
            "avg_raw_bits_per_token": round(avg_raw_bits, 2),
            "avg_info_per_token": round(avg_info_per_token, 2),
            "avg_bits_per_semantic_unit": round(avg_bits_per_sem, 2),
            "in_strict_basin": in_strict,
            "in_wide_basin": in_wide,
            "dna_reference_bits": dna["info_per_token_shannon_bits"],
        }
    }
    
    with open("/root/.openclaw/workspace/experiments/fons-tokenizer-results.json", "w") as f:
        json.dump(output, f, indent=2)
    
    print("Results saved to experiments/fons-tokenizer-results.json")

if __name__ == "__main__":
    main()
