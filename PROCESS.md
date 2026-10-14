# PROCESS: how to run every next round (read after HANDOFF.md; this is binding)

This is the full drill for improving the Rocky answer until two cold markers independently give 90 or more. Follow it step by step. Do not skip a step because a previous round "already checked" something: every round checks everything again from the verbatim sources.

---

## PART A. NON-NEGOTIABLE RULES (apply to the orchestrator and to every agent)

A1. **Verbatim or nothing.** Every legal proposition must be traced to the exact words of a reading, in full context: the sentence before and after, the judge heading, whether majority, concurrence or dissent, ratio or obiter, and what question the court was answering. A summary, a memory of contract law, the textbook, or another agent's report is never a source.

A2. **No fabrication, ever.** Never invent a fact, a quotation, a pin, a judge, a holding, a score or a result. If something cannot be proved from the text in this repository, label it CONTESTABLE (say what would settle it) or UNVERIFIABLE. Never present a guess as checked. Never report that an agent ran, finished or agreed unless its report file exists and you have read it.

A3. **Facts are only the problem's exact words.** Quote them from `drive/txt/ACTUAL TASKKK.txt` (beware ligature glitches: 'oQer' = 'offer', 'aQected' = 'affected', 'diQiculties' = 'difficulties', 'proﬁt' = 'profit'). Say who speaks (narrator or a party). Anything inferred is 'arguably' or further information, with its direction stated.

A4. **The lecturer's terminology only.** Use the words in the slides (`drive/txt/Class *.txt`), the reading guide and the casebook headings: e.g. 'invitation to treat', 'external manifestation of assent', 'counter-offer', 'bilateral contract', 'existing legal duty rule', 'past consideration', 'intention to create legal relations', 'preliminary agreement', 'letter of comfort', 'illusory promise', 'condition precedent', 'privity', 'stranger to the consideration', 'post-contractual conduct'. No proxy labels, no invented doctrine names, no glib phrasing ('clearly', 'obviously', 'simply').

A5. **Readings are truth; the textbook is never cited.** Optional textbook chapters may only be used to find a case, which is then checked in the casebook.

A6. **Binding instructions.** `work/YUSUF_INSTRUCTIONS_VERBATIM.md` (R1–R14, Z1–Z9, terminology list, Excellent standard, checklist) and the rulings in section 6.1 of `work/RUBRIC_RULINGS_SHEET_v12.txt` (R-P, R-Y, R-Z, R-AB, R-AC, R-AD, R-AE) override everything else, including this file if they conflict.

A7. **Word cap.** Body ≤ 1,597 words; 'Word count: N' line = body + 3 ≤ 1,600. Every addition must be funded by an identified cut. Always report the 1,500 risk.

A8. **Style.** His LAWS1061 Part A voice; multi-clause sentences with semicolons and colons; no em dashes, no double quotation marks, no contractions in the body; no meta language; party headings only; every point through a legal principle; chronological; reasons before verdicts; AGLC4 footnotes (citation only, pins on every case footnote, judge in brackets, 'dissenting' where so, Ibid and (n X) correct, short titles at first citation).

A9. **Honesty about state.** If a tool, download or agent fails, say so plainly with the error. If a usage limit stops agents, record it in the round log and do not invent their output.

---

## PART B. THE ROUND, STEP BY STEP

### Step 0. Freeze the version
- Copy `work/ANSWER.md` to `work/ANSWER_vN.md` (next number). Build `work/LAWS1150 Mid-Term T3 2026 - Rocky (vN).docx` with `python3 -I work/build.py work/ANSWER.md "work/LAWS1150 Mid-Term T3 2026 - Rocky (vN).docx"`.
- Run and save outputs: `python3 -I work/verify.py work/ANSWER.md > work/RN_VERIFY.txt` and `python3 -I work/stats.py work/ANSWER.md > work/RN_STATS.txt`. Any NOT FOUND other than a known ligature glitch must be fixed before markers run.
- Commit and push.

### Step 1. Launch the blind markers (at least 5, ideally 7)
Launch all in ONE message so they run in parallel, each in the background, each told:
- to read `work/MARKERS_PROMPT.md` in full and follow the common protocol and ONE role;
- its own output path `work/RN_<ROLE>.md`;
- **blindness**: do not open any earlier report (`MARK_*`, `TRACE_*`, `CAL_*`, `R2_*` … `R<N>_*`, or any 'Marker Feedback' file), and skip protocol item 8;
- to read the readings verbatim in full context before judging any sentence.

