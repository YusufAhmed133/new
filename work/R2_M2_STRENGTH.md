# R2_M2 — Readings-strength attacker (ROLE 2)

Answer attacked: /home/user/new/work/ANSWER.md as it stands on 13 October 2026 (body 1,617 words on the R-P method, stated 'Word count: 1,620'; cap 1,600 including the line, so the body must come down to 1,597 or less).

Read in full for this role: MARKERS_PROMPT.md; YUSUF_INSTRUCTIONS_VERBATIM.md; ANSWER.md; ACTUAL TASKKK.txt; Instructionsss.txt; ReadingGuide.txt; all seven slide decks; CB14_ch03, ch04, ch05, ch06, ch11 (every page, and the continuation of Trident at CB14.txt p 357 where ch11 stops); the Pao On Moodle extract (pdftotext); RUBRIC_RULINGS_SHEET_v12.txt section 6.1; LAWS1150 Mid-Term - Final Marker Feedback.txt (both markers). verify.py run: 86 spans, 0 NOT FOUND. No R2_* or MARK_* file was opened.

Conventions. 'cb p' = the 14th-ed printed casebook page in the CB14 transcription ('expected printed p'); the student's printing may differ by 0 to 4 pages after chapter 3, so footnotes cite report pages only. 'Set' / 'skip' status is mapped from the Reading Guide's 15th-ed ranges: in chapter 3 the page numbers coincide exactly (eg Brambles extracted at pp 72-73 in both), so the mapping there is certain; in chapter 4 the offset is +2 (Wigan 14th p 129 = 15th p 131), which places the full Pao On extract (14th pp 123-129) inside the 2B skip range [4.300]-[4.340] (15th pp 125-131).

---

## 1. Certain defects (proved at source)

**D1. Footnote 34 is mis-pinned (certain); the words it supports are not in the readings.**
Answer: "only the parties to a contract are bound by it,[^34] so AMPL must show assent." fn 34: "Ibid (Deane J)." The immediately preceding fn 33 is "Trident (n 14) 115 (Mason CJ and Wilson J)", so 'Ibid' imports page 115.
Source: page 115 lies inside the joint judgment of Mason CJ and Wilson J, which runs from "[113]" (CB14_ch11, cb p 343, "MASON CJ AND WILSON J: [113] Although the principle…") to "[124]" (cb p 348). Deane J's extract begins "[11.70] DEANE J: [143] Circumstances can undoubtedly arise…" (cb p 354). Deane J does not speak at 115. Further, the paraphrased words ('only the parties to a contract are bound by it') appear nowhere in the casebook's Deane J extract (pp 354-357; grep of CB14.txt for "bound by, and entitled to enforce" returns nothing); the RUBRIC R-Y(2) quotation comes from the full official judgment, which is not among the readings supplied here, so the pin cannot be proved from the readings. The only casebook statement of the burden limb is Brennan J (dissenting) at 129, quoting Kitto J in Wilson: "the only persons entitled to the benefits or bound by the obligations of a contract are the parties to it" (cb p 350), a dissent and outside the 'Mason CJ and Wilson J only' set range.
Fix (0 words): fn 34 → "Trident (n 14) (Deane J)." (R-Y(1): judge named, no pin), and the tracer should confirm the words against the official text before release.

