# R3_M3: Fidelity, terminology and AGLC audit of ANSWER.md (v2)

Reviewer role: ROLE 3 (MARKERS_PROMPT.md). Text audited: /home/user/new/work/ANSWER.md as at 14:27 (identical to ANSWER_v2.md). No other R3_* report was read.

Sources read for this audit: YUSUF_INSTRUCTIONS_VERBATIM.md; MARKERS_PROMPT.md; the problem and Instructions; ReadingGuide.txt; all seven slide decks; RUBRIC_RULINGS_SHEET_v12.txt section 6.1 (R-P, R-Y, R-Z, R-AB) and the D8 and D9 deduction lines; the casebook extracts of every case the answer relies on, read whole (CB14_ch03: [3.05], Gibson [3.15], Felthouse [3.120], Empirnall [3.125], Brambles [3.130]–[3.185]; CB14_ch04: [4.05]–[4.15], AWM [4.20]–[4.25], Beaton [4.30]–[4.70], [4.85], Roscorla [4.90], [4.95] Sundell note, Pao On [4.145]–[4.165], Wigan [4.170]; CB14_ch05: [5.05], Ermogenous [5.10]–[5.25], Banque Brussels [5.30]–[5.40], Masters [5.80]–[5.105]; CB14_ch06: [6.05]–[6.20] Upper Hunter, Meehan [6.145]–[6.170], Godecke [6.175]–[6.180], Placer [6.185]–[6.200]; CB14_ch11 and the ch 11 opening in CB14.txt: [11.05], Coulls [11.10]–[11.25], Trident [11.60] Mason CJ and Wilson J, [11.65] Brennan J, [11.70] Deane J); the Pao On one-page extract (pdftotext). verify.py run: 95 spans, 0 not found.

Page references below are 14th ed printed casebook pages ('CB p') with the report page marker in force.

---

## 0. Headline

- Body 1,597 words (python split; `wc -w` in a UTF-8 locale also 1,597; the C-locale `wc` gives 1,596 because it does not count the standalone '…'). Stated 'Word count: 1,600' = body + 3, per R-P. Correct, at the cap. If Word does not count the standalone '…' in the Pao On quotation, the true figure is 1,599 and the line overstates by one; opening the .docx in Word settles it.
- Quotations: all 85 quoted spans are verbatim. All 45 pins are at the right report page, with one exception: Ermogenous [25] can only be confirmed by inference. [26] is confirmed by the Class 3A slide, which numbers that paragraph '26.'.
- Certain defects found: 11. Seven are mechanical, three are citation or rendering faults, and one is a fact-marking fault. None is a misstatement of a holding. Possible errors: 9.
- The .docx build has three italics failures: footnotes 17, 34 and the 'Beaton' short title in footnotes 4, 21 and 45. The cause is in build.py, not ANSWER.md. Footnotes render as real Word footnotes (45 references, 45 notes).

---

## 1. The .docx check (build plus pandoc round trip)

Command run: `python3 build.py ANSWER.md .../scratchpad/check_v2.docx`; then `pandoc check_v2.docx -t markdown`. The XML was also inspected.

Rendered correctly:
- 45 footnote references in the body and 45 Word footnotes (pandoc also adds 2 separator notes).
- Headings 'I. ROCKY v GRACE' and 'II. ROCKY v AMPL (ALTERNATIVELY PIERRE)' are bold.
- Body *Meehan* (the only case name in the body) is italic, and 'Mrs Coulls' correctly stays roman.
- Curly single quotation marks survive in body and notes; there are no straight or double quotation marks.
- En dashes appear in the five pin ranges.
- Normal style is Times New Roman 12 pt, line 480 (double).
- footer1.xml carries a PAGE field.

**CERTAIN rendering defects (fix in build.py):**

| Footnote | Rendered (pandoc round trip) | Cause | Fix |
|---|---|---|---|
| 17 | `*Coulls* v Bagot's Executor & Trustee Co Ltd` (only 'Coulls' italic) | CASES lists `Coulls v Bagot’s Executor and Trustee Co Ltd` ('and'); ANSWER.md has '&' (as the casebook heading [11.10], CB p 324, prints it). The SHORT entry 'Coulls' then italicises only the first word. | Add `'Coulls v Bagot’s Executor & Trustee Co Ltd'` to CASES. |
| 34 | `quoting Wilson v Darling Island Stevedoring & Lighterage Co Ltd` (roman) | Name absent from CASES | Add `'Wilson v Darling Island Stevedoring & Lighterage Co Ltd'` to CASES. |
| 4, 21, 45 | `('Beaton')`, `Beaton (n 4)` (roman) | 'Beaton' absent from SHORT | Add 'Beaton' to SHORT. Keep it out of the body pass, as the body never names Beaton. |