Minimum panel:
| Agent | Role | Output |
|---|---|---|
| M1 | Role 1 completeness miner: every sentence of the problem numbered F1…, every doctrine each fact engages for either side, every argument in every earlier draft and Cowork artefact (they may read drafts and Cowork maps, but not marker reports) | `work/RN_M1_COMPLETENESS.md` |
| M2 | Role 2 readings-strength attacker: for each issue, the strongest passage in the readings for each side, used for what it decided | `work/RN_M2_STRENGTH.md` |
| M3 | Role 3 fidelity, terminology and AGLC auditor: every proposition traced, every term checked against the lecturer's words, every footnote checked | `work/RN_M3_FIDELITY.md` |
| M4A | Role 4 cold harsh lecturer A (rubric + holistic) | `work/RN_M4A_MARK.md` |
| M4B | Role 4 cold harsh lecturer B, independent of A | `work/RN_M4B_MARK.md` |
| M5 | Role 5 opposing counsel (AMPL, Pierre, Grace) and authenticity critic | `work/RN_M5_OPPOSING.md` |
| M6 (optional) | "Destroyer": attack each legal reasoning step in order; for every sentence state the strongest reading-based reason it is wrong, overstated, glib, or uses a proxy term | `work/RN_M6_DESTROYER.md` |
| M7 (optional) | "Week-by-week learner": read W1 L1, W1 L2, W2 L1, W2 L2, W3 L1, W3 L2, W4 L1 readings and slides verbatim, in order, first; only then read the answer and list every argument or term those weeks teach that the answer misses or misuses | `work/RN_M7_WEEKS.md` |

Each agent must, in its report:
- quote the answer's sentence and the source verbatim (file, casebook page, report pin, speaker, status) for every finding;
- separate CERTAIN DEFECTS (proved from text) from CONTESTABLE points;
- give every proposed change as exact replacement text, its word cost, and the exact cut that funds it, tested on a scratch copy with `stats.py`;
- give marks (if its role marks): SHEET_v12 arithmetic and a holistic mark out of 100, and whether it reaches 90.

If more independence is wanted, run the same roles in separate cloud sessions (separate environments) with only this repository attached, and collect their report files.

### Step 2. Wait; never poll; never predict
- Do not read partial outputs or summarise reports that have not arrived. When each finishes, read the full report file, not only its summary.
- If an agent fails (usage limit, crash), log it in `work/RN_LOG.md` and relaunch it later. Never fill the gap yourself and call it that agent's work.

### Step 3. Verify every finding at source (the orchestrator, not the markers)
For EVERY certain defect and every proposed addition, in a findings ledger `work/RN_LEDGER.md` with columns: ID | agent | claim | answer sentence | source passage (verbatim, file, page, pin, speaker, status) | verified? (CONFIRMED / REJECTED / CONTESTABLE) | reason | action | word cost | funding cut.
- Open the cited passage yourself (`grep -n` the casebook chapter, read the surrounding 40 lines and the judge heading).
- Check the reading guide: is the passage in the set reading for his printing? If not, record it (rulings decide whether it may still be used).
- Check that the agent's quotation exists exactly (run `verify.py` on a scratch file if needed).
- Reject anything that relies on memory, the textbook, an outside case, or misreads majority/dissent. Write down why.
- When two agents disagree, decide from the text and record the decision and its reason.

### Step 4. Decide the edit package
- Rank confirmed items by marks gained per word. Certain defects first (logic contradictions, misattributions, wrong pins, exposure inconsistent with earlier findings, facts not in the problem), then missing core arguments named by two or more agents, then single-agent additions.
- Fund every addition with a cut that loses no argument; prefer compressions. If no lossless cut exists, list the item as 'unfunded' with its cost and let the ledger show what was traded.
- Never cut: the issue framing, both sides of each issue, the onus, further information with its direction, the exposure statement, or anything a ruling makes core.

### Step 5. Apply, then re-check everything
- Edit `work/ANSWER.md`. Use temporary footnote numbers for new notes, then `python3 -I work/renumber.py work/ANSWER.md`; then check every Ibid and (n X) by hand (Ibid only when the immediately preceding note is the same single source).
- Update the 'Word count' line to body + 3.
- Run `verify.py` (0 NOT FOUND except known ligature glitches), `stats.py` (all voice targets inside range: mean 17.8–24.7; under-12 9.1–36.4%; colons ≥ 0.81/100; quoted < 20%; no sentence > 45 words).
- Grep the body for: '—', '–' used as a dash, '"', "n't", "'s " misuse, 'the problem', 'week', 'slide', 'course', 'reading', 'clearly', 'obviously'.
- Rebuild the .docx; check case names are italic (`pandoc file.docx -t markdown | grep '\*'`), A4 page size, footnotes present, .docx text equals ANSWER.md.
- Re-read the whole answer top to bottom once as Rocky's lawyer: is every step explicit, chronological, consistent between Parts I and II, and does the exposure paragraph match every earlier finding?

