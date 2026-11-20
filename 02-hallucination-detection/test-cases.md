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