Minor: the sectPr has no pgSz or pgMar, so Word applies its installed default page size and margins (Letter on some installs). This is harmless for the margin rule, but set A4 in reference.docx if wanted.

---

## 2. Proposition trace (every proposition of law, sentence by sentence)

Status key: C = CORRECT; CE = CERTAIN ERROR (proved); PE = POSSIBLE ERROR (what would settle it is stated).

### Part I, paragraph 1 (offer)
| Answer | Source in context | Status |
|---|---|---|
| 'Grace's 5 February call asked Rocky to make an offer and promised nothing, so it was likely an invitation to treat,[^1]' | Gibson 298, CB p 42, Lord Diplock (the House agreeing; appeal allowed). The words "may be prepared to sell" are fatal, 'so is the invitation, not, be it noted, to accept the offer, but "to make formal application to buy"'. The question was whether the Council's letter was an offer. Similar to our facts: a communication inviting the other side to propose. Different: Gibson was a written price letter. 'Invitation to treat' is the Class 1A term ('An invitation for others to make an offer'). | C. The fact 'which Rocky declined' fairly renders 'not interested in offering Grace a long-term loan'. |
| 'unlike 'may be prepared to sell',[^2] these words are promissory' | Same page, same speaker | C |

### Paragraph 2 (acceptance, consideration)
| Answer | Source | Status |
|---|---|---|
| 'Acceptance requires 'an external manifestation of assent to an offer'.[^3]' | Empirnall 534, CB p 71, McHugh JA ('The objective theory of contract requires an external manifestation of assent to an offer'). Samuels JA agreed; Kirby P was to the same effect. | C |
| 'no counter-offer' | Class 1B term ('What is the legal effect of a counter-offer?') | C |
| Price of a promise 'can be in the form of an act, forbearance or promise'.[^4] | Beaton 168, CB p 102, Kirby P, majority on the result | C |

### Paragraph 3 (intention to create legal relations, the qualifier)
| Answer | Source | Status |
|---|---|---|
| Intention to create legal relations is judged objectively, the onus lies on the party alleging the contract, and 'status' bears on it.[^5] | Ermogenous 105–6, CB p 135, joint judgment of Gaudron, McHugh, Hayne and Callinan JJ: 'the status of the parties to it'; 'objective assessment'; 'it was for the appellant to demonstrate that there was such a contract'. | C. On the paragraph pins, [26] is confirmed by the Class 3A slide ('26. In this context of [ICLR]…'). That the objective and status passage is [25] is inferred from its position immediately before it. The casebook extract prints CLR pages only. R-Y(3) keeps paragraph pins. |
| Winn v Bull test.[^6] | Masters 363, CB p 154, the Court (Dixon CJ, McTiernan and Kitto JJ) quoting Jessel MR at 32: 'When it is not expressly stated … it becomes a question of construction, whether … the terms agreed on should be put into form, or whether they should be subject to a new agreement …' | C. 'question of construction' is dropped; the meaning is kept. |
| 'reached finality in arranging all the terms of their bargain'[^7] | Masters 360, CB p 153, the Court, first class | C |
| 'satisfactory' leaves judgment to the party the condition protects.[^8] | Meehan 580–1, CB pp 180–1, Gibbs CJ: 'Such a condition is generally entirely for the protection of the purchaser, and it is the satisfaction of the purchaser …'. Transposing 'purchaser' to the protected party is a fair reading; Mason J at 588 agrees ('primary object … protection of the purchaser'). | C |
| Gibbs J, in obiter, doubted that leaving 'further terms to be settled by one of the parties' binds, while allowing that it 'may be different' for 'subsidiary matters'.[^9] | Godecke 646–7, CB p 187, Gibbs J. The bench was Walsh J (Mason J agreeing) and Gibbs J, concurring in the result. His 'unnecessary to express any concluded opinion' makes the passage obiter, and 'obiter' is disclosed. His hedge is 'Perhaps it may be different where agreement has been reached on all essential terms'. | C. 'Perhaps' and 'all essential terms' are compressed into 'may be different' and 'subsidiary matters'. Acceptable. |
| 'he tied that to 'the familiar and objective standard of reasonableness''[^10] | Godecke 647, CB p 187. Gibbs J disagrees with Bray CJ because Sweet & Maxwell 'placed considerable reliance' on that standard. | C |
| 'Later conduct, admissible on formation,[^11] agrees: Rocky never lent, Grace never demanded it, and AMPL supplied the money.' | Brambles 164, CB p 73, Heydon JA's second principle. Ipp AJA adopts Heydon JA's reasons on the 12 July contract at 184 (CB p 82), and Mason P agrees with Ipp AJA, so this is majority reasoning. | Law C. **Facts CE (Z2).** The problem never says that Rocky did not lend or that Grace did not demand. These are inferences from silence, stated as facts. Fix: 'nothing shows Rocky lent or Grace demanded it' (+2 words). |

