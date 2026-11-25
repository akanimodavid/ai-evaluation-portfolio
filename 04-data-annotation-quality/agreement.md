# Agreement Between Two Annotators

This agreement test used the [guidelines](guidelines.md) as they stood before the test. The guidelines were frozen before annotation to ensure both annotators used the same classification rules.

- **Annotator 1:** Human annotator and author of the guidelines.
- **Annotator 2:** Claude, an AI model, which independently labelled all 32 items using the written guidelines.

Both annotators completed their labels independently. The labels were compared only after both annotation sets had been completed.

## Disclosure

Annotator 2 was an AI model (Claude), not a human annotator. It was provided with the same dataset and written guidelines and completed a separate annotation without access to Annotator 1's labels.

This evaluation measures human–AI agreement, not human–human inter-annotator agreement. AI-generated labels were treated as annotations for comparison, not as ground truth.

## Labels Side by Side

| Item | Annotator 1 | Annotator 2 | Match |
|---|---|---|---|
| 1 | Request | Request | Yes |
| 2 | Complaint | Complaint | Yes |
| 3 | Complaint | Complaint | Yes |
| 4 | Question | Question | Yes |
| 5 | Complaint | Complaint | Yes |
| 6 | Question | Question | Yes |
| 7 | Complaint | Complaint | Yes |
| 8 | Request | Request | Yes |
| 9 | Praise | Praise | Yes |
| 10 | Other | Other | Yes |
| 11 | Question | Question | Yes |
| 12 | Complaint | Complaint | Yes |
| 13 | Request | Praise | No |
| 14 | Question | Question | Yes |
| 15 | Request | Request | Yes |
| 16 | Complaint | Complaint | Yes |
| 17 | Request | Request | Yes |
| 18 | Other | Other | Yes |
| 19 | Complaint | Complaint | Yes |
| 20 | Request | Request | Yes |
| 21 | Praise | Praise | Yes |
| 22 | Question | Question | Yes |
| 23 | Complaint | Complaint | Yes |
| 24 | Question | Request | No |
| 25 | Question | Question | Yes |
| 26 | Complaint | Complaint | Yes |
| 27 | Complaint | Complaint | Yes |
| 28 | Question | Question | Yes |
| 29 | Request | Request | Yes |
| 30 | Complaint | Complaint | Yes |
| 31 | Complaint | Complaint | Yes |
| 32 | Complaint | Complaint | Yes |

## Agreement Table

Rows represent Annotator 1; columns represent Annotator 2.

| A1 \ A2 | Complaint | Request | Question | Praise | Other | Total |
|---|---:|---:|---:|---:|---:|---:|
| Complaint | 13 | 0 | 0 | 0 | 0 | 13 |
| Request | 0 | 6 | 0 | 1 | 0 | 7 |
| Question | 0 | 1 | 7 | 0 | 0 | 8 |
| Praise | 0 | 0 | 0 | 2 | 0 | 2 |
| Other | 0 | 0 | 0 | 0 | 2 | 2 |
| **Total** | **13** | **7** | **7** | **3** | **2** | **32** |

## Agreement Measures

### Percent Agreement

The annotators agreed on 30 of the 32 items.

30 ÷ 32 × 100 = **93.75%**

### Chance Agreement

Expected agreement was calculated using the annotators' category distributions:

\[
P_e = \frac{(13 \times 13)+(7 \times 7)+(8 \times 7)+(2 \times 3)+(2 \times 2)}{32^2}
\]

\[
P_e = \frac{284}{1024} \approx 0.277
\]

**Expected chance agreement: 0.277 (27.7%)**

### Cohen's Kappa

\[
\kappa = \frac{P_o-P_e}{1-P_e}
\]

\[
\kappa = \frac{0.9375-0.277}{1-0.277}
\]

\[
\kappa \approx 0.91
\]

**Cohen's kappa: 0.91**

This indicates very high agreement beyond that expected by chance, based on the annotators' label distributions.

However, the result should be interpreted cautiously because the dataset contains only 32 items, and the second annotator was an AI model.

## Disagreements and Guideline Issues Identified

| Item | Message | A1 | A2 | Guideline issue identified | Proposed fix |
|---|---|---|---|---|---|
| 13 | "Nice one! Your app is very easy to use. Please add a dark mode." | Request | Praise | The original Request definition did not clearly cover feature suggestions. The message combines praise with a request, creating ambiguity about which label takes priority. | Extend the Request definition to include feature suggestions and clarify the priority rule for mixed-intent messages. |
| 24 | "Can you help me check whether my account is eligible for a loan?" | Question | Request | The original Question-versus-Request rule did not clearly distinguish asking for information from asking the bank to perform an eligibility check. | Clarify the distinction between general information-seeking and requests for the bank to perform a specific check. |

These disagreements revealed areas where the original guidelines could be interpreted differently.

## Borderline Items That Matched

### Item 11

> "Is it possible to deactivate my ATM card temporarily?"

Both annotators labelled this **Question**.

This item sits near the Question–Request boundary because it concerns the customer's own card. Under the original guidelines, however, it asks whether an action is possible rather than directly asking the bank to perform that action.

### Item 15

> "Kindly reverse the money that was deducted from my account."

Both annotators labelled this **Request**.

Although the reference to deducted money suggests a possible underlying problem, the message explicitly asks the bank to perform a reversal. Under the original classification rules, the requested action takes priority over an implied complaint that is not explicitly expressed.

## Rules Changed After the Test

The agreement figures above were calculated using the original version of [guidelines.md](guidelines.md).

Following the disagreement analysis, the guidelines were revised:

- The **Request** definition was expanded to include requests for changes to the app or service, including feature suggestions.
- **Rule 3** was clarified to distinguish requests for specific actions from general information-seeking.
- Additional rules and examples were introduced to address the identified ambiguities.

Under the revised guidelines, items 13 and 24 would both be classified as **Request**. No other labels would change.

These revised classifications represent retrospective resolution of the disagreements. Because the rules were revised after the disagreements were observed, they do not constitute independent evidence that the revised guidelines improve annotation agreement.

The revised guidelines have not yet been tested through a new annotation round.

## Limitations

- **Small dataset:** Only 32 items were evaluated, so the results may not generalise to larger datasets.
- **Single human annotator:** The guidelines were written by Annotator 1, who also performed the first annotation. The guidelines were not independently developed by multiple human annotators.
- **AI annotator:** Annotator 2 was an AI model. Human–AI agreement may differ from human–human agreement.
- **Synthetic data:** All messages were created for this project and may not fully represent the ambiguity, variation, and complexity of real customer messages.
- **Limited disagreement analysis:** Only two disagreements occurred, limiting the range of guideline issues identified.
- **Post-test guideline revisions:** The revised guidelines have not been independently retested, so their effect on agreement remains unverified.

## Conclusion

The initial annotation test produced **93.75% observed agreement (30 of 32 items)** and a **Cohen's kappa of approximately 0.91**. These results indicate high agreement between the human annotator and AI annotator on this dataset.

The two disagreements identified ambiguities in the original guidelines, particularly around feature suggestions and requests for eligibility checks. The guidelines were subsequently revised to address these issues.

However, the small and synthetic dataset, the use of an AI annotator, and the fact that the revised guidelines have not yet been independently retested limit the strength of the conclusions.

The next evaluation should use the revised, frozen guidelines and a fresh dataset, with both annotators completing their annotations independently before comparison. This would provide a stronger test of whether the guideline improvements lead to more consistent annotation.