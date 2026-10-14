# HANDOFF: LAWS1150/JURD7150 T3 2026 mid-term (Rocky problem)

Read this first. It is written so that any Claude session (Cowork or Code) given this repository can continue the work without the original conversation.

## 1. The task
- Student: Yusuf. Assessment: LAWS1150/JURD7150 Principles of Private Law, T3 2026 mid-term problem question (Rocky, Grace, AMPL, Pierre). Due Monday 19 October 2026, 9:00am.
- Problem: `drive/txt/ACTUAL TASKKK.txt` (original `drive/claudee/ACTUAL TASKKK.pdf`). Instructions and the ten marking criteria: `drive/txt/Instructionsss.txt`.
- Official limit is 1,500 words. Yusuf chose a cap of 1,600 including the count line, knowing the risk (markers estimate 74 to 76 under a strict 1,500 reading: −5, word-count row zero, nothing after word 1,500 marked). Always disclose this.
- His goal, in his words: "never miss any arguments cos thats the whole point the arguments the claculus the thinking"; "be chronological and clear"; "no proxy temrinology"; "this needs to be 90 +"; read everything verbatim, in full context, no parsing; the readings and slides are truth; the textbook is never cited.
- His full binding instructions (rules R1 to R14, lecturer terminology list, zero-hallucination protocol Z1 to Z9, Excellent standard, checklist, rulings R-P, R-Y, R-Z, R-AB, R-AC, R-AD, R-AE): `work/YUSUF_INSTRUCTIONS_VERBATIM.md`. These govern everything.
- Style: his voice from Part A of `drive/txt/2884827_Yusuf_Ahmed_zz568695_LAWS1061_Midterm_T2_2026_8743505_1153076233.txt`; multi-clause sentences joined by semicolons and colons; no em dashes, no double quotation marks, no contractions, no meta language (weeks, slides, course, readings, 'the problem'); party headings only; AGLC4 footnotes; case names italic.

