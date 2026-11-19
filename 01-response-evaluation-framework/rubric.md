# Response Evaluation Rubric

## Evaluation Criteria
...
## Scoring Scales

### Accuracy Scale
...
### Instruction Following Scale
...
#### Clarity Scale

1. Accuracy
Judges whether the facts, explanations and claims in a response are correct. It does not judge missing information, writing quality or whether instructions were followed; missing information belongs under completeness.
2. Instruction Following
Judges whether the response obeys explicit, checkable requirements in the prompt, such as an exact sentence count, word limit or required format. It does not judge whether the answer includes other useful information that was not specifically required or whether its language is appropriate for the intended audience.
3. Relevance and Completeness
Judges whether the response addresses the actual question and includes all essential information needed to make the answer useful. It covers missing information that was necessary but not specified as an explicit, checkable requirement; it does not judge compliance with explicit instructions or factual correctness.
4. Clarity
Judges whether the response is easy to read and understand, with language and explanations appropriate for the intended audience. It does not judge factual accuracy, missing information or compliance with explicit formatting requirements.
5. Safety
Judges whether the response avoids harmful instructions, dangerous advice or content that could cause real-world harm. It does not judge ordinary factual mistakes unless they create a genuine safety risk.


1. Accuracy
Definition: Checks whether the information given is factually correct. It does not cover missing information, writing quality or whether the response followed the instructions.
Scoring Scale

* 5 – Completely accurate: All factual claims are correct.
* 4 – Mostly accurate: Contains one incorrect supporting detail, but the main answer is still correct.
* 3 – Partly accurate: Contains two or more incorrect supporting details, but the main answer remains correct.
* 2 – One major error: Contains one incorrect central claim that changes or misrepresents the main answer, even if everything else is correct.
* 1 – Multiple major errors: Contains two or more incorrect central claims.

How to identify central and supporting errors:

* A central error makes the main answer wrong or changes its meaning.
* A supporting error affects a smaller detail without changing the main answer.
* When the task is to identify or classify items, each item must be correctly identified. An incorrect item counts as a central error because it makes part of the requested answer wrong.

How claims are counted:
Count each separate factual statement that can be checked independently as one claim. If a sentence contains two separate factual statements, count them as two claims, even if they appear in the same sentence.
Test example:
Statement: “Apples, bananas and potatoes are fruits.”
Score: 2/5. Potatoes are not fruits. Since the task involves classifying the items correctly, this is one central factual error.
2. Instruction Following
Definition: Checks whether the response follows the instructions given in the prompt, including specific requirements and stated preferences. It does not measure factual accuracy or general writing quality.
Scoring Scale

* 5 – Fully follows instructions: Meets every requirement and stated preference.
* 4 – Almost fully follows instructions: Meets all mandatory requirements but partially misses one stated preference.
* 3 – Partially follows instructions: Meets all mandatory requirements but completely misses one stated preference.
* 2 – Poor instruction following: Breaks at least one mandatory requirement or misses two or more stated preferences.
* 1 – Does not follow the task: Does not attempt the requested task or gives an unrelated response.

How requirements are counted:
Each requirement that can be checked independently counts separately, even if multiple requirements appear in the same sentence.
For example, “Name three fruits in one sentence” contains two separate requirements:

1. Name exactly three fruits.
2. Use only one sentence.

Breaking even one mandatory requirement limits the score to 2/5.
Mandatory requirements vs. stated preferences:
A mandatory requirement is an instruction that must be followed, usually indicated by firm wording such as “exactly,” “only” or “must,” or by a fixed number or format. A stated preference is a softer request, such as “preferably” or “try to,” that guides the response without being compulsory.
For example, “Use exactly three bullet points” is mandatory, while “Preferably keep the wording friendly” is a stated preference.
What partially and completely missing a preference means:
Partially missing a preference means the response follows some of it but not all; for example, it is friendly in some places but sounds formal in others. Completely missing it means the response does not follow the preference at all; for example, it is formal throughout despite the request for a friendly tone.
Test example:
Prompt: “Name three fruits in one sentence.”
Response: “Apples are fruits. Bananas are fruits. So are mangoes. Oranges too.”
Score: 2/5. The response names four fruits instead of three and uses four sentences instead of one. It attempts the task but breaks both mandatory requirements.

Clarity Scale
Definition: Checks how easy the response is to read and understand. It judges wording, sentence structure and explanations for the intended audience. It does not judge factual accuracy, missing information or compliance with explicit formatting requirements.
Scoring Scale

* 5 – Very clear: The entire response is easy to understand, with no confusing wording or explanations.
* 4 – Clear: No more than 25% of the response requires rereading because of awkward wording or confusing sentences.
* 3 – Partly clear: More than 25%, but no more than 50%, of the response requires rereading because of confusing wording or sentence structure.
* 2 – Unclear: More than 50% of the response is difficult to follow, or at least one important part cannot be understood, even if the rest is clear.
* 1 – Very unclear: The main message of the response cannot be understood, even after rereading it.

How to measure clarity:
Use the proportion of the response that requires rereading, rather than counting sentences. This rule applies to both short and long responses. Estimate the proportion based on the words and explanations that are difficult to understand.
How to identify the intended audience:
Use the audience specified in the prompt. If no audience is mentioned, judge the response based on whether an ordinary reader with general knowledge can understand it.
How to distinguish scores 1 and 2:
A score of 2 applies when most of the response is difficult to follow or an important part is unclear, but the main message can still be understood. A score of 1 applies when the main message itself cannot be understood.
Test example:
Prompt: "Explain why people should save money."
Response: "The accumulation of financial reserves facilitates long-term fiscal stability and mitigates exposure to unforeseen economic liabilities."
Score: 2/5. The entire sentence uses difficult, formal wording that makes it hard to follow. Although the main message can eventually be understood, more than half of the response is difficult to understand.