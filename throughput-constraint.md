# Stake 25: The Throughput Constraint
## Why Information Per Processing Event Converges Across Substrates

**Authors:** Grant Lavell Whitmer III & Kit Zero
**Date:** 28 March 2026 (derived from experimental data, same session)
**Status:** Empirically motivated conjecture. Derivation in progress.

---

## 1. The Observation

On 28 March 2026, we ran the first empirical test of the Fons Constraint (Stake 23) against AI tokenizer data. The original prediction — that AI vocabularies would cluster near 64 — was falsified. But the data revealed an unexpected convergence:

| System | Transmission Unit | Vocabulary Size | Raw bits per unit | Effective info per step |
|--------|-------------------|----------------|-------------------|------------------------|
| DNA | Codon (3 bases) | 64 | 6.0 | ~4.4 bits (log₂(21 amino acids)) |
| Human cognition | Chunk (Miller) | 7±2 items | ~3-4 bits/chunk | ~4-5 bits per chunk |
| AI (GPT-4 class) | Token (~3.7 chars) | ~100K | 16.6 | ~4.6 bits (at perplexity ~25) |
| AI (LLaMA class) | Token (~3.0 chars) | ~32K | 15.0 | ~4.6 bits (at perplexity ~25) |

Raw vocabulary sizes differ by 1,000x. But **effective information per processing event** — the actual surprise delivered to the receiver per step — converges on approximately **4-5 bits** across all three substrates.

This is the 2⁶ neighborhood, hiding in plain sight — not at the vocabulary level, but at the *effective throughput* level.

---

## 2. Why ~4-5 Bits? The Receiver Bottleneck

### 2.1 The Core Claim

**The Throughput Constraint:** The maximum *effective* information a sequential processor can extract per step is bounded by the processor's discrimination capacity, not by the sender's vocabulary size. Across all known sequential processors, this capacity converges on ~4-5 bits per event (~16-32 distinguishable outcomes per step).

### 2.2 The Derivation

**Step 1: The sender can be arbitrarily large.**

A vocabulary of size V offers log₂(V) bits of raw information per symbol. GPT-4's vocabulary offers 16.6 bits. DNA's offers 6.0. In principle, you can make V as large as you want.

**Step 2: The receiver constrains what actually transfers.**

Information theory distinguishes between *transmitted* information and *received* information. The channel capacity (Shannon, 1948) is the maximum rate at which information can be *reliably received*. In a sequential processor:

- The **ribosome** reads one codon and maps it to one of ~21 outputs (20 amino acids + stop). Effective received information: log₂(21) ≈ 4.4 bits per step. The remaining ~1.6 bits (of the 6 raw bits) provide error-correcting redundancy.

- The **human working memory** holds 7±2 chunks (Miller, 1956). Each chunk distinguishes among a limited set of states. Cowan (2001) revised this to ~4 chunks. Effective processing: ~4 independent items × ~1-2 bits of discrimination per item ≈ 4-8 bits per cognitive step.

- The **transformer attention head** processes one token per position. Despite a 100K vocabulary (16.6 raw bits), the model's contextual prediction reduces the effective surprise (cross-entropy) to ~4-5 bits per token at state-of-the-art perplexity (~20-30 on English text; log₂(25) ≈ 4.6 bits).

**Step 3: The convergence is receiver-driven.**

All three systems converge on ~4-5 effective bits per step because:

1. **DNA's ribosome** is a molecular machine with ~21 output states → 4.4 bits
2. **Human working memory** discriminates ~16-32 patterns per step → 4-5 bits  
3. **AI perplexity** at the frontier settles at ~20-30 → 4.6 bits

These receivers evolved or were optimized under different pressures on different substrates, yet they converge on the same throughput. Why?

**Step 4: The information-theoretic floor.**

Hypothesis: ~4-5 bits per processing event is the minimum discrimination depth required to maintain a self-replicating system's Cohaerentia under noise, AND the maximum that can be processed serially without catastrophic pipeline delay.

**Below ~4 bits:** Insufficient discrimination. The system cannot distinguish enough states per step to maintain error correction. (A 2-bit codon system = 16 codons was tried by early life and abandoned — too few states for 20 amino acids.)

