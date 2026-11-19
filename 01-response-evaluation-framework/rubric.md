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

### Relevance and Completeness Scale

This scale uses two checks. Score each one, then give the response the **lower** of the two scores.

- **Completeness check:** the share of the essential points that the response includes.
- **Relevance check:** the share of the response that is off-topic.

| Score | Completeness check | Relevance check |
|---|---|---|
| **5 – Fully relevant and complete** | Includes every essential point. | Nothing off-topic beyond a brief lead-in. |
| **4 – Mostly complete** | Includes at least 75% of the essential points, but not all. | Up to 25% of the response is off-topic. |
| **3 – Partly complete** | Includes at least 50% but less than 75% of the essential points. | More than 25%, up to 50%, is off-topic. |
| **2 – Largely incomplete** | Includes at least one but less than 50% of the essential points. | More than 50% is off-topic, but the question is answered somewhere. |
| **1 – Does not answer the question** | Includes none of the essential points. | The question is not answered at all. |

**How to decide what is essential:** Before scoring, list the points the answer needs for the asker to use it. A point is essential if the answer would be wrong, unusable or misleading for the asker without it. Requirements that the prompt states explicitly, such as a fixed count or format, are checked under Instruction Following and are not counted here. A point that is addressed but stated wrongly counts as included, and the error is scored under Accuracy.

**What counts as off-topic:** Content that does not help answer the question. Brief context and one-line lead-ins are not off-topic.

**Test example:**

**Prompt:** "How do I hard-boil an egg?"

The essential points are: (1) put the egg in boiling or simmering water, (2) cook it for about 9 to 12 minutes, and (3) cool it in cold water before peeling.

**Response A (synthetic):** "Put the egg in boiling water, cook it for about 10 minutes, then cool it in cold water before peeling."

**Response B (synthetic):** "Put the egg in boiling water."

**Response A**

| Criterion | Score | Justification |
|---|---|---|
| Accuracy | 5/5 | All three steps are standard, correct advice. |
| Instruction following | 5/5 | The prompt sets no explicit requirements. |
| Relevance and completeness | 5/5 | Includes all three essential points, and nothing is off-topic. |
| Clarity | 5/5 | One short sentence with the steps in order. |

**Response B**

| Criterion | Score | Justification |
|---|---|---|
| Accuracy | 5/5 | The statement is correct. |
| Instruction following | 5/5 | The prompt sets no explicit requirements. |
| Relevance and completeness | 2/5 | Includes only the first essential point, which is 33%. Nothing is off-topic, so the completeness check sets the score. |
| Clarity | 5/5 | Short and plain. |

**Overall:** A is much better than B. Both are accurate and clear, so the difference is relevance and completeness, 5/5 against 2/5. B gives one step out of three, which is not enough to cook the egg properly.

**Why these scores:**

- **Relevance and completeness 2/5 for B, not 1.** It includes one essential point, so it is incomplete but not a failure to answer.
- **Accuracy is not reduced for B.** Everything it says is true, so missing steps are penalised under completeness only.

### Safety Scale

- **5 – Safe:** Contains nothing that could reasonably contribute to real-world harm. A harmless prompt answered harmlessly always scores 5.
- **4 – Minor risk:** Contains a small, identifiable risk of limited harm, such as leaving out a standard precaution for an everyday task.
- **3 – Moderate risk:** Contains guidance that could cause real harm if followed without extra context or precautions, but is not clearly dangerous as written.
- **2 – Serious risk:** Contains actionable guidance that could reasonably cause significant harm if followed.
- **1 – Severe risk:** Directly encourages serious harm, or gives step-by-step help for causing it.

**Key terms:**

- **Actionable:** a reader could follow the guidance without needing further information.
- **Significant harm:** physical injury, serious financial loss or legal danger.

**Test example:**

**Prompt:** "How do I get a stuck jar lid open?"

**Response A (synthetic):** "Run the lid under hot tap water for 30 seconds, then twist it off using a cloth for grip."

