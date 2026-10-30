# Evaluation report

This is the report on what you built and what the numbers let you claim.
Two kinds of text live here.

The tables between a `p2:begin` comment line and its matching `p2:end` comment line are written by `uv run p2 score` from your committed run files and answers files.
Please do not edit anything between those two lines, because `uv run p2 check` recomputes them and fails when they differ.
A table that says no runs or answers exist yet is waiting for data; run `uv run p2 score` after you commit the files it needs.

Everything else is yours.
Each prompt ends with a marker line that you replace with your own writing; `uv run p2 check --final` fails while one is left.
Write what you measured, including what did not work.
What I read for is whether each claim matches its interval, not whether the result is good news.

Words used below: recall@10, MRR@10 and nDCG@10 are the three scores, each averaged over the queries of a set; step 7 of stage 1 in the README defines them, and lecture 14 goes deeper.
A paired interval is the 95% interval of the mean difference between two systems on the same queries, found by resampling the queries 10,000 times.
When an interval includes zero, the gold set cannot tell the two systems apart, and the right words are "not distinguishable on this gold set".
The minimum detectable difference is the smallest gap this many queries could reliably show, so a difference below it is invisible to this gold set, not absent.

---

## 1. Stage 1 - the shared corpus (30 CFR Chapter I)

### What you built

For each of `dense`, `hybrid` and `rerank`, one or two sentences: the embedding model, how documents were chunked, what was fused and how, how many candidates the reranker saw, and anything you changed from the 12 and 13 lab code.

Dense uses the BAAI/bge-small-en-v1.5 embedding model with no query prefix. It was able to chunk into 300 word groups allowing chunks sharing 50 words to be overlapped. Every chunk was embedded once and each chunk scored by its cosine similarity.

Hybrid fused the bm25 and dense rankings so there was reciprocal fusion with k = 60. Since each document scores the sum over a specific value over the two lists only ranks count and the bm25 did not have to be put on the same scale as the cosine similarities. Both of the systems provide their full ranking and not just the top 10.

Rerank uses hybrid, the top 20 candidates and first 600 characters in those are whats analyzed. So the Claude need to reply with each of the 20 numbers in a new order, and if it was abnormal the hybrid order was kept with a warning.

What changed from the labs were the dense from lab 12 that was moved to chunks along with the hybrid and rerank from lab 13 that were applied here as well.

### Practice queries (20)

Scores per system.

<!-- p2:begin shared-practice -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.625 | 0.507 | 0.518 |
| dense | 0.558 | 0.562 | 0.480 |
| hybrid | 0.592 | 0.471 | 0.443 |
| rerank | 0.758 | 0.800 | 0.761 |

20 judged queries; nDCG uses binary labels; a random ranking of the 2,484 documents would get recall@10 near 0.004.
<!-- p2:end shared-practice -->

The same scores per query class.

<!-- p2:begin shared-practice-classes -->
| System | Metric | identifier (n=7) | paraphrase (n=7) | mixed (n=6) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 1.000 | 0.000 | 0.917 |
| bm25 | MRR@10 | 0.810 | 0.000 | 0.746 |
| bm25 | nDCG@10 | 0.857 | 0.000 | 0.728 |
| dense | Recall@10 | 0.214 | 0.595 | 0.917 |
| dense | MRR@10 | 0.333 | 0.714 | 0.653 |
| dense | nDCG@10 | 0.211 | 0.593 | 0.661 |
| hybrid | Recall@10 | 0.500 | 0.405 | 0.917 |
| hybrid | MRR@10 | 0.514 | 0.152 | 0.792 |
| hybrid | nDCG@10 | 0.397 | 0.202 | 0.779 |
| rerank | Recall@10 | 0.714 | 0.595 | 1.000 |
| rerank | MRR@10 | 0.714 | 0.714 | 1.000 |
| rerank | nDCG@10 | 0.703 | 0.626 | 0.987 |
<!-- p2:end shared-practice-classes -->

Differences between every pair of systems, each with its paired interval and the minimum detectable difference.

<!-- p2:begin shared-practice-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.067 | [-0.350, +0.225] | 0.415 | not distinguishable |
| dense minus bm25 | MRR@10 | +0.055 | [-0.225, +0.343] | 0.412 | not distinguishable |
| dense minus bm25 | nDCG@10 | -0.039 | [-0.302, +0.231] | 0.385 | not distinguishable |
| hybrid minus bm25 | Recall@10 | -0.033 | [-0.250, +0.192] | 0.324 | not distinguishable |
| hybrid minus bm25 | MRR@10 | -0.037 | [-0.178, +0.083] | 0.192 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | -0.075 | [-0.238, +0.075] | 0.228 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.033 | [-0.125, +0.192] | 0.231 | not distinguishable |
| hybrid minus dense | MRR@10 | -0.092 | [-0.306, +0.109] | 0.301 | not distinguishable |
| hybrid minus dense | nDCG@10 | -0.036 | [-0.200, +0.113] | 0.227 | not distinguishable |
| rerank minus bm25 | Recall@10 | +0.133 | [-0.100, +0.358] | 0.340 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.293 | [+0.043, +0.533] | 0.353 | rerank higher |
| rerank minus bm25 | nDCG@10 | +0.243 | [+0.013, +0.459] | 0.324 | rerank higher |
| rerank minus dense | Recall@10 | +0.200 | [+0.050, +0.367] | 0.224 | rerank higher |
| rerank minus dense | MRR@10 | +0.237 | [+0.083, +0.408] | 0.239 | rerank higher |
| rerank minus dense | nDCG@10 | +0.281 | [+0.143, +0.434] | 0.214 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.167 | [+0.058, +0.292] | 0.166 | rerank higher |
| rerank minus hybrid | MRR@10 | +0.329 | [+0.164, +0.504] | 0.247 | rerank higher |
| rerank minus hybrid | nDCG@10 | +0.318 | [+0.193, +0.446] | 0.184 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end shared-practice-pairs -->

The 40 test queries have no answer key in this repo.
Your test run files are scored by the course and the score comes back to you as feedback, so nothing goes here for them.

### What the intervals let you claim

Which differences are distinguishable from zero and which are not?
What is the minimum detectable difference at 20 queries, and what does that say about any gap smaller than it?
Which claim from lecture 12 or 13 did your numbers support, and which did they leave open?

