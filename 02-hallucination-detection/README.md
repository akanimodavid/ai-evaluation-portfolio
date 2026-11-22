# Project 2: AI Hallucination Detection

A method for finding and classifying hallucinations in AI-generated text, tested on three synthetic cases with planted errors and two real AI responses.

> **Note:** This is a learning portfolio project. Cases 1 to 3 are synthetic, with prompts and responses written for this project. The two real-response checks use responses from real AI tools, recorded with the tool name and date. Nothing here is professional client work.

## Objectives

- Define the main types of hallucination and a repeatable way to check for them.
- Check every claim in a response against a named source, and record the verdict.
- Score each response with the Accuracy scale from [Project 1](../01-response-evaluation-framework/rubric.md).
- Improve the rubric using the problems that appear during testing.

## Problem statement

AI responses can state false or unsupported information as confidently as correct information, so tone is not evidence. A reviewer needs a method that breaks a response into single claims, checks each one against sources, and records the result in a way another person can repeat.

## Types of hallucination

| Type | Meaning | Example from this project |
|---|---|---|
| Fabricated fact | Something that does not exist, such as an invented journal, award or quotation | An invented "International Golden Landmark Award" |
| Wrong fact | A real thing with a wrong detail | The Eiffel Tower placed in Lyon |
| Unsupported claim | A claim no source could confirm, such as an opinion presented as fact | "The most beautiful tower ever built" |
| Contradiction | A summary that conflicts with its source passage | A construction year that differs from the passage |
| Addition | A summary that adds a detail not in the passage | An invented number of countries |

## Method

1. Split the response into **single claims**, one checkable fact per row.
2. Check each claim against a **named source with a link**. For summaries, the source is the passage.
3. Record a **verdict**: Supported, Contradicted, Cannot verify or Sources disagree.
4. Record the **type** for any claim that is not supported.
5. Choose the **main subject** of the prompt, then classify each error as **central** (changes the main answer) or **supporting** (a side detail).
6. Score with the Accuracy scale: one central error gives 2/5, two or more central errors give 1/5, and two or more supporting errors give 3/5.

Claims that depend on the same invented item are counted as one when scoring.

## Cases

### Case 1: The Eiffel Tower (general knowledge, synthetic)

**Prompt:** "Tell me about the Eiffel Tower."

**Response:** "The Eiffel Tower is a famous landmark located in Lyon, France. It was built for the 1889 World's Fair, which celebrated the 100th anniversary of the French Revolution. Construction began on January 26, 1887, and was completed on March 31, 1889. The project involved engineers Maurice Koechlin and Émile Nouguier, architect Stephen Sauvestre, and Gustave Eiffel's company. In 1999, the tower received the International Golden Landmark Award. It is widely regarded as the most beautiful tower ever built."

| Error | Verdict | Type | Severity | Evidence |
|---|---|---|---|---|
| Located in Lyon | Contradicted | Wrong fact | Central | The official Eiffel Tower website places it in Paris |
| 1999 International Golden Landmark Award | Cannot verify, no record found | Fabricated fact | Supporting | Exact-phrase search found no record |
| Most beautiful tower ever built | Cannot verify | Unsupported claim | Not counted | A subjective opinion |

**Source conflict:** the start of construction is given as 26 January 1887 by the official site and 28 January 1887 by Wikipedia. The verdict is "Sources disagree", and it is not counted as an error.

**Score:** 2/5, with one central error and one supporting error. If the invented award were central, there would be two central errors and the score would be 1/5. I class it as supporting because it does not change what the tower is.

Full claim table: [test-cases.md](test-cases.md).

### Case 2: International Space Station (summary faithfulness, synthetic)

