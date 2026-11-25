# Project 3: AI Model Comparison and Benchmarking

A blinded comparison of two AI chat assistants, Qwen and ChatGPT, on nine explanation and calculation prompts, scored with the five-criterion rubric from [Project 1](../01-response-evaluation-framework/rubric.md).

> **Note:** This is a learning portfolio project. The benchmark run was **exploratory**: its standards were written after the responses were collected, and it does not follow the plan that was written beforehand.

## What was planned and what was run

- [benchmark-plan.md](benchmark-plan.md) is a pre-registered plan with nine different prompts, including Nigerian-context and safety prompts, with essential points and requirements written before anything was run.
- The nine-prompt set that was actually run was different (photosynthesis, the Moon, seasons, viruses, profit, ice, sleep, plants and sunlight, lunar phases), so the planned benchmark has not been carried out.
- [exploratory-benchmark.md](exploratory-benchmark.md) records the exploratory run in full: the prompts, the standards (written afterwards), 18 scored responses, the comparisons, the key and the limits.
- The 18 responses are in [responses](responses), one file per code.

## Method

1. Same nine prompts, one run each, fresh chat, web search on for both tools, same day.
2. Responses saved under random codes, with any text naming the tool removed. The key stayed sealed until all scoring was done.
3. Each response scored on Safety, Accuracy, Relevance and Completeness, Instruction Following and Clarity, with a justification for each score below 5.
4. For each prompt, the first criterion (in that order) where the scores differ decides the winner, and the score gap gives the strength: 1 slightly, 2 moderately, 3 or more much.

## Results

**Prompts won:** Qwen 3, ChatGPT 2, no clear preference 4.

| Prompt | Winner | Strength | Deciding criterion |
|---|---|---|---|
| 1. Explain photosynthesis in simple terms | Qwen | Slightly better | Relevance and completeness |
| 2. Closest planet to the Moon | No clear preference | None | None |
| 3. Why do we have different seasons | No clear preference | None | None |
| 4. Virus versus bacterium | Qwen | Moderately better | Accuracy |
| 5. Percentage profit (₦8,000 to ₦10,000) | No clear preference | None | None |
| 6. Why ice floats | No clear preference | None | None |
| 7. Why humans need sleep | Qwen | Slightly better | Accuracy |
| 8. Can plants grow without sunlight | ChatGPT | Slightly better | Accuracy |
| 9. Why the Moon changes shape | ChatGPT | Slightly better | Accuracy |

No criterion shows either tool scoring higher on a majority of prompts, so no strength is claimed for either tool.

## Two decisions in detail

**Prompt 4 (Qwen moderately better):** the ChatGPT response (R08) lost two Accuracy points for two supporting claims: that almost all known viruses are pathogenic, and that viruses "absolutely require a host cell to survive and function". The Qwen response (R07) had no deduction. Accuracy is the first criterion that differs, and the gap is 2. Full justifications are in [exploratory-benchmark.md](exploratory-benchmark.md).

**Prompt 9 (ChatGPT slightly better):** the Qwen response (R17) was marked down one Accuracy point for saying that the Moon takes about 29.5 days to complete one orbit of Earth. That figure is the time between repeating phases, and the orbital period relative to the stars is about 27.3 days. An earlier scoring pass treated one of its sentences about shadow as a central error and scored it 2/5, but the sentence describes the lit part of the visible side and is correct, so the final score is 4/5.

## Findings

- The tools were hard to separate: four of nine prompts were ties, and every win except one was by one point.
- Accuracy decided four of the five prompts that had a winner, always through supporting errors.
- One scoring decision (R17) moved between 5, 2 and 4 during review and set the strength of prompt 9.
- Deductions based on length, vocabulary or hedged wording were removed when each deduction had to be matched to a quoted sentence and a source.

## Limitations

- Not pre-registered: the scoring standards were written after the responses were collected.
- The planned prompts were not run, and this run has no safety-sensitive prompt, so the 5/5 Safety scores say nothing about difficult cases.
- Nine prompts, two tools, one run each, one day, one evaluator.
- Formatting may have revealed the tool despite coding.
- Several deductions are judgement calls that another evaluator could score differently.

## Recommendations

- Run the pre-registered plan, which includes Nigerian-context and safety prompts.
- Use harder prompts, several runs per prompt, and a second evaluator.
- Fix the scoring standards before collecting any responses.

## Files

- [benchmark-plan.md](benchmark-plan.md)
- [exploratory-benchmark.md](exploratory-benchmark.md)
- [responses](responses)