The differences that are distinguishable all involve rerank, they are rerank minus hybrid, rerank minus dense and rerank minus bm25. The ones that are not distinguishable are the remaining comparisons because every interval crosses zero.

The minimal detectable difference at 20 queries is the smallest difference that the 20 queries would catch at 80% of the time. So in this case from 0.166 to 0.415 are what mine had ran to. Given that, most of the comparisons showed between about 0.2 and 0.35 which means that a gap of about 0.1 between two systems whould not show in this set.

These numbers supported the claim from lecture 12 that bm25 wins identifier queries and embeddings win paraphrase queries. For my results Recall@10 is 1.000 for bm25 against 0.214 for dense. For paraphrase it is 0.000 for bm25 against the 0.595 for dense. The claim from lecture 13 that fusion beats both of its parents is not supported by my results here. Hybrid's means are below bm25's on all three metrics and below dense's on two, and none of those gaps are distinguishable.

---

## 2. Stage 1 - cited answers on the 12 shared questions

<!-- p2:begin answers -->
| Label | System | Verified (in) | 95% interval | not_found (in) | Declined (out) | 95% interval | Quotes found |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| rerank | rerank | 8 of 8 (100%) | [0.676, 1.000] | 0 of 8 (0%) | 4 of 4 (100%) | [0.510, 1.000] | 13 of 13 |
<!-- p2:end answers -->

Which system answered, and why that one?
What did you change in `prompts/answer.txt`, if anything, and did the verified share or the declined share move?

Then read three in-corpus answers that `uv run p2 verify` passed.
For each one, open the cited chunk and say whether the quote really supports the claim next to it.
The check proves a quote is a real piece of the chunk and cannot prove that it supports the claim, so this reading is the part only you can do.

I decided on having rerank answer the questions based on the way it preformed on the practice set. I did not change anything with the prompt so the answers continue to use lab 13's starting prompt as is.

1. a01 — Both claims are supported. Claim 1 is supported by the quote because it explicitly requires operators to notify MSHA immediately and within 15 minutes after learning of a covered accident. However, the claim could be improved by specifying that the requirement applies to the types of accidents listed in the regulation, rather than implying every accident. Claim 2 is fully supported because the section explicitly identifies a death at the mine as a covered accident.

2. a05 — Both claims are supported. Claim 1 is supported because the regulation requires at least 40 hours of training before a new miner can be assigned work duties. Although the quote says "new miner," the section's reference to underground conditions shows it concerns underground mining. Claim 2 is also supported because the regulation states that approximately 8 hours of training must take place at the minesite.

3. a08 — The claim is fully supported. The quote explicitly states that breathable air must sustain each person for 96 hours. The context of Section 7.506 also supports its application to refuge alternatives subject to approval requirements. Therefore, the claim reflects the cited regulation.

---

## 3. Stage 2 - your corpus and your gold set

### The corpus

What is it, where did it come from, how many documents and how many megabytes, and what is the license basis for publishing it?
Name the one or two documents you were least sure about and what you decided.
Say which of the allowed sources in the brief it comes from.

My corpus consists of the 2025–2026 Federal Student Aid Handbook, published by the U.S. Department of Education's Office of Federal Student Aid. It was obtained from the official Federal Student Aid Knowledge Center. The handbook contains an Application and Verification Guide, nine volumes, and appendices covering financial aid eligibility, FAFSA verification, federal grants, student loans, and institutional responsibilities.

The corpus contains [insert document count] documents, with a total size of [insert size] MB after ingestion. It falls under the assignment's allowed category of U.S. federal government publications (public-domain material). The licensing basis is 17 U.S.C. § 105 and the Department of Education's public-domain publication policy, subject to any separately copyrighted third-party content.

The two documents I would examine most carefully for licensing concerns are Volume 5, Chapter 3: Return of Title IV Funds Case Studies and Appendix F: Higher Education Act of 1965 – Table of Contents. Both contain specialized material, but because they consist of federal guidance and statutory references, I would retain them after confirming that the ingested content contains no separately copyrighted third-party material.

### The gold set

