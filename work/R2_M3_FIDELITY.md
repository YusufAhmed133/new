# R2_M3: Fidelity, terminology and AGLC audit (Role 3)

Target: /home/user/new/work/ANSWER.md as it stood at 14:00 on 13 October 2026 ('Word count: 1,620'; body 1,617 words by whitespace count, so the stated line is body + 3 and the answer is 20 words over the 1,600 cap).

Read in full for this audit: YUSUF_INSTRUCTIONS_VERBATIM.md; MARKERS_PROMPT.md; the problem; the Instructions; the Reading Guide; all seven slide decks; RUBRIC_RULINGS_SHEET_v12.txt section 6.1 and the R7, R8, R9 and Part 9 items 30 to 31 of 6.2; CB14 chapters 3 (to [3.210]), 4, 5, 6 (to [6.200]) and 11 (Coulls, the agency note, Trident Mason CJ and Wilson J, Deane J); the Pao On extract (pdftotext); build.py (and a scratch build of the .docx). verify.py was run: 86 spans, 0 not found. Not opened: any R2_* or MARK_* file of another reviewer.

Casebook pages below are CB14 printed pages (the student's printing may differ by 0 to 4 pages after chapter 3; the report pins are identical).

Verifier corrections found by eye: 'be put into form' is at Masters 363 (the [363] marker precedes the Winn v Bull quotation at CB14 p 154), not 362 as verify.py reports; 'takes the case out of the principle' is at Meehan 589 (the [589] marker is elided; the phrase sits two lines before '[590]' at CB14 p 183, about 45 lines after '[588]'), not 588 as verify.py reports; 'practice to ensure' is quoted from Rogers CJ at 525 (CB14 p 144), not from the editors' facts bracket that verify.py hits first.

---

## 1. Certain defects (proved at source)

**C1. Footnote 34 points Deane J to page 115, which is inside Mason CJ and Wilson J's joint judgment; the proposition is not in the casebook extract of Deane J at all.**
- Answer: 'only the parties to a contract are bound by it,[^34] so AMPL must show assent.' fn 34: 'Ibid (Deane J).' The preceding fn 33 is 'Trident (n 14) 115 (Mason CJ and Wilson J).', so fn 34 reads 'Trident 115 (Deane J)'.
- Source: CB14_ch11 p 343, '[11.60] ... MASON CJ AND WILSON J: [113] ...', with '[115]' at p 343 inside their judgment; Deane J's judgment opens at CB14_ch11 p 354: '[11.70] DEANE J: [143] Circumstances can undoubtedly arise in which accepted processes of legal reasoning require a court ... to reverse the development of the law by disowning established principle.' Nothing in Deane J's extract at 143 to 148 states that only parties are bound; his extract speaks of 'the general common law rule of privity of contract' (143) and 'the requirement of privity as a general rule' (144). The words the footnote needs ('the general rule that only the parties to a contract are bound by, and entitled to enforce, its terms') are in the full Trident reading only, which R-Y(1) says 'carries no CLR page markers'.
- Fix (footnote only, 0 words): 'Trident (n 14) (Deane J).' (R-Y(1)'s accepted no-pin form). Never 'Ibid', because 'Ibid' inherits 115.

**C2. The build script corrupts three case names in the submitted .docx (stray asterisks, roman type).** Proved by building to the scratchpad with work/build.py and reading the .docx back with pandoc:
- fn 25 renders as '*TA* Sundell\* & Sons Pty Ltd v Emm Yannoulatos (Overseas) Pty Ltd\* (1955) 56 SR (NSW) 323, 327.' (only 'TA' italic; two literal asterisks printed).
- fn 31 renders as '*Council of the* Upper Hunter\* County District v Australian Chilling and Freezing Co Ltd\* (1968) ...' (same fault).
- fn 22 renders as '*Eccles v Bryant* and Pollock [1948] Ch 93' ('and Pollock' roman).
- Cause: ital() substitutes the short titles 'Sundell' and 'Upper Hunter' inside full names it has already wrapped in asterisks (its lookbehind tests only the preceding character), and CASES lists 'Eccles v Bryant' but not 'Eccles v Bryant and Pollock'.
- Fix (0 words): substitute only in text segments outside existing *...* spans (eg split on r'(\*[^*]+\*)' and process the even segments), and add 'Eccles v Bryant and Pollock' to CASES (and 'G Scammell & Nephew Ltd v Ouston' or 'Coulls v Bagot’s Executor & Trustee Co Ltd' if those spellings change). Under SHEET D10 each case name not italicised is −0.5 (three here), and his marker wrote 'case name should always be italicised (including in text)'.

**C3. 'Intention to create legal relations' is never named in full anywhere in the answer.**
- Answer, the only naming of the element: 'their status as ‘project developers’ supports intention' (S9); 'so intention likely exists on both sides' (S33).
- Course term: Reading Guide, Week 3 Class 3A topic 'Intention to create legal relations'; the 3A deck title 'Intention to Create Legal Relations'; CB14_ch05 p 133 '[5.05] The third element of contract formation is that the parties must manifest an intention to create legal relations.' Brief Part 4: 'intention to create legal relations (always in full)'. SHEET R7 accepts 'intention' as a short form only 'under the full heading'; R-AC removed element headings, so the full term must appear once in the text.
- Fix (+4): S33 end 'so intention likely exists on both sides' to 'so intention to create legal relations likely exists on both sides'.

**C4. The 5 February call and Pierre's 'expected' are described, not named: 'invitation to treat' never appears.**
- Answer S4: 'Grace’s 5 February call asked Rocky to make an offer, so it was not itself one,[^1] and Rocky declined.' S25: 'Pierre’s statement that he ‘expected’ Rocky to ensure Grace’s payments promised nothing, so it was a request rather than an offer;[^19]'.
- Course term: Class 1A slide 27, 'Invitation to treat | An invitation for others to make an offer or enter into a negotiation.'; Class 1A slide 19, 'What is the difference between an offer and an invitation to treat?'; CB14_ch03 p 52 heading 'Offers distinguished from invitations to treat'. SHEET R7 lists 'a request that Rocky make an offer' as a proxy instance by name.
- Source for the classification: Gibson 298, Lord Diplock (CB14_ch03 p 42): 'The words “may be prepared to sell” are fatal to this; so is the invitation, not, be it noted, to accept the offer, but “to make formal application to buy” upon the enclosed application form.' (the Council's letter invited Gibson to make the offer; House of Lords, Lord Edmund-Davies, Lord Russell, Lord Fraser and Lord Keith agreeing, CB14 p 43).
- Fix: S4 'so it was not itself one,' to 'so it was an invitation to treat,' (+1); S25 'so it was a request rather than an offer;' to 'so it was an invitation to treat;' (−2).

**C5. 'The duty to co-operate' is applied but not named; SHEET R7 names this exact wording as a proxy.**
- Answer S50: 'Nor does AMPL breach its duty ‘to do everything necessary on [its] part’ to give Rocky the benefit of the contract,[^45] since its call does not stop Grace repaying.'
- Course term: CB14_ch04 p 107, heading 'The duty to co-operate' over '[4.65] The McDivitts have a contractual duty to do everything necessary on their part to enable the plaintiff to have the benefit of the contract: Secured Income ... at 607 per Mason J.' (McHugh JA, Beaton 185). SHEET R7: 'describing the doctrine in the answer’s own words (... ‘the duty ’to do everything necessary’’) is ... one proxy instance'.
- Fix (+2): 'Nor does AMPL breach its duty' to 'Nor does AMPL breach the duty to co-operate,'.

**C6. Masters' classes of preliminary agreement are relied on but 'preliminary agreement' is never named.**
- Answer S9 to S13: 'The qualifier raises whether the parties intended to be bound immediately ... the question is whether the terms were to ‘be put into form’ or to be ‘subject to a new agreement the terms of which are not expressed in detail’;[^6] ... On balance, the loan was likely left to a new agreement.'
- Course term: CB14_ch05 p 152 heading 'PRELIMINARY AGREEMENTS'; p 133 '[5.05] ... 4. Where parties reach a preliminary agreement, the question may arise whether the parties intend to be bound immediately'; Class 3A slide 22 'What are preliminary agreements? What are the 3 categories and which are binding on the parties?'; Reading Guide 3A 'preliminary agreements'. SHEET R7: the term is required 'where the answer relies on the category'.
- Fix (+1): 'The qualifier raises whether the parties intended to be bound immediately,' to 'The qualifier raises whether this preliminary agreement was intended to bind immediately,'.

**C7. 'Bilateral contract' is not named; the answer writes 'a promise for a promise'.**
- Answer S25: 'Rocky’s reply, ‘I will do that if you also promise’, offered a promise for a promise,[^20] which Pierre accepted when he ‘agreed’.[^21]'
- Course term: Class 1A slide 12, 'Bilateral contract – contract is made by exchange of promises to do something'; slide 27, 'Bilateral contract | A contract in which both parties are under a contractual obligation to perform their side of the bargain at the time of formation.' Source cited (fn 20) uses the term: McHugh JA in Integrated Computer Services, quoted by Heydon JA in Brambles 177 (CB14_ch03 p 78): 'In classical theory, the typical contract is a bilateral one and consists of an exchange of promises by means of an offer and its acceptance'. SHEET R6.2 'II.A: ... Brambles 177 on the bilateral contract'.
- Fix (+2): 'offered a promise for a promise,' to 'offered a bilateral contract, an exchange of promises,'.

**C8. The exception to the existing legal duty rule for promises to third parties is applied but not named.**
- Answer S30: 'and if Pierre promised, any duty was owed to AMPL, and ‘a pre-existing contractual obligation to a third party can be valid consideration’.[^27]'
- Course term: Class 2B slide 'Existing Legal Duty Rule', '3 exceptions to the rule: • practical benefit ... • promises to third parties (Pao On v Lau Yiu Long – class 2A) • Genuine/ bona fide compromise'; CB14_ch04 p 123 heading 'Duty owed to a third party' over '[4.145] A promise to perform an act which the promisor is under an existing duty to a third party to perform may constitute good consideration.' SHEET R7 lists 'promises to third parties' among the required names.
- Fix, see C9 (one rewrite cures both).

**C9. The Pao On quotation is cut so that its subject changes.**
- Answer S30 quotes: ‘a pre-existing contractual obligation to a third party can be valid consideration’.
- Source: Pao On 632, the Board (judgment delivered by Lord Scarman), CB14_ch04 p 126: 'Their Lordships do not doubt that a promise to perform, or the performance of, a pre-existing contractual obligation to a third party can be valid consideration.' The Board's subject is the promise to perform or the performance; the quoted words, read as a sentence, make the obligation itself the consideration. Status: the Board's holding on its second question (the extrinsic evidence showed 'the real consideration for [632] the indemnity was the promise to perform, or the performance of, the plaintiffs pre-existing contractual obligations to Fu Chip', p 125 to 126). The answer's use (Rocky's duty owed to AMPL, his new promise made to Pierre) puts our parties in the Board's positions correctly.
- Fix A (−5, cures C8 and C9): 'and if Pierre promised, the exception for promises to third parties applies, any duty being owed to AMPL.[^27]'. Fix B (+12, keeps the rule's words): 'and if Pierre promised, any duty was owed to AMPL, and under the exception for promises to third parties a promise to perform ‘a pre-existing contractual obligation to a third party can be valid consideration’.[^27]'.

**C10. Three one-sentence paragraphs (R-AC(3): 'No one-sentence paragraphs').**
- P7: 'Thus Rocky has no contractual claim against Grace: ... anything he pays AMPL.' (one sentence, 36 words).
- P10: 'Rocky’s ‘you’ points to Pierre, but Pierre controls AMPL ... what follows runs against him.' (one sentence, 48 words).
- P18: 'Interest is shown paid only until 8 February 2025; further information is needed ... whichever start date applies.' (one sentence, 40 words).
- Fix (0 words): join P10 to the end of P9 (both settle who made the 8 April offer and acceptance); join P18 to the end of P17 (both concern when payments fell due); give P7 a second sentence by joining it to the last sentence of P6, or by splitting it at the colon ('Thus Rocky has no contractual claim against Grace. The Development Agreement ...').

**C11. Word cap.** 'Word count: 1,620' is correct arithmetic (body 1,617 + 3) but 20 over his 1,600 cap. Section 6 gives a funded set that lands exactly on 1,600.

**C12. Ten sentences exceed 45 words** (Role 3 item 4): S5 (62), S15 (59), S10 (56), S33 (54), S12 (52), S26 (52), S21 (51), S25 (48), S27 (48), S32 (47). Each can be split at its '; however,' or ';' at no word cost (eg S5 at '; however, ‘I will lend’', S15 at '; however, the discretion in Meehan', S33 at '; however, Rogers CJ'). This is a mechanics rule in the role brief; his own voice favours semicolons, so split only the four over 50.

## 2. Non-compliances with SHEET_v12 R8 that AGLC itself may tolerate (certain under the binding rubric, contestable under AGLC)

- **R1. fn 4 and fn 6 name every judge of a whole-Court judgment.** CB14_ch04 p 98: 'THE COURT (DIXON CJ, WILLIAMS, WEBB, FULLAGAR and KITTO JJ): [456]'; CB14_ch05 p 152: 'THE COURT (DIXON CJ, McTIERNAN and KITTO JJ): [360]'. SHEET R8: 'judge in brackets after the pin unless the whole Court or the Board speaks (no name for Masters, Australian Woollen Mills, Mobil ...)'. Fix: delete the brackets in fn 4 and fn 6 (fn 40 inherits). What would settle it under AGLC: AGLC4 r 1.? on judicial officers (not in the course files).
- **R2. fn 38 omits the English Reports parallel the casebook heading prints.** CB14_ch04 p 110: 'Roscorla v Thomas (1842) 3 QB 234; 114 ER 496'. SHEET R8 requires 'the ER parallel where the heading prints one ... (Roscorla (1842) 3 QB 234, 237; 114 ER 496 ...)'. Fix: 'Roscorla v Thomas (1842) 3 QB 234, 237; 114 ER 496 (Lord Denman CJ).'
- **R3. 'and' for '&' in Coulls, against every casebook printing.** CB14_ch11 running head 'Coulls v Bagot’s Executor & Trustee cont.'; p 332 '[11.30] ... Coulls v Bagot’s Executor & Trustee Co Ltd (1967) 119 CLR 460'; Mason CJ and Wilson J at 114 (p 343) 'Coulls v Bagot’s Executor & Trustee Co Ltd (1967) 119 CLR 460 at 498'. Only the 4A slide prints 'and'. The answer keeps '&' for Sundell (as [4.95] prints it), so fn 16 is also inconsistent with fn 25. The brief's checklist: ''and' not '&' in case names (except as reported)'. Fix: fn 16 'Coulls v Bagot’s Executor & Trustee Co Ltd' (and update build.py CASES). Contestable only if the 119 CLR report title (casebook p 324, not in this file) prints 'and'.
- Scammell (fn 31) is NOT a defect: Upper Hunter 437 prints 'G Scammell & Nephew Ltd v Ouston [1941] AC 251' with no pin, but Mason J in Meehan 587 (CB14_ch06 p 182) prints '(G Scammell and Nephew Ltd v Ouston [1941] AC 251 at 268)', so both the 'and' spelling and the pin 268 are verifiable in the course materials. The SHEET's note that 437 prints no pin does not make 268 an outside source.

## 3. Possible errors (not proved; what would settle each)

- **P1. Ambiguous onus (S9).** 'the onus lying on whichever party relies on it' — 'it' can be read as the qualifier. Ermogenous [26] (Gaudron, McHugh, Hayne and Callinan JJ, CB14_ch05 p 135): 'In this case, where issue was joined about the existence of a legally binding contract between the parties, there could be no doubt that it was for the appellant to demonstrate that there was such a contract.' The onus lies on the party asserting the contract, not on a party relying on the qualifier. Fix (0): 'the onus lying on whichever party asserts a contract,'.
- **P2. Brambles 164 hedge dropped (S44).** Heydon JA (CB14_ch03 p 73 to 74): 'The third relevant principle is that post-contractual conduct is not admissible on the question of what a contract means as distinct from the question of whether it was formed. As explained by Priestley JA ... the status of the relevant High Court authorities is unclear: hence unless it is demonstrated that the later decisions of the Victorian Full Court and Court of Appeal against admissibility ... are clearly wrong or they are overruled, they should be followed in New South Wales.' Status: majority on this point, because Ipp AJA (p 82, [184]) agreed 'For the reasons set out by Heydon JA' on the July 1990 contract and Mason P (p 73) agreed with Ipp AJA. The answer's 'cannot construe the term' is right for NSW, where the problem is set; the hedge is that the High Court position is 'unclear'. Optional fix (+3): 'cannot, in New South Wales, construe the term'. Low priority.
- **P3. Trident 115 'hitherto' (S20, S36, S40).** Mason CJ and Wilson J (CB14_ch11 p 343): 'This court has hitherto accepted that a third party cannot sue upon a contract and that a stranger to the consideration cannot maintain an action at law upon it'; they go on (p 347 to 348) to hold 'that it be recognised that McNiece was entitled to succeed', the question being 'whether the old rules apply to a policy of insurance'. Their departure is confined to insurance, so the quoted rule still governs a loan, but a harsh marker could say the citation is to judges who were reconsidering it. Settled by keeping the cite (the departure is confined to insurance); no change needed unless words allow 'hitherto accepted'.
- **P4. Trident 145 'ordinarily' dropped (S19).** Deane J (CB14_ch11 p 355): 'If the promisee contracts as agent for a disclosed or undisclosed principal, the principal will ordinarily himself be, for the purposes of the requirement of privity, a party to the contract.' The answer's 'a principal is a party where another ‘contracts as agent’ for him' omits 'ordinarily'. Harmless to the conclusion (the answer denies agency); no change needed.
- **P5. Australian Woollen Mills 457 used for an exchange of promises (S8).** The Court's words (CB14_ch04 p 98 to 99) concern 'cases of this class', 'an offer of a promise for an act': 'there must subsist, so to speak, [457] the relation of a quid pro quo'. The answer applies it to Grace's implied promise to repay against Rocky's promise to lend. The 2A slide uses it as the general 'bargain' or 'Quid Pro Quo' requirement, so a lecturer would accept it; it would be exact for S42 (AMPL's act of signing), where it is also used. No change needed; note 'consideration' is not named in Part I (it is named in Part II, which satisfies SHEET R7's 'unless the course name appears once elsewhere').
- **P6. Upper Hunter 437 used for reading a condition 'commercially' (S49).** Barwick CJ (CB14_ch06 p 159) was answering whether cl 5 was void for uncertainty: 'In the search for that intention, no narrow or pedantic approach is warranted, particularly in the case of commercial arrangements. Thus will uncertainty of meaning, as distinct from absence of meaning or of intention, be resolved.' The answer puts it in Rocky's mouth for construing who must repay. Arguable as a construction principle ('The question becomes one of construction, of ascertaining the intention of the parties'); a stricter marker would say the passage answers a different question. Settled by the answer's own rejection of the argument; no change needed.
- **P7. Banque Brussels status and hedge (S32, S33).** Rogers CJ sat at first instance ('Supreme Court of New South Wales – Action', CB14_ch05 p 139) and called the 'practice to ensure' question 'far more thorny', answering it only 'if the paragraph is read as follows' (p 144). The answer presents 'no relevant difference' without either. The brief asks for status 'where it matters'; here it bears on Rocky's own undertaking, a live point. Optional: 'Rogers CJ, at first instance, saw ...' (+3).
- **P8. Brambles 176 to 177 status undisclosed (S25, S26).** These are Heydon JA's reasons for a route Ipp AJA did not take (Ipp AJA, p 82: 'I have, however, done so by a route different to that followed by Heydon JA'); Mason P (p 73) agreed with Ipp AJA's reasons but added 'As Heydon JA demonstrates, this case shows the difficulties of pressing too far classical theory of contract formation based upon offer and acceptance'. The passages cited are Heydon JA's survey of that difficulty, quoting McHugh JA (Hope and Mahoney JJA concurring) and Lord Greene MR, so Mason P's endorsement covers them. Correct as cited; no 'dissenting' or minority label is required.
- **P9. Judge forms for the Board and the Court.** fn 27 '(Lord Scarman)'; R-P accepts the Board with no name or '(Lord Scarman for the Board)', and CB14 p 123 prints 'The judgment of their Lordships was delivered by LORD SCARMAN'. fn 38 '(Lord Denman CJ)' is expressly accepted by R-P. Optional fn 27: '(Lord Scarman for the Board)'.
- **P10. 'Placer' used in the body without a short title.** S14 'in Placer a promise ...'; fn 10 gives the full citation without '(‘Placer’)'. Placer is cited once, so AGLC needs no short title for the footnotes; the body's short form is ordinary prose usage. Optional fn 10 '... 361 (Taylor and Owen JJ) (‘Placer’).'
- **P11. Derived facts stated without a hedge (S39).** 'having ‘attended’ with a reasonable opportunity to object, Rocky arguably took the benefit of the $10,000 promise with knowledge of the clause'. The problem says only that 'Rocky, Grace, and Pierre attended a meeting at AMPL’s office' and 'the clause was included in the Loan Agreement before it was signed by Grace and AMPL'; nothing says Rocky saw the clause or could object. 'arguably' governs 'took', not the opportunity. Fix (+1): 'but, having ‘attended’, Rocky arguably had a reasonable opportunity to object and took the benefit of the $10,000 promise with knowledge of the clause;'.
- **P12. Ermogenous paragraph pins.** The casebook prints CLR page markers ([105], [106]), not paragraph numbers. The 3A slides print '26. In this context of [ICLR] there is frequent reference to "presumptions"' and '27. ... the use of the language of presumptions may lead', which fixes [26]; [25] is then the preceding paragraph ('Because the inquiry about this last aspect may take account of ... the status of the parties to it ...'), which carries 'objective assessment', 'status' and 'same sense ... other contractual contexts'. Correct on that inference; the 209 CLR text would settle it.

## 4. Sentence-by-sentence trace of every proposition of law

Status key: CORRECT; CERTAIN (proved defect); POSSIBLE. Speaker and status are given from the casebook judge headings; 'question' is what the court was answering.

| S | Answer (proposition) | fn | Source, CB14 page, report pin, speaker, status, question, context | Status |
|---|---|---|---|---|
| S3 | 'The first issue is whether the February dealings formed a loan contract' | — | Framing; no law. | CORRECT |
| S4 | A request that Rocky make an offer is not an offer | 1 | Gibson 298, Lord Diplock (House of Lords unanimous), ch03 p 42: 'The words “may be prepared to sell” are fatal to this; so is the invitation, not ... to accept the offer, but “to make formal application to buy”'. Question: whether the Council's letter was an offer. | CORRECT in law; CERTAIN proxy for 'invitation to treat' (C4) |
| S5 | 'I will lend' plus 'Please confirm agreement' is likely an offer, unlike 'may be prepared to sell' | 2 | Gibson 298 as above (Ibid correct). Similar: both are written communications naming price or terms; different: 'I will lend' is the indicative mood, which Lord Diplock contrasted ('with its use of the indicative mood ... might have been understood ... as indicating a firm offer', p 42). | CORRECT |
| S6 | Acceptance requires 'an external manifestation of assent to an offer' | 3 | Empirnall 534, McHugh JA (Samuels JA agreeing; Kirby P to the same effect), ch03 p 71: 'The objective theory of contract requires an external manifestation of assent to an offer.' | CORRECT |
| S7 | 'Confirmed' answered 'confirm agreement' and added no terms, so likely accepted | — | Application of S6. | CORRECT |
| S8 | Grace's implied promise would stand in 'the relation of a quid pro quo' to Rocky's promise | 4 | Australian Woollen Mills 457, the Court, ch04 p 99: 'there must subsist, so to speak, [457] the relation of a quid pro quo.' Context: promise for an act. | CORRECT (P5); fn 4 judge naming R1 |
| S9 | Whether parties intended to be bound immediately is judged objectively; onus on the party relying; status supports intention | 5 | Ermogenous [25] to [26], joint judgment of four (Kirby J separately), ch05 p 135: 'the search for the “intention to create contractual relations” requires an objective assessment'; 'the status of the parties to it'; '[a]t best, the use of that language does no more than invite attention to identifying the party who bears the onus of proof ... it was for the appellant to demonstrate that there was such a contract.' | CORRECT in law; POSSIBLE ambiguity 'relies on it' (P1); CERTAIN unnamed 'preliminary agreement' (C6) |
| S10 | Where not 'expressly stated to be subject to a formal contract', question is 'put into form' or 'subject to a new agreement' | 6 | Masters 363, the Court, quoting Jessel MR in Winn v Bull, ch05 p 154: 'When it is not expressly stated to be subject to a formal contract it becomes a question of construction, whether the parties intended that the terms agreed on should be put into form, or whether they should be subject to a new agreement the terms of which are not expressed in detail'. 'quoting' form correct. | CORRECT; fn 6 judge naming R1 |
| S11 | Godecke: solicitors' terms bound because they had to be reasonable 'in an objective sense' | 7 | Godecke 642 to 643, Walsh J (Mason J agreeing: 'I agree with the reasons for judgment prepared by my brother Walsh', p 188), ch06 p 186: 'It means that what is required must be reasonable in an objective sense, and in case of [643] dispute this is a matter which the court can decide.' Result: 'a binding agreement was made'. | CORRECT |
| S11 | 'satisfactory' leaves the judgment to the party the condition protects | 8 | Meehan 580 to 581, Gibbs CJ, ch06 p 180 to 181: 'its natural effect is to leave it to the purchaser to determine ...'; '[581] Such a condition is generally entirely for the protection of the purchaser, and it is the satisfaction of the purchaser, not that of some hypothetical reasonable man'. Our party in the purchaser's position: Rocky, as the party protected. | CORRECT |
| S12 | Gibbs J obiter doubted a contract where one party settles further terms; 'may be different' for 'subsidiary matters' | 9 | Godecke 646 to 647, Gibbs J (concurring in result), ch06 p 187: 'it does not necessarily follow ... that an agreement which left further terms to be settled by one of the parties, rather than by his solicitors, would be treated as a concluded contract'; '[647] ... Perhaps it may be different where agreement has been reached on all essential terms but the determination of subsidiary matters has been left to one of the parties'; p 188 'However, it is unnecessary to express any concluded opinion'. 'in obiter' and the 'Perhaps' hedge are kept. | CORRECT |
| S13 | Conclusion: loan likely left to a new agreement | — | Masters' third class (p 153, [5.95]). | CORRECT; unnamed category (C6) |
| S14 | Placer: no 'identifiable criteria', 'solely to the discretion', 'wholly unenforceable' | 10 | Placer 361, Taylor and Owen JJ (majority 3:2 with Kitto J; Menzies and Windeyer JJ dissenting, p 188), ch06 p 189: 'a complete absence ... of any identifiable criteria ...; this is left solely to the discretion of the Commonwealth ... as such, is wholly unenforceable.' Promisor's position matches (Commonwealth promisor; Rocky promisor). | CORRECT |
| S15 | As in Meehan, Rocky must judge honestly | 11 | Meehan 581, Gibbs CJ, ch06 p 181: 'No doubt it may be implied that the purchaser will act honestly in deciding whether or not he is satisfied.' (No majority on honest versus reasonable: Mason J 591 undecided; Wilson J 597 to 598 inclined to honesty.) The answer claims no majority. | CORRECT |
| S15 | Honesty 'takes the case out of the principle' | 12 | Meehan 589, Mason J, ch06 p 183: 'The limitation that the purchaser must act honestly, or honestly and reasonably, takes the case out of the principle that: where words which by themselves constitute a promise are accompanied by words which show that the promisor is [590] to have a discretion ...'. Paraphrase of the principle accurate. Pin 589 (marker elided). | CORRECT |
| S15 | Meehan's discretion related 'only to the fulfilment of a condition' | 13 | Meehan 581, Gibbs CJ, ch06 p 181: 'that principle does not apply where the discretion or option of the contracting party relates, not to the performance of the contractual obligations themselves, but only to the fulfilment of a condition upon which the contract depends.' | CORRECT |
| S16 | Email bound neither party; no claim that Rocky failed to lend | — | Conclusion. | CORRECT |
| S17–S18 | AMPL's advance did not perform Rocky's promise | — | Facts only ('$1,150,000', 'advanced by AMPL', 'recorded ... 4% per annum'). | CORRECT |
| S19 | A principal is a party where another 'contracts as agent' for him | 14 | Trident 145, Deane J, ch11 p 355: 'If the promisee contracts as agent for a disclosed or undisclosed principal, the principal will ordinarily himself be ... a party to the contract.' | CORRECT ('ordinarily' dropped, P4) |
| S20 | Privity: 'a third party cannot sue upon a contract' | 15 | Trident 115, Mason CJ and Wilson J, ch11 p 343: 'This court has hitherto accepted that a third party cannot sue upon a contract'. | CORRECT (P3) |
| S21 | Party status turns on 'the written instrument itself' | 16 | Coulls 487, Taylor and Owen JJ (with McTiernan J the majority; Barwick CJ and Windeyer J dissenting on construction), ch11 p 327: 'the mere fact that her signature appears does not make her a party; this is a question to be resolved upon a consideration of the written instrument itself.' | CORRECT |
| S21 | Not even a joint promisee | 17 | Coulls 486, Taylor and Owen JJ, ch11 p 326: joint promisees ('if one, only, of two joint promisees provides the consideration ... an action to recover must have been brought by both promisees'). | CORRECT |
| S21 | Signature is not the test; Mrs Coulls signed yet was not a party | 18 | Coulls 487, as for fn 16. | CORRECT |
| S22 | No contractual claim against Grace | — | Facts: 'if the Project made a profit'. | CORRECT; one-sentence paragraph (C10) |
| S25 | Pierre's 'expected' promised nothing, so not an offer | 19 | Gibson 298, as S4. | CORRECT in law; CERTAIN proxy (C4) |
| S25 | Rocky's reply offered a promise for a promise | 20 | Brambles 177, Heydon JA, quoting McHugh JA in Integrated (Hope and Mahoney JJA concurring), ch03 p 78: 'the typical contract is a bilateral one and consists of an exchange of promises by means of an offer and its acceptance'. Context: Heydon JA's survey of cases offer and acceptance does not fit; the quoted sentence states the classical case. | CORRECT; CERTAIN proxy for 'bilateral contract' (C7); status P8 |
| S25 | Pierre accepted when he 'agreed' | 21 | Empirnall 534, as S6. | CORRECT |
| S26 | Parties bound 'when, and in the manner in which, they intend' (said of exchanged contracts) | 22 | Brambles 176, Heydon JA, quoting Lord Greene MR in Eccles, ch03 p 77: 'Another example concerns the exchanges of contracts to sell land ...; despite that Lord Greene MR observed of the practice: “Parties become bound by contract when, and in the manner in which, they intend and contemplate becoming bound. It is a question of the facts of each case …”'. Confining words kept ('said of exchanged contracts'). | CORRECT |
| S27 | Objectively, Pierre likely contracted 'as agent' for AMPL | 23, 24 | Ermogenous [25] ('It describes what it is that would objectively be conveyed by what was said or done', p 135); Trident 145, Deane J, as S19. | CORRECT; one-sentence paragraph (C10); 'what follows runs against him' is an internal cross-reference |
| S28 | AMPL may invoke the existing legal duty rule | 25 | Sundell 327, the court, as reported in the editors' note [4.95], ch04 p 111: 'every promise allegedly given to the plaintiff by the defendant under the so called second agreement was identical with a promise given under the original agreement.' Paraphrase, cited by report alone (SHEET R8). | CORRECT |
| S29 | The rule bites on a promise 'made to the promisee under that contract', and none then existed | 26 | Wigan 594, Mason J (Walsh and Gibbs JJ agreeing; Menzies J and McTiernan ACJ same conclusion, p 130), ch04 p 129: 'The general rule is that a promise to perform an existing duty is no consideration, at least when the promise is made by a party to a pre-existing contract, when it is made to the promisee under that contract, and it is to do no more than the promisor is bound to do under the contract.' 'at least' marks the three conditions as sufficient, not necessary; harmless here because the answer's point is that no existing duty existed at all, and the rule's subject is 'a promise to perform an existing duty'. | CORRECT |
| S30 | Third-party duty can be valid consideration | 27 | Pao On 632, the Board, ch04 p 126 (quoted in C9). | CORRECT in law; CERTAIN truncation (C9) and unnamed exception (C8) |
| S31 | 'Rocky likely gave consideration.' | — | Conclusion (four-word one-clause sentence). | CORRECT |
| S32 | Presumptions only 'invite attention to identifying the party who bears the onus of proof', here Rocky | 28 | Ermogenous [26], ch05 p 135, quoted at S9 ('At best' dropped; it strengthens rather than weakens the point). Onus on Rocky as party asserting the $10,000 contract: correct party position. | CORRECT |
| S32 | Fixed-sum promise in business is 'appropriately promissory in character' | 29 | Banque Brussels 523, Rogers CJ (first instance), ch05 p 142: 'If the statements are appropriately promissory in character, courts should enforce them when they are uttered in the course of business and there is no clear indication that they are not intended to be legally enforceable.' | CORRECT (status P7) |
| S33 | Rogers CJ saw 'no relevant difference' between a 'practice to ensure' and a promise 'to ensure' | 30 | Banque Brussels 525, Rogers CJ, ch05 p 144: 'The question whether the third paragraph ... is promissory is far more thorny. However, in my view, if the paragraph is read as follows: “it is our practice to ensure that Spedley is at all times in a position to repay all loans made to it by your Bank”, its promissory nature is much clearer. I see no relevant difference between that and saying that “we promise to ensure that” Spedley ...'. | CORRECT (hedge P7); CERTAIN unnamed 'intention to create legal relations' (C3) |
| S34 | Not 'so obscure' as to be uncertain | 31 | Upper Hunter 437, Barwick CJ (appeal allowed), quoting Lord Wright, ch06 p 159: 'So long as the language employed by the parties ... is not “so obscure and so incapable of any definite or precise meaning that the court is unable to attribute to the parties any particular contractual intention”, the contract cannot be held to be void or uncertain'. Pin 268 for Scammell verified at Meehan 587, ch06 p 182. | CORRECT |
| S35 | Objectively, 'I will do that' contains no words of effort | 32 | Ermogenous [25], as S27. | CORRECT |
| S36 | Rocky is the promisee and no 'stranger to the consideration' | 33 | Trident 115, Mason CJ and Wilson J, ch11 p 343: 'a stranger to the consideration cannot maintain an action at law upon it'. | CORRECT |
| S37 | '[T]he clause' most naturally means the guarantee clause | — | Construction of the problem's 'the clause was included'; '[T]' capital alteration correct. | CORRECT |
| S38 | Only the parties to a contract are bound by it | 34 | See C1: wrong pin, not in casebook extract. | CERTAIN (C1) |
| S39 | Silence while a clause is included is generally insufficient | 35 | Empirnall 534, McHugh JA, ch03 p 71: 'the silent acceptance of an offer is generally insufficient to create any contract'. Hedge 'generally' kept. | CORRECT |
| S39 | Taking the benefit with knowledge of the terms and a reasonable opportunity to object | 36 | Empirnall 535 to 536, McHugh JA, ch03 p 71 to 72: '[535] ... the offeree will be bound because, knowing of the terms of the offer ..., he has exercised a choice and taken the benefit of the offer'; 'where an offeree with a reasonable opportunity to reject the offer ... takes the benefit of them ..., it is open to the tribunal of fact to hold that the offer was accepted'; '[536] ... taking the benefit of an offer with knowledge of its terms'. Similar: Empirnall took the benefit of work offered on terms; different: the $10,000 promise was a separate bargain from the clause, which the answer concedes ('he could answer ...'). | CORRECT; derived facts unhedged (P11) |
| S40 | AMPL must show consideration moving from itself | 37 | Trident 115, as S36. | CORRECT |
| S41 | AMPL's earlier advance is past consideration | 38 | Roscorla 237, Lord Denman CJ for the Court, ch04 p 111: 'the general rule, that a consideration past and executed will support no other promise than such as would be implied by law.' | CORRECT; fn 38 ER parallel R2 |
| S41 | Counts only if at the promisor's request, understood to be 'remunerated', 'legally enforceable had it been promised in advance' | 39 | Pao On 629, the Board, ch04 p 124 and the course extract: 'The act must have been done at the promisors’ request: the parties must have understood that the act was to be remunerated ... and payment ... must have been legally enforceable had it been promised in advance.' Party position: Rocky as promisor, AMPL as actor: correct. | CORRECT |
| S42 | Signing after the clause was an act 'really done in consideration of' the guarantee | 40 | Australian Woollen Mills 456, the Court, ch04 p 99: 'the act was really done in consideration of a potential promise inherent in the statement or announcement' (before '[457]'). Promise-for-act context matches. | CORRECT |
| S43 | Whether the call was premature turns on when the 12 months began | — | Framing. | CORRECT |
| S44 | Post-contractual conduct cannot construe the term | 41 | Brambles 164, Heydon JA (adopted by Ipp AJA, Mason P agreeing), ch03 p 73 to 74, quoted at P2. | CORRECT (hedge P2) |
| S44 | If ambiguous, mutually known facts showing 'the genesis of the transaction' are admissible | 42 | Brambles 191, Ipp AJA (Mason P agreeing), ch03 p 82: 'Where ambiguities exist, mutually known facts establishing the commercial purpose of the contract, the genesis of the transaction, the background and the context in which the parties are operating will be admissible'. The answer keeps the ambiguity condition ('the term being arguably ambiguous'). | CORRECT |
| S45–S46 | 'recorded' governs the rate too; term arguably ran from 8 April 2024 | — | Textual analysis of the problem. | CORRECT |
| S47 | March instalment; further information | — | Facts ('Between 8 April 2024 and 8 February 2025'). | CORRECT; one-sentence paragraph (C10) |
| S48 | 'once Grace repays the Loan' is a condition precedent to the obligation, not to the contract | 43 | Meehan 582, Gibbs CJ, ch06 p 181: 'It is clear that the condition in Special Condition 1(b) is not a condition precedent to contract ... Whether the condition is described as a condition precedent to completion, or as a condition subsequent, seems largely a matter of words'; 'a condition on whose fulfilment the obligation to complete the contract depended'. | CORRECT |
| S49 | Rocky could argue that, read commercially, his payment satisfies the condition | 44 | Upper Hunter 437, Barwick CJ, ch06 p 159 (quoted at P6). | POSSIBLE (P6) |
| S50 | AMPL does not breach its duty 'to do everything necessary on [its] part' | 45 | Beaton 185, McHugh JA (dissenting in result: Kirby P found no contract, Mahoney JA a frustrated contract; 'Appeal dismissed', ch04 p 108), citing Mason J in Secured Income 607, ch04 p 107 (quoted at C5). 'citing' is right (McHugh JA paraphrases Mason J, no quotation marks). Dissent disclosed in fn 45. | CORRECT in law; CERTAIN proxy (C5) |
| S51–S53 | Exposure: $1,150,000 if Rocky assented to the clause; damages if bound only orally; $10,000 falls due only if Grace repays | — | Terms of the clause ('personally guaranteed repayment of the Loan'); the condition (Meehan 582, S48). R-AE satisfied (source of each consequence named in the same paragraph or by cross-reference). | CORRECT |

## 5. Terminology: every legal term and doctrine name in the answer

| Term in answer | Lecturer's term and where it appears | Verdict |
|---|---|---|
| offer; 'not itself one' (S4); 'a request rather than an offer' (S25) | 'invitation to treat': Class 1A slides 19, 27; CB14 p 52 heading | PROXY ×2 (C4) |
| acceptance; 'external manifestation of assent' | Class 1B 'Agreement: Elements of Acceptance'; Empirnall 534 | OK |
| 'a promise for a promise' (S25) | 'bilateral contract': Class 1A slides 12, 27 | PROXY (C7) |
| 'the relation of a quid pro quo' | Class 2A slide 5 'There must be a relation of quid pro quo'; slide 7 'the “bargain” or “Quid Pro Quo” requirement' | OK ('consideration' named in Part II) |
| 'intended to be bound immediately' (S9); Masters' 'put into form' / 'new agreement' | 'preliminary agreement', 'the different categories of preliminary agreement': CB14 p 133, p 152; Class 3A slide 22; Reading Guide 3A | PROXY (C6) |
| 'intention' (S9, S33) | 'intention to create legal relations' (in full): Reading Guide 3A; 3A deck title; CB14 p 133 | PROXY (C3) |
| 'judged objectively'; 'Objectively' | 3A 'objective intention'; Ermogenous [25] | OK |
| onus; 'family presumptions' | 3A 'presumptions'; Ermogenous [26] | OK |
| 'in an objective sense'; 'no such standard' | 3B 'objective standard'; CB14 p 159 heading 'Implying objective standards' | OK |
| 'arguably illusory'; 'discretion' | CB14 p 179 heading 'ILLUSORY PROMISES'; 3B 'Illusory promise'; 'discretion as to its terms' | OK |
| 'condition precedent' | Meehan 582 (Gibbs CJ) | OK |
| privity; 'third party'; 'joint promisee'; 'stranger to the consideration' | 4A 'Privity of contract'; CB14 p 332 note 'joint promisee doctrine'; Trident 115 | OK |
| 'agent'; 'principal'; 'contracts as agent' | CB14 p 332 heading 'NON-APPLICATION OF THE PRIVITY RULE: AGENCY'; 4A 'Agency' | OK |
| 'existing legal duty rule' | 2B heading 'Existing Legal Duty Rule'; Reading Guide 2B | OK |
| third-party duty limb (S30) | 'promises to third parties' (2B slide); CB14 p 123 heading 'Duty owed to a third party' | PROXY (C8) |
| consideration; 'consideration moving from itself' | 2A 'Must flow between the parties in both directions'; Trident 115 | OK |
| 'letter of comfort'; 'moral assurance' | 3A 'letter of comfort'; Kleinwort Benson 'moral responsibility' (Banque 505) | OK |
| 'uncertain'; 'so obscure' | 3B 'Certainty'; CB14 p 158 heading 'CERTAINTY' | OK |
| 'Silence'; 'took the benefit ... with knowledge' | 1B 'Can silence be a valid acceptance?'; 'Acceptance by Conduct' (1B slide 19) | OK; 'acceptance by conduct' could be named at no cost ('assent' is accepted) |
| 'past consideration'; 'remunerated' | 2A 'Past consideration', 'Exception to past consideration rule' | OK |
| 'Post-contractual conduct'; 'genesis of the transaction' | Heydon JA 164 ('post-contractual conduct'); Class 1B slides 'post-formation conduct'; Ipp AJA 191 | OK |
| 'its duty ‘to do everything necessary on [its] part’' | 'The duty to co-operate': CB14 p 107 heading | PROXY (C5), named by SHEET R7 |
| 'further information' | Instructions ('indicate what further information you require') | OK |
| 'obiter' | standard; Gibbs J 'unnecessary to express any concluded opinion' | OK |

No invented abbreviations; 'AMPL', 'Loan', 'Loan Agreement', 'Development Agreement' are the problem's own definitions. No 'deal', 'meeting of the minds', 'collateral contract', 'gap-filling', 'branch' or similar.

## 6. AGLC 4, footnote by footnote

| fn | Text | Check | Verdict |
|---|---|---|---|
| 1 | Gibson ... [1979] 1 WLR 294, 298 (Lord Diplock) (‘Gibson’). | Report as CB14 p 40; short title placed after judge | OK |
| 2 | Ibid. | Same source and pin | OK |
| 3 | Empirnall ... (1988) 14 NSWLR 523, 534 (McHugh JA) (‘Empirnall’). | | OK |
| 4 | Australian Woollen Mills ... (1954) 92 CLR 424, 457 (Dixon CJ, Williams, Webb, Fullagar and Kitto JJ) (‘Australian Woollen Mills’). | Whole Court named | R1 |
| 5 | Ermogenous ... (2002) 209 CLR 95, [25]–[26] (Gaudron, McHugh, Hayne and Callinan JJ) (‘Ermogenous’). | Paragraph pins in brackets, en dash | OK (P12) |
| 6 | Masters ... 363 (Dixon CJ, McTiernan and Kitto JJ), quoting Winn v Bull (1877) 7 Ch D 29, 32 (Jessel MR). | 'quoting' form right; whole Court named | R1 |
| 7 | Godecke ... (1973) 129 CLR 629, 642–3 (Walsh J) (‘Godecke’). | fn 6 two-source, so no ibid needed (new source anyway) | OK |
| 8 | Meehan ... (1982) 149 CLR 571, 580–1 (Gibbs CJ) (‘Meehan’). | | OK |
| 9 | Godecke (n 7) 646–7 (Gibbs J). | | OK |
| 10 | Placer ... (1969) 121 CLR 353, 361 (Taylor and Owen JJ). | 'Limited' to 'Ltd' correct | OK (P10) |
| 11 | Meehan (n 8) 581 (Gibbs CJ). | | OK |
| 12 | Ibid 589 (Mason J). | | OK |
| 13 | Ibid 581 (Gibbs CJ). | | OK |
| 14 | Trident ... (1988) 165 CLR 107, 145 (Deane J) (‘Trident’). | | OK |
| 15 | Ibid 115 (Mason CJ and Wilson J). | | OK |
| 16 | Coulls v Bagot’s Executor and Trustee Co Ltd (1967) 119 CLR 460, 487 (Taylor and Owen JJ). | '&' as casebook prints | R3 |
| 17 | Ibid 486 (Taylor and Owen JJ). | | OK |
| 18 | Ibid 487 (Taylor and Owen JJ). | | OK |
| 19 | Gibson (n 1) 298 (Lord Diplock). | | OK |
| 20 | Brambles ... (2001) 53 NSWLR 153, 177 (Heydon JA) (‘Brambles’), quoting Integrated Computer Services ... (1988) 5 BPR 11,110, 11,117–18 (McHugh JA). | Short title before ', quoting' | OK |
| 21 | Empirnall (n 3) 534 (McHugh JA). | Not ibid after a two-source footnote | OK |
| 22 | Brambles (n 20) 176 (Heydon JA), quoting Eccles v Bryant and Pollock [1948] Ch 93, 104 (Lord Greene MR). | Name and report as Masters prints (CB14 p 154); pin as Brambles prints | OK in text; italics broken in build (C2) |
| 23 | Ermogenous (n 5) [25] (...). | | OK |
| 24 | Trident (n 14) 145 (Deane J). | | OK |
| 25 | TA Sundell & Sons Pty Ltd v Emm Yannoulatos (Overseas) Pty Ltd (1955) 56 SR (NSW) 323, 327. | As [4.95] prints; no judge (the court) | OK in text; italics broken in build (C2) |
| 26 | Wigan v Edwards (1973) 47 ALJR 586, 594 (Mason J). | ALJR as casebook | OK |
| 27 | Pao On ... [1980] AC 614, 632 (Lord Scarman) (‘Pao On’). | | OK (P9) |
| 28 | Ermogenous (n 5) [26] (...). | | OK |
| 29 | Banque Brussels ... (1989) 21 NSWLR 502, 523 (Rogers CJ). | | OK |
| 30 | Ibid 525 (Rogers CJ). | | OK |
| 31 | Upper Hunter ... (1968) 118 CLR 429, 437 (Barwick CJ) (‘Upper Hunter’), quoting G Scammell and Nephew Ltd v Ouston [1941] AC 251, 268 (Lord Wright). | Pin 268 verified at Meehan 587 | OK in text; italics broken in build (C2) |
| 32 | Ermogenous (n 5) [25] (...). | | OK |
| 33 | Trident (n 14) 115 (Mason CJ and Wilson J). | | OK |
| 34 | Ibid (Deane J). | Inherits 115 | CERTAIN (C1) |
| 35 | Empirnall (n 3) 534 (McHugh JA). | | OK |
| 36 | Ibid 535–6 (McHugh JA). | | OK |
| 37 | Trident (n 14) 115 (Mason CJ and Wilson J). | | OK |
| 38 | Roscorla v Thomas (1842) 3 QB 234, 237 (Lord Denman CJ). | ER parallel omitted | R2 |
| 39 | Pao On (n 27) 629 (Lord Scarman). | | OK |
| 40 | Australian Woollen Mills (n 4) 456 (...). | Inherits R1 | R1 |
| 41 | Brambles (n 20) 164 (Heydon JA). | | OK |
| 42 | Ibid 191 (Ipp AJA). | fn 41 single-source, so ibid right; 'Ipp AJA' as Mason P names him (CB14 p 73) | OK |
| 43 | Meehan (n 8) 582 (Gibbs CJ). | | OK |
| 44 | Upper Hunter (n 31) 437 (Barwick CJ). | (n X) after fn 43; fn 31 short title introduced | OK |
| 45 | Beaton v McDivitt (1987) 13 NSWLR 162, 185 (McHugh JA dissenting), citing Secured Income ... (1979) 144 CLR 596, 607 (Mason J). | 'dissenting' form right; 'citing' right | OK |

All footnotes end with a full stop; all ranges use en dashes (six, all in footnotes); no 'at' before pins; no textbook, slide, casebook or meta citation; one source per marker except the AGLC r 1.3 'quoting'/'citing' pairs.

## 7. Voice and mechanics

- Dashes in the body: none. Double quotation marks: none. Contractions: none (the problem's 'can’t', 'won’t', 'don’t' are not quoted). First person: none. Meta language: none of weeks, slides, course; one internal cross-reference, 'what follows runs against him' (S27), which reads as meta and can go (cut C1 in section 8 removes it).
- One-clause or near one-clause sentences: S6 'Acceptance requires ‘an external manifestation of assent to an offer’.' (10 words); S13 'On balance, the loan was likely left to a new agreement.' (11); S31 'Rocky likely gave consideration.' (4); S43 'Whether AMPL’s 9 March 2025 call was premature depends on when the 12 months began.' (15). He 'despises' one-clause sentences; S31 can join S30 ('...; Rocky therefore likely gave consideration'), S6 can join S7 with a semicolon, S13 can join S12, all at 0 to +1 word.
- Sentences over 45 words: C12.
- One-sentence paragraphs: C10.
- Fragments after semicolons: none found; each semicolon is followed by a full clause.
- Ambiguous pronoun: S9 'relies on it' (P1). Others ('it' in S4, S30, S37) resolve to the nearest noun.
- Zeugma or stacked quotation: S30 'ensuring ‘all payments’ ‘promptly’' (two adjacent quotations; repeated in S47); readable, but 'ensuring that Grace make ‘all payments’ ‘promptly’' as in S47 is the problem's syntax.
- Invented abbreviations: none.

## 8. Fixes ranked by marks per word, and a funded set that lands on 1,600

Ranked (mark source in brackets):
1. C1 fn 34 to 'Trident (n 14) (Deane J).' (0 words; R8, D13).
2. C2 build.py nesting fix and 'Eccles v Bryant and Pollock' (0; D10 −1.5 avoided; stray asterisks in a submitted footnote).
3. C10 merge P10 into P9, P18 into P17, and split or join P7 (0; R-AC(3)).
4. C4 S25 'so it was an invitation to treat;' (−2) and S4 'so it was an invitation to treat,' (+1) (R7, D12).
5. C9 and C8 together, Fix A: 'and if Pierre promised, the exception for promises to third parties applies, any duty being owed to AMPL.' (−5) (R7; quotation fidelity).
6. P1 'the onus lying on whichever party asserts a contract,' (0).
7. C6 'The qualifier raises whether this preliminary agreement was intended to bind immediately,' (+1).
8. C7 'offered a bilateral contract, an exchange of promises,' (+2).
9. C5 'Nor does AMPL breach the duty to co-operate,' (+2).
10. C3 'so intention to create legal relations likely exists on both sides.' (+4).
11. P11 'but, having ‘attended’, Rocky arguably had a reasonable opportunity to object and took the benefit ...' (+1).
12. R1, R2, R3 footnote forms (0).

Net cost of 4 to 11: −2 +1 −5 +0 +1 +2 +2 +4 +1 = +4. With the 20 already over, 24 words must go. Fidelity-neutral cuts (none removes an argument any source requires):
- S27 'if Pierre promised personally, what follows runs against him.' to 'if Pierre promised personally, he is bound instead.' (−1; also removes the meta cross-reference).
- S10 'the email fixes the amount, date, term and rate but leaves unnamed ‘conditions’ to Rocky.' to 'the email, though otherwise complete, leaves unnamed ‘conditions’ to Rocky.' (−5; S5 already lists amount, date, term and rate).
- S37 '‘[T]he clause’ most naturally means the guarantee clause; even if it means the $10,000 term, AMPL remains bound by its oral promise.' to '‘[T]he clause’ most naturally means the guarantee clause.' (−14; R-AB(2) lists 'the two readings of ‘the clause’' among minor matters that 'take a clause'; the oral promise is already established in P9 and P14, so the second limb repeats it).
- S18 'made after 15 February and in AMPL’s name,' to 'made after 15 February,' (−4; S19 then deals with AMPL lending in its own right).

Total −24, net −20: body 1,597, 'Word count: 1,600'. Re-run verify.py and rebuild the .docx after applying; check by eye that no fix moved a quotation off its pin.
