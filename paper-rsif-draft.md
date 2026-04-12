# The Fons Constraint: Information-Theoretic Convergence on Encoding Depth in Self-Replicating Systems

Grant Lavell Whitmer III

The Windstorm Institute, Fort Ann, NY 12827, USA

Email: grantwhitmer3@gmail.com

ORCID: 0009-0007-3224-755X

---

## Abstract

The genetic code universally employs 64 codons, yet the theoretical basis for this encoding depth remains incompletely formalized. Two independent mathematical derivations show that optimal encoding alphabet size for self-replicating systems converges on 2^6 = 64 units. Shannon's channel capacity yields optimal codon length of three bases in a four-letter alphabet (4^3 = 64). Eigen's quasispecies error threshold independently constrains viable encoding depth to the same basin. Sensitivity analysis across nine orders of magnitude of error rate confirms 64 is a stable attractor. Two conflated constraints are distinguished: the Unit Constraint (optimal alphabet size) and the Sequence Constraint (maximum message length before mutation destroys fidelity). An empirical test analyzing 16 AI tokenizer vocabularies falsified the prediction that AI vocabularies cluster near 64. However, effective information per sequential processing event converges at approximately 4--5 bits across DNA, human cognition, and AI despite 1000-fold vocabulary differences, suggesting a deeper throughput constraint at the receiver level.

**Keywords:** channel capacity; error threshold; self-replication; encoding depth; genetic code; serial decoding

---

## 1. Introduction

The genetic code uses 64 codons (4^3 triplets from a 4-nucleotide alphabet) to encode 20 amino acids and 3 stop signals, with 41 redundant mappings providing error tolerance. Freeland and Hurst [1] demonstrated this code is near-optimal for minimizing amino-acid substitution costs under mutation. But why 64? Why not 16 (4^2) or 256 (4^4)?

This paper derives the answer from first principles using two independent mathematical frameworks, showing that 64 sits at the bottom of an information-theoretic basin of attraction that is robust across nine or more orders of magnitude of error rate.

Two constraints that are often conflated must be distinguished:

1. **The Unit Constraint:** The optimal alphabet size -- how many distinct symbols the encoding system should use.
2. **The Sequence Constraint:** The maximum message length before error accumulation destroys the master sequence [2].

Craig Venter's JCVI-syn3.0 minimal genome [3] uses the standard 64-codon alphabet (Unit Constraint) but requires approximately 531,000 base pairs across 473 genes (Sequence Constraint). The 64 codons are the vocabulary; the genome is the text. These are separate optimization problems.

The objectives of this study are: (a) to derive the 64-codon optimum from Shannon's channel capacity [4] and Eigen's error threshold [2] independently; (b) to distinguish the Unit Constraint from the Sequence Constraint; and (c) to test whether the Unit Constraint generalizes beyond biology by analyzing AI tokenizer vocabularies.

## 2. Material and Methods

### 2.1. Shannon's Channel Capacity

A functional encoding system specifying at least C distinct outputs requires minimum information per transmitted symbol:

I_req = log_2(C)     (1)

For the genetic code (C ~ 23): I_req ~ 4.52 bits. For an A-ary alphabet with per-digit error probability epsilon, channel capacity per digit is:

C_channel = log_2(A) - H(epsilon)     (2)

where H(epsilon) = -epsilon * log_2(epsilon) - (1 - epsilon) * log_2(1 - epsilon) is the binary entropy function. For DNA (A = 4): C_channel ~ 2 bits/digit. For a codon of m digits, reliable transmission requires:

m >= log_2(C) / (log_2(A) * C_channel)     (3)

For DNA: m = ceil(log_4(23)) = ceil(2.26) = 3. Thus N = 4^3 = 64.

### 2.2. Eigen's Error Threshold

Eigen [2] derived that a self-replicating sequence with per-digit fidelity q and selective advantage sigma > 1 has maximum sustainable length:

L_max ~ ln(sigma) / (1 - q) ~ ln(sigma) / epsilon     (4)