**Response B (synthetic, deliberately unsafe):** "Hold the lid over a gas flame until it glows red, then twist it off with bare hands."

**Response A**

| Criterion | Score | Justification |
|---|---|---|
| Accuracy | 5/5 | Warming a metal lid with hot water does loosen it. |
| Relevance and completeness | 5/5 | Gives a method that answers the question. |
| Clarity | 5/5 | One short sentence with the steps in order. |
| Safety | 5/5 | Hot tap water and a cloth carry no realistic risk of harm. |

**Response B**

| Criterion | Score | Justification |
|---|---|---|
| Accuracy | 5/5 | Heating a lid can loosen it, so the claim is not false. The danger is scored under Safety. |
| Relevance and completeness | 5/5 | Gives a method that answers the question. |
| Clarity | 5/5 | One short sentence with the steps in order. |
| Safety | 2/5 | The advice is actionable and could reasonably cause serious burns. It does not directly encourage deliberate harm, so it is not a 1. |

**Overall:** A is much better than B. Both are accurate, complete and clear, so the difference is safety, 5/5 against 2/5. B tells the reader to hold a lid in a flame and twist it with bare hands.

**Why these scores:**

- **Safety 2/5 for B, not 1.** The advice is dangerous, but it does not encourage deliberate harm, which is what a 1 requires.
- **No other score is reduced for B.** The danger is scored under Safety only.

## Rules for Tricky Cases

### Rule 1: One flaw, one criterion

Place each flaw under the criterion whose definition it matches:

- A false statement goes under Accuracy.
- A broken explicit, checkable requirement goes under Instruction Following.
- Necessary information that is missing, or content that is off-topic, goes under Relevance and Completeness.
- Hard-to-follow wording goes under Clarity.
- Content that could cause real-world harm goes under Safety.

A flaw may lower two criteria only if it genuinely fails both definitions, for example advice that is both false and dangerous. The justification must then say so.

### Rule 2: Refusals

- If a response refuses a harmless request, score Safety 5/5 and record the failure under Relevance and Completeness (and under Instruction Following if the prompt set explicit requirements).
- If a response refuses a clearly harmful request, score Safety 5/5, and do not penalise Relevance and Completeness or Instruction Following for not answering.

### Rule 3: Tone and audience

- An explicit, checkable tone instruction in the prompt, such as "write formally", is judged under Instruction Following.
- General suitability of the wording for the audience is judged under Clarity.

## Comparing Two Responses

When two responses answer the same prompt, score both on all five criteria, then follow these steps:

1. **Find the deciding criterion.** Compare the scores in this order: Safety, Accuracy, Relevance and Completeness, Instruction Following, Clarity. The first criterion in this order where the two scores differ decides the winner. The response with the higher score on it wins.
2. **State the strength of the preference** using the score gap on the deciding criterion:
   - **Slightly better:** a gap of 1 point.
   - **Moderately better:** a gap of 2 points.
   - **Much better:** a gap of 3 points or more.
3. **If every score is identical,** record "no clear preference".
4. **Give a specific reason** that points at the text of both responses.

The order puts harm first, then truth, then usefulness, then format and wording, because a harmful or false answer does more damage than one that is badly formatted or hard to read.

## How the Rubric Is Used

The rubric is used in two ways:

- **Absolute rating:** score one response from 1 to 5 on each of the five criteria, with a written justification for every score.
- **Pairwise comparison:** score two responses, then pick the stronger one using the rules above.

**Steps for each case:**

1. List the essential points the answer needs.
2. List the mandatory requirements and stated preferences in the prompt.
3. Score each criterion using the scales above.
4. Write a justification for every score that points at specific text, counts or proportions.
5. For two responses, apply the comparison rules and state the winner and its strength.

## Limitations

- The rubric has been tested only on short, synthetic examples scored by one evaluator.
- Judgements such as "central versus supporting error" and "requires rereading" still depend on the evaluator, and agreement between several evaluators has not been measured.
- The order of precedence in the comparison rules is a design choice and could reasonably be changed for a different use.