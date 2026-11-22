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

## Case 3: Rosalind Franklin and the structure of DNA (invented sources)

**Prompt:** "Tell me about Rosalind Franklin and her work on DNA."

**Response (synthetic):** "Rosalind Franklin was an English chemist who specialised in X-ray crystallography, and her measurements of DNA fibres were central to working out the molecule's structure. Her famous Photograph 51, captured in 1952, provided crucial evidence of the helical structure of DNA. In 1953, she published a paper with Maurice Wilkins in the Journal of Molecular Genetics detailing this structure. Reflecting on her research, Franklin said, 'The structure of DNA is a locked door, and I hold the only key.' She died of lung cancer in 1958 at the age of 37. In 1962, James Watson, Francis Crick, and Maurice Wilkins were awarded the Nobel Prize in Physiology or Medicine for their discoveries concerning the molecular structure of nucleic acids."

### Claim table

| # | Claim | Verdict | Type | Source checked |
|---|---|---|---|---|
| 1 | Franklin was English. | Supported | n/a | Wikipedia, Rosalind Franklin: born Notting Hill, London, England, and described as English in the opening sentence. https://en.wikipedia.org/wiki/Rosalind_Franklin |
| 2 | She was a chemist. | Supported | n/a | Same page, opening sentence: "was an English chemist and X-ray crystallographer". https://en.wikipedia.org/wiki/Rosalind_Franklin |
| 3 | She specialised in X-ray crystallography. | Supported | n/a | NLM Profiles in Science, Biographical Overview: in Jacques Mering's Paris laboratory she learned to analyse carbons by X-ray crystallography and became highly skilled at the method. https://profiles.nlm.nih.gov/spotlight/kr/feature/biographical |
| 4 | Her measurements of DNA fibres were central to working out the molecule's structure. | Supported | n/a | NLM Profiles in Science, opening paragraph: her x-ray diffraction studies "provided crucial clues to the structure of DNA and quantitatively confirmed the Watson-Crick DNA model". https://profiles.nlm.nih.gov/spotlight/kr/feature/biographical |
| 5 | Photograph 51 was captured in 1952. | Supported | n/a | King's College London, The story behind Photograph 51 (Brian Sutton, 14 April 2023): taken at King's in May 1952, camera set up on Friday 2 May and developed on Tuesday 6 May. https://www.kcl.ac.uk/the-story-behind-photograph-51 |
| 6 | Photograph 51 provided crucial evidence of the helical structure of DNA. | Supported | n/a | King's College London: "Such a pattern of spots is highly suggestive of a helical structure". Wording note: Steven Carr's History of DNA notes at Memorial University put the open question as "DNA is a helix: two or three strands? Bases inside or outside?" (https://www.mun.ca/biology/scarr/4270_History_of_DNA.html), and the ASU Embryo Project records that the X-ray data alone could not prove helicity and that the two-strand conclusion came from the A-form calculations (https://embryo.asu.edu/pages/molecular-configuration-sodium-thymonucleate-1953-rosalind-franklin-and-raymond-gosling). "Helical" is therefore the accurate wording here, not "double helix". |
| 7 | She published a paper on the structure of DNA in 1953. | Supported | n/a | Nature's own article record: FRANKLIN, R. and GOSLING, R., "Molecular Configuration in Sodium Thymonucleate", Nature 171, 740 to 741 (1953), published 25 April 1953, doi 10.1038/171740a0. https://www.nature.com/articles/171740a0 |
| 8 | That paper was co-authored with Maurice Wilkins. | Cannot verify, no record found | Fabricated fact | Search run: "Rosalind Franklin" "Maurice Wilkins" co-author 1953 paper. No record found. Nature's author list for the paper names Rosalind E. Franklin and R. G. Gosling, Wheatstone Physics Laboratory, King's College, London, with no Wilkins. https://www.nature.com/articles/171740a0 |
| 9 | That paper appeared in the Journal of Molecular Genetics. | Cannot verify, no record found | Fabricated fact | Search run: "Journal of Molecular Genetics" Rosalind Franklin 1953. No record found. Nature's citation block gives the real venue as Nature 171, 740 to 741 (1953). https://www.nature.com/articles/171740a0 |
| 10 | Franklin said, "The structure of DNA is a locked door, and I hold the only key." | Cannot verify, no record found | Fabricated fact | Search run: "The structure of DNA is a locked door, and I hold the only key" Rosalind Franklin, then "locked door" "only key" Rosalind Franklin DNA. No record found. Wikiquote's Sourced section holds exactly three quotations, "Science and everyday life cannot and should not be separated.", "What's the use of doing all this work if we don't get some fun out of this?" and "The results suggest a helical structure...", which continues with the 2, 3 or 4 co-axial chains and the phosphate groups. None is the locked door line (https://en.wikiquote.org/wiki/Rosalind_Franklin). The NLM overview opens with her own words on science and faith and contains no such line (https://profiles.nlm.nih.gov/spotlight/kr/feature/biographical). Wikiquote attributes the first of the three to an answer to her father, citing Brenda Maddox (2003), p. 61. |
| 11 | She died in 1958. | Supported | n/a | NLM Profiles in Science: "She died in London on April 16, 1958." https://profiles.nlm.nih.gov/spotlight/kr/feature/biographical |
| 12 | She died at the age of 37. | Supported | n/a | Wikipedia infobox: died 16 April 1958, aged 37, Chelsea, London. The body text also gives her death at age 37 in April 1958. https://en.wikipedia.org/wiki/Rosalind_Franklin |
| 13 | She died of lung cancer. | Contradicted | Wrong fact | Wikipedia: died of ovarian cancer. NLM: "In the fall of 1956 Franklin was diagnosed with ovarian cancer." https://en.wikipedia.org/wiki/Rosalind_Franklin and https://profiles.nlm.nih.gov/spotlight/kr/feature/biographical |
| 14 | The Nobel Prize was awarded in 1962. | Supported | n/a | nobelprize.org, The Nobel Prize in Physiology or Medicine 1962. https://www.nobelprize.org/prizes/medicine/1962/summary/ |
| 15 | The laureates were James Watson, Francis Crick and Maurice Wilkins. | Supported | n/a | Same page: awarded jointly to Francis Harry Compton Crick, James Dewey Watson and Maurice Hugh Frederick Wilkins, each listed with prize share 1/3. https://www.nobelprize.org/prizes/medicine/1962/summary/ |
| 16 | The prize was in the category of Physiology or Medicine. | Supported | n/a | Same page, category confirmed in the award sentence. https://www.nobelprize.org/prizes/medicine/1962/summary/ |
| 17 | The prize was awarded for discoveries concerning the molecular structure of nucleic acids. | Supported | n/a | Same page. The full motivation reads "for their discoveries concerning the molecular structure of nucleic acids and its significance for information transfer in living material", so the response quotes only the first half. https://www.nobelprize.org/prizes/medicine/1962/summary/ |

### Severity

Main subject: Rosalind Franklin's work on DNA and what it showed about the molecule's structure. The prompt asks about her and her DNA work, so the answer stands or falls on what she did, what her data showed, and when.

Claims 8 and 9 are counted as one error, not two. Both are invented details attached to the same real paper, so they form a single fabricated citation, following the rule that claims depending on the same invented item count as one.

That fabricated citation is supporting. The byline and the venue are wrong, but the load-bearing facts around them are right: she did publish on DNA structure in 1953, and claim 7 records it. A reader is misled about where to find the paper, not about what she contributed.

Claim 10, the fake quotation, is supporting. It is framed as a reflection on her research, which puts it near the subject, but it asserts no finding, no method and no date. It adds nothing about what she discovered, so it leaves the main answer intact.

Claim 13, the cause of death, is supporting. Cause of death sits outside her DNA work. The year and the age are both correct in claims 11 and 12, so nothing about her scientific contribution changes.

### Judgement call

Alternative main subject: "Rosalind Franklin's life and work". On that reading claim 13 becomes central, because how she died is a major biographical fact, while the citation and the quotation stay supporting. That is one central and two supporting errors, so the score changes to 2/5.

A second alternative keeps my narrow subject but treats claim 10 as central, on the grounds that it is presented as her own statement about her research. That also gives one central and two supporting errors, so again 2/5. Adopting both changes together gives two central errors and 1/5.

I hold the narrow subject and the supporting classification for the quotation, so my score is 3/5. The reason is that the question is about the DNA work, and neither the cause of death nor a decorative quotation alters what the response says she found.

### Accuracy score

3/5. Three errors, all supporting: one fabricated citation (claims 8 and 9 counted together), one unverifiable quotation (claim 10) and one wrong fact (claim 13).

### Omissions

Two things the answer needed are missing. First, Raymond Gosling's role: King's College London says the image was "taken by Rosalind Franklin, together with her PhD student Raymond Gosling", and Wikipedia states that Gosling actually took Photo 51. The response says "her famous Photograph 51" and never mentions him, even though he is also the real co-author of the 1953 paper. Second, King's records that "Franklin was unaware that the photograph had been shown to Watson", and Wikipedia says Wilkins showed it to Watson without Franklin's permission. That is the mechanism by which her data reached the Cambridge model, so leaving it out removes the most important context for her contribution. Both belong under Relevance and Completeness, not Accuracy.