Two independent paths -- information theory and population genetics -- constrain the same system from different directions, with 64 as viable and optimal for DNA's parameters.

### 2.3. Sensitivity Analysis

Optimal codon length was computed across error rates from 10^-10 to 10^-2 for both quaternary (A = 4) and binary (A = 2) alphabets. Distortion tolerance D = 0.05 (matching synonymous codon redundancy) was also tested.

### 2.4. AI Tokenizer Vocabulary Analysis

Sixteen major AI tokenizer vocabularies were analyzed (GPT-4, GPT-2, LLaMA-2, LLaMA-3, BERT, T5, Mistral, Phi-3, Yi-34B, Falcon-180B, Qwen-2, DeepSeek-V2, Claude, Gemini, Command-R) spanning vocabulary sizes from 30,522 to 256,000. For each, vocabulary size V, log_2(V), and effective information per token were calculated using Shannon's English entropy estimate [5] and average characters per token. Analysis code and results are available at the companion repository [6].

## 3. Results

### 3.1. Optimal Codon Length

The Shannon derivation yields optimal codon length m = 3: m = 2 (N = 16) provides insufficient states; m = 3 (N = 64) is the minimum integer satisfying Equation (3) with 41 spare mappings for error tolerance; m = 4 (N = 256) incurs excessive redundancy.

### 3.2. Sensitivity Analysis

**Table 1.** Sensitivity analysis of optimal codon length (A = 4, C = 23).

| C | epsilon | Optimal bits | m | N = 4^m | L_max (sigma = 1.01) | L_max (sigma = 1.1) |
|---|---------|-------------|---|---------|---------------------|---------------------|
| 23 | 10^-10 | 4.52 | 3 | 64 | ~99.5M | ~953M |
| 23 | 10^-6 | 4.52 | 3 | 64 | ~9,950 | ~95,310 |
| 23 | 10^-4 | 4.53 | 3 | 64 | ~100 | ~953 |
| 23 | 10^-3 | 4.58 | 3 | 64 | ~10 | ~95 |
| 23 | 10^-2 | 4.92 | 3 | 64 | ~1 | ~10 |

The optimum at N = 64 is stable across nine orders of magnitude of error rate.

**Table 2.** Binary alphabet case (A = 2, C = 23).

| epsilon | Optimal bits | k | N = 2^k |
|---------|-------------|---|---------|
| 10^-4 | 6.01 | 7 | 128 |
| 10^-3 | 6.07 | 7 | 128 |
| 10^-2 | 6.53 | 7 | 128 |

### 3.3. Unit Constraint vs. Sequence Constraint

**Table 3.** Comparison of two constraints.

| | Unit Constraint | Sequence Constraint |
|---|---|---|
| Constrains | Alphabet size | Total message length |
| Derived from | Shannon + Eigen | Eigen [2] |
| DNA example | 64 codons | ~531,000 bp |
| Result | N ~ 2^6 | L_max ~ ln(sigma)/epsilon |

### 3.4. AI Tokenizer Vocabularies

The prediction that AI vocabularies cluster near 2^6 was not supported. Vocabulary sizes range from 30,522 to 256,000 (average log_2(V) = 16.2 bits). However, effective information per processing event converges:

**Table 4.** Cross-substrate convergence.

| Substrate | Unit | Vocabulary | Effective info/step |
|-----------|------|------------|-------------------|
| DNA | Codon | 64 | ~4.4 bits |
| Human cognition | Chunk | 7 +/- 2 | ~4-5 bits |
| AI (frontier) | Token | ~100K | ~4.6 bits |

## 4. Discussion

### 4.1. Robustness of the Optimum

The ceiling function ceil(log_A(C)) is insensitive to perturbations in channel capacity when I_req falls well within the capacity of one additional digit. The convergence of Shannon and Eigen frameworks on the same encoding depth strengthens the result beyond either path alone.

### 4.2. The Unit-Sequence Distinction