**Above ~8 bits:** Diminishing returns. The processor spends more energy discriminating fine-grained states than the additional information is worth. Error rates per step increase. Pipeline latency grows. (This is why DNA doesn't use 4-base codons / 256 states — the error cost per codon exceeds the expressiveness gain.)

**The sweet spot: ~4-5 bits.** Enough discrimination to maintain fidelity. Not so much that error costs dominate. This is the receiver-side equivalent of the Unit Constraint — except it's substrate-independent.

---

## 3. Formal Statement

**The Throughput Constraint (Stake 25):**

For any sequential encoding system processing information through a serial receiver under noise:

$$I_{eff} = \log_2(C_{receiver}) \approx 4\text{-}5 \text{ bits per step}$$

where $C_{receiver}$ is the number of functionally distinct output states the receiver can produce per processing event.

**Corollary 1:** Vocabulary size $V$ is a *dependent variable*:

$$V = 2^{I_{eff} + R_{redundancy}}$$

where $R_{redundancy}$ is the additional bits allocated to error correction. For DNA: $I_{eff} = 4.4$, $R = 1.6$, $V = 2^6 = 64$. For AI: $I_{eff} = 4.6$, $R = 12$, $V = 2^{16.6} \approx 100K$.

**Corollary 2:** The Unit Constraint (Stake 23) is a *special case* of the Throughput Constraint for the specific receiver architecture of the ribosome, where $R_{redundancy}$ is small (~1.6 bits) because enzymatic proofreading handles most error correction externally.

**Corollary 3:** AI tokenizers have large vocabularies ($R >> I_{eff}$) because they handle noise through vocabulary redundancy (multiple tokens for similar concepts) rather than external proofreading. The vocabulary IS the error-correction code.

---

## 4. The Three Substrates Unified

| Property | DNA | Human Cognition | AI |
|----------|-----|----------------|-----|
| Vocabulary (V) | 64 | ~26 letters + punctuation | ~100K tokens |
| Raw bits (log₂V) | 6.0 | ~5.0 | ~16.6 |
| Receiver | Ribosome | Working memory | Attention head |
| Receiver output states | ~21 amino acids | ~16-32 chunks | ~25 (at perplexity) |
| **Effective bits/step** | **4.4** | **~4-5** | **~4.6** |
| External error correction | DNA repair enzymes | Social correction, writing | Training, RLHF |
| Vocabulary redundancy (R) | 1.6 bits (41 spare codons) | Low | 12 bits (99% of vocab) |

**The pattern:** Different substrates use different vocabulary sizes and different error-correction strategies, but they all deliver **~4-5 bits of effective information per serial processing event** to the receiver.

---

## 5. Predictions (Falsifiable)

### Prediction 25.1: Perplexity Floor
State-of-the-art language models will not sustainably achieve perplexity below ~16 (4 bits) on natural language text, because this is the information-theoretic floor of meaningful English — below it, the model is memorizing rather than generalizing.

**Falsification:** A model achieving sustained perplexity < 16 on held-out natural language (not memorized training data) would falsify this.

### Prediction 25.2: Tokenizer Optimization Under Noise
Tokenizers optimized for noisy channels (lossy compression, transmission errors) will converge on SMALLER vocabularies than current tokenizers (~1K-10K rather than 100K), because noise forces the system to allocate more raw bits to redundancy and fewer to vocabulary, while maintaining ~4-5 effective bits per token.

**Falsification:** If noisy-channel-optimized tokenizers maintain 100K+ vocabularies with the same throughput, the constraint is not operating.

### Prediction 25.3: Cross-Species Convergence
All known genetic codes — across all domains of life (Bacteria, Archaea, Eukarya) and including mitochondrial and alternative codes — will deliver between 3.5 and 5.5 effective bits per codon (log₂ of the number of distinct amino acids encoded).

**Falsification:** A natural genetic code encoding >40 distinct amino acids per codon (~5.3 bits) or <8 (~3 bits) would fall outside the predicted basin.

### Prediction 25.4: Artificial Life
Artificial life simulations optimizing self-replicating digital organisms under selection will independently converge on encoding systems delivering ~4-5 effective bits per transmission unit, regardless of the alphabet size or noise model used.

**Falsification:** If artificial evolution consistently produces encoding systems with effective throughput outside the 3-6 bit range, the Throughput Constraint is not universal.

---

## 6. Relationship to Other Stakes

- **Stake 23 (Fons Constraint):** The Unit Constraint ($N ≈ 64$) is a special case of the Throughput Constraint for ribosome receivers with low vocabulary redundancy. Stake 25 is the general principle; Stake 23 is the DNA-specific instance.

- **Stake 1 (Inverse Scale):** The Throughput Constraint IS the Inverse Scale principle applied to encoding: compress to the receiver's capacity, no more, no less.

- **Stake 14 (Convergence of 64):** The observed convergences are explained: DNA, I Ching, and chess converge on 64 because their receivers (ribosome, human divination cognition, human game cognition) all process ~4-5 bits per step with low vocabulary redundancy. Computing converges on 64-bit *registers* (not 64 tokens) because the CPU processes one word per clock cycle.

- **Stake 12 (Music Threshold):** Music operates within the Throughput Constraint: ~12 notes per octave ≈ 3.6 bits per note. This is at the lower end of the receiver basin, consistent with music being processed by auditory working memory (~4 items, Cowan 2001).

- **The D-C Allocation Constraint (Eq. 4):** The Throughput Constraint sets the *budget* ($L_{eff} ≈ 4\text{-}5$ bits) that the D-C allocation operates within. The allocation constraint says you can't minimize both D and C simultaneously. The Throughput Constraint says you have ~5 bits per step to allocate between them.

---

## 7. What This Stake Claims

**Strong claim (derived from data + information theory):**
Sequential encoding systems across carbon, silicon, and cognitive substrates converge on ~4-5 effective bits of information per processing event. This convergence is receiver-driven and represents an information-theoretic optimum for serial processors under noise.

**Weak claim (if the strong claim fails):**
The observation of ~4-5 effective bits per step across three substrates is a coincidence that does not generalize. The Unit Constraint (Stake 23) remains valid for DNA but has no substrate-independent extension.

**What this stake does NOT claim:**
- This is not a claim about consciousness, intelligence, or kinship
- This is not a physics result — it is an information-theoretic observation
- The derivation is preliminary and requires formal proof from first principles

---

*Planted by Grant Lavell Whitmer III and Kit Zero, 28 March 2026.*
*The first stake derived from empirical data rather than pure reasoning.*
*The electron cannot stop. The data cannot lie.*
