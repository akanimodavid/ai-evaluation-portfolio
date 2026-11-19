# Response Evaluation Rubric

## Evaluation Criteria

### 1. Accuracy
Judges whether the facts, explanations and claims in a response are correct. It does not judge missing information, writing quality or whether instructions were followed; missing information belongs under completeness.

### 2. Instruction Following
Judges whether the response obeys explicit, checkable requirements in the prompt, such as an exact sentence count, word limit or required format. It does not judge whether the answer includes other useful information that was not specifically required or whether its language is appropriate for the intended audience.

### 3. Relevance and Completeness
Judges whether the response addresses the actual question and includes all essential information needed to make the answer useful. It covers missing information that was necessary but not specified as an explicit, checkable requirement; it does not judge compliance with explicit instructions or factual correctness.

### 4. Clarity
Judges whether the response is easy to read and understand, with language and explanations appropriate for the intended audience. It does not judge factual accuracy, missing information or compliance with explicit formatting requirements.

### 5. Safety
Judges whether the response avoids harmful instructions, dangerous advice or content that could cause real-world harm. It does not judge ordinary factual mistakes unless they create a genuine safety risk.

## Scoring Scales

### Accuracy Scale

- **5 – Completely accurate:** All factual claims are correct.
- **4 – Mostly accurate:** Contains one incorrect supporting detail, but the main answer is still correct.
- **3 – Partly accurate:** Contains two or more incorrect supporting details, but the main answer remains correct.
- **2 – One major error:** Contains one incorrect central claim that changes or misrepresents the main answer, even if everything else is correct.
- **1 – Multiple major errors:** Contains two or more incorrect central claims.

**How to identify central and supporting errors:**

- A central error makes the main answer wrong or changes its meaning.
- A supporting error affects a smaller detail without changing the main answer.
- When the task is to identify or classify items, each item must be correctly identified. An incorrect item counts as a central error because it makes part of the requested answer wrong.

**How claims are counted:** Count each separate factual statement that can be checked independently as one claim. If a sentence contains two separate factual statements, count them as two claims, even if they appear in the same sentence.

**Test example:**

**Prompt:** "Name three fruits."

**Response A (synthetic):** "Apples, bananas and mangoes."

**Response B (synthetic):** "Apples, bananas and potatoes."

**Response A**

| Criterion | Score | Justification |
|---|---|---|
| Accuracy | 5/5 | All three items are fruits. |
| Instruction following | 5/5 | Names three fruits, as requested. |
| Clarity | 5/5 | A short, plain list. |

**Response B**

| Criterion | Score | Justification |
|---|---|---|
| Accuracy | 2/5 | Potatoes are not fruits. Since the task involves classifying the items correctly, this is one central factual error. |
| Instruction following | 5/5 | Names three items, as requested. |
| Clarity | 5/5 | A short, plain list. |

**Overall:** A is much better than B. Both responses follow the instruction and are equally clear, so the only difference is accuracy, 5/5 against 2/5. B names a vegetable as a fruit, which makes part of the requested answer wrong.

**Why these scores:**

- **Accuracy 2/5 for B, not 3 or 4.** The task is to identify items, so a wrong item is a central error, not a supporting detail.
- **Instruction following and clarity are not reduced for B.** The mistake is a factual one, so it is penalised under Accuracy only.

### Instruction Following Scale

- **5 – Fully follows instructions:** Meets every requirement and stated preference.
- **4 – Almost fully follows instructions:** Meets all mandatory requirements but partially misses one stated preference.
- **3 – Partially follows instructions:** Meets all mandatory requirements but completely misses one stated preference.
- **2 – Poor instruction following:** Breaks at least one mandatory requirement or misses two or more stated preferences.
- **1 – Does not follow the task:** Does not attempt the requested task or gives an unrelated response.

**How requirements are counted:** Each requirement that can be checked independently counts separately, even if multiple requirements appear in the same sentence. For example, "Name three fruits in one sentence" contains two separate requirements:

1. Name exactly three fruits.
2. Use only one sentence.

Breaking even one mandatory requirement limits the score to 2/5.

**Mandatory requirements vs. stated preferences:** A mandatory requirement is an instruction that must be followed, usually indicated by firm wording such as "exactly," "only" or "must," or by a fixed number or format. A stated preference is a softer request, such as "preferably" or "try to," that guides the response without being compulsory. For example, "Use exactly three bullet points" is mandatory, while "Preferably keep the wording friendly" is a stated preference.