### Step 6. Record and push
- Write `work/RN_LOG.md`: agents launched, which finished, marks given, ledger summary (confirmed / rejected / unfunded), changes applied, final stats.
- Update `HANDOFF.md` section 2 (current state, scores, what changed, unfunded items).
- Commit with a clear message and push to `claude/continue-cowork-task-qwmtn3`. Confirm the push succeeded; if it fails, say so.

### Step 7. Repeat until done
- Stop only when two independent cold lecturers (M4A and M4B, both blind) give 90 or more on the current version, M3 reports zero certain defects, and M5 has no unanswered strongest argument that can be funded.

---

## PART C. FINAL DELIVERABLES (only when Step 7 is met)
1. Final submission .docx (built by `build.py`), plus the .md.
2. Final reasoning map: for each issue in order, the facts (verbatim), each side's best argument, the authority with verbatim words, pin and status, the decisive reason, the lean, further information and its direction.
3. Side-by-side table: every fact of the problem (verbatim) | the reading passage applied to it (verbatim) | case, judge, status | casebook page (14th ed) and report pin | how the answer uses it.
4. Final marker report: both cold marks with arithmetic, the fidelity result, the opposing-counsel result, and an honest statement of residual risks (1,500 limit; Port Jackson, Brambles 164/191 in skip ranges; Trident 129 is Brennan J dissenting quoting Kitto J; casebook pages are 14th ed).
5. Publish or send them to Yusuf, upload to Google Drive (Claudee / "Rocky mid-term work …"), commit and push.

---

## PART D. CHECKLIST OF ISSUES EVERY ROUND MUST COVER (none may be missing from the review)
Part I (Rocky v Grace): 5 February call (invitation to treat; Rocky's refusal of a 'long-term loan'); 12 February email as offer (Gibson 298, both paragraphs; other bullet points; 'Confirming discussions'); 'Confirmed' as acceptance (Empirnall 534; counter-offer); consideration (Beaton 168); intention and preliminary agreements (Ermogenous [25]–[26]; Masters 360, 361, 361–2, 363 with Winn v Bull; fourth category note [5.105]; 'subject to satisfactory conditions' vs 'subject to success of Hail Mary Project'; Meehan 580–2; later conduct on formation, Brambles 164); certainty and illusory promises (Pace 151 citing Placer; Meehan 581–2, 589; Godecke 642–3 Walsh J, 646–7 Gibbs J); Rocky's claim through AMPL's advance; agency (Trident 145 Deane J; Port Jackson 240); privity (Trident 115, 123; Coulls 486–7; joint promisee); signature (Empirnall 535–6; Coulls 487); the Development Agreement ('if the Project made a profit'; 'minimal').
Part II (Rocky v AMPL or Pierre): 8 April offer and acceptance (Gibson 298; Brambles 177; Empirnall 534; Masters 361–2 on binding before signing); who promised (agency); existing legal duty rule (Sundell 327; Wigan 594 'at least when'; promises to third parties, Pao On 632); intention (Ermogenous [26]; Banque Brussels 523, 525; timing difference); certainty ('ensure', Upper Hunter 437; result vs effort; 'check in' emails, Brambles 164; AMPL's promise not illusory, Meehan 582); privity of the $10,000 (Trident 115; 'to me directly'); whether the guarantee clause binds Rocky (Trident 129 Brennan J dissenting; Empirnall 534, 535–6; Brambles 195 quoting Brogden 686); consideration for the guarantee (Trident 115; Roscorla 237; Pao On 629; Australian Woollen Mills 456); when the 12 months began (construction objective; post-contractual conduct; genesis, Brambles 163–4, 191; 'recorded'; 8 April; the March instalment); 'once Grace repays' as a condition precedent (Meehan 582; Upper Hunter 437 commercial reading); duty to co-operate (Beaton 185 McHugh JA dissenting, citing Secured Income 607); exposure stated precisely and consistently (oral undertaking; the clause; AMPL or Pierre; nominal damages if Pierre alone, Trident 118; forfeiture of the $10,000; 9 March call timing).
