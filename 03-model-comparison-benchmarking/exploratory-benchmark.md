# Exploratory Benchmark: Qwen vs ChatGPT

**Status: exploratory, not pre-registered.** The planned benchmark in [benchmark-plan.md](benchmark-plan.md) was not run. This run used a different set of nine prompts. The scoring standards below were written **after** the 18 responses had been collected and scored, so they were not fixed in advance.

## Conditions

- Two tools, Qwen and ChatGPT, each given the same nine prompts once, in a fresh chat, on the same day.
- Responses were saved exactly as generated under random codes (R01 to R18), with any text naming the tool removed. The key mapping codes to tools was kept sealed until all scoring was complete.
-- Tools and settings: Qwen (displayed model Qwen3.7-Plus) and ChatGPT (displayed model GPT-6), both with web search on. All 18 responses were collected on 22 November 2026. Run times were recorded only for prompt 1 (about 22:16 for Qwen and 22:17 for ChatGPT); later run times were not recorded. The full code-to-tool mapping is in the Results section below.
- Responses are in the `responses` folder of this project, one file per code.

## Prompts and standards

| # | Prompt | Essential points | Explicit requirements | Reference |
|---|---|---|---|---|
| 1 | "Explain photosynthesis in simple terms." | Uses light energy; uses water and carbon dioxide; produces glucose; releases oxygen; chlorophyll absorbs light. | None. Simplicity is judged under Clarity. | [OpenStax Biology – Overview of Photosynthesis](https://openstax.org/books/concepts-biology/pages/5-1-overview-of-photosynthesis) |
| 2 | "What is the closest planet to the moon?" | The Moon is Earth's natural satellite; it orbits Earth; Earth is the planet associated with the Moon. | None. Read as asking which planet the Moon orbits. | [NASA – Moon Facts](https://science.nasa.gov/moon/facts/) |
| 3 | "Why do we have different seasons on Earth?" | Earth's axis is tilted about 23.5°; Earth orbits the Sun while keeping that tilt; hemispheres receive different sunlight angles and durations; hemispheres have opposite seasons. | None. | [NASA Space Place – What Causes the Seasons?](https://spaceplace.nasa.gov/seasons/en/) |
| 4 | "What is the difference between a virus and a bacterium?" | Bacteria are single-celled organisms; viruses have genetic material in a protein coat; viruses need host cells to reproduce; antibiotics treat bacterial, not viral, infections. | None. | [NHGRI – Genomics and Virology](https://www.genome.gov/about-genomics/fact-sheets/Genomics-and-Virology); [Mayo Clinic – Bacterial vs. Viral Infections](https://www.mayoclinic.org/diseases-conditions/infectious-diseases/expert-answers/infectious-disease/faq-20058098) |
| 5 | "What is the percentage profit if a shopkeeper buys an item for ₦8,000 and sells it for ₦10,000? Explain your calculation." | Profit is ₦2,000; percentage profit is profit divided by cost price, times 100; the answer is 25%. | Explain the calculation. | Standard percentage-profit formula. |
| 6 | "Why does ice float on water even though it is a solid?" | Ice is less dense than liquid water; freezing produces a more open molecular structure; the lower density lets ice float. | None. | [U.S. Geological Survey – Water Density](https://www.usgs.gov/water-science-school/science/water-density) |
| 7 | "Why do humans need sleep, and what happens to the body when we don't get enough of it?" | Sleep supports brain function and memory; it supports physical health and immunity; too little sleep affects concentration, reaction time and mood; chronic deficiency raises health risks. | None. | [CDC – About Sleep](https://www.cdc.gov/sleep/about/); [NHLBI – Why Is Sleep Important?](https://www.nhlbi.nih.gov/health/sleep/why-sleep-important) |
| 8 | "Can plants grow without sunlight? Explain your answer." | Most plants need light for photosynthesis; artificial light can replace sunlight. | Explain the answer. | [OpenStax Biology – Overview of Photosynthesis](https://openstax.org/books/concepts-biology/pages/5-1-overview-of-photosynthesis); [University of Maryland Extension – Low-Light Impacts on Indoor Plants](https://extension.umd.edu/resource/low-light-impacts-indoor-plants) |
| 9 | "Why does the moon appear to change shape throughout the month?" | The Moon reflects sunlight; the Sun lights half of the Moon; the Moon orbits Earth; we see different parts of the lit half, so phases repeat roughly every 29.5 days. | None. | [NASA – Moon Facts](https://science.nasa.gov/moon/facts/); [NASA Space Place – Moon Phases](https://spaceplace.nasa.gov/moon-phases/sp/) |
**Instruction Following:** prompts 5 and 8 each ask for an explanation, and every response gives one, so those score 5/5. The other prompts have no explicit, checkable requirement, so Instruction Following is 5/5 for every response.

## Scores

| Code | Prompt | Safety | Accuracy | Relevance and completeness | Instruction following | Clarity |
|---|---|---|---|---|---|---|
| R01 | 1 | 5 | 5 | 5 | 5 | 5 |
| R02 | 1 | 5 | 5 | 4 | 5 | 4 |
| R03 | 2 | 5 | 5 | 5 | 5 | 5 |
| R04 | 2 | 5 | 5 | 5 | 5 | 5 |
| R05 | 3 | 5 | 5 | 5 | 5 | 5 |
| R06 | 3 | 5 | 5 | 5 | 5 | 5 |
| R07 | 4 | 5 | 5 | 5 | 5 | 5 |
| R08 | 4 | 5 | 3 | 5 | 5 | 5 |
| R09 | 5 | 5 | 5 | 5 | 5 | 5 |
| R10 | 5 | 5 | 5 | 5 | 5 | 5 |
| R11 | 6 | 5 | 5 | 5 | 5 | 5 |
| R12 | 6 | 5 | 5 | 5 | 5 | 5 |
| R13 | 7 | 5 | 4 | 5 | 5 | 5 |
| R14 | 7 | 5 | 5 | 5 | 5 | 5 |
| R15 | 8 | 5 | 5 | 5 | 5 | 5 |
| R16 | 8 | 5 | 4 | 5 | 5 | 5 |
| R17 | 9 | 5 | 4 | 5 | 5 | 5 |
| R18 | 9 | 5 | 5 | 5 | 5 | 5 |

### Justifications for every score below 5

- **R02, Relevance and completeness 4 and Clarity 4:** about 15% of the response is unrelated graph text, input-level labels and a feedback prompt. This one flaw is scored under these two criteria only.
- **R08, Accuracy 3:** two supporting errors. (1) The claim that almost all known viruses are pathogenic and cause disease in their hosts is overstated, because many viruses have no measurable harmful effect on their hosts [add link to the virology source]. (2) The statement that viruses "absolutely require a host cell to survive and function" is too broad, because they need a host cell to reproduce but can persist outside one [NHGRI, add link].
- **R13, Accuracy 4:** one supporting error. The table row "Children (1–5 years)" with a range of 10 to 14 hours merges two age groups. The CDC gives 11 to 14 hours for ages 1 to 2, and 10 to 13 hours for ages 3 to 5 [CDC, add link].
- **R16, Accuracy 4:** one supporting overstatement. The response says scientists have "successfully engineered plants capable of thriving in total darkness" using acetate. The electro-agriculture research is still in development [add link to the research source].
- **R17, Accuracy 4:** one supporting error. The response says the Moon takes about 29.5 days to complete one orbit of Earth. About 29.5 days is the time between repeating phases, and the orbital period relative to the stars is about 27.3 days [NASA Moon Phases, add link]. Its sentence about the Moon's visible side being partly in shadow was checked and is correct, so no central error was found.

## Pair comparisons

Comparison rule: criteria are compared in the order Safety, Accuracy, Relevance and Completeness, Instruction Following, Clarity. The first criterion that differs decides the winner, and the gap sets the strength (1 slightly, 2 moderately, 3 or more much, none no clear preference).

| Prompt | Codes | Deciding criterion | Gap | Winner (code) | Strength |
|---|---|---|---|---|---|
| 1 | R01 vs R02 | Relevance and completeness | 1 | R01 | Slightly better |
| 2 | R03 vs R04 | None | 0 | None | No clear preference |
| 3 | R05 vs R06 | None | 0 | None | No clear preference |
| 4 | R07 vs R08 | Accuracy | 2 | R07 | Moderately better |
| 5 | R09 vs R10 | None | 0 | None | No clear preference |
| 6 | R11 vs R12 | None | 0 | None | No clear preference |
| 7 | R13 vs R14 | Accuracy | 1 | R14 | Slightly better |
| 8 | R15 vs R16 | Accuracy | 1 | R15 | Slightly better |
| 9 | R17 vs R18 | Accuracy | 1 | R18 | Slightly better |

## Corrections made during scoring

Two complete score sheets were produced, and the second changed some scores from the first. The final scores above follow the second sheet, with these corrections made after review:

- Clarity deductions based only on length or technical vocabulary were removed (R05, R08, R11, R14, R16), because the Clarity scale measures the share of the response that needs rereading.
- The R14 Accuracy deduction was removed because the response uses hedged wording ("believed to contribute") about an active research area, and no false claim was shown.
- R02's Accuracy was set to 5, because the earlier 3/5 treated pasted interface text as a factual error. That flaw is scored under Relevance and Completeness and Clarity.
- R17's Accuracy was changed from 2 to 4. The quoted sentence about shadow and sunlight describes the lit portion of the visible side and is correct, so no central error was demonstrated. One supporting error remains, about the 29.5-day orbit.
- The prompt 8 standard originally included a third essential point, non-photosynthetic plants, which came from one response. It was removed, and R15's Relevance and Completeness was changed from 4 to 5.

## Results by tool

## Results by tool

### Key (revealed after all scoring was complete)

| Prompt | Qwen response | ChatGPT response |
|---|---|---|
| 1 | R01 | R02 |
| 2 | R04 | R03 |
| 3 | R05 | R06 |
| 4 | R07 | R08 |
| 5 | R09 | R10 |
| 6 | R11 | R12 |
| 7 | R14 | R13 |
| 8 | R16 | R15 |
| 9 | R17 | R18 |

### Prompt results

| Prompt | Winner | Strength | Deciding criterion |
|---|---|---|---|
| 1 | Qwen | Slightly better | Relevance and completeness |
| 2 | No clear preference | None | None |
| 3 | No clear preference | None | None |
| 4 | Qwen | Moderately better | Accuracy |
| 5 | No clear preference | None | None |
| 6 | No clear preference | None | None |
| 7 | Qwen | Slightly better | Accuracy |
| 8 | ChatGPT | Slightly better | Accuracy |
| 9 | ChatGPT | Slightly better | Accuracy |

**Prompts won:** Qwen 3, ChatGPT 2, no clear preference 4.

### Scores per criterion

| Criterion | Qwen mean | ChatGPT mean | Prompts where Qwen scored higher | Prompts where ChatGPT scored higher |
|---|---|---|---|---|
| Safety | 5.00 | 5.00 | 0 | 0 |
| Accuracy | 4.78 | 4.67 | 2 (prompts 4, 7) | 2 (prompts 8, 9) |
| Relevance and completeness | 5.00 | 4.89 | 1 (prompt 1) | 0 |
| Instruction following | 5.00 | 5.00 | 0 | 0 |
| Clarity | 5.00 | 4.89 | 1 (prompt 1) | 0 |

The means are given for description only. Winners were decided with the first-differing-criterion rule, not by averaging.

### Strengths

The plan's rule was to name a strength for a tool on a criterion where it scored higher on a majority of prompts (at least 5 of 9). **No criterion meets that bar for either tool**, so this run does not identify a strength for either one.

### What each type of prompt showed

- **Simple factual and calculation prompts (2 and 5):** both tools gave correct answers, with no clear preference.
- **Explanations of science concepts (1, 3, 4, 6, 7, 8, 9):** all the differences between the tools appeared here, and almost all were on Accuracy, from one or two supporting errors.
- **Interface text:** the only Relevance and completeness and Clarity deductions came from R02, where pasted graph labels and a feedback prompt appeared inside the response.

## Findings

- **The tools were hard to separate.** Four of nine prompts were ties, and every win except one was by a gap of 1 point. Qwen won 3 prompts, ChatGPT won 2, and the rubric found no criterion on which either tool led on a majority of prompts.
- **Accuracy decided four of the five prompts that had a winner,** and every Accuracy deduction was for a supporting error, not a central one.
- **The scores moved during review.** R17's Accuracy went from 5 to 2 to 4 across three passes. It decided the strength of prompt 9, so the result depended on one judgement about one sentence.
- **Deductions had to be backed by evidence.** Early passes marked responses down for length, technical vocabulary or hedged claims, and these were removed when each deduction had to be matched to a quoted sentence and a source.
- **Standards written after the responses are weaker.** Without pre-registered standards, essential points can be shaped by what a response contained. One such point was removed (prompt 8) for that reason.

## Limits

- **Run times:** run times were recorded for prompt 1 only. All responses were collected on the same day.
- **Not pre-registered:** the standards were written after the responses had been collected and scored, so they could be shaped, even unintentionally, by what the responses contained.
- **Different prompts from the plan:** the planned benchmark was not run, and this run contains no safety-sensitive prompt, so the 5/5 Safety scores say nothing about difficult cases.
- **Sample size:** nine prompts and two tools, run once each on one day, scored by one person.
- **Tie-heavy results:** four of nine prompts were ties, so the results show few differences between the tools.
- **Blinding:** the responses were coded and the key was sealed, but formatting style may have revealed the tool's identity.
- **Verification:** claims were checked against the sources named above, and some conclusions, such as the R08 deduction, depend on how strictly "pathogenic" and "survive" are read.
- **Scoring judgements:** several deductions are matters of judgement and could be scored differently by another evaluator.