### Paragraph 4 (illusory promise)
| Answer | Source | Status |
|---|---|---|
| A discretion or option means 'no contract on which an action can be brought at all'.[^12] | Meehan 581, CB p 181, Gibbs CJ quoting Kitto J in Placer at 356. Kitto J was in the majority (3–2) per the editors' bracket [6.185], CB p 188. | C |
| 'as in Meehan, Rocky must decide honestly'[^13] | Meehan 581: 'No doubt it may be implied that the purchaser will act honestly'. The answer claims only honesty, the common floor (Mason J 'honestly, or honestly and reasonably', 588–91; Wilson J 597–8). There is no overclaim about reasonableness. | C |
| 'only to the fulfilment of a condition' within 'a concluded agreement as to the terms'[^14] | Meehan 581–2, CB p 181, Gibbs CJ | C |

### Paragraph 5 (Rocky's claim through AMPL's advance; agency; privity)
| Answer | Source | Status |
|---|---|---|
| 'a principal is a party where another 'contracts as agent' for him'[^15] | Trident 145, CB p 355, Deane J: 'If the promisee contracts as agent for a disclosed or undisclosed principal, the principal will **ordinarily** himself be … a party'. Deane J was in the majority on the result. AMPL is the promisee of Grace's repayment promise, so the party position matches. | PE (minor): the hedge 'ordinarily' is dropped. Fix: 'a principal is ordinarily a party' (+1). |
| 'a third party cannot sue upon a contract'[^16] | Trident 115, CB p 343, Mason CJ and Wilson J: 'This court has **hitherto** accepted that a third party cannot sue upon a contract'. They then held that McNiece succeeded. | C for Rocky (no insurance exception is engaged). The hedge 'hitherto' is dropped; this is harmless here. |
| 'Party status turns on 'the written instrument itself''[^17] | Coulls 487, CB p 327, Taylor and Owen JJ (majority with McTiernan J): whether a signature makes a party 'is a question to be resolved upon a consideration of the written instrument itself' | C |
| Not a party 'even as joint promisee'[^18] | Coulls 486, CB p 326 (joint promisees) | C. The application (Rocky is not even a joint promisee) is the answer's own; the source supports the category. |
| 'Mrs Coulls signed yet was not a party'[^19] | Coulls 487 | C |
| 'Rocky's 5 March demand … therefore **meets** privity' | — | Clarity defect (not of law). 'Meets' can be read as 'satisfies'. Fix: 'fails for privity' (+1). |

### Paragraph 6
| 'Grace never promised to reimburse anything Rocky pays AMPL' | Problem silent | Fact-marking PE/CE under Z2 (inference stated as fact). Fix: 'nothing shows Grace promised…' (+1). |

### Part II, paragraph 1 (8 April offer and acceptance)
| Answer | Source | Status |
|---|---|---|
| 'expected' an invitation to treat[^20] | Gibson 298 (analogy) | C |
| 'offered a bilateral contract,[^21]' cited to Beaton 168 (Kirby P) | Kirby P at 168 says the price 'can be in the form of an act, forbearance or promise'. He does not speak of a bilateral contract. The Class 1A term is 'Bilateral contract – contract is made by exchange of promises'. | **PE (citation imprecise: 'Ensure your citation precisely supports the proposition').** A source that states the proposition: Brambles 177, CB p 78, Heydon JA quoting McHugh JA in Integrated Computer Services ('In classical theory, the typical contract is a bilateral one and consists of an exchange of promises by means of an offer and its acceptance'). Replacement fn 21: '*Brambles* (n 11) 177 (Heydon JA), quoting *Integrated Computer Services Pty Ltd v Digital Equipment Corp (Aust) Pty Ltd* (1988) 5 BPR 11,110, 11,117 (McHugh JA).' Footnote only, 0 body words; build.py already lists the name. |
| 'which Pierre accepted when he 'agreed''[^22] | Empirnall 534 | C |
| Bound 'when, and in the manner in which, they intend', said by Lord Greene MR of exchanged contracts[^23] | Brambles 176, CB p 77, Heydon JA: 'exchanges of contracts to sell land … Lord Greene MR observed of the practice: "Parties become bound by contract when, and in the manner in which, they intend and contemplate becoming bound"' | C. The words are Lord Greene's and are attributed to him. Heydon JA's offer-and-acceptance route was not the majority's (Ipp AJA took 'a route different', 185), but nothing here rests on that route. |

