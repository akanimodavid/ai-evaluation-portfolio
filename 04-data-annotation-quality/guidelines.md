# Annotation Guidelines: Mobile Banking Customer Messages

All items are synthetic, written for this project.

## Task

Classify short customer messages about mobile banking into one of five categories based on their meaning. Each message must receive exactly one label.

## Labels

| Label | Definition |
|---|---|
| Complaint | A message reporting a problem that has already happened to the customer, expressing dissatisfaction, or describing a failure, delay, wrong charge or missing item. |
| Request | A message asking the bank to perform a specific action on the customer's account or transaction, or asking for a change to the app or service, such as a new feature. |
| Question | A message asking for information, clarification, or whether something is possible, without reporting a customer problem or requesting a specific action. |
| Praise | A message expressing satisfaction, gratitude or appreciation without a complaint or request taking priority. |
| Other | A message that does not fit Complaint, Request, Question or Praise, such as a neutral statement or unrelated message. |

## Rules for borderline cases

1. **Priority order:** If a message contains more than one intent, use the first applicable label in this order: Complaint, Request, Question, Praise, Other.
2. **Complaint test:** A message is a Complaint if it reports a problem that has already happened to the customer (such as a failure, delay, wrong charge or missing item), or uses clear words expressing frustration or dissatisfaction.
3. **Request vs Question:** If the message directly asks the bank to do or check something for the customer ("can you…", "please…", "help me…", "I want to…"), label it Request, even when it is phrased as a question. If it only asks whether something is possible or how it works ("is it possible…", "is there a way…", "what is…"), label it Question.
4. **Praise:** Use Praise when the message expresses satisfaction or appreciation and no higher-priority label applies.
5. **Language:** Judge the meaning, not spelling, grammar or style. Informal English, abbreviations and typos do not change the label.
6. **Feature requests:** A request for a new feature or a change to the app or service is a Request.
7. **Reversals:** A request to reverse or refund a charge, with no problem stated, is a Request. If the message says the charge was wrong, unauthorised or duplicated, it is a Complaint under Rule 2.

## Examples

| # | Item | Label | Reason |
|---|---|---|---|
| 1 | My transfer failed, but the money was deducted from my account. | Complaint | The customer reports a transaction problem. |
| 2 | What is the daily transfer limit on my account? | Question | The customer is requesting information. |
| 3 | Please block my ATM card immediately. | Request | The customer asks the bank to perform an action. |
| 4 | Your mobile app is easy to use. Thank you! | Praise | The customer expresses appreciation. |
| 5 | Why has my transfer still not arrived? I've been waiting since yesterday. | Complaint | The customer reports a delay. |
| 6 | Can you reverse the $50 debit on my account? | Request | The customer asks for a specific action (Rule 7). |
| 7 | Thank you for helping me recover my account, but I still haven't received my refund. | Complaint | The unresolved problem takes priority over praise. |
| 8 | Is there a way to increase my transfer limit? | Question | The customer asks about a general possibility (Rule 3). |
| 9 | Nice app! Please add a dark mode. | Request | A feature request takes priority over praise (Rules 1 and 6). |
| 10 | Can you help me check whether my account is eligible for a loan? | Request | The customer directly asks the bank to check something on the account (Rule 3). |