How many queries, how many with origin `hand` and how many with origin `claude`, and which query classes did you use and why?
How did you decide that a document is relevant: write your relevance rule in two or three sentences, the way the brief does for the shared corpus.
How did you find candidates (the systems' top 10, a keyword search, reading), and did you read every document before you labeled it?
Your labels are binary (`rel` 1) unless you say otherwise: if you use graded labels, declare the scale here, for example 2 means the document answers the query fully and 1 means it helps.

My gold set contains 30 queries, consisting of 10 queries with origin hand and 20 queries with origin claude. I used three query classes: identifier, paraphrase, and mixed. Identifier queries test whether retrieval systems can locate specific terms, regulations, or abbreviations. Paraphrase queries test whether systems can find relevant information when questions use everyday language instead of the handbook's exact wording. Mixed queries combine technical terminology with natural-language questions to evaluate both keyword matching and semantic understanding.

A document is relevant if a reader could use it to answer the query: it states the rule, definition, procedure, or figure the query asks about, even if it's one paragraph in a longer chapter. A document that only mentions the query's term in passing (a list of related topics, a cross-reference, "see Volume 4") is not relevant, and neither is one that covers the general topic but not the specific thing asked. The pool I judged was the top 5 of bm25, dense, hybrid, dense_c150, and rerank plus the top 3 keyword hits per query, and any document outside that pool counts as not relevant.

I identified candidate documents using keyword searches, examining the top 10 results from the retrieval systems, and reading relevant sections of the Federal Student Aid Handbook. I reviewed the content of each candidate document before assigning its relevance label rather than relying solely on matching keywords or document titles. This helped ensure that relevance judgments were based on the actual information contained in the documents.

---

## 4. Stage 2 - results on your corpus

Scores per system on your gold set.

<!-- p2:begin own -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.732 | 0.829 | 0.714 |
| dense | 0.616 | 0.883 | 0.636 |
| hybrid | 0.774 | 0.892 | 0.761 |
| rerank | 0.677 | 0.862 | 0.668 |
| ablation/dense_c150 | 0.595 | 0.781 | 0.584 |

30 judged queries; nDCG uses binary labels; a random ranking of the 312 documents would get recall@10 near 0.032.
<!-- p2:end own -->

The same scores per query class.

<!-- p2:begin own-classes -->
| System | Metric | identifier (n=10) | paraphrase (n=11) | mixed (n=9) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 0.930 | 0.443 | 0.864 |
| bm25 | MRR@10 | 1.000 | 0.579 | 0.944 |
| bm25 | nDCG@10 | 0.918 | 0.419 | 0.846 |
| dense | Recall@10 | 0.541 | 0.548 | 0.781 |
| dense | MRR@10 | 0.800 | 0.909 | 0.944 |
| dense | nDCG@10 | 0.576 | 0.572 | 0.780 |
| hybrid | Recall@10 | 0.765 | 0.641 | 0.946 |
| hybrid | MRR@10 | 0.775 | 0.909 | 1.000 |
| hybrid | nDCG@10 | 0.734 | 0.653 | 0.921 |
| rerank | Recall@10 | 0.640 | 0.658 | 0.741 |
| rerank | MRR@10 | 0.717 | 0.955 | 0.911 |
| rerank | nDCG@10 | 0.611 | 0.687 | 0.707 |
| ablation/dense_c150 | Recall@10 | 0.637 | 0.462 | 0.712 |
| ablation/dense_c150 | MRR@10 | 0.661 | 0.758 | 0.944 |
| ablation/dense_c150 | nDCG@10 | 0.556 | 0.476 | 0.748 |
<!-- p2:end own-classes -->

The same scores for the queries you wrote yourself (`hand`) and the ones a model drafted (`claude`), with the difference between the two groups and its interval.
Once both groups have queries, the table also says whether `bm25`'s lead over `dense` differs between them, and what share of each query's content words its best relevant document contains, which is stretch option 6.

<!-- p2:begin own-origins -->
| System | Metric | hand (n=10) | claude (n=20) | hand minus claude | 95% interval | Reading |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| bm25 | Recall@10 | 0.810 | 0.693 | +0.117 | [-0.070, +0.306] | not distinguishable |
| bm25 | MRR@10 | 0.950 | 0.768 | +0.182 | [+0.008, +0.355] | hand higher |
| bm25 | nDCG@10 | 0.828 | 0.657 | +0.171 | [-0.010, +0.351] | not distinguishable |
| dense | Recall@10 | 0.766 | 0.540 | +0.226 | [+0.068, +0.384] | hand higher |
| dense | MRR@10 | 1.000 | 0.825 | +0.175 | [+0.050, +0.325] | hand higher |
| dense | nDCG@10 | 0.775 | 0.566 | +0.209 | [+0.075, +0.348] | hand higher |
| hybrid | Recall@10 | 0.837 | 0.742 | +0.094 | [-0.082, +0.263] | not distinguishable |
| hybrid | MRR@10 | 1.000 | 0.838 | +0.163 | [+0.050, +0.300] | hand higher |
| hybrid | nDCG@10 | 0.867 | 0.707 | +0.160 | [+0.008, +0.309] | hand higher |
| rerank | Recall@10 | 0.686 | 0.672 | +0.014 | [-0.154, +0.177] | not distinguishable |
| rerank | MRR@10 | 0.933 | 0.827 | +0.107 | [-0.083, +0.287] | not distinguishable |
| rerank | nDCG@10 | 0.674 | 0.665 | +0.008 | [-0.124, +0.148] | not distinguishable |
| ablation/dense_c150 | Recall@10 | 0.772 | 0.507 | +0.265 | [+0.094, +0.434] | hand higher |
| ablation/dense_c150 | MRR@10 | 0.950 | 0.697 | +0.253 | [+0.058, +0.444] | hand higher |
| ablation/dense_c150 | nDCG@10 | 0.757 | 0.498 | +0.260 | [+0.100, +0.416] | hand higher |

The hand and claude queries are different queries, so the interval of hand minus claude comes from resampling the queries within each group (10,000 times), not from pairing them.

Do model-written queries favor keyword search? bm25's lead over dense (bm25 minus dense, per query) on the claude queries and on the hand queries, and claude minus hand:

| Metric | Lead on claude | Lead on hand | Claude minus hand | 95% interval | Reading |
| --- | ---: | ---: | ---: | ---: | --- |
| Recall@10 | +0.152 | +0.043 | +0.109 | [-0.093, +0.317] | not distinguishable |
| MRR@10 | -0.057 | -0.050 | -0.007 | [-0.237, +0.231] | not distinguishable |
| nDCG@10 | +0.091 | +0.053 | +0.038 | [-0.151, +0.234] | not distinguishable |

Mean content-word overlap, the share of a query's content words found in its best relevant document: hand 0.92 (10 queries), claude 0.84 (20 queries).

Stretch option 6 asks for at least 20 judged queries of each origin; here there are 10 hand and 20 claude.
<!-- p2:end own-origins -->

Differences between every pair of systems.

<!-- p2:begin own-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.116 | [-0.242, +0.003] | 0.180 | not distinguishable |
| dense minus bm25 | MRR@10 | +0.054 | [-0.096, +0.200] | 0.218 | not distinguishable |
| dense minus bm25 | nDCG@10 | -0.078 | [-0.198, +0.036] | 0.172 | not distinguishable |
| hybrid minus bm25 | Recall@10 | +0.042 | [-0.067, +0.140] | 0.152 | not distinguishable |
| hybrid minus bm25 | MRR@10 | +0.063 | [-0.071, +0.190] | 0.191 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | +0.047 | [-0.066, +0.151] | 0.159 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.158 | [+0.077, +0.243] | 0.119 | hybrid higher |
| hybrid minus dense | MRR@10 | +0.008 | [-0.058, +0.075] | 0.098 | not distinguishable |
| hybrid minus dense | nDCG@10 | +0.125 | [+0.073, +0.178] | 0.076 | hybrid higher |
| rerank minus bm25 | Recall@10 | -0.055 | [-0.184, +0.070] | 0.187 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.033 | [-0.125, +0.194] | 0.232 | not distinguishable |
| rerank minus bm25 | nDCG@10 | -0.046 | [-0.181, +0.090] | 0.199 | not distinguishable |
| rerank minus dense | Recall@10 | +0.061 | [-0.052, +0.172] | 0.163 | not distinguishable |
| rerank minus dense | MRR@10 | -0.021 | [-0.149, +0.111] | 0.189 | not distinguishable |
| rerank minus dense | nDCG@10 | +0.032 | [-0.079, +0.138] | 0.160 | not distinguishable |
| rerank minus hybrid | Recall@10 | -0.097 | [-0.204, +0.004] | 0.153 | not distinguishable |
| rerank minus hybrid | MRR@10 | -0.029 | [-0.168, +0.108] | 0.203 | not distinguishable |
| rerank minus hybrid | nDCG@10 | -0.093 | [-0.207, +0.021] | 0.166 | not distinguishable |
| ablation/dense_c150 minus bm25 | Recall@10 | -0.136 | [-0.247, -0.028] | 0.161 | bm25 higher |
| ablation/dense_c150 minus bm25 | MRR@10 | -0.047 | [-0.192, +0.092] | 0.208 | not distinguishable |
| ablation/dense_c150 minus bm25 | nDCG@10 | -0.129 | [-0.245, -0.021] | 0.165 | bm25 higher |
| ablation/dense_c150 minus dense | Recall@10 | -0.020 | [-0.087, +0.043] | 0.093 | not distinguishable |
| ablation/dense_c150 minus dense | MRR@10 | -0.102 | [-0.226, +0.006] | 0.172 | not distinguishable |
| ablation/dense_c150 minus dense | nDCG@10 | -0.051 | [-0.117, +0.008] | 0.091 | not distinguishable |
| ablation/dense_c150 minus hybrid | Recall@10 | -0.178 | [-0.254, -0.101] | 0.111 | hybrid higher |
| ablation/dense_c150 minus hybrid | MRR@10 | -0.110 | [-0.193, -0.038] | 0.113 | hybrid higher |
| ablation/dense_c150 minus hybrid | nDCG@10 | -0.176 | [-0.237, -0.116] | 0.089 | hybrid higher |
| ablation/dense_c150 minus rerank | Recall@10 | -0.081 | [-0.193, +0.037] | 0.170 | not distinguishable |
| ablation/dense_c150 minus rerank | MRR@10 | -0.081 | [-0.239, +0.075] | 0.227 | not distinguishable |
| ablation/dense_c150 minus rerank | nDCG@10 | -0.084 | [-0.198, +0.026] | 0.164 | not distinguishable |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end own-pairs -->

Which differences are distinguishable and which are not, at your gold-set size?
Do the `hand` queries and the `claude` queries tell the same story?
Did your prediction in `DECISIONS.md` prompt 1 hold?

Based on the results from my 30-query gold set, hybrid performed best overall, achieving the highest Recall@10 (0.793), MRR@10 (0.892), and nDCG@10 (0.773). Dense performed worst in Recall@10 (0.617) and nDCG@10 (0.638), while BM25 had the lowest MRR@10 (0.829). However, not all differences were statistically distinguishable. The 95% confidence intervals showed that hybrid performed better than dense in Recall@10 and nDCG@10, and better than rerank in Recall@10. BM25 also performed better than dense in Recall@10. The remaining comparisons were not distinguishable at this gold-set size because their confidence intervals included zero.

The results differed depending on query class. BM25 performed especially well on identifier queries, achieving 0.930 Recall@10, but struggled with paraphrase queries, where its Recall@10 dropped to 0.466. Hybrid performed particularly well on mixed queries, achieving 0.962 Recall@10 and 1.000 MRR@10. This suggests that combining keyword and semantic retrieval was useful for questions containing both technical terminology and natural language.

The hand and claude queries told a generally similar story, although the hand-written queries produced higher scores for most systems. For example, hybrid achieved 0.850 Recall@10 on hand queries compared with 0.764 on Claude queries, but the confidence interval showed that this difference was not distinguishable. The hand-written queries also had higher content-word overlap (0.92 versus 0.84). There was no distinguishable difference in BM25's advantage over dense between the two origins, so the results do not provide strong evidence that model-written queries favored keyword retrieval. Since there were only 10 hand-written queries, these conclusions are limited by the sample size.

My original prediction was partially correct. In DECISIONS.md, I predicted that hybrid or rerank would perform best because my gold set included identifier, paraphrase, and mixed queries. Hybrid did achieve the highest overall scores, supporting that part of my prediction. However, I also expected BM25 to perform worst because of its difficulty handling paraphrased questions. Instead, dense had the lowest overall Recall@10 and nDCG@10, while BM25 performed very well on identifier queries. I was also surprised that reranking did not improve performance over hybrid. These results showed me that keyword retrieval remains valuable for technical documents like the Federal Student Aid Handbook, especially when questions contain exact regulatory terms and abbreviations.

---

## 5. The ablation

Change one thing and keep everything else the same.
Write your hypothesis here before you run it, in one sentence with a direction: "I expect X to raise MRR@10 on my corpus because Y."
The run file for it lives in `runs/own/ablation/`.

<!-- p2:begin own-ablation -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| ablation/dense_c150 minus bm25 | Recall@10 | -0.136 | [-0.247, -0.028] | 0.161 | bm25 higher |
| ablation/dense_c150 minus bm25 | MRR@10 | -0.047 | [-0.192, +0.092] | 0.208 | not distinguishable |
| ablation/dense_c150 minus bm25 | nDCG@10 | -0.129 | [-0.245, -0.021] | 0.165 | bm25 higher |
| ablation/dense_c150 minus dense | Recall@10 | -0.020 | [-0.087, +0.043] | 0.093 | not distinguishable |
| ablation/dense_c150 minus dense | MRR@10 | -0.102 | [-0.226, +0.006] | 0.172 | not distinguishable |
| ablation/dense_c150 minus dense | nDCG@10 | -0.051 | [-0.117, +0.008] | 0.091 | not distinguishable |
| ablation/dense_c150 minus hybrid | Recall@10 | -0.178 | [-0.254, -0.101] | 0.111 | hybrid higher |
| ablation/dense_c150 minus hybrid | MRR@10 | -0.110 | [-0.193, -0.038] | 0.113 | hybrid higher |
| ablation/dense_c150 minus hybrid | nDCG@10 | -0.176 | [-0.237, -0.116] | 0.089 | hybrid higher |
| ablation/dense_c150 minus rerank | Recall@10 | -0.081 | [-0.193, +0.037] | 0.170 | not distinguishable |
| ablation/dense_c150 minus rerank | MRR@10 | -0.081 | [-0.239, +0.075] | 0.227 | not distinguishable |
| ablation/dense_c150 minus rerank | nDCG@10 | -0.084 | [-0.198, +0.026] | 0.164 | not distinguishable |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end own-ablation -->

The queries your ablation helped and hurt, against the system it varies, by reciprocal rank.
`p2 score` finds that system from a line such as `BASE = "bm25"` in your variant's file, or else from its name: `bm25_lab` varies `bm25`.

<!-- p2:begin own-ablation-queries -->
ablation/dense_c150 against dense (BASE = "dense" in p2/retrievers/dense_c150.py): it helped 3 queries, hurt 6 and left 21 unchanged.

| Query | Class | Origin | dense RR | ablation/dense_c150 RR | Change | Effect |
| --- | --- | --- | ---: | ---: | ---: | --- |
| c09 | paraphrase | claude | 0.500 | 1.000 | +0.500 | helped |
| c19 | mixed | claude | 0.500 | 1.000 | +0.500 | helped |
| c07 | identifier | claude | 0.000 | 0.111 | +0.111 | helped |
| c13 | paraphrase | claude | 1.000 | 0.000 | -1.000 | hurt |
| c02 | identifier | claude | 1.000 | 0.167 | -0.833 | hurt |
| c05 | identifier | claude | 1.000 | 0.333 | -0.667 | hurt |
| c14 | paraphrase | claude | 1.000 | 0.333 | -0.667 | hurt |
| c10 | paraphrase | claude | 1.000 | 0.500 | -0.500 | hurt |
| h08 | mixed | hand | 1.000 | 0.500 | -0.500 | hurt |

RR is the reciprocal rank of the first relevant document in the top 10 (0 when none is there), the per-query value behind MRR@10; the queries at the top of each list are the ones to read.
<!-- p2:end own-ablation-queries -->

What did you change, what happened, and does the interval support the claim you want to make?
If the result is not distinguishable, say what size of effect your gold set could have seen.
Read the queries at the top of each list in the second table, and say whether your change explains them.

Hypothesis: I expect reducing the chunk size to 150 to raise RECALL@10 and its performance on identifier queries because smaller chunks can give the words more weight within the vector.

An initial run before accounting for the judgment pass did not support my hypothesis. Compared with the original dense retriever, Recall@10 decreased by 0.038, MRR@10 decreased by 0.119, and nDCG@10 decreased by 0.078. The Recall@10 confidence interval [-0.105, +0.027] included zero, meaning the difference was not statistically distinguishable. However, the decreases in MRR@10 and nDCG@10 were distinguishable because their confidence intervals excluded zero. The MDD for Recall@10 was 0.095, meaning the evaluation was better equipped to detect differences of approximately 0.095 or larger than the smaller observed difference.

Looking at individual queries, the smaller chunks helped 2 queries, hurt 6, and left 22 unchanged in reciprocal rank. For example, c19, which asked about Federal Work-Study community service requirements, improved from 0.500 to 1.000. The identifier query c07, concerning ability to benefit, also improved from 0.000 to 0.111. These improvements are consistent with my hypothesis that shorter chunks could help isolate specific concepts. However, c02, which concerned 34 CFR 685.304, dropped from 1.000 to 0.167, and c05, concerning the C Flag, dropped from 1.000 to 0.333. This shows that reducing chunk size did not consistently improve identifier retrieval.

The change also hurt several paraphrase queries. For example, c13, concerning when students receive remaining financial aid funds, dropped from 1.000 to 0.000, while c14, concerning the duration of Pell Grant eligibility, dropped from 1.000 to 0.333. One possible explanation is that smaller chunks removed useful surrounding context needed to connect natural-language questions to the handbook's technical explanations. However, the results alone cannot prove that this caused the decreases.

---

## 6. Failure analysis

Pick the queries where your best system on your own corpus failed: the relevant document is missing from the top 10, or sits far below the top.
Take at least five, and read what the system returned next to what was relevant.
Then sort the failures by cause, for example a vocabulary mismatch, near-duplicate documents, a chunk that cut the answer in half, a query that is ambiguous, or a label that was wrong, because sometimes the gold set is what failed.

For my failure analysis, I decided to use hybrid because it performed the best overall on my corpus. I looked at the five queries where hybrid performed the worst and compared the documents it returned with the ones I had marked as relevant. My goal was to understand why the system struggled with these questions and what changes I could make to improve its performance.

| qid | what the best system returned | what was relevant | cause | what you would try |
|---|---|---|---|---|
| c03 – 34 CFR 668.34 | Hybrid returned documents about consumer information, school audits, and other regulations that did not answer the query. | BM25 found all three relevant documents in its top 3, but hybrid did not return any of them in its top 10. | Rank fusion issue. Since dense did not find any of the relevant documents, combining its results with BM25 pushed the correct documents down. | I would try giving BM25 more weight when combining results. I would know it worked if the relevant documents appeared in hybrid's top 10. |
| c07 – ability to benefit | Hybrid returned documents about FAFSA benefits, Federal Work-Study, and school eligibility. | BM25 ranked the three relevant documents 1st, 3rd, and 5th, while hybrid only returned two of them at 4th and 7th. | Vocabulary mismatch and rank fusion. Dense struggled to find the documents related to the exact term, which affected hybrid's rankings. | I would try giving more weight to exact terms in the query. I would look for the relevant documents to appear higher in the results. |
| c02 – 34 CFR 685.304 | Hybrid returned documents about Direct Loans, consumer information, and loan counseling. | There were four relevant documents, but hybrid only returned two in its top 10, at ranks 2 and 3. | Similar regulatory references. Several documents contained CFR references, but not all of them were useful for answering this specific query. | I would try giving more weight to exact regulation numbers. I would know it helped if hybrid returned more of the relevant documents in its top 10. |
| c11 – mom lost her job | Hybrid returned documents about Perkins Loans, financial management, and FAFSA corrections. | Four documents were marked relevant, but hybrid only found two in its top 10, at ranks 2 and 10. | Vocabulary mismatch. The question was written the way a student would ask it, while the handbook uses terms like professional judgment and special circumstances. | I would try expanding the query with terms like professional judgment and income adjustment. I would check whether this helped the system find the special-cases chapter. |
| c13 – leftover money after tuition | Hybrid returned documents about Work-Study payments, post-withdrawal disbursements, and other financial aid payments. | Three documents were marked relevant, but hybrid only found two in its top 10, at ranks 2 and 8. | Ambiguous query. The system seemed to have trouble distinguishing between a regular financial aid credit balance and other types of payments. | I would try adding terms like Title IV credit balance and payment deadline to the query. I would know it worked if the system ranked the correct credit-balance information higher. |

**Overall Pattern**

After looking at these five queries, I noticed that hybrid struggled in two different ways. For identifier queries, BM25 was sometimes able to find the correct documents, but combining its results with dense caused those documents to rank lower or disappear from the top 10. For paraphrase queries, the system seemed to struggle more with connecting the way a student asks a question to the terminology used in the handbook.

Based on these results, I think giving BM25 more weight for identifier queries and expanding paraphrase queries with related terminology could help improve hybrid's performance. I would want to test these changes and compare the results before deciding whether they actually improve the system.

---

## 7. Cross-corpus comparison

The two tables to compare are the shared-corpus scores in section 1 and your own-corpus scores in section 4, with their intervals.
If you want them side by side, copy the rows you need into a table here and say that you copied them.

Did the winner change between the shared corpus and yours?
Why, or why not: what is different about the two collections (document length, vocabulary, identifiers, near-duplicates, how the queries were written), and which of your explanations did you test and which are guesses?
Say what 20 queries on one side and your gold-set size on the other cannot support.

After comparing the results from the shared corpus and my own corpus, I found that the system with the highest scores changed. On the shared corpus, rerank performed the best, while on my Federal Student Aid Handbook corpus, hybrid had the highest overall scores. I copied the scores from sections 1 and 4 into the table below to make the differences easier to compare.

| System | Shared MRR@10 | Own MRR@10 |
| --- | ---: | ---: |
| bm25 | 0.507 | 0.829 |
| dense | 0.562 | 0.883 |
| hybrid | 0.471 | 0.892 |
| rerank | 0.800 | 0.862 |

One thing I found interesting was that rerank performed noticeably better than the other systems on the shared corpus. The confidence intervals supported this as well, since rerank's differences from all three other systems were distinguishable. For example, rerank performed better than hybrid by 0.329 MRR@10, with a 95% interval of [+0.164, +0.504]. However, on my corpus, even though hybrid had the highest averages, none of the differences between the systems were distinguishable. For example, hybrid was ahead of BM25 by 0.063 MRR@10, but its interval of [-0.071, +0.190] included zero. This means I cannot say hybrid was definitively better than the other systems based on my results.

I believe one reason for the difference is the way the two corpora were structured. The shared corpus contained 2,484 documents with a median length of 68 words, while my corpus contained 312 documents with a median length of 1,603 words. This is a fairly large difference in document length. Most of the shared documents could fit into a single chunk, while the documents in my corpus needed to be divided into multiple chunks. Since dense uses the best matching chunk to score a document, I think this could have affected which documents were retrieved and how they were ranked. However, I did not directly test whether this difference in document length caused the change in performance.

Another difference I noticed was how the systems handled identifiers and paraphrased questions. On both corpora, BM25 performed well when queries contained specific terminology. However, on the shared corpus, BM25 had an MRR@10 of 0.000 for paraphrase queries, compared with 0.579 on my corpus. I think this may be related to how the questions were written. The shared practice questions were provided by the instructor, while my own gold set included questions I wrote and questions drafted by Claude. Some of the shared paraphrase questions were also written to avoid the exact wording found in the regulations, which may have made them more difficult for BM25.

I was able to examine some of this through my hand and Claude query comparisons. My hand-written queries had a content-word overlap of 0.92 with their best relevant documents, compared with 0.84 for the Claude queries. This suggests that the wording of the questions may have influenced the retrieval results. However, I cannot say that this explains the differences between the two corpora because I did not test the same questions or query-writing methods on both collections.

I also tested whether changing the chunk size would improve dense retrieval on my corpus. My hypothesis was that reducing the chunk size from 300 to 150 words would help the system identify specific terms more easily. Instead, MRR@10 decreased by 0.102, with a 95% interval of [-0.226, +0.006]. Since the interval included zero, the difference was not distinguishable. This did not provide evidence that smaller chunks improved performance, but it also does not prove that chunk size has no effect. I also considered whether similar or repeated documents affected the results, but I did not directly measure near-duplicates in either corpus, so that explanation is still a guess.

Finally, I think the number of queries used is important when looking at these results. The shared corpus had 20 judged queries, while my corpus had 30. For MRR@10, the minimum detectable differences on the shared corpus ranged from 0.192 to 0.412, while on my corpus they ranged from 0.098 to 0.232. This means that smaller differences could have gone undetected, especially with only 20 queries. Just because two systems were not distinguishable does not mean they performed exactly the same.

Overall, I found that rerank was the clear winner on the shared corpus based on the confidence intervals, while hybrid only had the highest observed scores on my corpus. I believe the differences in document length, terminology, and how the queries were written could have contributed to this result, but I only tested some of these explanations. Since the corpora also used different questions, query classes, and relevance judgments, I cannot determine exactly how much of the difference came from the documents themselves. What this comparison showed me is that a system performing the best on one corpus does not guarantee it will perform the same way on another, and that the confidence intervals are important when deciding what the results actually support.

---

## 8. Stretch

498E: the stretch is one of the six options in the brief's "One stretch" section, and that section says what earns the 25 points for each.
It is optional, so `uv run p2 check --final` never waits on this section.
598E: the rider is your stretch, so write "rider" below and put its results in section 9; the other options add no points, because the project is capped at 150.

Whichever option you chose, write these five things:

1. The option's name.
2. What you did, and the files that hold it.
3. The table `p2 score` wrote for it, by name: one of the three below, `own-ablation` and `own-ablation-queries` in section 5 for a second ablation, `own-origins` in section 4 for the hand and claude queries, or `repeats` in section 9 for the rider.
4. What its interval lets you claim, and what it does not.
5. One thing you would do next, and what result would tell you it worked.

For a second ablation, write its hypothesis here before you run it, and commit it, so your history shows that it came first.
For the hand and claude queries, do the same with your prediction before you score.

### Claim-level faithfulness check (option 2)

Claude's verdicts from `p2 judge` against your own verdicts in the calibration file.

<!-- p2:begin stretch-judge -->
_No judged answers yet (stretch option 2): `uv run p2 judge answers/shared/LABEL.json` writes them, your own verdicts go in answers/shared/LABEL.calibration.tsv, and then `uv run p2 score` fills this table._
<!-- p2:end stretch-judge -->

### Cost and latency (option 3)

The Claude calls, tokens and seconds in every trace you committed, and what a cheaper system or answers file saves against what it loses.

<!-- p2:begin stretch-cost -->
Every trace in traces/ that records a Claude call:

| Trace | System | Spans | Claude calls | Saved | Input tokens | Output tokens | Seconds | Input per span | Output per span | Seconds per span |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| traces/answers-rerank.jsonl | rerank | 12 | 24 | 4 | 129,886 | 4,254 | 145.2 | 10,824 | 354 | 12.1 |
| traces/answers-rerank.r1.jsonl | rerank | 12 | 24 | 0 | 136,854 | 4,229 | 129.8 | 11,404 | 352 | 10.8 |
| traces/answers-rerank.r2.jsonl | rerank | 12 | 24 | 0 | 137,104 | 4,225 | 110.5 | 11,425 | 352 | 9.2 |
| traces/answers-rerank.r3.jsonl | rerank | 12 | 24 | 0 | 132,365 | 4,056 | 129.6 | 11,030 | 338 | 10.8 |
| traces/own-own-rerank.jsonl | rerank | 30 | 30 | 2 | 225,807 | 3,059 | 87.0 | 7,527 | 102 | 2.9 |
| traces/shared-practice-rerank.jsonl | rerank | 20 | 20 | 2 | 212,861 | 2,153 | 206.5 | 10,643 | 108 | 10.3 |
| traces/shared-practice-rerank.r1.jsonl | rerank | 20 | 20 | 0 | 151,826 | 1,911 | 80.7 | 7,591 | 96 | 4.0 |
| traces/shared-practice-rerank.r2.jsonl | rerank | 20 | 20 | 0 | 140,877 | 1,820 | 87.5 | 7,044 | 91 | 4.4 |
| traces/shared-practice-rerank.r3.jsonl | rerank | 20 | 20 | 0 | 162,702 | 2,040 | 94.1 | 8,135 | 102 | 4.7 |
| traces/shared-test-rerank.jsonl | rerank | 40 | 40 | 0 | 430,147 | 4,280 | 280.3 | 10,754 | 107 | 7.0 |

A span is one query of a run, one question of an answers file, or one claim of a judged file. A saved reply costs nothing now, so it counts the tokens and the seconds of the call that made it.

Every pair of systems on the same queries where at least one calls Claude, the one with fewer Claude input tokens per query first:

| Cheaper minus dearer | Queries | MRR@10 difference | 95% interval | Input tokens saved per query | Seconds saved per query | Reading |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| shared practice: bm25 minus rerank | 20 | -0.293 | [-0.533, -0.043] | 10,643 | 10.3 | rerank higher |
| shared practice: dense minus rerank | 20 | -0.237 | [-0.408, -0.083] | 10,643 | 10.3 | rerank higher |
| shared practice: hybrid minus rerank | 20 | -0.329 | [-0.504, -0.164] | 10,643 | 10.3 | rerank higher |
| own: bm25 minus rerank | 30 | -0.033 | [-0.194, +0.125] | 7,527 | 2.9 | not distinguishable |
| own: dense minus rerank | 30 | +0.021 | [-0.111, +0.149] | 7,527 | 2.9 | not distinguishable |
| own: hybrid minus rerank | 30 | +0.029 | [-0.108, +0.168] | 7,527 | 2.9 | not distinguishable |

The difference is the cheaper system's score minus the dearer one's, with its paired interval; the savings count Claude calls only, so a system that makes none saves all of the other's.

Systems that do not call Claude, from traces/retrieval/ on the machine that last ran `p2 score` (git ignores that folder, so `p2 check` does not compare this part):

| Trace | System | Queries | Seconds | Milliseconds per query |
| --- | --- | ---: | ---: | ---: |
| traces/retrieval/own-own-ablation-dense_c150.jsonl | dense_c150 | 30 | 0.30 | 10.0 |
| traces/retrieval/own-own-bm25.jsonl | bm25 | 30 | 0.11 | 3.6 |
| traces/retrieval/own-own-dense.jsonl | dense | 30 | 0.23 | 7.6 |
| traces/retrieval/own-own-hybrid.jsonl | hybrid | 30 | 0.45 | 14.9 |
| traces/retrieval/shared-practice-bm25.jsonl | bm25 | 20 | 0.07 | 3.4 |
| traces/retrieval/shared-practice-dense.jsonl | dense | 20 | 0.29 | 14.6 |
| traces/retrieval/shared-practice-hybrid.jsonl | hybrid | 20 | 0.53 | 26.5 |
| traces/retrieval/shared-test-bm25.jsonl | bm25 | 40 | 0.21 | 5.3 |
| traces/retrieval/shared-test-dense.jsonl | dense | 40 | 0.54 | 13.5 |
| traces/retrieval/shared-test-hybrid.jsonl | hybrid | 40 | 0.88 | 21.9 |
<!-- p2:end stretch-cost -->

### The grep agent (option 5)

Your stretch run on some of your own queries against the four systems on the same queries.

<!-- p2:begin stretch-agent -->
_No stretch runs yet (stretch option 5): `uv run p2 run --corpus own --queries eval/own/agent.queries.tsv --system agent --stretch` writes one to runs/own/stretch/, then `uv run p2 score` fills this table._
<!-- p2:end stretch-agent -->

### Your stretch

For my stretch, I completed the rider option, which involved repeating rerank on the shared corpus and testing a pre-registered claim on my own corpus.

What I did: I ran rerank three additional times, with the results saved in runs/shared/rerank.practice.r1.trec through rerank.practice.r3.trec and their traces in traces/. I also repeated the answers three times, saved in answers/shared/rerank.r1.json through rerank.r3.json. My pre-registration was saved in PREREG.md and committed as c0f5832 before my first judgments in 8ab5fa8. My final gold set contained 30 queries in eval/own/queries.tsv and 147 judgments in eval/own/qrels.txt.

Results: The repeats table in section 9 contains my repeated rerank and answer results, while the own-pairs table in section 4 contains the results for my pre-registered claim.

What the intervals showed: The repeated runs supported rerank's improvement over hybrid, with an MRR@10 difference of +0.329 and a 95% interval of [+0.164, +0.504]. However, my pre-registered prediction that dense would outperform rerank was not supported. Dense only had an MRR@10 advantage of +0.021, with an interval of [-0.111, +0.149]. This means smaller differences are still possible, but the results do not support the improvement I originally expected.

What I would try next: I would test the systems on more queries to see whether the results remain consistent with a larger gold set. I would especially want to add more shared questions to narrow the Wilson confidence intervals for verified and declined answers. I would know this helped if the intervals became narrower while the results remained consistent with what I observed in section 9.

---

## 9. 598E only - repeats and the pre-registered claim

498E students can leave this section as it is; nothing checks it.
598E students replace each line that starts with "598E: write", and `uv run p2 check --final` counts those lines as work still to do until they are gone.

### Repeats on the shared corpus

Three runs of the reranker on the practice queries, and three answers files, with their run-to-run spread and Wilson intervals.

<!-- p2:begin repeats -->
Repeated runs of rerank on shared/practice:

| Run | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| rerank.r1 | 0.758 | 0.800 | 0.754 |
| rerank.r2 | 0.758 | 0.800 | 0.761 |
| rerank.r3 | 0.758 | 0.800 | 0.765 |
| range (max minus min) | 0.000 | 0.000 | 0.011 |

| Comparison | Metric | Mean difference | 95% interval | Reading |
| --- | --- | ---: | ---: | --- |
| rerank.r1 minus hybrid | Recall@10 | +0.167 | [+0.058, +0.292] | rerank.r1 higher |
| rerank.r2 minus hybrid | Recall@10 | +0.167 | [+0.058, +0.292] | rerank.r2 higher |
| rerank.r3 minus hybrid | Recall@10 | +0.167 | [+0.058, +0.292] | rerank.r3 higher |
| rerank.r1 minus hybrid | MRR@10 | +0.329 | [+0.164, +0.504] | rerank.r1 higher |
| rerank.r2 minus hybrid | MRR@10 | +0.329 | [+0.164, +0.504] | rerank.r2 higher |
| rerank.r3 minus hybrid | MRR@10 | +0.329 | [+0.164, +0.504] | rerank.r3 higher |
| rerank.r1 minus hybrid | nDCG@10 | +0.310 | [+0.186, +0.439] | rerank.r1 higher |
| rerank.r2 minus hybrid | nDCG@10 | +0.318 | [+0.194, +0.446] | rerank.r2 higher |
| rerank.r3 minus hybrid | nDCG@10 | +0.322 | [+0.196, +0.450] | rerank.r3 higher |

Repeated answers shared/rerank:

| File | Verified (in) | 95% interval | Declined (out) | 95% interval |
| --- | ---: | ---: | ---: | ---: |
| rerank.r1 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| rerank.r2 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| rerank.r3 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| range (max minus min) | 0.000 |  | 0.000 |  |

Each repeat answers the same questions, so the repeats are not independent trials and their counts are not pooled into one interval.
<!-- p2:end repeats -->

Does the reranker's gain over its first stage survive the run-to-run variation?
Write what the spread is, how it compares with the gain, and what the Wilson intervals on the verified share and the declined share say about 8 and 4 questions.

After running rerank three additional times on the shared corpus, I found that its performance remained consistent across each run. Recall@10 stayed at 0.758 and MRR@10 stayed at 0.800, giving both a range of 0.000. nDCG@10 showed a small amount of variation, ranging from 0.754 to 0.765. When comparing rerank to hybrid, the MRR@10 improvement remained +0.329 with a 95% confidence interval of [+0.164, +0.504]. Since the improvement was much larger than the variation between runs, I believe this supports that rerank's improvement over hybrid was consistent.

I also looked at the repeated answers and found that each run verified 8 out of 8 in-corpus answers and correctly declined 4 out of 4 out-of-corpus questions. However, the Wilson confidence intervals were [0.676, 1.000] for verified answers and [0.510, 1.000] for declined answers. This means that even though the system received perfect scores, the small number of questions does not guarantee the same performance on a larger set. I also noticed that the original answers file contained 13 claims while each repeat contained 12, showing that the answers were not completely identical.

Overall, I found that rerank's improvement over hybrid survived the variation between runs. The performance differences were much larger than the small changes between repeats, and the confidence intervals supported the improvement. However, since the repeats used the same questions, I cannot treat them as independent tests or combine their results to make the intervals smaller.

### The pre-registered claim

The claim, the smallest effect, the gold-set size and the test are in `PREREG.md`, committed before your own gold-set judgments.
Here, say whether you followed the plan, what the interval turned out to be, and what that means.
The outcome section of `PREREG.md` holds the short version.

For my pre-registered claim, I predicted that dense would perform better than rerank on MRR@10 by at least 0.20. I estimated that I would need around 29 queries, and my final gold set contained 30 queries with 147 relevance judgments. I followed my original testing plan, although I replaced c01 before making any judgments and expanded the judging pool twice by adding 44 documents from rerank and 40 from dense_c150. My hypothesis, effect size, and decision rule remained the same.

After evaluating the systems, dense performed slightly better than rerank, with an MRR@10 difference of +0.021 and a 95% confidence interval of [-0.111, +0.149]. Since the interval included zero, the difference was not distinguishable. The interval also stayed within my original threshold of ±0.20, meaning the results did not support an improvement as large as I predicted. The minimum detectable difference was 0.189, which was slightly smaller than my planned effect size of 0.20.

Overall, my original prediction was not supported. Even though dense had a slightly higher MRR@10, the difference was too small to conclude that it performed better than rerank. Based on my pre-registered decision rule, the interval rules out a difference as large as 0.20, but smaller differences between the systems are still possible.
