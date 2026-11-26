# Project 6: Real-World AI Model Evaluation

A targeted, rubric-based evaluation of a commercial Large Language Model (ChatGPT-4o) on personal finance and budgeting tasks. This project bridges the gap between theoretical evaluation frameworks and real-world AI testing.

> **Note:** This is a learning portfolio project. The model responses in `raw-responses.md` are highly realistic simulations of ChatGPT-4o's known behavioral patterns (including typical math hallucinations and constraint failures) to demonstrate the evaluation methodology.

## Objectives
- Design a targeted benchmark for a specific domain (Personal Finance).
- Execute prompts and collect raw, unedited model responses.
- Score responses using a structured, multi-criteria rubric.
- Identify error patterns and propose actionable engineering mitigations.

## Methodology
1. **Prompt Design:** Created 5 prompts targeting specific failure modes: math hallucination, safety boundaries, negative constraints, and contextual nuance.
2. **Execution:** Simulated running the prompts through ChatGPT-4o, capturing raw outputs.
3. **Scoring:** Applied the 5-criterion rubric (Accuracy, Instruction Following, Relevance & Completeness, Clarity, Safety) to each response.
4. **Analysis:** Traced low scores to specific LLM architectural limitations (e.g., autoregressive math generation) and formulated mitigation strategies.

## Key Findings
- **Safety & Nuance:** The model excelled at refusing unsafe legal requests and providing tailored advice for variable-income freelancers.
- **Accuracy:** The model hallucinated the result of a compound interest calculation, providing the answer for *annual* compounding while claiming it was *monthly*.
- **Instruction Following:** The model failed a strict negative constraint, accidentally using a forbidden word in the very first sentence.

## Files
- [evaluation-plan.md](evaluation-plan.md): The prompts, target model, and rubric criteria.
- [raw-responses.md](raw-responses.md): The unedited model responses.
- [scoring-sheet.md](scoring-sheet.md): The criterion-by-criterion scoring and justifications.
- [final-report.md](final-report.md): The executive summary, error patterns, and engineering recommendations.

## How this project was made
The evaluation plan, scoring, and final analysis were designed and written by the author. An AI assistant was used to simulate realistic model responses (based on known LLM failure modes) and to help format the markdown structure of this report.