## 2. Current state
- Current answer: `work/ANSWER.md` (identical to `work/ANSWER_v5.md`). Built submission: `work/LAWS1150 Mid-Term T3 2026 - Rocky (v5).docx` (A4, TNR 12, double spaced, footnotes, case names italic). Also uploaded to Google Drive: Claudee / "Rocky mid-term work (Claude, 14 Oct 2026)".
- v5 metrics: body 1,597 words, 'Word count: 1,600'; 51 footnotes; 89 quoted spans, all found at source (the one 'NOT FOUND' is the problem fact 'proposed that Rocky offer', a ligature glitch in the txt: 'oQer'); quoted words 16.5%; mean sentence 23.5 words; under-12-word sentences 10.3%; no sentence over 45 words; semicolons 1.06 and colons 1.00 per 100 words.
- Structure: I. ROCKY v GRACE (offer and invitation to treat; acceptance; consideration; intention and Masters classes; certainty and illusory promise with Pace, Meehan, Godecke; Rocky's claim through AMPL's advance, agency, privity, signature; Development Agreement). II. ROCKY v AMPL (ALTERNATIVELY PIERRE) (offer and acceptance at 8 April; agency via Port Jackson 240; existing legal duty rule; intention and letter of comfort; certainty; privity of the $10,000; whether the guarantee clause binds Rocky; AMPL's consideration and past consideration; when the 12 months began; condition precedent and duty to co-operate; exposure).
- Version history and scores (cold markers, SHEET_v12 rubric / holistic):
  - original Cowork submission (`drive/txt/submission.txt`): 70 / 78 (calibration, `work/CAL_M4_OLD_SUBMISSION.md`)
  - v3: 79 / 81–82
  - v4: 83–84 / 84–85 (round 5: `work/R5_*.md`)
  - v5: not yet marked. Round 6 agents were launched but died on a usage limit (weekly limit reset 17 Oct 2026, 7am UTC). `work/R6_M5_OPPOSING.md` is a partial report only.
- What v5 changed from v4 (all checked at source before applying): fixed the 'unless the clause preceded the bargain' contradiction (now 'unless he also promised AMPL a guarantee when he asked'); agency criterion re-sourced to Port Jackson 240 (Barwick CJ dissenting) as the rulings sheet prefers (note: Port Jackson sits in the reading guide's skip range for his printing; Deane J at Trident 145 is kept for the bare route); exposure paragraph restated consistently (oral undertaking likely binds; $1,150,000 under the clause only if the clause binds and AMPL promised the $10,000); added Gibbs J's 'concluded bargain' / 'a vital matter' dictum in Godecke, later conduct on formation (Brambles 164), 'check in' emails cannot construe the undertaking (Brambles 164), Brogden 'necessarily' test via Brambles 195 (Ipp AJA), 'minimal' profit, 'AMPL and Grace entered into', 'outside insurance' (Trident 115, 123), split fn 12, construction is objective (Brambles 164), genesis (Brambles 163); cut 'and rate', 'in New South Wales', Rocky's duty arising once conditions met, AMPL's 'later invoked the Loan Agreement'.
- Arguments considered but not funded within 1,600 (could be added if something else is cut): Masters 'fourth category' for Grace (casebook note [5.105], Baulkham Hills 628 quoting Sinclair, Scott 317; about 20–33 words); Gibson second-paragraph comparison (about 23 words); Banque Brussels timing difference (AMPL had already advanced; about 11 words); Trident 118 nominal damages on the Pierre branch (about 12 words); positive 8 April reason for the 12 months (about 12 words); Rocky declining a 'long-term loan' on 5 February (about 3 words).

## 3. Pending work (in order)
1. Run round 6: five independent adversarial markers on v5, blind to each other and to earlier reports. Prompt protocol and roles: `work/MARKERS_PROMPT.md` (role 1 completeness, 2 readings-strength, 3 fidelity/terminology/AGLC, 4 cold harsh lecturer x2, 5 opposing counsel). Yusuf has asked for these to be genuinely independent and super adversarial: destroy each legal reasoning step from the verbatim readings, find any proxy terminology or glib phrasing, and propose stronger arguments.
2. Verify every finding at source (casebook text plus `work/verify.py`) before applying (Z7). Apply only confirmed fixes, staying at body ≤ 1,597; renumber footnotes; re-run stats and verify; rebuild the .docx; commit and push.
3. Iterate until two cold markers give 90 or more.
4. Final deliverables Yusuf asked for: the final .docx; a final reasoning map (facts, both sides, authorities with pins and status, decisive reason, marks); a side-by-side table of every fact with the verbatim reading passage and pinpoint (casebook page and report page); a final marker report.
5. Disclose to Yusuf: the 1,600 vs 1,500 risk; Trident 129 is Brennan J dissenting quoting Kitto J; casebook pages are from the 14th ed (report pins are identical in his printing); Brambles 164/191 and Port Jackson fall in reading-guide skip ranges.

## 4. Tools (run from repo root; python3 -I)
- `work/verify.py ANSWER.md`: finds every quoted span in the casebook chapters, the W1 casebooks, the Pao On extract and the problem, with page and report-page marker.
- `work/stats.py ANSWER.md`: body words, stated count, quoted share, sentence stats, semicolons and colons per 100 words. Voice targets: mean 17.8–24.7; under-12 9.1–36.4%; colons ≥ 0.81/100; quoted < 20%; no sentence > 45.
- `work/renumber.py ANSWER.md`: renumbers footnotes by first appearance and remaps (n X). Recheck every Ibid by hand afterwards.
- `work/build.py ANSWER.md "OUT.docx"`: pandoc build with `work/reference.docx`, italicises case names (CASES and SHORT lists), bolds headings, sets A4.
- 'Word count' line = body + 3.

## 5. Sources in this repository
- Casebook (Robertson and Paterson, Contract: Cases and Materials, 14th ed): `drive/casebook/CB14.pdf`, full text `CB14.txt`, chapters `CB14_ch03.txt` (offer, acceptance), `ch04` (consideration), `ch05` (intention), `ch06` (certainty), `ch11` (privity), page-tagged. Printed page = PDF page − 38. His own printing differs by 0–4 pages after chapter 3; report page markers like [534] are identical. Footnotes cite report pages only.
- Reading guide: `drive/casebook/ReadingGuide.pdf`, `drive/txt/ReadingGuide.txt`.
- Slides (all seven decks), Cowork drafts, maps, marker feedback, FINAL package, Interim v4, practice book: `drive/claudee/` (originals) and `drive/txt/` (text).
- Weekly readings: `drive/readings/` with manifests `MANIFEST_W1.tsv` to `MANIFEST_W4.tsv`; W1 casebook text `drive/txt/W1L1_casebook.txt`, `W1L2_casebook.txt`; Pao On extract PDF in W2 L1.
- Rubric and rulings: `work/RUBRIC_RULINGS_SHEET_v12.txt` (section 6 of the FINAL package; 6.1 rulings override SHEET_v12).
- All drafts `work/ANSWER_v1.md` to `ANSWER_v5.md`; every marker report `work/MARK_*`, `TRACE_v1`, `R2_*` to `R6_*`, `CAL_*`.
- `work/ROCKY_EVERYTHING.zip`: every file above in original formats; `work/ROCKY_EVERYTHING.md`: the same as one text dump.

## 6. Known gaps (not in this repository)
- Files over 10 MB in his Google Drive could not be downloaded (Drive tool limit; direct download blocked): W1 L1, W1 L2, W2 L1, W2 L2, W3 L1, W3 L2 'Optional' PDFs (about 18 MB each; their text layers are present as `*.drive.txt` where Drive provided them); W2 L1, W2 L2, W3 L1, W3 L2, W4 L1 'Casebook' PDFs (37–80 MB, scanned); the W4 L1 lecture video. The 14th ed casebook text covers every case in those casebook extracts. File IDs are in the manifests.
- The raw conversation transcripts of the Claude Code session were not copied in (blocked by a safety check). This file and the reports carry the substance.
- The original Cowork conversation itself is not available; Yusuf's Cowork instructions are reproduced verbatim in `work/YUSUF_INSTRUCTIONS_VERBATIM.md`.

## 7. Yusuf's messages in the Claude Code session (verbatim)
- "how do i continue flawleslsly from my cowork task here"
- "read thoruh every in context, each page in each of the readigns evrbatim every file verbatim. no parsing allowed"
- "ill let you have an extra 100 words, and then void word limit issue, but max 1600 please but yeah never miss any arguments cos thats the whole point the arguments the claculus the thinking and stuff so yeah then prsent final submisison as docx, final map, full to verbatim reaings pinpoint etc and facts side by side, and then final marker, this needs to be 90 + so yeah be chronological and clear"
- "no proxy temrinology"
- "wait for next term read all verbatim. ill upload rest of the cowork deets so you get it clean"
- "also the biggest thing is agents will need to get into my computer to Context … get these, like the drive is the verbatim readings, casebooks, plus optionals which are part of readings, everything ogtten word for word, cos this is integral …"
- "i grant system postiions get in"; "how do i attach folders to you"
- "find a way maybe. need ot push a bunch of stuff to the github or smth idk js find. possible way i cant upload its like 100mb each week sometimes, and i cant compress upload all 10 folders hell along"
- "done its in drive in claudee"
- "you can do compressing idk work till you can somehow sort a way to do this shi urself dont delegate ot me"
- "nope continue flawlessly so keep going till you have the full full verbatim context and all those instrucitons you know exactly everythign i said to it and you have somthing to work off but yeah and you can see, so just see so it had arguments it didnt include... plus like it needs 5 proper markers adversarial. using theverbatim readings to prove any and evreythign wrong, or prove stronger rguments in the lecture readings context and proepr terminolgoy etc.. fix this prompt to yk be perfect nd then act on it"
- "so this is a 66?" (answer: 66 was an early draft's mark; the original submission calibrated at 70 rubric / 78 holistic)
- "genuinely run 5 fable 5.1 blind to each other, in different environemtns to run the midterm facts and have the verbatim w1a,b,2ab,3ab,4ab readings verbatim and understanding and learning verbatim 1:1 with temrinology to understand and create arguments. for the submission, and they should each be super adversarial seeing how to improve it, or how to destroy each legal reaosning in the submission, finding any proxy terminology glib etc."
- "all i want you to do is push to git, every file, plus push every file to google drive too, that drive you had."
- "output one massive file with everything here then including all mds everything too. full entire everything"
- "no dont drop anything … dont give me markdowns when they arent mark downs genunely everyhting porperly as they are."
- "absolutely notig missing not even context, so that any cowork or code given access ot it can continue flawlessly?"
