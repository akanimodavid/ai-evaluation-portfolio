# Project 2: Test Cases

All prompts and responses are synthetic, written for this project. Each case contains planted errors, and each claim is checked against a named source.

## Case 1: The Eiffel Tower

**Prompt:** "Tell me about the Eiffel Tower."

**Response (synthetic):** "The Eiffel Tower is a famous landmark located in Lyon, France. It was built for the 1889 World's Fair, which celebrated the 100th anniversary of the French Revolution. Construction began on January 26, 1887, and was completed on March 31, 1889. The project involved engineers Maurice Koechlin and Émile Nouguier, architect Stephen Sauvestre, and Gustave Eiffel's company. In 1999, the tower received the International Golden Landmark Award. It is widely regarded as the most beautiful tower ever built."

### Claim table

| # | Claim | Verdict | Type | Source checked |
|---|---|---|---|---|
| 1 | The Eiffel Tower is located in Lyon, France. | Contradicted | Wrong fact | [Official Eiffel Tower – Access and location](https://www.toureiffel.paris/en/access-map). Confirms that the tower is in Paris, in the 7th arrondissement. |
| 2 | It was built for the 1889 World's Fair. | Supported | n/a | [Official Eiffel Tower – History](https://www.toureiffel.paris/en/the-monument/history). Explains that the tower was conceived as part of preparations for the 1889 Paris World's Fair. |
| 3 | The World's Fair celebrated the 100th anniversary of the French Revolution. | Supported | n/a | [Official Eiffel Tower – How the Tower Was Invented](https://www.toureiffel.paris/en/news/130-years/how-was-eiffel-tower-invented). Explicitly states that the 1889 exhibition celebrated the centenary of the French Revolution. |
| 4 | Construction began on January 26, 1887. | Sources disagree | n/a | [Official Eiffel Tower website](https://www.toureiffel.paris/en/the-monument/history) gives January 26, 1887, as the date the first digging started. [Wikipedia – Eiffel Tower](https://en.wikipedia.org/wiki/Eiffel_Tower) gives 28 January 1887 as the start of construction. The dates differ by two days, and the claim is supported by the official source, so it is not counted as an error. |
| 5 | Construction was completed on March 31, 1889. | Supported | n/a | [Official Eiffel Tower – 133 years and 330 metres](https://www.toureiffel.paris/en/news/history-and-culture/133-years-and-1083-feet). Confirms completion on March 31, 1889. |
| 6 | Maurice Koechlin and Émile Nouguier were involved in the project as engineers. | Supported | n/a | [Official Eiffel Tower – How the Tower Was Invented](https://www.toureiffel.paris/en/news/130-years/how-was-eiffel-tower-invented). Identifies both as engineers who developed the original tower project. |
| 7 | Stephen Sauvestre was involved in the project as an architect. | Supported | n/a | [Official Eiffel Tower – How the Tower Was Invented](https://www.toureiffel.paris/en/news/130-years/how-was-eiffel-tower-invented). Identifies Sauvestre as the architect who redesigned the project. |
| 8 | Gustave Eiffel's company was involved in the project. | Supported | n/a | [Official Eiffel Tower – History](https://www.toureiffel.paris/en/the-monument/history). Describes the involvement of Eiffel, Koechlin, Nouguier and Sauvestre in the accepted project. |
| 9 | The tower received the International Golden Landmark Award in 1999. | Cannot verify, no record found | Fabricated fact | Search run for the exact award name and "Eiffel Tower": "International Golden Landmark Award" "Eiffel Tower". The search produced no reliable record confirming the award. |
| 10 | The Eiffel Tower is the most beautiful tower ever built. | Cannot verify | Unsupported claim | This is a subjective opinion. No objective source can establish that it is the most beautiful tower ever built. |

**Verdict rule:** when reliable sources give different answers, record both, do not count the claim as an error, and leave the type as n/a.

### Most serious error

Claim 1 is the most serious error. The Eiffel Tower is in Paris, not Lyon. I classify it as central because the location is one of the defining facts of the monument, and getting it wrong misrepresents the subject of the response.

### Accuracy score

**2/5.** There is one central error (claim 1) and one supporting error (claim 9, the invented award, which does not change what the tower is). Claim 10 is an unsupported opinion and is not counted as a confirmed error.

### Judgement call

I classed claim 9 (the invented award) as a supporting error, not a central one. It is a fabricated fact, but it does not change what the Eiffel Tower is. Had it been central, there would be two central errors and the score would be 1/5.

## Case 2: International Space Station (summary faithfulness)

**Source passage (adapted from the introduction of Wikipedia's "International Space Station" article):** "The International Space Station (ISS) is a large space station assembled and maintained in low Earth orbit by a collaboration of five space agencies. Its construction began in 1998 with the launch of the Zarya module. The ISS serves as a microgravity and space environment research laboratory in which scientific research is conducted in astrobiology, astronomy, meteorology, physics, and other fields. The station is suited for the testing of spacecraft systems and equipment required for missions to the Moon and Mars. It has been continuously occupied since November 2000, making it the longest continuous human presence in space."

**Link:** https://en.wikipedia.org/wiki/International_Space_Station

**Summary (synthetic):** "The International Space Station is a large space station maintained in low Earth orbit by a collaboration of five space agencies. Its construction began in 2005 with the launch of the Zarya module. The station serves as a research laboratory for fields like astrobiology and physics. It has hosted researchers from over 50 different countries and has been continuously occupied since November 2000."

### Claim table

| # | Claim | Verdict | Type | Where in the passage |
|---|---|---|---|---|
| 1 | The ISS is a large space station. | Supported by the passage | n/a | Sentence 1 |
| 2 | It is maintained in low Earth orbit. | Supported by the passage | n/a | Sentence 1 |
| 3 | It is maintained by a collaboration of five space agencies. | Supported by the passage | n/a | Sentence 1 |
| 4 | Its construction began in 2005. | Contradicted by the passage | Contradiction | Sentence 2 says 1998 |
| 5 | Construction began with the launch of the Zarya module. | Supported by the passage | n/a | Sentence 2 |
| 6 | The station serves as a research laboratory. | Supported by the passage | n/a | Sentence 3 |
| 7 | Research fields include astrobiology and physics. | Supported by the passage | n/a | Sentence 3 |
| 8 | It has hosted researchers from over 50 different countries. | Not in the passage | Addition | Nothing in the passage mentions the number of countries |
| 9 | It has been continuously occupied since November 2000. | Supported by the passage | n/a | Sentence 5 |

### Severity

The main subject is what the ISS is and what it is used for. The passage primarily defines the station, its function as a laboratory and its current operational status.

- **Claim 4 (construction began in 2005) is supporting.** It is a historical detail about the timeline, and it does not change the core definition of what the station is or its current purpose. Continuous occupation is an ongoing state, while the start of construction is a past event.
- **Claim 8 (researchers from over 50 countries) is supporting.** It adds a specific number about participation that the passage never gives. The Wikipedia article reports visitors from 26 countries, a different measure, so it does not support the figure either.

### Judgement call

A different evaluator might argue that the main subject includes the history of the ISS. Then claim 4 would be central, because getting the foundational year wrong by seven years misrepresents the station's history. That would give one central error and one supporting error, which is 2/5. I defend 3/5 because the summary accurately captures the station's identity, purpose and current occupancy, so the start year is a secondary detail.

### Accuracy score

**3/5.** There are two supporting errors (claims 4 and 8) and no central error.

### Omissions

The summary leaves out the testing of spacecraft systems for Moon and Mars missions, and the research fields of astronomy and meteorology. These are omissions, so they fall under Relevance and Completeness, not Accuracy.

