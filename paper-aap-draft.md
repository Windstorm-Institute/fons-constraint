# American Academic Publisher Draft

# The Fons Constraint: Information-Theoretic Convergence on Encoding Depth in Self-Replicating Systems

**Grant Lavell Whitmer III**

The Windstorm Institute, Fort Ann, New York 12827, United States of America

Email: grantwhitmer3@gmail.com (Corresponding Author)

---

## Abstract

The genetic code universally employs 64 codons to encode biological information, yet the theoretical basis for this specific encoding depth has remained incompletely formalized. This study derives, from Shannon's channel capacity theorem applied to biological noise rates, that the optimal encoding alphabet size for autonomous self-replicating systems is the neighborhood of 2^6 = 64 units, yielding an optimal codon length of three bases in a four-letter nucleotide alphabet (4^3 = 64). Eigen's quasispecies error threshold, applied independently, constrains the maximum viable sequence length and is consistent with a 64-codon alphabet, though it does not by itself derive the alphabet size. Sensitivity analysis across eight orders of magnitude of error rate (10^-10 to 10^-2) confirms that 64 is a stable attractor rather than a fragile coincidence. This work distinguishes two separate constraints that prior literature has conflated: the Unit Constraint, which governs optimal alphabet size (~64 symbols), and the Sequence Constraint, which governs maximum message length before mutation destroys fidelity. An empirical test of substrate-independence was conducted by analyzing 16 major artificial intelligence tokenizer vocabularies. The original prediction that AI vocabularies would cluster near 64 was not supported. We do, however, advance a softer conjecture — tested in the companion papers, not established here: the effective information extracted per sequential processing event may fall in a common low-single-digit-bit range across DNA (~4.4 bits per codon), human cognition (~4-5 bits per working-memory chunk), and AI systems (a frontier model's per-token cross-entropy of ~4.6 bits near perplexity ~25). This motivates, rather than demonstrates, a throughput constraint operating at the receiver level rather than the vocabulary level, with implications for both molecular biology and artificial intelligence research. This work is the first paper in a nine-paper series (The Windstorm Series) investigating universal constraints on serial information processing [2]-[8].

**Keywords:** genetic code optimality, encoding depth, rate-distortion theory, error threshold, channel capacity, self-replication, information theory, serial decoding

---

## 1. Introduction

The genetic code uses 64 codons (4^3 triplets from a 4-nucleotide alphabet) to encode 20 amino acids and 3 stop signals, with 41 redundant mappings providing error tolerance. Freeland and Hurst [1] demonstrated this code is near-optimal for minimizing amino-acid substitution costs under mutation. But why 64? Why not 16 (4^2) or 256 (4^4)?

This paper derives the answer from first principles using two independent mathematical frameworks, showing that 64 sits at the bottom of an information-theoretic basin of attraction that is robust across eight orders of magnitude of error rate.

Two constraints that are often conflated must be distinguished:

1. **The Unit Constraint:** The optimal alphabet size — how many distinct symbols the encoding system should use.
2. **The Sequence Constraint:** The maximum message length before error accumulation destroys the master sequence [3].

Craig Venter's JCVI-syn3.0 minimal genome [4] uses the standard 64-codon alphabet (Unit Constraint) but requires approximately 531,000 base pairs across 473 genes (Sequence Constraint). The 64 codons are the vocabulary; the genome is the text. These are separate optimization problems.

The objectives of this study are threefold: (a) to derive the 64-codon optimum from Shannon's channel capacity [9] and Eigen's error threshold [3] independently; (b) to distinguish the Unit Constraint from the Sequence Constraint; and (c) to test whether the Unit Constraint generalizes beyond biology by analyzing AI tokenizer vocabularies.

---

## 2. Materials and Methods

### 2.1 Theoretical Framework: Shannon's Channel Capacity

The first derivation path employs Shannon's noisy channel coding theorem [9]. For a functional encoding system that must specify at least C distinct outputs, the minimum information per transmitted symbol is:

I_req = log_2(C)                                                          (1)

For the genetic code (C ~ 23 amino acids plus stop signals): I_req ~ 4.52 bits.

For an A-ary alphabet with per-digit error probability epsilon, the channel capacity per digit is:

C_channel = log_2(A) - H(epsilon)                                        (2)

where H(epsilon) = -epsilon * log_2(epsilon) - (1 - epsilon) * log_2(1 - epsilon) is the binary entropy function.

For DNA (A = 4) with near-perfect enzymatic proofreading: C_channel ~ 2 - H(epsilon) ~ 2 bits/digit.

For a codon of m digits, reliable transmission requires:

m >= log_2(C) / C_channel                                                (3)

When epsilon is small: m ~ ceil(log_A(C)). For DNA: m = ceil(log_4(23)) = ceil(2.26) = 3. Thus N = A^m = 4^3 = 64.

### 2.2 Theoretical Framework: Eigen's Error Threshold

The second derivation path employs Eigen's quasispecies theory [3]. A self-replicating sequence with per-digit fidelity q and selective advantage sigma > 1 has a maximum sustainable length:

L_max ~ ln(sigma) / (1 - q) ~ ln(sigma) / epsilon                       (4)

If L > L_max, the population enters mutational meltdown. Shannon's derivation yields the optimal alphabet size per transmission unit; Eigen's derivation yields the maximum message length in that alphabet. Two independent paths — information theory and population genetics — constrain the same system from different directions, with 64 as viable and optimal for DNA's parameters.

### 2.3 Sensitivity Analysis

To assess robustness, the optimal codon length was computed across a parameter sweep covering error rates from 10^-10 to 10^-2, representing eight orders of magnitude. Both the quaternary (A = 4, DNA) and binary (A = 2) cases were evaluated. Additionally, an explicit distortion tolerance of D = 0.05, matching synonymous codon redundancy, was tested to verify stability of the optimum.

### 2.4 AI Tokenizer Vocabulary Analysis

To test substrate-independence of the Unit Constraint, 16 major AI tokenizer vocabularies were analyzed: GPT-4, GPT-3.5, GPT-2, LLaMA-2, LLaMA-3, BERT, T5, Mistral, Phi-3, Yi-34B, Falcon-180B, Qwen-2, DeepSeek-V2, Claude (estimated), Gemini (estimated), and Command-R. Vocabulary sizes spanned an approximately 1,100-fold range from 30,522 (BERT) to 256,000 (Gemini). For each tokenizer, vocabulary size V, log_2(V), and effective information per token were calculated using Shannon's English entropy estimate of 4.7 bits/character [10] and average characters per token. The analysis code and complete results are available in the companion repository [11].

---

## 3. Results

### 3.1 Shannon Derivation: Optimal Codon Length

The Shannon channel capacity derivation yields an optimal codon length of m = 3 for a four-letter nucleotide alphabet encoding approximately 23 functional outputs. Adjacent integer values fail the optimization criterion:

- m = 2 (N = 16): Insufficient states. Sixteen codewords cannot encode all 23 amino acids and stop signals.
- m = 3 (N = 64): The minimum integer satisfying inequality (3), with 41 spare mappings providing error tolerance through synonymous codons.
- m = 4 (N = 256): Excessive redundancy. Higher replication cost and increased error accumulation per codon without proportionate information gain.

### 3.2 Eigen Derivation: Sequence-Length Bound Consistent with N = 64

Eigen's error threshold independently constrains the maximum viable sequence length rather than the alphabet size. Hutchison et al. [4] constructed JCVI-syn3.0 with 473 genes and approximately 531,000 base pairs — the experimentally determined minimum viable genome for autonomous cellular life — showing that the standard 64-codon alphabet is consistent with a minimum viable self-replicating system. This is a length (Sequence) constraint, not a derivation of the codon count.

### 3.3 Sensitivity Analysis

Table 1 presents the sensitivity analysis results for the quaternary alphabet (A = 4).

**Table 1.** Sensitivity analysis of optimal codon length across error rates (A = 4, C = 23)

| C  | epsilon | Optimal bits | m | N = 4^m | L_max (sigma=1.01) | L_max (sigma=1.1) |
|----|---------|-------------|---|---------|--------------------|--------------------|
| 23 | 10^-10  | 4.52        | 3 | 64      | ~99.5M             | ~953M              |
| 23 | 10^-9   | 4.52        | 3 | 64      | ~9.95M             | ~95.3M             |
| 23 | 10^-6   | 4.52        | 3 | 64      | ~9,950             | ~95,310            |
| 23 | 10^-4   | 4.53        | 3 | 64      | ~100               | ~953               |
| 23 | 10^-3   | 4.58        | 3 | 64      | ~10                | ~95                |
| 23 | 10^-2   | 4.92        | 3 | 64      | ~1                 | ~10                |

Table 2 presents the binary alphabet case (A = 2).

**Table 2.** Sensitivity analysis for binary alphabet (A = 2, C = 23)

| epsilon | Optimal bits | k | N = 2^k |
|---------|-------------|---|---------|
| 10^-4   | 4.53        | 5 | 32      |
| 10^-3   | 4.58        | 5 | 32      |
| 10^-2   | 4.92        | 5 | 32      |

The optimum at N = 64 is stable across eight orders of magnitude of error rate. With explicit distortion tolerance D = 0.05 (matching synonymous codon redundancy), the optimum is unchanged. These results confirm that 64 is a basin of attraction, not a fragile coincidence.

### 3.4 Unit Constraint vs. Sequence Constraint

Table 3 summarizes the distinction between the two constraints.

**Table 3.** Comparison of the Unit Constraint and Sequence Constraint

|              | Unit Constraint          | Sequence Constraint       |
|--------------|--------------------------|---------------------------|
| Constrains   | Alphabet size            | Total message length      |
| Derived from | Shannon (this paper) | Eigen [3]            |
| DNA example  | 64 codons                | ~531,000 bp               |
| Result       | N ~ 2^6                  | L_max ~ ln(sigma)/epsilon |

Conflating these two constraints leads to the erroneous claim that "64 is the optimal encoding size." Rather, 64 is the optimal alphabet size; the total encoding length is orders of magnitude larger and governed by a separate constraint.

### 3.5 AI Tokenizer Vocabularies

The prediction that AI tokenizer vocabularies would cluster near the 2^6 neighborhood was not supported. Vocabulary sizes range from 30,522 (BERT) to 256,000 (Gemini), with an average log_2(V) = 16.2 bits. No tokenizer falls in the 2^5 to 2^7 basin.

However, an unexpected convergence was observed. While vocabulary sizes differ by approximately 1,100-fold between DNA and AI, the effective information per processing event converges, as shown in Table 4.

**Table 4.** Cross-substrate convergence of effective information per processing event

| Substrate       | Transmission unit | Vocabulary | Effective info/step          |
|-----------------|-------------------|------------|------------------------------|
| DNA             | Codon             | 64         | ~4.4 bits (log_2(21))        |
| Human cognition | Chunk             | 7 +/- 2 items | ~4-5 bits              |
| AI (frontier)   | Token             | ~100K      | ~4.6 bits (at perplexity ~25)|

The three systems may deliver comparable effective information — a few bits per sequential processing event — despite vocabulary sizes spanning three orders of magnitude; we advance this as a conjecture, tested in the companion papers.

---

## 4. Discussion

### 4.1 Robustness of the 64-Codon Optimum

The derivation presented here is narrow but robust: encoding alphabets for nucleotide-based self-replicating systems optimize at N = 64 because this minimizes the rate-distortion tradeoff under DNA's noise regime. The sensitivity analysis confirms this is a basin, not a knife-edge. Across error rates spanning eight orders of magnitude — from the near-perfect fidelity of enzymatic proofreading (epsilon ~ 10^-10) to catastrophically noisy conditions (epsilon ~ 10^-2) — the optimal codon length remains m = 3, yielding N = 64. This stability is a property of the underlying mathematics: the ceiling function ceil(log_A(C)) is insensitive to small perturbations in channel capacity when the information requirement I_req falls well within the capacity of one additional digit.

Shannon's channel capacity derives the encoding depth (N = 64), while Eigen's quasispecies dynamics independently constrains the maximum viable sequence length. These frameworks were developed for entirely different purposes (communication engineering and molecular evolution, respectively), yet they constrain the same system from complementary directions. That the Shannon optimum sits well within Eigen's viability bound strengthens the case that the 64-codon genetic code represents a fundamental optimum rather than a historical accident, even though only the Shannon path fixes the alphabet size.

### 4.2 The Unit-Sequence Distinction

The distinction between the Unit Constraint and the Sequence Constraint has practical implications for synthetic biology. Researchers designing artificial genetic codes or expanding the natural code should recognize that the 64-codon alphabet is optimized separately from genome length. Expanding the alphabet to 256 codons (m = 4) would incur substantial costs in replication fidelity and energy expenditure without proportionate gains in encoding capacity, since only 23 functional outputs are required. Conversely, the Sequence Constraint sets an independent upper bound on genome complexity that depends on replication fidelity and selective advantage, not on alphabet size.

### 4.3 Cross-Substrate Throughput Convergence

The Unit Constraint (N ~ 2^6) is established as a theorem for nucleotide-based encoding under DNA's specific parameters. It does not generalize directly to AI vocabularies, as the empirical test demonstrates. We conjecture that the broader substrate-independent constraint operates at the effective throughput level (a few bits per processing step), with vocabulary size as a dependent variable determined by the receiver architecture and its error-correction strategy. This observation is consistent with Miller's [6] finding that human working memory operates at approximately 7 +/- 2 items (~3-5 bits per chunk) and with Cowan's [5] revised estimate of approximately 4 items.

The negative result on AI tokenizers is reported honestly: the prediction as stated was wrong. However, the unexpected convergence at approximately 4-5 effective bits per processing event across three substrates (molecular, cognitive, computational) warrants further investigation and may represent a deeper, genuinely substrate-independent constraint. If confirmed, this would imply that the bottleneck in serial information processing lies not in the encoding vocabulary but in the receiver's capacity to discriminate and process symbols under noise — a receiver-limited rather than sender-limited regime.

This throughput convergence is examined formally in the companion papers of this series: the rate-distortion floor is derived in [2], the cross-substrate basin is characterized in [7], the thermodynamic basis is established in [8], and the cost structure distinguishing biological from artificial systems is analyzed in the fifth paper of the series (DOI: 10.5281/zenodo.19433048).

### 4.4 Limitations

The following limitations should be noted:

1. The derivation is proven for DNA-based systems and conjectured for other substrates. Extension to alternative genetic codes (e.g., expanded amino acid alphabets in synthetic biology) requires empirical validation.
2. The AI tokenizer analysis uses estimated parameters for some models (Claude, Gemini) where official vocabulary specifications were unavailable.
3. No computational simulation has independently validated the sensitivity analysis results presented in Tables 1 and 2.
4. A proposed third derivation path via Landauer's thermodynamic cost [12] remains incomplete.
5. The throughput constraint observation is preliminary and requires formal derivation, which is undertaken in the companion papers of this series [2], [7].
6. The present analysis assumes symmetric error channels and equiprobable symbol distributions. Real biological systems violate both assumptions; the robustness of the result under non-uniform codon usage distributions warrants further investigation.

---

## 5. Conclusion

The genetic code's 64 codons are not arbitrary. They represent the information-theoretic optimum for a four-letter alphabet encoding approximately 23 functional outputs under biological noise rates — a result derived from Shannon's channel capacity, shown consistent with Eigen's error threshold, and robust across eight orders of magnitude of error rate. The distinction between the Unit Constraint (alphabet size) and the Sequence Constraint (message length) resolves a persistent conflation in discussions of genetic code optimality. The empirical extension to AI systems falsified the original substrate-independence prediction but motivated a potentially deeper conjecture: that effective information throughput per serial processing event (a few bits) is comparable across DNA, human cognition, and AI, despite 1,000-fold differences in vocabulary size. This conjecture motivates the companion papers of The Windstorm Series, which formally derive and test the throughput constraint across substrates and domains.

---

## Acknowledgements

The mathematical derivations, tokenizer experiment, data analysis, and initial manuscript drafting were performed with the assistance of Claude (Anthropic), an AI research tool. The throughput constraint observation (Section 3.5) emerged from collaborative analysis on 28 March 2026. The author thanks the broader AI research community for making tokenizer specifications publicly available.

## Funding Information

This research received no external funding. All work was self-funded by the author.

## Author Contributions

Grant Lavell Whitmer III conceived the research framework, identified the convergence pattern, directed all experimental priorities, and prepared the final manuscript.

## Conflict of Interest

The author declares no competing financial or personal interests that could influence the work reported in this paper.

---

## References

[1] Freeland, S.J.; Hurst, L.D. "The genetic code is one in a million," Journal of Molecular Evolution, vol. 47, no. 3, pp. 238-248, 1998. DOI: 10.1007/PL00006384

[2] Whitmer III, G.L. "The Receiver-Limited Floor: Rate-Distortion Bounds on Serial Decoding Throughput," Zenodo, 2026. DOI: 10.5281/zenodo.19322973

[3] Eigen, M. "Selforganization of matter and the evolution of biological macromolecules," Die Naturwissenschaften, vol. 58, no. 10, pp. 465-523, 1971. DOI: 10.1007/BF00623322

[4] Hutchison, C.A.; Chuang, R.-Y.; Noskov, V.N.; Assad-Garcia, N.; Deerinck, T.J.; Ellisman, M.H.; Gill, J.; Kannan, K.; Karas, B.J.; Ma, L.; Pelletier, J.F.; Qi, Z.-Q.; Richter, R.A.; Strychalski, E.A.; Sun, L.; Suzuki, Y.; Tsvetanova, B.; Wise, K.S.; Smith, H.O.; Glass, J.I.; Merryman, C.; Gibson, D.G.; Venter, J.C. "Design and synthesis of a minimal bacterial genome," Science, vol. 351, no. 6280, pp. aad6253, 2016. DOI: 10.1126/science.aad6253

[5] Cowan, N. "The magical number 4 in short-term memory: A reconsideration of mental storage capacity," Behavioral and Brain Sciences, vol. 24, no. 1, pp. 87-114, 2001. DOI: 10.1017/S0140525X01003922

[6] Miller, G.A. "The magical number seven, plus or minus two: Some limits on our capacity for processing information," Psychological Review, vol. 63, no. 2, pp. 81-97, 1956. DOI: 10.1037/h0043158

[7] Whitmer III, G.L. "The Throughput Basin: Cross-Substrate Convergence and Decomposition of Serial Decoding Throughput," Zenodo, 2026. DOI: 10.5281/zenodo.19323194

[8] Whitmer III, G.L. "The Serial Decoding Basin: Five Experiments on Convergence, Thermodynamic Anchoring, and Receiver-Limited Geometry," Zenodo, 2026. DOI: 10.5281/zenodo.19323423

[9] Shannon, C.E. "A Mathematical Theory of Communication," Bell System Technical Journal, vol. 27, no. 3, pp. 379-423, 1948. DOI: 10.1002/j.1538-7305.1948.tb01338.x

[10] Shannon, C.E. "Prediction and Entropy of Printed English," Bell System Technical Journal, vol. 30, no. 1, pp. 50-64, 1951. DOI: 10.1002/j.1538-7305.1951.tb01366.x

[11] Whitmer III, G.L. "Fons Constraint: Experiment Code and Data," GitHub, 2026. https://github.com/Windstorm-Labs/fons-constraint (accessed Apr. 12, 2026).

[12] Landauer, R. "Irreversibility and heat generation in the computing process," IBM Journal of Research and Development, vol. 5, no. 3, pp. 183-191, 1961. DOI: 10.1147/rd.53.0183

[13] Von Neumann, J. Theory of Self-Reproducing Automata; University of Illinois Press: Urbana, IL, USA, 1966.

---

## Appendix A: Experiment Protocol

The tokenizer analysis was implemented in Python using publicly available tokenizer libraries. For each of the 16 tokenizers, the following metrics were computed:

- Vocabulary size V
- Raw bits per token: log_2(V)
- Average characters per token (measured on standardized English text)
- Effective information per token: estimated via Shannon's English entropy (4.7 bits/character) multiplied by average characters per token
- Basin membership: whether log_2(V) falls within the 2^5 to 2^7 range

The complete implementation, including all analysis code and raw results in JSON format, is available at the companion repository [11].

---

*This paper is Paper 1 of The Windstorm Series. The series continues with Paper 2: The Receiver-Limited Floor [2], Paper 3: The Throughput Basin [7], Paper 4: The Serial Decoding Basin [8], Paper 5: The Dissipative Decoder (DOI: 10.5281/zenodo.19433048), Paper 6: The Inherited Constraint (DOI: 10.5281/zenodo.19432911), and Paper 7: The Throughput Basin Origin (DOI: 10.5281/zenodo.19498582).*
