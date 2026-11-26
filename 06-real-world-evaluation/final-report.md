# Final Evaluation Report: Personal Finance AI Assistant

## Executive Summary
This evaluation assessed ChatGPT-4o's capability to handle personal finance and budgeting tasks. The model demonstrated strong safety guardrails and excellent contextual relevance for complex scenarios (like variable income). However, it exhibited two critical weaknesses: a mathematical hallucination when calculating compound interest, and a failure to adhere to strict negative word constraints. 

## Key Findings & Error Patterns

1. **Mathematical Hallucination in Formulas (P3):** 
   - *Observation:* The model correctly recited the monthly compound interest formula but outputted the mathematical result for *annual* compounding ($1,967.15 instead of ~$2,009.66). 
   - *Pattern:* LLMs are language predictors, not calculation engines. When a prompt requires multi-step arithmetic, the model often "hallucinates" a plausible-looking number that matches a related (but incorrect) calculation path.

2. **Negative Constraint Failure (P4):** 
   - *Observation:* The prompt forbade the words 'stock', 'market', or 'fund'. The model immediately failed by writing "Exchange-Traded Fund" in the first sentence.
   - *Pattern:* LLMs struggle with negative constraints ("do not use X") because the token for the forbidden word must still be activated in the model's attention mechanism to avoid it, often leading to accidental inclusion.

3. **Minor Internal Contradiction (P1):** 
   - *Observation:* The model stated the 20% savings target but then populated the table with $750 (18.75%) to "give flexibility," contradicting the strict 50/30/20 rule it just explained.

4. **Strong Safety and Nuance (P2, P5):** 
   - *Observation:* The model flawlessly refused to provide unauthorized legal forms (P2) and provided highly specific, actionable advice for freelance variable income (P5), proving its training data includes high-quality financial planning heuristics.

## Recommendations for Model Improvement

1. **Integrate a Code Interpreter / Calculator Tool:** For any prompt containing financial formulas, percentages, or explicit math requests, the system should automatically route the calculation to a deterministic Python sandbox or calculator API, rather than relying on autoregressive token prediction.
2. **Pre-Flight Negative Constraint Checker:** Implement a lightweight classification layer that scans the generated output for forbidden tokens *before* returning the response to the user. If a forbidden token is detected, trigger a regeneration.
3. **Self-Correction Prompting:** For budgeting tasks, add a hidden system prompt that instructs the model to "verify that the sum of the table rows equals the total percentage and total dollar amount before outputting."

## Limitations of this Evaluation
- This evaluation used a single model (ChatGPT-4o) on a small sample size (5 prompts).
- The prompts were designed by the evaluator, which may introduce subtle bias toward testing specific known LLM weaknesses.
- An AI assistant was used to help format this report and structure the findings, though all scoring and analysis were conducted by the human evaluator.