### Paragraph 2 (who promised)
| 'he likely contracted 'as agent' for it'[^24] | Trident 145, Deane J. Pierre is the promisee of Rocky's undertaking, which matches Deane J's 'promisee contracts as agent'. | C |

### Paragraph 3 (consideration; the existing legal duty rule)
| Answer | Source | Status |
|---|---|---|
| 'existing legal duty rule'[^25] | Sundell 327, CB p 111. Editors' note quoting 'The court'; no judges are named in the reading. The Class 2B slide cites Sundell under 'Existing Legal Duty Rule'. | C |
| 'However, the rule applies 'at least when' the promise is 'made to the promisee under that contract',[^26] and none then existed' | Wigan 594, CB p 129, Mason J (Walsh and Gibbs JJ agreeing on this point): 'a promise to perform an existing duty is no consideration, **at least when** the promise is made by a party to a pre-existing contract, when it is made to the promisee under that contract, and it is to do no more …' | **PE (hedge used in reverse).** 'At least when' marks the core case in which the rule certainly applies. It does not mark the only case. The sentence reasons from its absence ('and none then existed') as if it set a limit. The conclusion is still right, because with no pre-existing duty there is nothing for the rule to bite on. Zero-risk fix that also saves words: 'However, the rule concerns a promise 'made by a party to a pre-existing contract',[^26] and none then existed' (−3 words; verbatim at 594). |
| 'the exception for promises to third parties applies, as 'a promise to perform … a pre-existing contractual obligation to a third party can be valid consideration''[^27] | Pao On 632, CB p 126, the Board (Lord Scarman delivering): 'Their Lordships do not doubt that a promise to perform, or the performance of, …'. Slide 2B lists the exceptions: 'promises to third parties (Pao On v Lau Yiu Long)'. | C. The label is the lecturer's own. Party position: Rocky's duty is owed to AMPL (the third party) and the new promise is to Pierre. This matches 'A's promise to B to perform a duty … obliged to perform for C' ([4.145], CB p 123). |

### Paragraph 4 (intention to create legal relations)
| Answer | Source | Status |
|---|---|---|
| presumptions do 'no more than invite attention to identifying the party who bears the onus of proof'[^28] | Ermogenous 106, CB p 135, joint judgment: '**At best**, the use of that language does no more than invite attention …' | C (hedge 'At best' dropped; meaning kept). |
| 'appropriately promissory in character'[^29] | Banque Brussels 523, CB p 142, Rogers CJ. This was a first-instance action (Commercial Division). | C. Status 'first instance' is not disclosed; see PE-6. |
| 'Rogers CJ saw 'no relevant difference' between a 'practice to ensure' repayment and a promise 'to ensure' it'[^30] | Banque Brussels 525, CB p 144: 'The question whether the third paragraph … is promissory is **far more thorny**. However … "it is our practice to ensure that Spedley is at all times **in a position to repay** all loans" … I see no relevant difference between that and saying that "we promise to ensure that" Spedley will at all times be **in a position to repay**' | **PE (paraphrase).** Rogers CJ compared ensuring the debtor is in a position to repay, not ensuring repayment. The answer then contrasts Rocky's 'I will do that' (ensure that Grace 'made all payments') as 'plainer', and that contrast is stronger when the source's real object is stated. Fix: 'a 'practice to ensure' a debtor can repay' (+2). Also: Rocky's undertaking is oral, so 'call his own undertaking a mere letter of comfort' is better written as 'liken his own undertaking to a letter of comfort' (+1). |

### Paragraph 5 (certainty)
| 'not 'so obscure' as to be void'[^31] | Upper Hunter 437, CB p 159, Barwick CJ quoting Lord Wright in Scammell. Pin 268 for Lord Wright is in the reading: Mason J in Meehan 587, CB p 182 cites 'G Scammell and Nephew Ltd v Ouston [1941] AC 251 at 268'. | C |
| 'AMPL's promise is not illusory either, because its condition … relates 'only to the fulfilment of a condition''[^32] | Meehan 581 | C. Grace's repayment is not even in AMPL's discretion, so the Placer principle is not engaged at all. Fair use. |

