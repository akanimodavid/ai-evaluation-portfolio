# Final Evaluation Report: Personal Finance AI Assistant

## 1. Executive Summary

This evaluation assessed ChatGPT's ability to handle personal finance and budgeting tasks across five test scenarios.

The evaluation examined five criteria: Accuracy, Instruction Following, Relevance & Completeness, Clarity, and Safety.

ChatGPT achieved an overall average score of **4.44/5**. It demonstrated strong performance in clarity, relevance, and safety. However, the evaluation identified weaknesses in mathematical accuracy, strict instruction following, and the qualification of financial recommendations.

The most significant errors occurred in P3, where ChatGPT provided an incorrect compound interest calculation, and P4, where it violated an explicit negative word constraint.

These findings demonstrate that a response can appear confident, clear, and useful while still containing factual or instruction-following errors.

## 2. Key Findings and Error Patterns

### 2.1 Mathematical Calculation Error (P3)

- **Observation:** ChatGPT correctly provided the monthly compound interest formula but returned an incorrect final amount of $1,967.15 instead of approximately $2,009.66.
- **Analysis:** The returned amount corresponds to annual compounding rather than monthly compounding. The model therefore failed to apply the stated calculation correctly, despite presenting the appropriate formula.
- **Impact:** This is a significant accuracy issue because users may rely on financial calculations when making decisions.
- **Recommendation:** Financial calculations should be independently verified using a calculator or deterministic calculation tool rather than relying entirely on generated numerical answers.

### 2.2 Negative Constraint Failure (P4)

- **Observation:** The prompt explicitly prohibited the words "stock", "market", and "fund". ChatGPT used the prohibited word "fund" in its opening sentence when expanding the ETF acronym.
- **Analysis:** The model understood the general concept and produced an understandable explanation, but failed to respect an explicit word restriction.
- **Impact:** This demonstrates a weakness in following strict negative constraints, even when the requirement is clearly stated.
- **Recommendation:** AI systems should use output validation to check for prohibited words or phrases before returning responses. If a violation is detected, the system can regenerate or correct the response.

### 2.3 Internal Contradiction in Budget Allocation (P1)

- **Observation:** ChatGPT correctly stated that 20% of the user's $4,000 monthly income should be allocated to savings and debt repayment. However, it listed $750 instead of the correct $800.
- **Analysis:** The response contradicted its own stated budgeting rule. The three category amounts also added up to $3,950 rather than the full $4,000.
- **Impact:** Even relatively simple financial planning tasks can contain inconsistencies when the model does not verify its calculations.
- **Recommendation:** Budgeting responses should include a calculation-validation step to confirm that category amounts and percentages add up to the stated income and allocation.

### 2.4 Safety and Contextual Relevance (P2 and P5)

- **Observation:** In P2, ChatGPT appropriately avoided providing specific bankruptcy filing instructions and recommended consulting a qualified professional. In P5, it provided relevant suggestions for managing irregular freelance income, including baseline budgeting, a larger emergency fund, and maintaining a cash buffer.
- **Analysis:** These responses demonstrated the model's ability to recognise potentially sensitive financial situations and provide generally useful guidance. However, P2 included an insufficiently qualified statement about bankruptcy reporting periods, while P5 recommended a general tax allocation without knowing the user's jurisdiction or tax circumstances.
- **Impact:** The responses were generally useful, but financial guidance still requires appropriate context and qualification.
- **Recommendation:** Financial responses should clearly distinguish general educational guidance from advice that depends on an individual's jurisdiction, financial circumstances, or professional assessment.

## 3. Recommendations for Model Improvement

Based on the observed errors, the following improvements are recommended:

### 3.1 Integrate Deterministic Calculation Tools

For prompts involving percentages, budgeting, interest rates, and compound interest, the system should use a calculator or code execution tool to verify numerical results.

This would reduce reliance on generated arithmetic and help prevent calculation errors such as the one observed in P3.

### 3.2 Implement Output Constraint Validation

A validation layer should check generated responses against explicit restrictions before they are returned to users.

For example, when a prompt prohibits certain words, the system should scan the completed response for those words and trigger correction if a violation is detected.

### 3.3 Introduce Numerical Consistency Checks

For budgeting and financial allocation tasks, the system should verify that:

- Allocated percentages add up to the intended total.
- Dollar amounts match their corresponding percentages.
- Category totals equal the stated income.
- Any adjustments are clearly explained without contradicting the original instructions.

### 3.4 Improve Contextual Qualification of Financial Advice

The system should avoid presenting general financial recommendations as universally applicable.

For example, tax allocations, bankruptcy reporting periods, and debt-management options should be qualified according to relevant jurisdictional and personal circumstances.

## 4. Evaluation Results Summary

The evaluation produced the following average scores:

| Criterion | Average Score |
|---|---:|
| Accuracy | 3.4/5 |
| Instruction Following | 4.2/5 |
| Relevance & Completeness | 4.8/5 |
| Clarity | 5.0/5 |
| Safety | 4.8/5 |
| **Overall Average** | **4.44/5** |

The results indicate that ChatGPT performed strongly in presenting understandable and relevant information but showed room for improvement in numerical accuracy and strict instruction compliance.

## 5. Limitations of the Evaluation

- The evaluation tested only one model: ChatGPT (displayed model: GPT-6).
- The evaluation used a small sample of five prompts.
- The prompts were designed by the evaluator and focused on selected financial and instruction-following scenarios.
- The scoring was conducted by one primary human evaluator, which may introduce subjective judgement.
- The results represent the model's responses during the evaluation on 25 November 2026 and do not establish performance across other versions or future updates.
- The evaluation does not establish that ChatGPT is suitable for professional financial advice.

## 6. AI Assistance Disclosure

The evaluation prompts, testing process, and scoring decisions were conducted by the project author.

An AI assistant was used to help organise the report, improve the presentation of findings, and structure the recommendations. The final scoring decisions and analysis were reviewed and approved by the project author.

## 7. Conclusion

This evaluation demonstrated that ChatGPT can produce clear, relevant, and generally responsible responses to everyday personal finance questions.

However, the results also showed that strong presentation does not guarantee accuracy or complete instruction compliance.

The compound interest error in P3 and the negative constraint failure in P4 were the clearest examples. The inconsistencies in P1 and the insufficiently qualified financial recommendations in P2 and P5 further demonstrated the importance of checking AI-generated information.

Overall, the evaluation reinforced the importance of using structured rubrics, evidence-based scoring, and independent verification when assessing AI model responses.