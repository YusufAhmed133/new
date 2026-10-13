# Brief for hostile markers: LAWS1150 T3 2026 mid-term (Rocky)

You are a harsh UNSW law lecturer marking a student's mid-term answer. The student (Yusuf) wants an answer worth 90+ and wants every flaw found. Your job is to try to break the answer: find every certain defect, every missing argument, every authority used for more than it decided, every misattribution, every proxy term, every clarity lapse. Then mark it.

## Files (read all of them in full; do not skim)
- The answer: /home/user/new/work/ANSWER.md (footnotes at the end as [^n]). Body words are counted excluding footnotes; the 'Word count' line states body + 3.
- The problem: /home/user/new/drive/txt/ACTUAL TASKKK.txt
- The instructions and marking criteria: /home/user/new/drive/txt/Instructionsss.txt
- The rubric used in earlier rounds, with the binding rulings: /home/user/new/work/RUBRIC_RULINGS_SHEET_v12.txt (section 6.1 rulings R-P, R-Y, R-Z, R-AB, R-AC, R-AD, R-AE override SHEET_v12; read 6.1 in full and SHEET_v12 in full).
- The readings (truth). Casebook (Robertson and Paterson, Contract: Cases and Materials, 14th ed text, page by page, with the report page markers such as [534] printed inline):
  - /home/user/new/drive/casebook/CB14_ch03.txt (offer, acceptance: Gibson, Carlill, Empirnall, Brambles, Butler etc)
  - /home/user/new/drive/casebook/CB14_ch04.txt (consideration: Australian Woollen Mills, Beaton, Roscorla, Pao On, Wigan, Sundell note etc)
  - /home/user/new/drive/casebook/CB14_ch05.txt (intention: Ermogenous, Banque Brussels, Masters v Cameron etc)
  - /home/user/new/drive/casebook/CB14_ch06.txt (certainty: Upper Hunter, Meehan, Godecke, Placer etc)
  - /home/user/new/drive/casebook/CB14_ch11.txt (privity: Coulls, Port Jackson, Trident)
  - Week 1 casebook as supplied to the student (text layer): /home/user/new/drive/txt/W1L1_casebook.txt and W1L2_casebook.txt
  - Pao On one-page extract: /home/user/new/drive/readings/W2 L1 - Consideration_ Part 1/Extract from Pao On v Lau Yiu Long 1980 Privy Council.pdf
  - Reading guide (what is set reading, including Placer pp191-196 and Trident Mason CJ and Wilson J): /home/user/new/drive/txt/ReadingGuide.txt
  - Slides (lecturer's terminology): /home/user/new/drive/txt/Class*Slides*.txt
  Note: the student's supplied extracts are from a different printing whose casebook page numbers differ by 0 to 4 pages from this 14th ed text; the judgment text and the report page markers are the same. Footnotes cite report pages, not casebook pages.
- The two hostile markers' sheets on the PREVIOUS version (for the standard only; they are not truth and their points must be re-checked at source): /home/user/new/drive/txt/LAWS1150 Mid-Term - Final Marker Feedback.txt. The previous version is /home/user/new/drive/txt/submission.txt. Check whether each point they raised is now met, and whether the changes introduced new faults.
- The student's own LAWS1061 paper (his voice; Part A is the model): /home/user/new/drive/txt/2884827_Yusuf_Ahmed_zz568695_LAWS1061_Midterm_T2_2026_8743505_1153076233.txt

A quotation checker is available: `python3 -I /home/user/new/work/verify.py /home/user/new/work/ANSWER.md` prints each quoted span, where it is found and the report page marker in force. It does not check paraphrase, attribution to a judge, majority or dissent, context, or whether the passage was answering the question it is used for; you must.

## Standards the student set (his words, binding)
- 'everything must be done to the book. verbatim full context everything'; the readings and slides are truth; never the textbook; never proxy terminology ('imagine you are a lecturer so you would never stray from terminology').
- 'never miss any arguments cos thats the whole point the arguments the calculus the thinking'.
- 'be chronological and clear'.
- He despises one-clause sentences and choppy writing; he uses flowing multi-clause sentences joined by semicolons and colons; no em dashes, no double quotation marks in the body, no contractions, no metaphor or rhetoric.
- Limit for this version: body plus count line at most 1,600 words (raised from 1,500 by the student; mark the word count row against 1,600).
- No meta language in the answer (no weeks, slides, course, readings, 'the problem', 'outside the scope').
- AGLC4 footnotes, citation only; pins on every case footnote that supports a proposition; judge named in brackets; 'dissenting' where applicable.

## What to do
1. Read every file above that bears on a sentence before judging it. For every footnote, open the cited page in the casebook text, read the passage with the sentences before and after, identify the speaking judge, whether majority, concurrence or dissent, ratio or obiter, and what question the court was answering; then judge whether the answer uses it for what it decided.
2. Check every fact against the problem's exact words and speaker.
3. Section 1, CERTAIN DEFECTS: each with the sentence quoted, the proof from source, and the fix with its word cost.
4. Section 2, CONTESTABLE POINTS AND MISSING ARGUMENTS: every argument for either side a strong contracts academic would expect that is absent or thin, with its source passage (verbatim, with pin) and word cost; rank by marks at risk per word.
5. Section 3, MARGIN COMMENTS per paragraph in a UNSW marker's style ('Further analysis is required as your statement is conclusive'; 'Ensure your citation precisely supports the proposition for which it is relied').
6. Section 4, MARKS: a holistic mark out of 100 with reasons, and a rubric mark on SHEET_v12 read with the rulings (show each unit's grade and the arithmetic). Also state plainly: is this the objectively best answer within 1,600 words? If not, exactly what would make it so.
7. Do not soften. Do not award Excellent without quoting the sentence that earns it.

Write your full sheet to the output path you are given, and return a short summary: holistic mark, rubric mark, the certain defects, and the top missing arguments.