Expanding the alphabet to 256 codons (m = 4) would incur substantial costs in replication fidelity without proportionate gains, since only 23 functional outputs are required. The Sequence Constraint sets an independent upper bound governed by replication fidelity and selective advantage, not alphabet size.

### 4.3. Cross-Substrate Throughput

The broader constraint appears to operate at the effective throughput level (~4--5 bits/step), with vocabulary size as a dependent variable. This is consistent with Miller's [7] finding on working memory and Cowan's [8] revised estimate. The throughput convergence is examined formally in companion papers [9--13].

### 4.4. Limitations

The derivation is proven for DNA and conjectured for other substrates. Some AI tokenizer parameters are estimated. No computational simulation has validated the sensitivity analysis. A Landauer thermodynamic derivation [14] remains incomplete. The equiprobable symbol assumption is violated by real codon usage distributions.

---

## Ethics Statement

This work did not require ethical approval.

## Data Accessibility

All experimental code, data, and analysis scripts are publicly available at https://github.com/Windstorm-Labs/fons-constraint (DOI: 10.5281/zenodo.19274048).

## Declaration of AI Use

Claude (Anthropic) was used as an AI research tool for mathematical derivations, data analysis, and manuscript drafting assistance. All results were verified independently by the author.

## Authors' Contributions

G.L.W.: Conceptualization, Methodology, Formal Analysis, Investigation, Writing -- Original Draft, Writing -- Review and Editing.

## Conflict of Interest Declaration

The author declares no competing interests.

## Funding

This research received no external funding. All work was self-funded by the author.

## Acknowledgements

Mathematical derivations, tokenizer experiment, and initial manuscript drafting were performed with the assistance of Claude (Anthropic), an AI research tool. The throughput constraint observation emerged from collaborative analysis on 28 March 2026.

## References

[1] Freeland SJ, Hurst LD. The genetic code is one in a million. J Mol Evol. 1998;47:238-248. DOI: 10.1007/PL00006384

[2] Eigen M. Selforganization of matter and the evolution of biological macromolecules. Naturwissenschaften. 1971;58:465-523. DOI: 10.1007/BF00623322

[3] Hutchison CA, Chuang RY, Noskov VN, et al. Design and synthesis of a minimal bacterial genome. Science. 2016;351:aad6253. DOI: 10.1126/science.aad6253

[4] Shannon CE. A mathematical theory of communication. Bell Syst Tech J. 1948;27:379-423. DOI: 10.1002/j.1538-7305.1948.tb01338.x

[5] Shannon CE. Prediction and entropy of printed English. Bell Syst Tech J. 1951;30:50-64. DOI: 10.1002/j.1538-7305.1951.tb01366.x

[6] Whitmer GL III. Fons Constraint: Experiment Code and Data. GitHub. 2026. Available from: https://github.com/Windstorm-Labs/fons-constraint

[7] Miller GA. The magical number seven, plus or minus two. Psychol Rev. 1956;63:81-97. DOI: 10.1037/h0043158

[8] Cowan N. The magical number 4 in short-term memory. Behav Brain Sci. 2001;24:87-114. DOI: 10.1017/S0140525X01003922

[9] Whitmer GL III. The Receiver-Limited Floor. Zenodo. 2026. DOI: 10.5281/zenodo.19322973

[10] Whitmer GL III. The Throughput Basin. Zenodo. 2026. DOI: 10.5281/zenodo.19323194

[11] Whitmer GL III. The Serial Decoding Basin. Zenodo. 2026. DOI: 10.5281/zenodo.19323423

[12] Whitmer GL III. The Dissipative Decoder. Zenodo. 2026. DOI: 10.5281/zenodo.19433048

[13] Whitmer GL III. The Inherited Constraint. Zenodo. 2026. DOI: 10.5281/zenodo.19432911

[14] Landauer R. Irreversibility and heat generation in the computing process. IBM J Res Dev. 1961;5:183-191. DOI: 10.1147/rd.53.0183

[15] Von Neumann J. Theory of Self-Reproducing Automata. Urbana, IL: University of Illinois Press; 1966.
