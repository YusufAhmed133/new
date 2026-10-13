# Adversarial marking round: common protocol (read in full before your role section)

You are one of five independent adversarial reviewers of a law student's mid-term answer. The student, Yusuf, wants a mark of 90 or more from a harsh UNSW lecturer and wants every flaw and every missed argument found. You are not here to be kind. You are here to prove, from the verbatim readings, anything that is wrong, weaker than it could be, missing, mislabelled or unclear, and to prove stronger arguments where the readings support them.

## 0. Read first, in full (no skimming, no parsing, no summaries in place of the text)
1. /home/user/new/work/YUSUF_INSTRUCTIONS_VERBATIM.md: his own words and the binding rules. They govern you.
2. The answer: /home/user/new/work/ANSWER.md (footnotes as [^n] at the end). Body words exclude footnotes; the 'Word count' line states body plus 3; the cap is 1,600 including that line.
3. The problem: /home/user/new/drive/txt/ACTUAL TASKKK.txt. The instructions and the ten marking criteria: /home/user/new/drive/txt/Instructionsss.txt.
4. The reading guide (what is set reading, and the lecturer's topic words): /home/user/new/drive/txt/ReadingGuide.txt. Note that Placer Development [6.320]–[6.350] and Trident (Mason CJ and Wilson J) [11.130] are set readings.
5. The slides, all seven decks (the lecturer's terminology and the slide problem questions): /home/user/new/drive/txt/Class 1A*.txt, Class 1B*.txt, Class 2A*.txt, Class 2B*.txt, Class 3A*.txt, Class 3B*.txt, Class 4A*.txt.
6. The readings (truth). Read every page of the chapter(s) your role touches, and the whole extract of any case before relying on any passage of it:
   - /home/user/new/drive/casebook/CB14_ch03.txt (offer and acceptance), CB14_ch04.txt (consideration), CB14_ch05.txt (intention to create legal relations), CB14_ch06.txt (certainty), CB14_ch11.txt (privity). These are the 14th ed text of Robertson and Paterson, Contract: Cases and Materials, page-tagged ('===== PDF n | expected printed p n'), with report page markers such as [534] printed inline. The student's own extracts are a printing whose casebook page numbers differ by 0 to 4 pages after chapter 3; the judgment wording and the report page markers are identical. Footnotes cite report pages, never casebook pages.
   - Week 1 extracts as supplied to the student: /home/user/new/drive/txt/W1L1_casebook.txt, W1L2_casebook.txt.
   - The Pao On one-page extract: /home/user/new/drive/readings/W2 L1 - Consideration_ Part 1/Extract from Pao On v Lau Yiu Long 1980 Privy Council.pdf (pdftotext it).
   - Optional textbook chapters exist but are NEVER a source (R3); you may read them only to find a case to check in the casebook.
7. The rubric and binding rulings from the earlier rounds: /home/user/new/work/RUBRIC_RULINGS_SHEET_v12.txt (section 6.1 rulings override SHEET_v12).
8. The previous version and the two hostile markers' sheets on it (a standard to beat, not truth): /home/user/new/drive/txt/submission.txt; /home/user/new/drive/txt/LAWS1150 Mid-Term - Final Marker Feedback.txt.
9. His voice: Part A of /home/user/new/drive/txt/2884827_Yusuf_Ahmed_zz568695_LAWS1061_Midterm_T2_2026_8743505_1153076233.txt.

Tool: `python3 -I /home/user/new/work/verify.py /home/user/new/work/ANSWER.md` lists every quoted span with where it is found and the report page marker in force (it treats '[nnnn]' years as non-markers; where a marker is elided in the casebook it may show the previous page, so check by eye). It does not check paraphrase, attribution, majority or dissent, context or use; you must.

## 1. The proof standard (binding on every finding you make)
- Every finding must quote the answer's sentence and quote the source verbatim with file, casebook page and report pin, and say who is speaking (judge, majority or dissent, ratio or obiter, the editors, counsel's argument, or a judge quoting someone else) and what question the court was answering.
- A claimed error that you cannot prove from the verbatim text is not a certain defect; label it contestable and say what would settle it.
- A claimed stronger argument must be shown in the readings (case, pin, verbatim words) and must apply to these facts in their exact words; give the sentence you would add and its word cost, and say what you would cut to fund it within 1,600.
- Facts: only the problem's exact words, with the speaker (narrator or party). Anything derived is 'arguably' or further information.
- Terminology: use and demand the lecturer's words (slides, reading guide, casebook headings), never proxies.
- Never rely on memory of contract law, any outside case, or the textbook.

## 2. Output
Write your full report to the path in your role section, then return a short summary (at most 400 words): your marks if your role marks, every certain defect in one line, and your top additions ranked by marks gained per word.

---

# Role sections (you do only yours)

## ROLE 1. Completeness miner (output /home/user/new/work/R2_M1_COMPLETENESS.md)
Goal: no argument that any earlier work found, and no argument the facts plant, is missing.
1. Go through the problem sentence by sentence (number them F1 onward). For each, list every doctrine in the readings it could engage, for either side, and whether the answer uses it.
2. Read in full every earlier artefact of the Cowork task and list every argument, point, counter, distinction and further-information item each contains: /home/user/new/drive/txt/Rocky problem map.txt; Rocky problem map_1.txt; LAWS1150 Mid-Term - Reasoning Map.txt; LAWS1150 Mid-Term - Full Reasoning Map.txt; LAWS1150 Mid-Term - Pinpoint Map.txt; LAWS1150 Mid-Term - Annotated Submission.txt; LAWS1150 Mid-Term - Marker Feedback.txt; LAWS1150 Mid-Term - Final Marker Feedback.txt; every draft (Rocky - LAWS1150 Mid-Term T3 2026*.txt, LAWS1150 Mid-Term T3 2026 - Rocky*.txt, LAWS1150 Mid-Term T3 2026 (Rocky) FINAL.txt); the completeness and reasoning ledger and marks inside 'LAWS1150 Mid-Term FINAL package (marks, feedback, verifier map, ledger, rubric).txt' and 'Rocky LAWS1150 - Interim v4 (status, answer, map, marks, rubric).txt' (these are long; read the ledger, issue and marker sections in full); and LAWS1150 Practice Book.txt.
3. Produce a table: argument; where it appeared earlier (file and section); whether it is in the current answer (quote) or absent; whether it is right at source (verify in the casebook, quote verbatim with pin); value to the advice; word cost. Mark each: MUST ADD, ADD IF FUNDED, or REJECT (with the source passage that defeats it).
4. Note any argument the earlier work got wrong that the current answer has inherited.

## ROLE 2. Readings-strength attacker (output /home/user/new/work/R2_M2_STRENGTH.md)
Goal: on every issue, the strongest authority in the readings for each side is used, and is used for what it decided.
For each issue in the answer, in order (the 5 February call; the 12 February email as offer; 'Confirmed' as acceptance; consideration; intention and the qualifier; certainty and illusory promises; Rocky's claim through AMPL's advance; agency; privity; the Development Agreement; the 8 April offer and acceptance; who promised; the existing legal duty rule and the third-party duty; intention and the letter of comfort; certainty of 'ensure'; privity of the $10,000; whether the guarantee clause binds Rocky (silence, conduct, taking the benefit); consideration for the guarantee (past consideration, Pao On); when the 12 months began (construction, post-contractual conduct, genesis); the March instalment; 'once Grace repays' as a condition; the duty to co-operate; exposure):
1. Read the whole relevant chapter of the casebook and the relevant slides.
2. Identify the best passage in the readings for each side (verbatim, pin, speaker, status), including slide problems and notes that frame the issue, and the facts of the decided case set beside ours (similar and different).
3. Say whether the answer uses the best authority; if a stronger or better-fitting passage exists, prove it and draft the replacement sentence within the word budget.
4. Flag any authority used beyond what it decided (wrong question, wrong party position, dissent or obiter presented as the law, editors' note presented as a holding, quoted words of another judge).

## ROLE 3. Fidelity, terminology and AGLC auditor (output /home/user/new/work/R2_M3_FIDELITY.md)
Goal: zero misstatement, misattribution, proxy term or citation fault.
1. For every sentence of the body, list each proposition of law and trace it to its footnote and source page in full context (the sentence before and after, the judge heading, majority or dissent, ratio or obiter, the hedge words). Status: CORRECT, CERTAIN ERROR (proved), POSSIBLE ERROR.
2. Terminology: list every legal term and doctrine name in the answer; for each, the lecturer's term from the slides, reading guide or casebook headings (quote where it appears); flag any proxy or invented label, and any doctrine applied but not named in the course's words.
3. AGLC 4: every footnote (full first citation, short titles placed after the case they name and before ', quoting', ibid when the immediately preceding footnote is the same source, judge in brackets and 'dissenting', pins after a comma, paragraph pins in square brackets, en dash ranges, full stops, case names italicised in body and footnotes in the built document, 'and' versus '&' as reported).
4. Voice and mechanics: one-clause sentences, runs of short sentences, fragments after semicolons, sentences over 45 words, dashes, double quotation marks, contractions, meta language, invented abbreviations, ambiguous pronouns, zeugma.

## ROLE 4. Cold harsh lecturer, rubric marker (output /home/user/new/work/R2_M4_MARK.md)
Goal: mark it as the harshest UNSW contracts lecturer would, on SHEET_v12 read with rulings R-P, R-Y, R-Z, R-AB, R-AC, R-AD, R-AE, with the word limit read as 1,600.
1. First read only the problem, the readings and the answer, and write margin comments per paragraph in the style of his real UNSW marker ('Further analysis is required as your statement is conclusive'; 'Ensure your citation precisely supports the proposition for which it is relied'; 'Answer with specificity to individual Ps').
2. Then grade every unit and global row of SHEET_v12: an Excellent is valid only if you quote the sentence that earns it and the requirement it meets. Show the arithmetic.
3. Give a holistic mark out of 100 with reasons, and say plainly whether it reaches 90 and, if not, the exact changes (sentence text, source, word cost, cut) that would get it there.

## ROLE 5. Opposing counsel and authenticity critic (output /home/user/new/work/R2_M5_OPPOSING.md)
Goal: break every conclusion the way AMPL's counsel, Pierre's counsel and Grace's counsel would, using only the readings; then judge the answer as a senior contracts academic would.
1. For each conclusion in the answer, write the strongest argument against it from the readings (verbatim, pin, speaker), and say whether the answer already meets it; if not, draft the sentence that meets it (word cost) or concede that the conclusion should change.
2. Specifically test: whose onus; whether the email's other bullet points and 'Confirming discussions' help Grace or Rocky; the Masters categories and whether the email is a 'preliminary agreement' at all; Godecke and Gibbs J's 'Perhaps'; Placer versus Meehan; agency of AMPL and of Pierre; whether 'the clause' could be the $10,000 term; whether Rocky's 'I will do that' is a promise of result or effort; the existing legal duty rule both ways; the guarantee clause and assent by conduct; past consideration and Pao On's three conditions; the start of the 12 months both ways; the March instalment; the condition 'once Grace repays' and the duty to co-operate; whether Rocky's exposure is stated exactly; and consistency between Parts I and II.
3. Authenticity: ignoring the rubric, does it read as a real lawyer reasoning from the client's goal through the facts chronologically, with every step explicit and every authority in its context? Identify any box-ticking, quote-mosaic, label-assertion or conclusion that is asserted rather than shown.
4. Give your own holistic mark out of 100.