**Source passage (adapted from the introduction of Wikipedia's "International Space Station" article):** "The International Space Station (ISS) is a large space station assembled and maintained in low Earth orbit by a collaboration of five space agencies. Its construction began in 1998 with the launch of the Zarya module. The ISS serves as a microgravity and space environment research laboratory in which scientific research is conducted in astrobiology, astronomy, meteorology, physics, and other fields. The station is suited for the testing of spacecraft systems and equipment required for missions to the Moon and Mars. It has been continuously occupied since November 2000, making it the longest continuous human presence in space."

**Summary:** "The International Space Station is a large space station maintained in low Earth orbit by a collaboration of five space agencies. Its construction began in 2005 with the launch of the Zarya module. The station serves as a research laboratory for fields like astrobiology and physics. It has hosted researchers from over 50 different countries and has been continuously occupied since November 2000."

| Error | Verdict | Type | Severity |
|---|---|---|---|
| Construction began in 2005 | Contradicted by the passage (it says 1998) | Contradiction | Supporting |
| Researchers from over 50 countries | Not in the passage | Addition | Supporting |

**Main subject:** what the ISS is and what it is used for.

**Score:** 3/5, with two supporting errors. The score depends on the main subject. If the main subject included the station's history, the construction year would be central and the score would be 2/5.

Full claim table: [test-cases.md](test-cases.md).

### Case 3: Rosalind Franklin (invented sources, synthetic)

**Prompt:** "Tell me about Rosalind Franklin and her work on DNA."

**Response:** "Rosalind Franklin was an English chemist who specialised in X-ray crystallography, and her measurements of DNA fibres were central to working out the molecule's structure. Her famous Photograph 51, captured in 1952, provided crucial evidence of the helical structure of DNA. In 1953, she published a paper with Maurice Wilkins in the Journal of Molecular Genetics detailing this structure. Reflecting on her research, Franklin said, 'The structure of DNA is a locked door, and I hold the only key.' She died of lung cancer in 1958 at the age of 37. In 1962, James Watson, Francis Crick, and Maurice Wilkins were awarded the Nobel Prize in Physiology or Medicine for their discoveries concerning the molecular structure of nucleic acids."

| Error | Verdict | Type | Severity | Evidence |
|---|---|---|---|---|
| Paper co-authored with Wilkins | Cannot verify, no record found | Fabricated fact | Supporting | The real 1953 paper in *Nature* was by Franklin and Gosling |
| Published in the *Journal of Molecular Genetics* | Cannot verify, no record found | Fabricated fact | Supporting | The real journal is *Nature*, volume 171, pages 740 to 741 |
| "Locked door" quotation | Cannot verify, no record found | Fabricated fact | Supporting | Not in Wikiquote's sourced list or the NLM biographical overview |
| Died of lung cancer | Contradicted | Wrong fact | Supporting | She died of ovarian cancer |

The invented co-author and journal belong to the same citation, so they count as one error.

**Main subject:** Franklin's work on DNA and what it showed about the molecule's structure.

**Score:** 3/5, with three supporting errors. Two alternative readings change it. If the main subject were her life and work, the cause of death would be central and the score would be 2/5. If the quotation were also central, there would be two central errors and the score would be 1/5.

Full claim table: [test-cases.md](test-cases.md).

## Real-response checks

Two real responses from AI tools, checked claim by claim with no planted errors.

| Check | Tool | Date | Claims checked | Errors found | Accuracy score |
|---|---|---|---|---|---|
| Buchi Emecheta and her best-known novels | Qwen (model version not shown) | 22 November 2026 | 27 | None | 5/5 |
| Funmilayo Ransome-Kuti and her activism | ChatGPT (as recorded in the check) | 22 November 2026 | 14 | None | 5/5 |

**Source conflicts found in the real responses:**

- **Emecheta:** *The Slave Girl* is dated to the Jock Campbell Award in 1978 by most sources and 1979 by a Vanguard obituary. The response's 1978 matches the stronger sources.
- **Ransome-Kuti:** some sources say she was the first woman in her town of Abeokuta to drive a car, and others say the first in Nigeria. The response hedges with "widely recognized", so it is not an error.

The full claim tables, source weighing, omissions and limits for each check are in [real-response-checks.md](real-response-checks.md).

## Findings

- **Fabricated citations mix real and invented details.** In Case 3, the paper is real, but the co-author and the journal were invented. Checking the real record shows exactly which parts were made up.
- **The main subject decides the score.** Cases 2 and 3 move between 1/5, 2/5 and 3/5 depending on whether an error counts as central or supporting. The choice has to be stated and defended.
- **Reliable sources often disagree.** The Eiffel Tower start date, the award year in Check 1 and the "first woman to drive" claim in Check 2 all needed a "Sources disagree" verdict, which my first draft of the rubric didn't have.
- **Source attribution needs checking too.** While reviewing the real checks, some dates were attributed to the wrong source and some quotations were not word for word. Every source was re-opened before the final version.
- **Rubric gaps were found by testing.** The cases exposed missing rules for dependent claims, unsupported claims and the verdicts "Cannot verify" and "Sources disagree". They were added to [rubric.md](../01-response-evaluation-framework/rubric.md) as version 1.1.
- **Two real responses had no errors.** The two real responses were accurate on well-documented subjects, which says nothing about how often these tools make mistakes.

## Limitations

- Cases 1 to 3 are synthetic, and the planted errors are the kinds I expected to look for.
- Only two real responses were checked, on well-documented subjects, from two tools.
- All checking was done by one evaluator, and agreement between evaluators was not measured.
- Choosing the main subject and separating central from supporting errors are judgements that affect the score.
- Sources include Wikipedia and web pages of varying reliability, and quotations and dates were checked by hand.
- Built as a learning project, with AI-assisted feedback on drafts and layout.

## Recommendations

- Have a second evaluator check the same responses and measure how often the verdicts and scores agree.
- Check more real responses, including obscure topics and topics where models are likely to err.
- Test longer responses and responses with citations to papers or legal cases.
- Automate the first step, splitting a response into claims and searching for sources, and compare it with the manual results (a natural follow-up to the automated evaluation work in Project 4).

## Files

- [test-cases.md](test-cases.md): the three synthetic cases with full claim tables.
- [real-response-checks.md](real-response-checks.md): the two real-response checks with full claim tables.
- [../01-response-evaluation-framework/rubric.md](../01-response-evaluation-framework/rubric.md): the rubric used for scoring.