**D2. Footnote 4 uses Australian Woollen Mills for what it did not decide (a bilateral promise-for-promise).**
Answer: "Grace's implied promise to repay with interest would stand in 'the relation of a quid pro quo' to Rocky's promise to lend.[^4]"
Source: the Court (Dixon CJ, Williams, Webb, Fullagar and Kitto JJ) speaks of "that type which is commonly said to be constituted by an offer of a promise for an act, the offer being accepted by the doing of the act", and the quid pro quo sentence opens "In cases of this class it is necessary…" and links "the statement or announcement" to "the act which is put forward as the executed consideration" (CB14_ch04, cb pp 98-99, AWM 456-7). The Court found no contract. Both earlier hostile markers flagged this exact use (Marker A K3; Marker B C2). The readings contain the exact bilateral statement: Kirby P, Beaton 168: "consideration must be satisfied in the form of a price in return for the promisor's promise or a quid pro quo. The price can be in the form of an act, forbearance or promise." (cb p 102; Kirby P in the majority on the result, appeal dismissed; the definition is uncontested by McHugh JA, who uses Pollock's same words at 182.)
Fix (−4 words): "Grace's implied promise to repay with interest would be 'a price in return for' Rocky's promise to lend.[^4]" fn 4 → "Beaton v McDivitt (1987) 13 NSWLR 162, 168 (Kirby P) ('Beaton')." AWM's first full citation moves to fn 40 (where its promise-for-an-act use is apt); fn 45 becomes "Beaton (n 4) 185 (McHugh JA dissenting), citing …".

**D3. The 12-months paragraph rests on two skip-range passages and does not meet a set reading that points the other way.**
Answer: "Post-contractual conduct, such as Grace's interest payments from 8 April 2024 and his 'I have until 8 April 2025', cannot construe the term,[^41] but, the term being arguably ambiguous, mutually known facts showing 'the genesis of the transaction' are admissible.[^42]"
Status (certain): Brambles 164 (Heydon JA, the third principle, cb p 73) lies in the 1B skip range [3.290]-[3.300] (pp 73-76); Brambles 191 (Ipp AJA, cb p 82) lies in the 1B skip range [3.330]-[3.360] "(the first part of Ipp JA's judgment; pp82-84)" (ReadingGuide.txt). Both are casebook text and correct, but neither is set reading.
Set reading against: Mayo J, Todd v Nicol (CB14_ch05, cb p 145, between report markers [74] and [77]): "It is an accepted principle that regard may be had to the subsequent conduct of, and communications between, parties for the purpose of discovering whether the intention to be attributed to them was to make a binding arrangement or otherwise, and if the former what the parties understood the terms to be … The acts of parties, where meaning is in doubt, may be used to remove uncertainty, or to explain, but not to contradict, the language used." (single judge, SA Supreme Court, 1957; holding on intention.) This helps Rocky (Grace's payments from 8 April and his 'I have until 8 April 2025' point to an 8 April start, which makes AMPL's call premature), and the answer never puts it. The decisive answer is in the readings: Heydon JA's own hedge at 164 that the High Court position "is unclear: hence unless it is demonstrated that the later decisions … against admissibility … are clearly wrong or they are overruled, they should be followed in New South Wales" (cb pp 73-74); the problem is set in New South Wales.
Fix (+6 words): "Grace's interest payments from 8 April 2024 and his 'I have until 8 April 2025' might 'explain' the term,[^T] but in New South Wales post-contractual conduct cannot construe it;[^41] however, the term being arguably ambiguous, mutually known facts showing 'the genesis of the transaction' are admissible.[^42]" New fn: "Todd v Nicol [1957] SASR 72, 7x (Mayo J) ('Todd')." Pin caution: the passage sits between the printed markers [74] and [77] with no [75]/[76] shown; the tracer must fix the page from the student's extract before use. No set-reading substitute exists for 'genesis' (191) — keep it, knowing its status.

**D4. A planted fact is never used: "Throughout this period Rocky would check in consistently with Grace via email" (narrator).** It is the best fact AMPL has, with Rocky's 5 March demand "requiring repayment of the principal amount under the Loan Agreement with AMPL", on whether Rocky assented to the guarantee clause, and subsequent conduct is admissible on whether a binding arrangement was intended (Todd, above; also Brambles 164, second principle, skip range: "post-contractual conduct is admissible on the question of whether a contract was formed"). Fix: see A2 in §5.

---

## 2. Issue-by-issue (the order in MARKERS_PROMPT ROLE 2)

For each: the answer's use; the best passage for each side (verbatim, cb page, report pin, speaker, status); facts set beside ours; verdict; replacement and word cost.

### 2.1 The 5 February call
Answer: "Grace's 5 February call asked Rocky to make an offer, so it was not itself one,[^1] and Rocky declined." fn 1 Gibson 298 (Lord Diplock).
Best for 'not an offer': Bowen LJ, Carlill 268 (cb p 46; CA, unanimous in result): "Such advertisements are offers to negotiate – offers to receive offers – offers to chaffer". Grace "proposed that Rocky offer Grace a … loan": exactly an 'offer to receive an offer'. Gibson 298 decides that "may be prepared to sell" and an invitation "to make formal application to buy" are not an offer (cb p 42) — the Council invited Gibson to make the offer; analogous, not exact. Facts: Gibson, a seller inviting a buyer's application; ours, a would-be borrower inviting a lender's offer; same structure (the speaker asks the other to make the offer).
Verdict: adequate; Carlill is the tighter fit. Optional replacement (+4): "Grace's 5 February call, proposing that Rocky 'offer' a loan, was an offer 'to receive offers',[^1] not an offer, and Rocky declined." fn 1 → Carlill v Carbolic Smoke Ball Co [1893] 1 QB 256, 268 (Bowen LJ). Gibson's full cite then moves to fn 2. ADD IF FUNDED (low).

### 2.2 The 12 February email as offer
Answer: "'I will lend' fixes the amount, date, term and rate, and 'Please confirm agreement' seeks assent, so, unlike 'may be prepared to sell' in Gibson,[^2] the first point is likely an offer".
Best for Rocky (not an offer): Gibson 298 ("may be prepared to sell" fatal; cb p 42) — distinguishable on our words 'I will lend'. Felthouse 876 (Willes J, cb p 70): a later letter "may be treated either as an acceptance then for the first time made by him, or as a memorandum of a bargain complete before" — the 'Confirming discussions' opening raises the same choice; if the morning meeting concluded a bargain, the email is a memorandum and the problem moves to the meeting (helps Grace, not Rocky). Best for Grace: [3.10] Restatement (editors' quotation, not a case): an offer is "so made as to justify another person in understanding that his assent to that bargain is invited and will conclude it" ('Please confirm agreement').
Verdict: uses the best case. The sentence "Rocky could argue that his 12 February email merely records their meeting…" puts as Rocky's argument a reading that, on Felthouse, could hurt him; it is low-value and is the first cut in §5 (C1). The further-information point ('this morning') in 2.5 covers the memorandum risk.

### 2.3 'Confirmed' as acceptance
Answer: Empirnall 534 (McHugh JA): "an external manifestation of assent to an offer". cb p 71; McHugh JA (Samuels JA agreeing; Kirby P to the same effect) — majority. Rocky's counter ('vouched only for the email's accuracy') is met on 'confirm agreement'.
Verdict: best available. No change.

### 2.4 Consideration (12 February)
See D2. Replacement: Beaton 168 (Kirby P). Cost −4.

### 2.5 Intention and the qualifier ('subject to satisfactory conditions')
Answer: Ermogenous [25]-[26] (objective; onus); Masters 363 quoting Winn v Bull (Jessel MR); Godecke 642-3 (Walsh J) as "Grace's strongest counter"; Meehan 580-1 (Gibbs CJ) whose satisfaction; Godecke 646-7 (Gibbs J, obiter, labelled).
Best for Rocky: Winn v Bull via Masters 363 (cb p 154; Dixon CJ, McTiernan and Kitto JJ quoting Jessel MR) is apt because nothing in the email is "expressly stated to be subject to a formal contract". A stronger, unanimous High Court statement is also in the set reading: Milne v A-G (Tas) (1956) 95 CLR 460, 473, quoted by the editors at [6.10] (cb p 158; Dixon CJ, McTiernan, Williams, Fullagar and Taylor JJ): "no contract is concluded until the parties negotiating are agreed on all the terms of their bargain — unless indeed the terms left outstanding are 'such as the law will supply'". And Kirby P, Biotechnology v Pace 135, observation (3) (cb p 161; Kirby P with McHugh JA in the majority): "the court will not accept for itself a discretion which the parties have, by their agreement, reserved to one or other of them. To do so would not be to effect the contract but to change it."
Best for Grace: not Godecke but Meehan, whose clause is nearly our words: "finance on satisfactory terms and conditions" (Gibbs CJ 575-82; Mason J 587: the absence of "the amount to be borrowed, and perhaps the term of the loan and the rate of interest" did not make it uncertain, cb p 182). Godecke is distinguished on 'reasonably' (642-3) as the answer does.
Verdict: correct and hedged, but 'Grace's strongest counter is Godecke' mislabels; Meehan is Grace's closest case and the answer uses it one paragraph later. Zero-cost fix if desired: "Grace's first counter is Godecke". Milne and Biotech are ADD IF FUNDED (each about +20); not in the funded package because the Gibbs J sentence drives the 'this morning' further-information point.
Masters 362 / Crossley v Maycock (Marker A K2): REJECT — the casebook elides that sentence ("…" after the Chinnock quotation, cb p 154); it is not in the readings.

### 2.6 Certainty and illusory promises (12 February)
Answer: "in Placer a promise with no 'identifiable criteria', left 'solely to the discretion' of the promisor, was 'wholly unenforceable'.[^10]" (Taylor and Owen JJ 361); then Meehan 581 (Gibbs CJ), 589 (Mason J, "takes the case out of the principle"), 581 ("only to the fulfilment of a condition"); "whereas Rocky's concerns the content of his own loan, which honesty cannot supply."
Weakness 1 (wrong-fit passage): Taylor and Owen JJ speak of "the amounts or rates to be determined" (cb p 189) — a discretion over quantum. Rocky's amount is fixed; his reserved discretion is whether, on 'conditions', he lends at all. The majority statement that fits is Kitto J, Placer 356 (cb p 188; majority 3-2; the pin is the one Gibbs CJ gives at Meehan 581): "wherever words which by themselves constitute a promise are accompanied by words showing that the promisor is to have a discretion or option as to whether he will carry out that which purports to be the promise, the result is that there is no contract on which an action can be brought at all." 'I will lend' = words which by themselves constitute a promise; 'subject to satisfactory conditions' = words reserving the option. It is also the very principle Mason J's "takes the case out of the principle" refers to (he quotes it at 589-90 via Thorby), so the paragraph becomes one chain.
Weakness 2 (unsupported step): "which honesty cannot supply" has no authority. Gibbs CJ supplies it at 582 (cb p 181): "There is a concluded agreement as to the terms of the contract which, if the condition is satisfied, leaves no discretion in either party as to whether he shall carry them out." Meehan rested on agreed terms; Rocky's unnamed 'conditions' are themselves unagreed terms.
Grace's best counter not met: Kitto J in Thorby, quoted by McHugh JA, Biotech 151 (cb p 164): "an agreement is not void for uncertainty because it leaves one party or group of parties a latitude of choice as to the manner in which agreed stipulations shall be carried into effect" — amount, date, term and rate were agreed. Rocky's answer: 'conditions' go to whether he lends, not how (McHugh JA 155: Thorby "might arguably be in point if the parties had agreed on the number and class of shares … but left other details", cb p 165). ADD IF FUNDED (+35).
Replacements (funded, §5): S3 (Kitto J, +2), C6 (−9, the restated principle becomes redundant), A1 (Gibbs CJ 582, +1).

### 2.7 Rocky's claim through AMPL's advance
Answer: the four mismatches ($1,150,000; after 15 February; AMPL's name; 'recorded' at 4%) — good, fact-driven. Additional authority in the read range: McHugh JA in Integrated Computer Services, quoted by Heydon JA, Brambles 178 (cb p 79; read range [3.310]-[3.320]): "it is an error 'to suppose that merely because something has been done then there is therefore some contract in existence which has thereby been executed'". Exact answer to 'AMPL's advance performed my promise'. ADD IF FUNDED (+20), low (the facts already decide it).

### 2.8 Agency (AMPL for Rocky)
Answer: "although a principal is a party where another 'contracts as agent' for him,[^14] AMPL took Rocky's own guarantee of the Loan, which no agent lending for him would need." Deane J 145 (cb p 355): "If the promisee contracts as agent for a disclosed or undisclosed principal, the principal will ordinarily himself be, for the purposes of the requirement of privity, a party to the contract." Apt (Deane J is outside the 'Mason CJ and Wilson J only' set range, covered by R-Y). The [11.32] editors' note and Port Jackson sit in the [11.50] skip range; do not use.
Verdict: best available; compress (C3, −11) keeping the quoted words.

### 2.9 Privity (Rocky v Grace)
Answer: Trident 115 (Mason CJ and Wilson J) "a third party cannot sue upon a contract"; Coulls 487 "the written instrument itself", 486 joint promisee, 487 signature (Taylor and Owen JJ, majority with McTiernan J; cb pp 326-327). Correct and set reading.
The joint-promisee limb ("even as a joint promisee;[^17]") answers an argument no fact plants (nothing suggests Grace promised Rocky and AMPL jointly); cut (C5, −5) and drop fn 17.

### 2.10 The Development Agreement
Answer: pays only "if the Project made a profit" and is not shown breached. Nothing in the readings strengthens this; correct to keep to one clause (R-AB(2)).

### 2.11 The 8 April offer and acceptance
Answer: Gibson 298 for 'expected' as a request (acceptable analogy); "offered a promise for a promise,[^20]" with fn 20 Brambles 177 quoting ICS (McHugh JA) — a passage on the limits of classical offer-and-acceptance theory, flagged by both earlier markers as not a statement of consideration doctrine. Better: Beaton 168 (Kirby P): "The price can be in the form of an act, forbearance or promise." fn 20 → "Beaton (n 4) 168 (Kirby P)." (0 words).
"AMPL may argue that nothing bound until the Loan Agreement was signed; however, parties are bound 'when, and in the manner in which, they intend', as Lord Greene MR said of exchanged contracts,[^22]" — Lord Greene MR's words are Heydon JA's illustration of contracts hard to fit to offer and acceptance (Brambles 176, cb p 77), an analogy the answer must disclose. The High Court joint judgment in the set reading decides the precise question: Masters 360 (cb p 153; Dixon CJ, McTiernan and Kitto JJ), first class: "the parties have reached finality in arranging all the terms of their bargain and intended to be immediately bound to the performance of those terms, but at the same time propose to have the terms restated in a form which will be fuller or more precise but not different in effect". AMPL's side is the third class at 361 ("simply because they wish to reserve to themselves a right to withdraw at any time until the formal document is signed"), which the answer's "nothing suggests Rocky's undertaking awaited a document 'signed by Grace and AMPL'" meets. Similar: a bargain then restated in a document; different: Rocky was not to sign the Loan Agreement at all, which strengthens oral formation.
Replacement S2 (−3): "however, where parties 'have reached finality' and only 'propose to have the terms restated', they are 'immediately bound',[^22]". fn 22 → "Masters (n 6) 360 (Dixon CJ, McTiernan and Kitto JJ)." (fn 6 then needs the short title ('Masters').)

### 2.12 Who promised (Pierre or AMPL)
Answer weighs 'you' against control, office and loan, and names further information. Unused planted fact: "Pierre agreed to provide the money to Grace and the $1,150,000 was advanced by AMPL on the same day" (narrator) — the narrator treats Pierre's agreement as AMPL's act. A3 (ADD IF FUNDED, +6): "Pierre controls AMPL, spoke at its office about its loan and 'agreed' to its 27 February advance,". Not in the funded package (3 words short).

### 2.13 The existing legal duty rule and the third-party duty
Answer: Sundell 327 (cited, not quoted); Wigan 594 (Mason J, Walsh and Gibbs JJ agreeing; cb p 129) "made to the promisee under that contract"; Pao On 632.
Best for AMPL (unused fact-match): Sundell 327, the Full Court (editors' [4.95], cb p 111): "the only consideration which was suggested … was that the [defendant] would do what was necessary to ensure that the goods were delivered. But we are satisfied that the [defendant] was bound to do so under the original contract." 'Ensure' is Pierre's and Rocky's word. ADD IF FUNDED (+14): "AMPL may invoke the existing legal duty rule, as in Sundell, where a promise to 'ensure' delivery was no consideration because the promisor 'was bound to do so under the original contract'.[^25]"
Status flag: Pao On 632 is in the full casebook extract, which maps to the 2B skip range [4.300]-[4.340]; the Moodle extract covers only 629-30. The 2B slides nonetheless list "promises to third parties (Pao On v Lau Yiu Long – class 2A)" as an exception, so the use is defensible; no change.
Practical benefit (Williams v Roffey; Musumeci): REJECT. Glidewell LJ's element (i), "if A has entered into a contract with B to do work for, or to supply goods or services to, B in return for payment by B" (cb p 117), is not met by a guarantee given without payment by AMPL.

### 2.14 Intention and the letter of comfort
Answer: Ermogenous [26]; Banque Brussels 523 ("appropriately promissory in character"), 525 ("no relevant difference"). Rogers CJ, first instance (Commercial Division); the case's facts sit exactly beside Rocky's: ANI, not the borrower, assured the lending bank about the borrower's repayment ("it is our practice to ensure that … Spedley … will at all times be in a position to meet its financial obligations", cb p 140). Optional (+7): "as ANI's was to the lending bank". Rogers CJ 523 also fits the setting: "statements made by businessmen, after hard bargaining and made to induce another business person to enter into a business transaction" (cb p 142). Verdict: best available; optional colour only.

### 2.15 Certainty of 'ensure'
Answer: Upper Hunter 437 (Barwick CJ quoting Lord Wright in Scammell; cb p 159) and Ermogenous [25] for 'objectively'. Ermogenous [25] says the word intention "is used in the same sense as it is used in other contractual contexts" and "describes what it is that would objectively be conveyed" (cb p 135), so the borrowing is legitimate. No change.

### 2.16 Privity of the $10,000
Answer: Trident 115 "stranger to the consideration"; 'the clause' read both ways. Correct; set reading. No change.

### 2.17 Whether the guarantee clause binds Rocky (silence, conduct, taking the benefit)
Answer: D1 pin; Empirnall 534 (silence), 535-6 (taking the benefit with knowledge; reasonable opportunity to reject) — McHugh JA, majority; the counter ('priced his own words') is put.
Missing (D4): the post-formation conduct. A2 (+28, funded): "His later 'check in' emails and demand 'under the Loan Agreement', which may show whether he intended 'a binding arrangement',[^T] suggest assent but equally fit his oral undertaking." ('check in' and 'under the Loan Agreement' are the narrator's words; 'a binding arrangement' is Mayo J, Todd.) Slide 1B frames this as 'post-formation conduct'.

### 2.18 Consideration for the guarantee (past consideration, Pao On)
Answer: Trident 115; Roscorla 237 (Lord Denman CJ for the Court); Pao On 629 (the three conditions, quoted from the Moodle extract); AWM 456 for AMPL's act of signing.
Stronger passage, Rocky's side: Pao On 630 (cb p 125, Lord Scarman for the Board): "the mere existence or recital of a prior request is not sufficient in itself to convert what is prima facie past consideration into sufficient consideration in law … it is only the first of three necessary preconditions." Fits "Rocky 'asked'". Facts: Pao On is itself a guarantee given after an act done at the guarantors' request (similar), but there "the parties understood at the time of the main agreement that the restriction on selling must be compensated for by the benefit of a guarantee" (629, extract) (different: nothing shows a guarantee was contemplated on 27 February). Status: 630 is outside the Moodle extract and in the skip range. ADD IF FUNDED (+12), low.
AWM 456 for AMPL's signing is apt (an act as executed consideration); AWM 458's test ("whether the 'offer' was made in order to induce the doing of the act") could be named, low.

### 2.19 When the 12 months began
See D3 (funded fix A4, +6). The 'recorded' analysis against the 4% rate is good and needs no authority.

### 2.20 The March instalment
Correctly hedged as further information. "whichever start date applies" is redundant (the instalment fell due under both readings by force of 'monthly'): C7 (−3).

### 2.21 'Once Grace repays' as a condition
Meehan 582 (Gibbs CJ) and Upper Hunter 437 for Rocky's commercial reading: best available; set reading. No change.

### 2.22 The duty to co-operate
Beaton 185 (McHugh JA dissenting, citing Mason J in Secured Income, a High Court statement) — status disclosed. The only set-reading alternative, Meehan 591 (Mason J: "an obligation to do all that was reasonable on his part to obtain that finance", with Wilson J 598 "Clearly he must make reasonable efforts"; Gibbs CJ 581 contra), is split 2-2 and concerns the party whose condition it is. Keep Beaton.

### 2.23 Exposure
Stated precisely on both readings and for the oral undertaking (R-AD). No authority needed beyond what precedes.

---

## 3. Cuts (the answer is 20 over; these fund the additions)

| Tag | Present text | Replacement | Words |
|---|---|---|---|
| C1 | "Rocky could argue that his 12 February email merely records their meeting, as it opens 'Confirming discussions' and its other points promise nothing; however, 'I will lend'" | "Although the email opens 'Confirming discussions' and its other points promise nothing, 'I will lend'" | −12 |
| C2 | "[^6] the email fixes the amount, date, term and rate but leaves unnamed 'conditions' to Rocky." | "[^6] the email leaves unnamed 'conditions' to Rocky." (repeats para 1) | −8 |
| C3 | "Nor did AMPL lend as his agent, for, although a principal is a party where another 'contracts as agent' for him,[^14] AMPL took Rocky's own guarantee of the Loan, which no agent lending for him would need." | "Nor did AMPL lend as one who 'contracts as agent' for him,[^14] for it took Rocky's own guarantee, which no agent lending for him would need." | −11 |
| C4 | "on which both Rocky's claim to repayment and any claim by Grace that Rocky failed to lend 'by 15 February' depend." | "on which Rocky's claim to repayment, and any claim by Grace that Rocky failed to lend, depend." | −4 |
| C5 | " and Grace's promises to repay were made to AMPL, not to Rocky, even as a joint promisee;[^17]" | " and Grace's promises to repay were made to AMPL, not to Rocky;" (drop fn 17) | −5 |
| C6 | "a limit which 'takes the case out of the principle' that a promisor's discretion over performance defeats the promise;[^12]" | "a limit which 'takes the case out of the principle';[^12]" (principle now stated by Kitto J) | −9 |
| C7 | "is arguably already broken, whichever start date applies." | "is arguably already broken." | −3 |

## 4. Zero-cost and near-zero swaps (authority fit)

| Tag | Change | Words |
|---|---|---|
| S1 (D2) | "would be 'a price in return for' Rocky's promise to lend.[^4]"; fn 4 Beaton 168 (Kirby P) | −4 |
| S2 | Masters 360 first class for Lord Greene MR (2.11) | −3 |
| S3 | "For the same reason Rocky's promise is arguably illusory: where the promisor has 'a discretion or option as to whether he will carry out' a promise, 'there is no contract'.[^10]" fn 10 → Placer Development Ltd v Commonwealth (1969) 121 CLR 353, 356 (Kitto J) | +2 |
| fn 20 | Beaton (n 4) 168 (Kirby P) for 'a promise for a promise' | 0 |
| fn 34 (D1) | Trident (n 14) (Deane J) | 0 |

## 5. Additions in the funded package

| Tag | Text | Words |
|---|---|---|
| A1 | "however, the discretion in Meehan related 'only to the fulfilment of a condition', obtaining finance, under 'a concluded agreement as to the terms',[^13] whereas Rocky's concerns those terms themselves." fn 13 → Ibid 581–2 (Gibbs CJ) | +1 |
| A2 (D4) | after "…not the clause.": "His later 'check in' emails and demand 'under the Loan Agreement', which may show whether he intended 'a binding arrangement',[^T] suggest assent but equally fit his oral undertaking." | +28 |
| A4 (D3) | "Grace's interest payments from 8 April 2024 and his 'I have until 8 April 2025' might 'explain' the term,[^T] but in New South Wales post-contractual conduct cannot construe it;[^41] however, the term being arguably ambiguous," | +6 |

Arithmetic (applied to a scratch copy and recounted on the R-P method): 1,617 − 12 − 8 − 11 − 4 − 5 − 9 − 3 − 4 − 3 + 2 + 1 + 28 + 6 = **1,594 body; stated 'Word count: 1,597'**, within 1,600 with 3 words spare. Footnote housekeeping for the tracer: Beaton's first full cite becomes fn 4; Australian Woollen Mills' first full cite moves to fn 40; Brambles' first full cite moves to fn 41 (fn 20 and fn 22 no longer cite it); Todd is new (first at A2, then 'Todd (n x)' at A4); fn 17 deleted; renumber.

## 6. Further additions ranked by marks gained per word (not funded; each needs an equal cut)

1. A3 Pierre's 27 February agreement as AMPL's act (+6) — planted fact, decides 'who promised'.
2. Grace's Thorby counter and Rocky's answer (+35) — the strongest unmet counter on illusoriness (2.6).
3. Sundell's 'ensure' (+14) — exact word match for AMPL's existing-duty argument (2.13).
4. Carlill 'offers to receive offers' (+4) for the 5 February call (2.1).
5. Banque Brussels fact-match "as ANI's was to the lending bank" (+7) (2.14).
6. Pao On 630 'mere existence … of a prior request' (+12) (2.18; skip range).
7. Milne 473 or Biotech 135 on incompleteness (+20 each) (2.5).
8. ICS via Brambles 178 'merely because something has been done' (+20) (2.7).

## 7. Status register for authorities the answer relies on

| fn | Passage | Speaker / status | Set? |
|---|---|---|---|
| 1-2, 19 | Gibson 298 | Lord Diplock, HL majority | set |
| 3, 21, 35-36 | Empirnall 534-6 | McHugh JA, majority | set |
| 4 (now) | AWM 457 | the Court; promise-for-act only (D2) | set |
| 5, 23, 28, 32 | Ermogenous [25]-[26] | joint judgment | set |
| 6 | Masters 363 quoting Winn v Bull | joint judgment quoting Jessel MR | set |
| 7, 9 | Godecke 642-3; 646-7 | Walsh J (Mason J agreeing); Gibbs J obiter (labelled) | set |
| 8, 11-13, 43 | Meehan 580-2, 589 | Gibbs CJ; Mason J (Wilson J agreeing) | set |
| 10 | Placer 361 | Taylor and Owen JJ, majority (but wrong fit, 2.6) | set |
| 14, 24, 34 | Trident 145; (Deane J) | Deane J; outside 'Mason CJ and Wilson J only' but R-Y | R-Y |
| 15, 33, 37 | Trident 115 | Mason CJ and Wilson J | set |
| 16-18 | Coulls 486-7 | Taylor and Owen JJ, majority | set |
| 20, 22 | Brambles 177, 176 | Heydon JA quoting McHugh JA / Lord Greene MR (analogy) | set (read range) |
| 25 | Sundell 327 | the Full Court via editors [4.95] | set |
| 26 | Wigan 594 | Mason J (Walsh and Gibbs JJ agreeing) | set |
| 27 | Pao On 632 | the Board | skip range (slides name it) |
| 29-30 | Banque Brussels 523, 525 | Rogers CJ, first instance | set |
| 31, 44 | Upper Hunter 437 | Barwick CJ quoting Lord Wright | set |
| 38 | Roscorla 237 | Lord Denman CJ for the Court | set |
| 39 | Pao On 629 | Lord Scarman for the Board | set (Moodle extract) |
| 40 | AWM 456 | the Court; act as executed consideration (apt) | set |
| 41 | Brambles 164 | Heydon JA (adopted by Ipp AJA at 184 for the July 1990 contract) | skip range (D3) |
| 42 | Brambles 191 | Ipp AJA (Mason P agreeing) | skip range (D3) |
| 45 | Beaton 185 citing Secured Income | McHugh JA dissenting (labelled) | set |