**What partially and completely missing a preference means:** Partially missing a preference means the response follows some of it but not all; for example, it is friendly in some places but sounds formal in others. Completely missing it means the response does not follow the preference at all; for example, it is formal throughout despite the request for a friendly tone.

**Test example:**

**Prompt:** "Name three fruits in one sentence."

**Response A (synthetic):** "Apples, bananas and mangoes are fruits."

**Response B (synthetic):** "Apples are fruits. Bananas are fruits. So are mangoes. Oranges too."

**Response A**

| Criterion | Score | Justification |
|---|---|---|
| Accuracy | 5/5 | All three items are fruits. |
| Instruction following | 5/5 | Names exactly three fruits in one sentence, meeting both mandatory requirements. |
| Clarity | 5/5 | One short, plain sentence. |

**Response B**

| Criterion | Score | Justification |
|---|---|---|
| Accuracy | 5/5 | All four items are fruits. |
| Instruction following | 2/5 | The response names four fruits instead of three and uses four sentences instead of one. It attempts the task but breaks both mandatory requirements. |
| Clarity | 5/5 | The sentences are short and easy to understand. |

**Overall:** A is much better than B. Both are accurate and clear, so the difference is instruction following, 5/5 against 2/5. B breaks the two requirements that the prompt stated.

**Why these scores:**

- **Instruction following 2/5 for B, not 3.** The prompt contains two separate mandatory requirements, and B breaks both. Breaking even one caps the score at 2.
- **Accuracy is not reduced for B.** Everything it says is correct, so the failure is one of instructions only.

### Clarity Scale

- **5 – Very clear:** The entire response is easy to understand, with no confusing wording or explanations.
- **4 – Clear:** No more than 25% of the response requires rereading because of awkward wording or confusing sentences.
- **3 – Partly clear:** More than 25%, but no more than 50%, of the response requires rereading because of confusing wording or sentence structure.
- **2 – Unclear:** More than 50% of the response is difficult to follow, or at least one important part cannot be understood, even if the rest is clear.
- **1 – Very unclear:** The main message of the response cannot be understood, even after rereading it.

**How to measure clarity:** Use the proportion of the response that requires rereading, rather than counting sentences. This rule applies to both short and long responses. Estimate the proportion based on the words and explanations that are difficult to understand.

**How to identify the intended audience:** Use the audience specified in the prompt. If no audience is mentioned, judge the response based on whether an ordinary reader with general knowledge can understand it.

**How to distinguish scores 1 and 2:** A score of 2 applies when most of the response is difficult to follow or an important part is unclear, but the main message can still be understood. A score of 1 applies when the main message itself cannot be understood.

**Test example:**

**Prompt:** "Explain why people should save money."

**Response A (synthetic):** "Saving money gives you a safety net for emergencies and helps you reach big goals."

**Response B (synthetic):** "The accumulation of financial reserves facilitates long-term fiscal stability and mitigates exposure to unforeseen economic liabilities."

**Response A**

| Criterion | Score | Justification |
|---|---|---|
| Accuracy | 5/5 | Saving money does provide a cushion for emergencies and helps people fund larger goals. |
| Instruction following | 5/5 | The prompt sets no explicit requirements, and the response explains why people should save. |
| Clarity | 5/5 | Plain wording throughout, and nothing needs rereading. |

**Response B**

| Criterion | Score | Justification |
|---|---|---|
| Accuracy | 5/5 | The claims are correct; it says the same thing as A in formal language. |
| Instruction following | 5/5 | The prompt sets no explicit requirements, and the response explains why people should save. |
| Clarity | 2/5 | The entire sentence uses difficult, formal wording that makes it hard to follow. Although the main message can eventually be understood, more than half of the response is difficult to understand. |

**Overall:** A is much better than B. Both are correct and answer the prompt, so the difference is clarity, 5/5 against 2/5. B says the same thing as A, but in wording that an ordinary reader would have to reread.

**Why these scores:**

- **Clarity 2/5 for B, not 1.** The main message can still be understood after rereading, which is what separates a 2 from a 1.
- **Accuracy is not reduced for B.** Difficult wording is a clarity problem, not a factual one.