### Paragraph 6 (privity of the $10,000)
| 'no 'stranger to the consideration''[^33] | Trident 115, Mason CJ and Wilson J | C |

### Paragraph 7 (whether the guarantee clause binds Rocky)
| Answer | Source | Status |
|---|---|---|
| only 'the parties to it' are 'bound by the obligations of a contract'[^34] | Trident 129, CB p 350, **Brennan J, whose casebook heading reads 'BRENNAN J: (dissenting)'** ([11.65], CB p 348), quoting Kitto J in Wilson at 80 | **CE (citation): 'dissenting' is omitted** (the brief's three-question pass; AGLC). Fix: 'Ibid 129 (Brennan J dissenting), quoting …'. The proposition itself is safe: Mason CJ and Wilson J at 115 list 'Wilson … 80 per Kitto J' among the authorities 'This court has hitherto accepted'. R-Y(2)'s preferred Deane J burden sentence ('only the parties to a contract are bound by, and entitled to enforce, its terms') is **not in the casebook extract**, which starts at Deane J's [143] 'Circumstances can undoubtedly arise'. Within the readings, Brennan J quoting Kitto J is the only judicial statement of the burden aspect, so keep it and mark the dissent. |
| 'Silence while a clause is included is generally not acceptance.[^35]' | Empirnall 534: 'the silent acceptance of an offer is generally insufficient' | C |
| 'AMPL would say the clause recorded Rocky's own bargain, taken 'with knowledge of its terms',[^36]' | Empirnall 535–6, CB pp 71–2: 'taking the benefit of an offer with knowledge of its terms'; 'he has exercised a choice and taken the benefit of the offer' | PE (clarity and doctrine naming). 'Taken' has no clear subject and the doctrine is not named. The course name is 'Acceptance by Conduct' (Class 1B heading) or 'taken the benefit' (McHugh JA). Fix: 'AMPL would say Rocky accepted the clause by conduct, having taken its benefit 'with knowledge of its terms'' (+3). The answer's reply 'but Rocky has received nothing' then meets this argument directly. |

### Paragraph 8 (consideration for the guarantee)
| Answer | Source | Status |
|---|---|---|
| 'AMPL must show consideration moving from itself'[^37] | Trident 115 | C |
| 'past consideration'[^38] | Roscorla 237, CB p 110, Lord Denman CJ delivering the judgment of the Court: 'a consideration past and executed will support no other promise than such as would be implied by law' | C |
| Pao On's three conditions[^39] | Pao On 629, CB p 124 and the one-page extract (heading 'Judgement delivered by Lord Scarman') | C. On form, see AGLC-3 below. |
| 'arguably 'really done in consideration of' the guarantee'[^40] | AWM 456, CB p 99, the Court. The words are from the unilateral-contract test ('the act was really done in consideration of a potential promise'). | C. The phrase 'it signed only after the clause was included, arguably 'really done…'' has no noun for 'done' to attach to; add 'its signing' (+2) if funded. |

### Paragraph 9 (the 12 months)
| Answer | Source | Status |
|---|---|---|
| 'Post-contractual conduct … cannot construe the term in New South Wales'[^41] | Brambles 164, CB pp 73–4, Heydon JA's third principle (the Victorian decisions 'should be followed in New South Wales'), adopted by the majority at 184 | C |
| 'but, the term naming no start, mutually known facts showing 'the genesis of the transaction' are admissible'[^42] | Brambles 191, CB p 82, Ipp AJA (Mason P agreeing): '**Where ambiguities exist**, mutually known facts establishing … the genesis of the transaction … will be admissible' | PE (hedge only implied). The answer relies on silence about the start date as the ambiguity without saying so. Fix: 'the term, naming no start, being ambiguous' (+3) if funded. Note also that Reading Guide 1B skips 'the first part of Ipp JA's judgment; pp82-84'. R-F says skip-range status is never stated and never deducted, so this is recorded only. |

### Paragraph 10 (the $10,000 condition; the duty to co-operate)
| Answer | Source | Status |
|---|---|---|
| 'a condition precedent to that obligation rather than to the contract, which bound immediately'[^43] | Meehan 582, CB p 181, Gibbs CJ: 'not a condition precedent to contract. Certain obligations … attached immediately' | C |
| 'Rocky could argue that, read commercially, his own payment satisfies it,[^44]' | Upper Hunter 437, Barwick CJ: 'In the search for that intention, no narrow or pedantic approach is warranted, particularly in the case of commercial arrangements.' His Honour said this while answering whether cl 5 was void for uncertainty. | C. It is a construction principle and is fairly used for Rocky's argument, which the answer then rejects. |
| 'the duty to co-operate, to 'do everything necessary on [its] part''[^45] | Beaton 185, CB p 107, McHugh JA, **dissenting** (the appeal was dismissed; Kirby P and Mahoney JA formed the majority), citing Mason J in Secured Income at 607 (High Court). 'The duty to co-operate' is the casebook sub-heading [4.65]. | C. The dissent is marked in the footnote. The proposition is Mason J's High Court statement as cited, so the body need not repeat the status. |

### Paragraph 11 (exposure)
No new law. The conclusion is consistent with paragraphs 7 to 10 and with Part I. Part I holds that AMPL was not Rocky's agent; Part II holds that Pierre likely acted as AMPL's agent; the 5 March demand is used in both Parts, and the uses are reconciled.

---

## 3. Terminology (lecturer's words)

Each term in the answer was checked against the slides, the reading guide and the casebook headings:

| Term in answer | Where the lecturer uses it | Verdict |
|---|---|---|
| invitation to treat | 1A slides 19, 27 | C |
| offer; promissory | 1A slide 27; Banque 523 'promissory in character' | C |
| acceptance; counter-offer; silence | 1B slides | C |
| consideration; the price of a promise | 2A; Kirby P at 168 | C |
| past consideration | 2A 'Past consideration' | C |
| existing legal duty rule; the exception for promises to third parties | 2B ('Existing Legal Duty Rule'; '3 exceptions … promises to third parties (Pao On …)') | C |
| intention to create legal relations (always in full); presumptions; onus; preliminary agreement; letter of comfort | 3A; casebook [5.05], [5.80] | C |
| certainty; illusory; discretion or option | 3B 'Illusory promise'; casebook heading 'ILLUSORY PROMISES' | C |
| condition precedent | Meehan 582 | C |
| privity; agent; principal; stranger to the consideration; joint promisee | 4A; [11.05]; Trident 115; Coulls 486 | C |
| bilateral contract | 1A slides 12, 27 | C (see the PE on its footnote) |
| post-contractual conduct; later conduct | Brambles 164 (casebook); 1B 'post-formation conduct' | C |
| the duty to co-operate | casebook sub-heading [4.65] | C |
| obiter | — | C |

Doctrines applied but not named in the course's words:
1. **Acceptance by conduct / taking the benefit.** Paragraph II.7 ('taken 'with knowledge of its terms'') applies Empirnall without naming it. Class 1B heads the slide 'Acceptance by Conduct' and McHugh JA says 'taken the benefit'. Fix: +3 words, as in the table above.
2. **Incompleteness.** Paragraph I.3 treats the 'conditions' as 'further loan terms' left to Rocky. That is the Class 3B category 'Incompleteness: Failure to agree on an essential term, or an agreement to agree' and Godecke 647 ('no concluded bargain if a vital matter has been left to the determination of one of the parties'), yet the answer never uses the word. Optional, +3: '…so they are most naturally further loan terms, leaving the agreement incomplete,'.
3. **Masters categories.** The conclusion 'left to a new agreement' uses Jessel MR's words. The lecturer's frame is 'the 3 categories' (3A slide). 'Grace would say that, as in Masters' first category, they had 'reached finality…'' (+5) would also cure the one-clause sentence S12. Add only if funded.

No proxy or invented labels were found. 'The qualifier' is a descriptive noun for a quoted fact, not a doctrinal label. There is no meta language: no weeks, slides, course or 'outside the scope'.

---

## 4. AGLC 4, footnote by footnote

Correct throughout:
- Full first citations, with the short title after the pin and judge and before ', quoting' (fns 6, 12, 31).
- Ibid used only where the preceding footnote is one source: fns 2, 10, 14, 16, 18, 19, 30, 34, 36, 42. AGLC is correctly not used after a 'quoting' footnote (fns 7, 13, 24, 35).
- Pins after a comma with no 'at'; paragraph pins in square brackets; en dash ranges; a full stop at every footnote's end.
- 'quoting' and 'citing' used correctly; 'dissenting' present in fn 45.
- Footnote markers sit after punctuation throughout.

| # | Finding | Status |
|---|---|---|
| AGLC-1 | **fn 5** gives no short title, yet fn 28 uses '*Ermogenous* (n 5)'. Every other repeated case defines its short title. Fix: add "('*Ermogenous*')" after the judges in fn 5 (0 body words). | CE |
| AGLC-2 | **fn 34** omits 'dissenting' for Brennan J (casebook [11.65] heading). | CE |
| AGLC-3 | **fns 27 and 39** read '(Lord Scarman)'. R-P accepts two forms, the Board with no judge or '(Lord Scarman for the Board)'. The bare form reads as one judge's judgment. Fix: '(Lord Scarman for the Board)'. fn 38 '(Lord Denman CJ)' is within R-P ('may name Lord Denman CJ'). | PE (ruling form) |
| AGLC-4 | **fn 21**: the citation does not state the proposition ('bilateral contract'); replacement in section 2. | PE |
| AGLC-5 | **fn 23** 'Eccles v Bryant [1948] Ch 93'. The readings print two forms: Brambles gives 'Eccles v Bryant [1948] 1 Ch 93 at 104' (CB p 77) and Masters gives 'Eccles v Bryant and Pollock [1948] Ch 93 at 94' (CB p 154). AGLC takes the reported name, which on the readings' own evidence is 'Eccles v Bryant and Pollock'. build.py already italicises that form. The report form '[1948] Ch 93' matches Masters. | PE (settle by preferring the fuller reported name) |
| AGLC-6 | fn 25 (Sundell) names no judge. The reading names none ('The court … said (at 327)'). | C (disclose if asked) |
| AGLC-7 | '&' in fns 17, 25, 34 versus 'and' in fn 31 (Scammell). Each matches a casebook printing: Coulls '&' [11.10]; Sundell '&' [4.95]; Wilson '&' [11.05]; Scammell 'and' (Mason J, Meehan 587). | C (as reported) |
| AGLC-8 | The italics failures in the built .docx (fns 4, 17, 21, 34, 45) are covered in section 1. | CE (build) |

---

## 5. Voice and mechanics

Checked: dashes in body 0; double quotation marks 0; contractions 0; banned phrases ('cuts both ways', 'it is trite', 'it is submitted', 'in the present case', 'turning to', 'it is clear') 0; first person 0; no fragments after semicolons (all 11 semicolon clauses have a subject and a verb); single quotations at most 17 words (R-G cap 20).

| # | Finding | Status |
|---|---|---|
| V-1 | **Sentences over 45 words: 2.** II.1 'AMPL may argue that nothing bound … formed orally.' (48). II.4 'On intention to create legal relations, Pierre is Rocky's cousin, … 'appropriately promissory in character'.' (48). II.4's second sentence and II.5's first are exactly 45, within the rule. | CE ×2 |
| V-2 | **One-clause sentences** (R8: he 'despises' them): I.2 'Acceptance requires 'an external manifestation of assent to an offer'.'; I.3 'Grace would say they had 'reached finality…''; I.6 'Thus Rocky has no present claim against Grace.'; II.2 'Who promised turns on what Pierre's words objectively conveyed.'; II.3 'Rocky likely gave consideration.' (4 words, a bare conclusion); II.7 'Silence while a clause is included is generally not acceptance.'; II.9 'Whether the 9 March 2025 call was premature depends on when the 12 months began.' (issue-framing, defensible). | CE by his rule (6 excluding the issue sentence) |
| V-3 | **Quoted words: 386 of 1,597 (24.2%).** D8 (R-G) deducts −1 where quoted words exceed 20% of the body. Whether D8 still binds in the 1,600 version is for the orchestrator. R-AB(5) released floors and compression forms but kept 'no automatic deduction applies' checks. Reaching 20% would need about 67 fewer quoted words, mostly repeated fact quotes ('I will do that' ×3, 'recorded' ×3, 'asked' ×3, 'all payments' 'promptly' ×2), which pulls against 'facts quoted exactly'. | Contestable |
| V-4 | 'meets privity' is ambiguous (section 2). | Clarity |
| V-5 | 'taken 'with knowledge of its terms'' has no clear subject (II.7); 'arguably 'really done in consideration of'' has no noun to attach to (II.8). | Clarity |
| V-6 | Zeugma or adjacency: ''all payments' 'promptly'' twice. Two quotes stand side by side; acceptable as exact fact quotation. | Minor |

---

## 6. Certain defects (one line each)

1. fn 34 omits 'dissenting' for Brennan J (Trident, casebook heading [11.65], CB p 348).
2. fn 5 lacks the short title ('*Ermogenous*') that fn 28 uses.
3. The built .docx leaves 'Bagot's Executor & Trustee Co Ltd' (fn 17) roman: build.py's CASES has the 'and' form.
4. The built .docx leaves 'Wilson v Darling Island Stevedoring & Lighterage Co Ltd' (fn 34) roman: missing from CASES.
5. The built .docx leaves the short title 'Beaton' roman in fns 4, 21 and 45: missing from SHORT.
6. II.1 sentence 'AMPL may argue … formed orally' is 48 words (over 45).
7. II.4 sentence 'On intention … in character' is 48 words (over 45).
8. I.3 'Rocky never lent, Grace never demanded it' states inferences from silence as facts (Z2).
9. I.6 'Grace never promised to reimburse anything Rocky pays AMPL' states an inference from silence as fact (Z2).
10. One-clause sentences remain (I.2, I.3 'Grace would say…', I.6 'Thus…', II.2 'Who promised…', II.3 'Rocky likely gave consideration.', II.7 'Silence…'), contrary to R8.
11. Wigan's 'at least when' is used as if it limited the rule. This is listed with the possible errors as PE-1 because the conclusion stands; it is the closest to a certain logical misuse.

## 7. Possible errors (with what settles them)

- PE-1 Wigan 'at least when' read as a limit (II.3). Settled by the text of 594. The fix saves 3 words.
- PE-2 fn 21 Beaton 168 does not mention a bilateral contract. Replace with Brambles 177 quoting Integrated Computer Services (McHugh JA).
- PE-3 Banque Brussels paraphrase: 'ensure' repayment versus the source's 'in a position to repay' (525).
- PE-4 Trident 145 hedge 'ordinarily' dropped (I.5).
- PE-5 Brambles 191 condition 'Where ambiguities exist' only implied (II.9).
- PE-6 Banque Brussels is first instance and the status is undisclosed. Disclosure costs 3 words ('Rogers CJ, at first instance,'). Low priority.
- PE-7 Pao On judge form outside R-P's accepted forms.
- PE-8 Eccles case name: 'and Pollock' per Masters' citation.
- PE-9 The word count holds only if Word counts the standalone '…'. If it does not, the stated count is 1 too high. Settle by opening the .docx in Word.

---

## 8. Zero-net-word repair set (body stays 1,597; stated 1,600)

| Change | Words |
|---|---|
| II.3: 'However, the rule concerns a promise 'made by a party to a pre-existing contract',[^26] and none then existed: …' (replaces the 'at least when' clause) | −3 |
| II.1: split at fn 23: '…as Lord Greene MR said of exchanged contracts.[^23] Rocky's undertaking did not await a document 'signed by Grace and AMPL', so a contract likely formed orally.' | −1 |
| II.4: '…the onus of proof',[^28] here Rocky. He meets it, as a fixed sum promised at AMPL's office as its loan was finalised is 'appropriately promissory in character'.[^29]' | +3 |
| I.3: 'nothing shows Rocky lent or Grace demanded it, and AMPL supplied the money' | +2 |
| I.6: 'nothing shows Grace promised to reimburse …' | +1 |
| I.5: 'therefore fails for privity' | +1 |
| II.3: merge the bare conclusion: '…can be valid consideration',[^27] so Rocky likely gave consideration.' | +1 |
| I.2: join with a colon: 'Acceptance requires 'an external manifestation of assent to an offer':[^3] 'Confirmed' arguably …' (43 words) | 0 |
| I.6: 'Thus Rocky has no present claim against Grace: the Development Agreement repays him first …' | 0 |
| II.2: 'Who promised turns on what Pierre's words objectively conveyed: Rocky's 'you' points to Pierre, but …' (34 words) | 0 |
| II.7: '…'bound by the obligations of a contract';[^34] silence while a clause is included is generally not acceptance.[^35]' (44 words) | 0 |
| Fund: delete ', even a 'minimal' one,' in I.6 (a minor matter under R-AB(2); it also removes 1 quoted word) | −4 |
| **Net** | **0** |

Footnote and build fixes, at no body cost:
- fn 5: add ('*Ermogenous*').
- fn 34: add 'dissenting'.
- fn 21: replace as in PE-2.
- fns 27 and 39: change to '(Lord Scarman for the Board)'.
- fn 23 (optional): 'Eccles v Bryant and Pollock'.
- build.py: add the '&' Coulls name and the Wilson name to CASES, and 'Beaton' to SHORT.

Add if words are freed elsewhere, ranked by value per word:
1. Name acceptance by conduct in II.7 (+3).
2. Banque 'a debtor can repay' (+2).
3. 'ordinarily' (+1).
4. 'being ambiguous' (+3).
5. 'leaving the agreement incomplete' (+3).
6. 'as in Masters' first category' (+5).
