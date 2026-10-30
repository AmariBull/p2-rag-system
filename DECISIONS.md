# Decision log

Your methods section, in your own words.
About one to two pages in total.

Answer these as you go, not the night before it is due.
Each answer is easier to write while the decision is still fresh, and prompt 1 only works if you write it before you see your own-corpus numbers.
Specifics beat polish: a short, honest answer with a number in it is worth more than a long vague one.

Each prompt ends with a marker line.
Replace that line with your answer.
`uv run p2 check` reports a marker as unfinished work, and `uv run p2 check --final` fails while any marker is left, so a finished log is part of being done.

Please do not let the agent write these for you.
These answers are about what you chose and what you knew, and the agent cannot know that.
Prompt 3 in particular only works in your own words.

---

## 1. Why this corpus, and what you expected

Why did you pick the corpus you used in stage 2, and why does it belong to a field or a question you care about?
Then say what you expected before you measured anything: which of `bm25`, `dense`, `hybrid` and `rerank` do you think will win on it, and which will do worst, and why?

Commit this answer before your first `uv run p2 score` on the own corpus.
Git history then shows that the expectation came first, which is what lets it be wrong in a way that teaches you something.
If you were surprised later, say so in prompt 4 or in EVAL.md; do not come back and rewrite this one.

The corpus I decided to use in stage 2 was the Federal Student Aid handbook from the Federal Student Aid website. My goal with choosing this documentation was to develop and answer questions on a set that I had experience with and ample knowledge about.

Before measuring anything and after doing initial review of the performance of the models on the provided corpus, I believe that hybrid or rerank will win on it. I say this because the questions that I plan to supply my gold set will be a combination of items that judge the models ability to identify based on terminology straight from the handbook, paraphrase based on language from a student asking and an answer that the document would have, and a combination of both. My questions will be structured this way in order to test a variety of options that may be brought to the system and determine how well it performs on more than just simple requests. I hypothesize that bm25 may perform the worst simply because of the importance of paraphrasing that some of my questions will do. Plus, given my initial runs I have found that paraphrasing is the worst metric that bm25 produces. I am excited to see if these assumptions will be true or what will surprise me later on.

---

## 2. A fork in the road

Name one real design choice where you could have gone two ways: the chunk size, the embedding model, how the two systems are fused, how many documents the reranker sees, a sentence in `prompts/answer.txt`, how you cleaned the corpus.

Say which you picked, what the alternative was, and what you gave up by not taking it.
If you measured both, give both numbers.
If you rejected the alternative without measuring it, say why that was a fair call, and what it cost you in time, tokens or complexity.

"There was no alternative" is not an answer.
Find the fork.

One fork I ran into was with deciding which embedding model to use, the options were between bge-small and two other models one of which was potion-retrieval that ran faster but was not as precise in paraphrasing and another that was bge-small with a query instruction added to each query. I decided to move forward with the bge-small because although it took a longer time to run I had believed that the result would be more detailed results especially when it came to the paraphrasing measure that it was ran against. By not taking the alternative I resulted in an increase to 0.714 on the paraphrase compared to the bm25 class but it cost me time in about 5 minutes that was used to initially run the model. I plan on still measuring the performance of potion to be sure that this was the right choice but as for right now I am going to continue runs with bge-small.

---

## 3. Where you overruled the agent

One time Claude suggested, wrote or claimed something and you did not take it.
It might be a relevance judgment you disagreed with, a retriever it called finished when a run file showed otherwise, a number it summarized wrongly, or a license it said was fine.

What did it do?
How did you notice?
What did you do instead?

If it genuinely never happened, say so plainly, and then say what you would have had to check in order to notice.
Being honest here costs you far less than a story you cannot defend when you record your video.

One time I overruled Claude was when I was expanding my judging pool for rerank. Claude recommended that I only judge rerank's top 2 results, which would have added 12 documents. However, I decided to judge all 44 documents from rerank's top 5 instead because I wanted to make sure the evaluation was fair and that I was not leaving out potentially relevant documents.

I noticed that only judging 12 documents could leave some of rerank's results unjudged, which might affect how its performance was measured compared with the other systems. After adding all 44 documents and reviewing their relevance, the MRR@10 difference between rerank and dense changed from -0.060 to -0.021.

Overall, I decided not to follow Claude's recommendation because I wanted the judging pool to be more complete rather than taking the shorter approach. This showed me that even when an agent suggests something that would save time, I still need to consider whether that suggestion could affect the reliability of my results.

---

## 4. A number you do not trust

Pick one number in `EVAL.md` that you do not fully trust, and say why.
It could be a mean over a small query class, a difference whose interval includes zero, a verified share of 100%, a score on a gold set you wrote yourself, or a result you got only once.

What would have to be true for you to trust it?
Did you do anything to test it, and what did that show?

One number in my evaluation that I do not fully trust is the MRR@10 score for my own corpus, where the systems scored between 0.829 and 0.892. Even though these results showed fairly good performance, I noticed that my relevance judgments only covered the top 5 results from each system. This meant that between 66 and 97 of each system's 300 top-10 results were still unjudged and counted as not relevant, even though some of them could have contained useful information.

I think this could have affected the scores because the systems may have retrieved relevant documents that were never judged. I was able to test this partly when I expanded the judging pool to include rerank's top 5 results. After reviewing those additional documents, rerank's MRR@10 increased from 0.823 to 0.862. This showed me that the relevance judgments could change the evaluation results without changing the retrieval system itself.

Overall, I would trust these scores more if I reviewed all of the top 10 results from each system and made sure every document was judged using the same relevance rule. Although I expanded the judging pool and saw the scores change, I did not complete a full top-10 judgment pass. Because of this, I think the current results are useful for comparing the systems, but I cannot assume they represent their full retrieval performance.

---

## 5. What is still wrong

One thing in your system, your corpus or your gold set that is not right, not finished, or that you do not fully understand.

What would you do next, and how would you find out whether it matters?
Name the file, the query or the document where someone could look.

One thing I noticed that still needs improvement is how hybrid handles identifier queries. For example, on query c03, which asked about 34 CFR 668.34, BM25 ranked all three relevant documents in its top 3 results, while hybrid did not return any of them in its top 10. This was surprising because hybrid combines BM25 and dense, so I expected it to benefit from BM25 finding the correct documents.

I think the problem may be related to how the rankings are combined. Since dense did not retrieve the relevant documents, combining the two rankings may have pushed BM25's correct results further down. To improve this, I would try giving BM25 more weight during rank fusion in p2/retrievers/hybrid.py and compare the results against the original rankings in runs/own/hybrid.trec.

Overall, I would test this change on the identifier queries in my gold set and compare Recall@10 and MRR@10 before and after. I would know the change helped if hybrid started returning the relevant documents for c03 in its top 10 and improved its overall identifier performance without hurting the other query classes. This would help me determine whether changing the fusion weights actually fixes the problem or if something else is affecting the rankings.
