# R5 M3: Fidelity, terminology and AGLC audit of ANSWER.md (v4) and the v4 .docx

Role 3 under MARKERS_PROMPT.md, run on /home/user/new/work/ANSWER.md (identical to ANSWER_v4.md) and on /home/user/new/work/LAWS1150 Mid-Term T3 2026 - Rocky (v4).docx. No earlier marker report was read (no R2, R3 or R4 file, no TRACE, no MARK file).

Sources read for this audit: YUSUF_INSTRUCTIONS_VERBATIM.md; MARKERS_PROMPT.md; RUBRIC_RULINGS_SHEET_v12.txt section 6.1; the problem (ACTUAL TASKKK.txt); Instructionsss.txt; ReadingGuide.txt; CB14_ch03 (pp 39 to 86 in full: Gibson, Carlill, Clarke, Felthouse, Empirnall, Brambles), CB14_ch04 (pp 97 to 131 in full), CB14_ch05 (pp 133 to 155 in full), CB14_ch06 (pp 157 to 189, Upper Hunter, Pace, Whitlock, Hall v Busst, United Group, Meehan, Godecke, Placer to Windeyer J), CB14_ch11 (pp 325 to 356 in full: Coulls, the [11.32] agency note, Port Jackson, Trident including Brennan J and Deane J); the student's supplied W1L2 extract (page run checked); the Pao On one-page extract (pdftotext); slides 2A, 2B, 3A, 3B, 4A for terminology. `verify.py` was run (82 spans, 0 not found); its report-page column was checked by eye and is wrong in three places (noted in section 3), none of which affects the answer's pins.

Statuses used: **CORRECT**; **CERTAIN ERROR** (proved from the verbatim text); **POSSIBLE ERROR** (contestable; what would settle it is stated).

---

## 1. Result in one screen

**Certain defects (5)**

| # | Where | Defect | Fix | Body words |
|---|---|---|---|---|
| C1 | II, agency sentence, fn 25 | Deane J at Trident 145 states neither element the sentence attributes to him. ‘[W]ith its consent’ and ‘rather than solely for himself’ are the casebook editors' words at [11.32] (CB14 pp 332 to 333), not Deane J's. | See 5.1 (Option A, minus 2 words, or Option B, minus 1 word plus a Port Jackson citation) | minus 1 or 2 |
| C2 | fn 10 | `Meehan (n 9) 582` follows fn 9, which cites only *Meehan*. AGLC 4 r 1.4.3 requires ‘Ibid’. | `Ibid 582 (Gibbs CJ).` | 0 |
| C3 | II, guarantee paragraph | The quotation ‘a reasonable opportunity to reject’ (McHugh JA, *Empirnall* 535) sits in a sentence that has no footnote. A judge's words are quoted without a citation. | Add a footnote after ‘the clause.’: `Ibid 535 (McHugh JA).` Footnotes 38 to 46 become 39 to 47. No (n X) points to 38 or above, so no cross-reference changes. | 0 |
| C4 | I, AMPL's advance paragraph | ‘[T]he advance differed in amount, date, lender and rate’. The problem gives no rate for the 27 February advance. The only rate is the 4% the 8 April agreement ‘recorded’, and the answer's own Part II says that rate is something ‘nothing shows predated 8 April’. The answer contradicts itself on a derived fact. | ‘the advance differed in amount, date and lender’ | minus 1 |
| C5 | .docx, body | In ‘signature is not necessary, *Empirnall* being bound unsigned’, the builder italicises *Empirnall*. Here the word names the party (Empirnall Holdings, the company bound), not the case, so it must be roman, as ‘Mrs Coulls’ is. | Exclude this occurrence from the italic pass in build.py | 0 |

**Possible defects (most significant first)**

- P1. The text that ‘Construction is objective’ and the ‘in New South Wales’ limb rest on is at *Brambles* 164 (Heydon JA). The pin is right, but the text sits on casebook p 74. That page is inside the reading guide's skip range ([3.290] to [3.300], pp 73 to 76) and is missing from the student's supplied W1L2 extract, which runs pp 72, 73, then 76. In-range alternatives are given in 5.4.
- P2. ‘[T]he genesis of the transaction’ (*Brambles* 191, Ipp AJA) is on p 82, inside the guide's ‘Skip … the first part of Ipp JA's judgment; pp82-84’. Heydon JA at 163 (p 73, in range and in the extract) says the same thing: ‘casts light on the genesis of the contract’. Ipp AJA adopted his reasons on the July 1990 contract, and Mason P agreed with Ipp AJA. The swap saves 1 word (5.4).
- P3. The *Pao On* holding at 632 (the third-party duty) comes from the casebook's full extract, whose pages appear to fall in the 2B skip range. That inference is from the 2-page offset: Wigan is at [4.350] p 131 in the student's edition and at p 129 in CB14. The holding is otherwise carried only by slide 2B (‘promises to third parties (Pao On v Lau Yiu Long)’). R-Z(2) makes 632 the citation, so this is a status note, not a fault.
- P4. Fn 38 (‘AMPL must also show consideration moving from itself’) pins *Trident* 115. The on-point passage is 115 to 116 (Mason CJ and Wilson J): ‘C cannot compel A to carry out his promise, because, though a party to the contract, C is a stranger to the consideration’. That passage is slide 4A's ‘multi-party agreement where privity is satisfied but one party has not given consideration’. Change the pin to 115–16 (0 words).
- P5. Hedges dropped. In *Banque Brussels* 525, Rogers CJ called the third-paragraph point ‘far more thorny’ before holding it promissory, and he sat at first instance. In *Trident* 115 the plurality says ‘This court has hitherto accepted’ before reforming the rule for insurance. Neither omission misstates the law. A harsh marker could still note it.
- P6. *Roscorla* (fn 39) gives the pinpoint for the nominate report only (3 QB 234, 237). AGLC practice for English Reports parallels is to pin both. The ER page cannot be verified from the readings because the casebook carries only QB markers. This is settled only by the official report.
- P7. Fact nuance. ‘The Development Agreement repays him first only ‘if the Project made a profit’, none yet shown’ is accurate as far as it goes. But the narrator says the parties ‘realised that the profit from the Project would be minimal’, which implies a profit that would trigger Rocky's priority. ‘[N]one yet shown’ is not wrong, but it reads as though there will be no profit.
- P8. ‘AMPL named Rocky guarantor’ is a derived actor. The problem says only that ‘[t]he Loan Agreement also included a clause’ and that ‘the clause was included … before it was signed by Grace and AMPL’. Write ‘the Loan Agreement named Rocky guarantor’ (plus 1 word).
- P9. ‘[S]o it was no counter-offer’ applies the counter-offer rule with no authority attached. R-Z requires a case for every proposition. Brambles 176 (Heydon JA: ‘the rejection of the offer by a counter-offer’) is available.
- P10. The .docx sectPr has no pgSz or pgMar, so Word applies its own defaults (normally US Letter and 1-inch margins). Set A4 and explicit margins in reference.docx. The instructions ask for margins for comments.
- P11. The .docx and ANSWER.md match exactly: 20 paragraphs, 46 footnotes, identical text. The stated count is correct: the body is 1,596 words and the line says 1,599.

**Net word effect of the recommended fixes:** C1 Option A (minus 2), C4 (minus 1) and P2 (minus 1) take the body to 1,592 and the count line to ‘Word count: 1,595’. That frees 5 words for P8 (plus 1) and, if wanted, the clarity fix in 6.2.

---

## 2. Sentence-by-sentence trace (every proposition, at source, in context)

Abbreviations: cb = CB14 casebook page; rep = report page; ‘read range’ means inside the reading guide's ‘Read’ range for the student's edition.

### Part I, paragraph 1 (5 February call; 12 February email as offer)

| Answer's words | Source and context | Speaker and status | Verdict |
|---|---|---|---|
| ‘Grace's 5 February call asked Rocky to make an offer and promised nothing; it was likely an invitation to treat.’ [1] | *Gibson* 298 (cb 41 to 42): ‘The words “may be prepared to sell” are fatal to this; so is the invitation, not, be it noted, to accept the offer, but “to make formal application to buy”’. Question: whether the council's letter was a contractual offer. | Lord Diplock, leading speech. Lords Fraser and Keith agreed; ratio. | CORRECT. The fact is the narrator's: ‘proposed that Rocky offer Grace’ (‘asked’ is a fair paraphrase). ‘Invitation to treat’ is the slide 1A term and is not Lord Diplock's phrase, which is acceptable because the footnote supports the analogy. |
| ‘Unlike ‘may be prepared to sell’, those words are promissory’ [2 Ibid] | *Gibson* 298, same passage. | As above. | CORRECT. Ibid with no pin repeats 298, which is right. |
| Email facts: ‘records discussions’, ‘Potential’, ‘wait and see’, ‘I will lend’, ‘seeks agreement’ | Rocky's email: ‘Confirming discussions from our meeting this morning’; ‘Potential project over in Eastwood’; ‘wait and see at present’; ‘I will lend $1 million … by 15 February for 1 year at a rate of 5%’; ‘Please confirm agreement.’ | Rocky. | CORRECT (amount, date, term, rate). |

### Part I, paragraph 2 (acceptance; consideration)

| Answer | Source | Status | Verdict |
|---|---|---|---|
| ‘Acceptance requires an external manifestation of assent.’ [3] | *Empirnall* 534 (cb 71): ‘The objective theory of contract requires an external manifestation of assent to an offer.’ The passage concerns silent acceptance. | McHugh JA; Samuels JA agreed; Kirby P to the same effect. | CORRECT. |
| ‘‘Confirmed’ … answered a request to ‘confirm agreement’ without new terms, so it was no counter-offer’ | No footnote. | — | POSSIBLE (P9): no authority for the counter-offer rule. Grace's words, ‘Mr Rocky, Confirmed. Best, Grace.’, are quoted correctly. |
| ‘a promise can be the price of a promise’ [4] | *Beaton* 168 (cb 102): ‘The price can be in the form of an act, forbearance or promise.’ Pollock: ‘the price for which the promise of the other is bought’. | Kirby P. The appeal was dismissed and Kirby P is in the majority on the result; this is a general statement. | CORRECT. The derived ‘implied promise to repay’ is marked ‘arguably’. |

### Part I, paragraph 3 (intention; preliminary agreement; Masters)

| Answer | Source | Status | Verdict |
|---|---|---|---|
| ‘judged objectively, the alleging party bearing the onus’ [5: Ermogenous [25]–[26]] | Rep 105 (cb 135): ‘requires an objective assessment of the state of affairs between the parties’. Rep 106: ‘At best, the use of that language does no more than invite attention to identifying the party who bears the onus of proof … it was for the appellant to demonstrate that there was such a contract.’ | Joint judgment (Gaudron, McHugh, Hayne and Callinan JJ), ratio. | CORRECT. The paragraph numbers are not in the casebook, but slide 3A prints the onus passage as para ‘26.’ and the next as ‘27.’, so [25]–[26] holds. ‘[S]tatus of the parties’ is at rep 105 ([25]). |
| ‘project developers’ | Narrator: ‘Mr Grace and Mr Rocky are both project developers’. | Narrator. | CORRECT. |
| ‘nothing was made ‘subject to a formal contract’ … ‘be put into form’ or left to ‘a new agreement’’ [6] | *Masters* 363 (cb 154, after the [363] marker), quoting *Winn v Bull* 32: ‘When it is not expressly stated to be subject to a formal contract it becomes a question of construction, whether the parties intended that the terms agreed on should be put into form, or whether they should be subject to a new agreement’. | The Court (Dixon CJ, McTiernan and Kitto JJ) quoting Jessel MR. | CORRECT. The ‘quoting’ form is right. verify.py wrongly shows rep 362 for ‘be put into form’; the words follow the [363] marker. |
| ‘reached finality’, first class [7] | *Masters* 360 (cb 153). | The Court. | CORRECT. |
| Third class, ‘have dealt only with major matters’ [8] | *Masters* 361 (cb 153): ‘because they have dealt only with major matters and contemplate that others will or may be regulated by provisions to be introduced into the formal document’. | The Court. | CORRECT. The confining words about a formal document are handled honestly by ‘though no formal document was contemplated’. |
| ‘‘satisfactory’ leaves them to the protected party's judgment’ [9] | *Meehan* 580–1 (cb 180 to 181): ‘its natural effect is to leave it to the purchaser to determine’; [581] ‘Such a condition is generally entirely for the protection of the purchaser’. | Gibbs CJ. Murphy J and Wilson J broadly concur on 1(b). | CORRECT. Rocky as promisor-lender is in the purchaser's position, as the protected party whose obligation is conditional. |
| ‘Were the conditions settled ‘this morning’, the email would bind, but Rocky's duty would arise only once they were met.’ [10] | *Meehan* 582 (cb 181): ‘does not mean that there is no binding contract once the condition is fulfilled … a condition on whose fulfilment the obligation to complete the contract depended’. | Gibbs CJ. | CORRECT in law. Fn 10 is CERTAIN ERROR C2 (should be Ibid). |

### Part I, paragraph 4 (illusory promise)

| Answer | Source | Status | Verdict |
|---|---|---|---|
| ‘a consideration is illusory if it ‘depends upon an unfettered discretion vested in the promisor’’ [11: Pace 151 (McHugh JA), citing Placer 356, 360–1] | *Pace* rep 150 to 151 (cb 163): ‘A contract made for a consideration which is illusory is unenforceable: Placer Development Ltd v Commonwealth at 356, [151] 360–1 and Meehan v Jones … 581. A consideration is illusory if its payment or fulfilment depends upon an unfettered discretion vested in the promisor.’ | McHugh JA. Majority with Kirby P; Hope JA dissented. | CORRECT. The quoted sentence is on 151, after the marker. **On the Placer citation:** McHugh JA's own citation of Placer at 356 and 360–1 is attached to the sentence before the quoted definition, and he cites Placer again (no pin) as his first illustration. ‘citing’ is therefore a fair signal, and the pins are his. Placer 356 is Kitto J, verifiable through *Meehan* 581, where Gibbs CJ quotes Kitto J ‘at 356’. Placer 360–1 is Taylor and Owen JJ (cb 189 [361]: ‘left solely to the discretion of the Commonwealth … wholly unenforceable’). Placer was 3–2, Menzies and Windeyer JJ dissenting. Not an error. |
| ‘Grace may reply that, as in Meehan, Rocky must judge honestly, perhaps reasonably, and that the fixed terms are ‘specified parameters’.’ [12: Meehan 581 (Gibbs CJ), 589 (Mason J); Pace 151] | *Meehan* 581: ‘No doubt it may be implied that the purchaser will act honestly’. *Meehan* 589 (Mason J; the [589] marker is elided in cb 182 to 183, but *Pace* 132 places Mason J's ‘draconian’ passage at 589 and the following text runs to [590]): ‘relieves the purchaser from performance only in the event that, acting honestly, or honestly and reasonably’. *Pace* 151 (cb 164): ‘notwithstanding that the promisor retains a discretion, the consideration will not be illusory if the discretion must be exercised within specified parameters’, illustrated by the $7,000 to $9,000 salary range in *Lewandowski*. | Gibbs CJ (honesty); Mason J (undecided on reasonableness at 591); McHugh JA (majority). | CORRECT. ‘[P]erhaps reasonably’ keeps the lack of a majority on honest versus reasonable. ‘Specified parameters’ is used for Grace at full strength. The answer's reply, ‘no range confines’, meets the passage's own illustration (*Lewandowski*'s range), so the authority is used for what it says. McHugh JA's passage concerns firm promises to remunerate services; the ‘specified parameters’ sentence is general, so the transposition is fair. |
| ‘its discretion related ‘only to the fulfilment of a condition’, finance, within agreed terms’ [13] | *Meehan* 581–2: ‘that principle does not apply where the discretion or option … relates, not to the performance of the contractual obligations themselves, but only to the fulfilment of a condition … There is a concluded agreement as to the terms of the contract’. | Gibbs CJ. | CORRECT. |
| ‘Godecke bound because its added terms had to be ‘reasonable in an objective sense’’ [14: 642–3 (Walsh J)] | *Godecke* 642 (cb 186): ‘It means that what is required must be reasonable in an objective sense, and in case of [643] dispute this is a matter which the court can decide. Clause 6 does not mean that the purchaser is making an agreement to agree later’. | Walsh J, with Mason J (‘I agree with the reasons for judgment prepared by my brother Walsh’). This is the majority reasoning; Gibbs J concurred on a different ground (terms left to the vendor's solicitors). | CORRECT. 642–3 is the right range because the marker falls mid-sentence. ‘Godecke bound because …’ correctly states the majority's reason. |
| ‘Gibbs J's obiter ‘[p]erhaps’, for subsidiary matters once ‘all essential terms’ are agreed, likewise assumed ‘the familiar and objective standard of reasonableness’’ [14: 646–7 (Gibbs J)] | *Godecke* 647 (cb 187): ‘Perhaps it may be different where agreement has been reached on all essential terms but the determination of subsidiary matters has been left to one of the parties. In Sweet & Maxwell … [the Court of Appeal] placed considerable reliance on the fact that the parties had imported the familiar and objective standard of reasonableness’. Next: ‘However, it is unnecessary to express any concluded opinion on these matters’. | Gibbs J, obiter, hedged. | CORRECT. Hedge, obiter label and capitalisation alteration (‘[p]erhaps’) are all right. ‘[L]ikewise assumed’ is the answer's reading of Gibbs J's reliance on *Sweet & Maxwell* and his rejection of Bray CJ's no-‘reasonably’ extension. It is a fair inference, and it is labelled as the answer's own (‘likewise assumed’), not quoted as his. The checklist demand (keep ‘Perhaps’, obiter, essential terms only) is met. |
| ‘The email therefore likely bound neither party, defeating Grace's claim.’ | Conclusion. | — | CORRECT. |

### Part I, paragraph 5 (Rocky's claim through AMPL; agency; privity)

| Answer | Source | Status | Verdict |
|---|---|---|---|
| ‘made because he ‘asked’’ | Narrator: ‘Rocky asked A-Maize Pty Ltd … to advance $1,150,000 to Grace’. | Narrator. | CORRECT. |
| ‘the advance differed in amount, date, lender and rate’ | Amount ($1.15m against $1m), date (27 Feb against ‘by 15 February’) and lender (AMPL against Rocky) are all correct. **Rate:** the problem states no rate for the 27 February advance. The 4% is what the 8 April agreement ‘recorded’, and the answer's Part II says the 4% is something ‘nothing shows predated 8 April’. | — | CERTAIN ERROR C4 (unsupported derived fact, internally inconsistent). |
| ‘As Pierre ‘agreed to provide the money’ and AMPL named Rocky guarantor, which no lender acting for him would need, AMPL did not contract ‘as agent’ for him.’ [15: Trident 145 (Deane J)] | *Trident* 145 (cb 355): ‘If the promisee contracts as agent for a disclosed or undisclosed principal, the principal will ordinarily himself be, for the purposes of the requirement of privity, a party to the contract.’ | Deane J, concurring in the result (dismissing the appeal) on trust grounds; obiter on agency. | CORRECT use. Deane J's frame is a promisee contracting as agent, and AMPL is the promisee of Grace's promises, so the fit is exact. Fact: ‘Pierre agreed to provide the money to Grace’ is the narrator, quoted correctly. ‘AMPL named Rocky guarantor’ is POSSIBLE P8 (derived actor). |
| ‘Rocky's 5 March demand under the Loan Agreement, arguably assuming a 27 February start’ | Narrator: ‘On 5 March 2025, Rocky instructed his solicitor to send a letter of demand … requiring repayment of the principal amount under the Loan Agreement with AMPL’. | — | CORRECT. ‘[A]rguably’ marks the inference. |
| ‘‘a third party cannot sue upon a contract’, nor can ‘a stranger to the consideration’’ [16: Ibid 115 (Mason CJ and Wilson J)] | *Trident* 115 (cb 343): ‘This court has hitherto accepted that a third party cannot sue upon a contract and that a stranger to the consideration cannot maintain an action at law upon it’. | Mason CJ and Wilson J (plurality, the set reading). | CORRECT. Both fragments are on 115. verify.py sent ‘a stranger to the consideration’ to Coulls 478 only because of a line break at cb 343. The hedge ‘hitherto accepted’ is dropped (P5). |
| ‘Party status turns on ‘the written instrument itself’’ [17: Coulls 487 (Taylor and Owen JJ)] | *Coulls* 487 (cb 327): ‘the mere fact that her signature appears does not make her a party; this is a question to be resolved upon a consideration of the written instrument itself’. | Taylor and Owen JJ, with McTiernan J the majority; ratio on party status. | CORRECT. |
| ‘Grace's promises were made to AMPL, not Rocky, even as joint promisee’ [18: Ibid 486] | *Coulls* 486 (cb 325 to 326): ‘If, however, the correct conclusion is that the widow was a party … she is entitled … notwithstanding that she, personally, gave no consideration … We do not accept the contention … that if one, only, of two joint promisees provides the consideration … the other promisee cannot … sue’. | Taylor and Owen JJ. | CORRECT. The cite supports the joint-promisee route, which the answer then shuts on the facts. |
| ‘signature is not necessary, Empirnall being bound unsigned’ [19: Empirnall 535–6] | *Empirnall* 536 (cb 72): ‘“Eric does not sign contracts” … an objective bystander would conclude that Empirnall had accepted the offer on those terms’. 535 states the taking-the-benefit rule. | McHugh JA. | CORRECT in law. In the .docx the party name is italicised: CERTAIN ERROR C5 (formatting). |
| ‘nor decisive, Mrs Coulls signing without becoming a party’ [20: Coulls 487] | Same passage as fn 17. | Majority. | CORRECT. |

### Part I, paragraph 6 (conclusion)

‘The Development Agreement repays him first only ‘if the Project made a profit’, none yet shown; and Grace never promised to reimburse what he pays AMPL.’ The quotation is the narrator's description of the clause and is correct. ‘[N]one yet shown’: see P7. The rest is CORRECT.

### Part II, paragraph 1 (offer and acceptance, 8 April)

| Answer | Source | Status | Verdict |
|---|---|---|---|
| ‘Pierre's expressed expectation promised nothing, so it was likely an invitation to treat.’ [21: Gibson 298] | As fn 1. Fact (narrator): ‘Pierre expressed during the meeting that he expected Rocky to ensure that Grace made all payments … promptly’. | Lord Diplock. | CORRECT (by analogy). |
| ‘‘I will do that if you also promise’ offered a bilateral contract’ [22: Brambles 177 (Heydon JA), quoting Integrated 11,117–18 (McHugh JA)] | *Brambles* 177 (cb 78): ‘In classical theory, the typical contract is a bilateral one and consists of an exchange of promises by means of an offer and its acceptance’. | McHugh JA (Hope and Mahoney JJA concurring) in *Integrated*, quoted by Heydon JA. Heydon JA's acceptance-by-conduct reasoning is his alone, since Ipp AJA took ‘a route different’, but this is a definitional statement. | CORRECT. Note the context: McHugh JA's point is that commercial dealings often do not fit classical theory. The answer uses only the definition. In read range (cb 78). |
| ‘which Pierre accepted when he ‘agreed’’ [23: Empirnall 534] | ‘external manifestation of assent’. Narrator: ‘Pierre agreed’. | McHugh JA. | CORRECT. |
| ‘that ‘depends upon the intention disclosed by the language’ used, and Rocky reserved no right to withdraw pending a document’ [24: Masters 361–2] | *Masters* 362 (cb 154): ‘The question depends upon the intention disclosed by the language the parties have employed’. 361: ‘or simply because they wish to reserve to themselves a right to withdraw at any time until the formal document is signed’. | The Court. | CORRECT. The range covers both limbs. Fact: ‘before it was signed by Grace and AMPL’. |

### Part II, paragraph 2 (who promised: agency)

| Answer | Source | Status | Verdict |
|---|---|---|---|
| ‘Who promised turns on agency: Pierre bound AMPL if, with its consent, he contracted ‘as agent’ for it rather than solely for himself.’ [25: Trident 145 (Deane J)] | Deane J at 145 says only: ‘If the promisee contracts as agent for a disclosed or undisclosed principal, the principal will ordinarily himself be, for the purposes of the requirement of privity, a party to the contract.’ The two elements come from the **editors' note** at [11.32] (cb 332 to 333): ‘it is necessary to show that the principal expressly or impliedly consented to the agent acting on his or her behalf … the agent was purporting to act on behalf of the principal and not solely on his or her own behalf.’ | Deane J obiter; editors' note. | **CERTAIN ERROR C1.** The paraphrase attributes the editors' two-element test to Deane J, who states neither element. In addition, ‘Pierre bound AMPL’ is the promisor side (the $10,000), while Deane J speaks of the promisee side. Fix in 5.1. |
| ‘Pierre controls AMPL, had agreed to its 27 February advance, and spoke at its office about its loan’ | Narrator: ‘a company owned and controlled by Rocky's cousin, Pierre’; ‘Pierre agreed to provide the money’; ‘attended a meeting at AMPL's office’. | — | CORRECT. |

### Part II, paragraph 3 (consideration: existing legal duty rule)

| Answer | Source | Status | Verdict |
|---|---|---|---|
| ‘as in Sundell, promising to ensure performance already owed adds nothing’ [26: Sundell 327] | cb 111 [4.95], editors quoting the Court at 327: ‘the only consideration … was that the [defendant] would do what was necessary to ensure that the goods were delivered. But we are satisfied that the [defendant] was bound to do so under the original contract.’ | The Court (joint), quoted in an editors' note. | CORRECT. The ‘ensure’ analogy is exact. ‘[A]lso’ is hedged ‘arguably’. |
| ‘the rule applies ‘at least when’ the promise is made to the promisee under an existing contract’ [27: Wigan 594 (Mason J)] | *Wigan* 594 (cb 129): ‘The general rule is that a promise to perform an existing duty is no consideration, at least when the promise is made by a party to a pre-existing contract, when it is made to the promisee under that contract, and it is to do no more than the promisor is bound to do’. | Mason J; Walsh and Gibbs JJ agreed on this point; majority reasoning. | CORRECT. The hedge ‘at least when’ is quoted faithfully. The answer's ‘and none existed’ carries the weight, since there is no existing duty at all; it does not read ‘at least when’ as ‘only when’. |
| ‘and if Pierre promised, the exception for promises to third parties applies, any duty running to AMPL’ [28: Pao On 632] | *Pao On* 632 (cb 126): ‘Their Lordships do not doubt that a promise to perform, or the performance of, a pre-existing contractual obligation to a third party can be valid consideration.’ | Lord Scarman for the Board; ratio. | CORRECT. Status note P3 (casebook skip range; slide 2B names the exception). |
| Facts: ‘on 27 February Rocky only ‘asked’’; ‘the clause, arguably included after Pierre ‘agreed’’; ‘‘all payments’ ‘promptly’’; ‘‘repayment of the Loan’’ | Narrator throughout. ‘[R]epayment of the Loan’ is the narrator's description of the clause (‘a clause that Rocky personally guaranteed repayment of the Loan’), not necessarily its text. | — | CORRECT. The answer does not claim the clause's verbatim words. |

### Part II, paragraph 4 (intention to create legal relations; letter of comfort)

| Answer | Source | Status | Verdict |
|---|---|---|---|
| ‘presumptions at most identify who bears the onus, here Rocky’ [29: Ermogenous [26]] | Rep 106 / [26]: ‘At best, the use of that language does no more than invite attention to identifying the party who bears the onus of proof.’ | Joint judgment. | CORRECT. ‘Pierre is Rocky's cousin’ is the narrator's fact. |
| ‘‘appropriately promissory in character’’ [30: Banque 523] | Rep 523 (cb 142): ‘If the statements are appropriately promissory in character, courts should enforce them when they are uttered in the course of business and there is no clear indication that they are not intended to be legally enforceable.’ | Rogers CJ, Commercial Division, first instance. | CORRECT. First-instance status is not disclosed (immaterial). |
| ‘Rogers CJ saw ‘no relevant difference’ between a ‘practice to ensure’ that a borrower could repay and a promise ‘to ensure’ it’ [31: Ibid 525] | Rep 525 (cb 144): ‘The question whether the third paragraph … is promissory is far more thorny. However, in my view, if the paragraph is read as follows: “it is our practice to ensure that Spedley is at all times in a position to repay …”, its promissory nature is much clearer. I see no relevant difference between that and saying that “we promise to ensure that” Spedley will … repay’. | Rogers CJ. | CORRECT. The ‘far more thorny’ hedge is omitted (P5). verify.py wrongly shows rep 123 for ‘practice to ensure’; the words are at 525. |

### Part II, paragraph 5 (certainty)

| Answer | Source | Status | Verdict |
|---|---|---|---|
| ‘not ‘so obscure’ as to be void’ [32: Upper Hunter 437 (Barwick CJ), quoting Scammell 268 (Lord Wright)] | Rep 437 (cb 159): ‘So long as the language employed by the parties, to use Lord Wright's words in G Scammell & Nephew Ltd v Ouston [1941] AC 251, is not “so obscure and so incapable of any definite or precise meaning …”’. Barwick CJ gives no Scammell pin; the pin 268 comes from Mason J in *Meehan* 587 (cb 182). | Barwick CJ quoting Lord Wright. | CORRECT. |
| ‘it leaves ‘no discretion’’ [33: Meehan 582] | Rep 582: ‘if the condition is satisfied, leaves no discretion in either party as to whether he shall carry them out’. | Gibbs CJ. | CORRECT. |

### Part II, paragraph 6 (privity of the $10,000)

‘[H]e is its promisee, no stranger to the consideration’ [34: Trident 115]. Same passage as fn 16: CORRECT. ‘[T]o me directly’ is Rocky's words. ‘[T]he clause’ is the narrator's words. CORRECT.

### Part II, paragraph 7 (whether the guarantee clause binds Rocky)

| Answer | Source | Status | Verdict |
|---|---|---|---|
| ‘A guarantee was ‘provided by Rocky’’ | Narrator: ‘AMPL called for payment of the Loan under the personal guarantee provided by Rocky’. | Narrator, not AMPL. | CORRECT. The answer treats it as the narrator's words. |
| ‘only ‘the parties to it’ are ‘bound by the obligations of a contract’’ [35: Ibid 129 (Brennan J dissenting), quoting Wilson 80 (Kitto J)] | *Trident* 129 (cb 350, after the [129] marker): ‘Kitto J spoke (at 80) of “the elementary general rule that the only persons entitled to the benefits or bound by the obligations of a contract are the parties to it”’. | Brennan J dissenting, quoting Kitto J. | CORRECT. Dissent and quotation are labelled. R-Y(2) preferred a Deane J wording that does not appear in the casebook's Deane J extract (rep 143 to 148), so this is the verifiable source for the burden aspect of privity. |
| ‘Silence while a clause is included is generally not acceptance.’ [36: Empirnall 534] | ‘the silent acceptance of an offer is generally insufficient to create any contract’. | McHugh JA. | CORRECT. The ‘generally’ hedge is kept. |
| ‘taking the $10,000 promise knowing its terms’ [37: Ibid 535–6] | Rep 535: ‘knowing of the terms of the offer and the offeror's intention to enter into a contract, he has exercised a choice and taken the benefit of the offer’. Rep 536: ‘taking the benefit of an offer with knowledge of its terms’. | McHugh JA. | CORRECT. Facts: ‘attended’ (narrator); ‘later invoked the Loan Agreement’ (5 March demand). |
| ‘nothing shows ‘a reasonable opportunity to reject’ the clause’ (no footnote) | Rep 535 (cb 72, before the [536] marker): ‘where an offeree with a reasonable opportunity to reject the offer of goods or services takes the benefit of them under circumstances which indicate that they were to be paid for … it is open to the tribunal of fact to hold that the offer was accepted’. The words with the article ‘a’ are McHugh JA's own reformulation, not Judge Levine's (‘with reasonable opportunity to reject’). | McHugh JA. | Substance CORRECT and attributable to McHugh JA. **Citation: CERTAIN ERROR C3** (quotation without footnote). |
| ‘by the clause only if he saw its words’ | Empirnall's knowledge-of-terms element. | — | CORRECT. |

### Part II, paragraph 8 (consideration for the guarantee; past consideration)

| Answer | Source | Status | Verdict |
|---|---|---|---|
| ‘AMPL must also show consideration moving from itself’ [38: Trident 115] | Rep 115 (as above). Better: 115 to 116 (cb 343 to 344): ‘if A, B and C are parties to a contract and A promises B and C that he will [116] pay C $1 000 if B will erect a gate for him, C cannot compel A to carry out his promise, because, though a party to the contract, C is a stranger to the consideration’. | Mason CJ and Wilson J. | CORRECT. Better pin 115–16 (P4). |
| ‘Otherwise its advance is past consideration’ [39: Roscorla 237] | Rep 237 (cb 111): ‘a consideration past and executed will support no other promise than such as would be implied by law’. | Lord Denman CJ for the Court. | CORRECT. |
| ‘counting only if requested, understood to be remunerated, and enforceable if promised in advance; … unlike Pao On, where a return was understood ‘at the time of the main agreement’’ [40: Pao On 629] | Rep 629 (cb 124; also the Moodle extract): ‘The act must have been done at the promisors' request: the parties must have understood that the act was to be remunerated …: and payment … must have been legally enforceable had it been promised in advance … The parties understood at the time of the main agreement that the restriction on selling must be compensated for’. Both passages are before the [630] marker. | Lord Scarman for the Board. | CORRECT. The three conditions are covered by fn 40, the next footnote in the same sentence (AGLC placement). The conditions are kept apart from the 632 holding, as the checklist requires. |
| ‘‘really done in consideration of’ the guarantee’ [41: AWM 456] | Rep 456 (cb 99, before [457]): ‘the act was really done in consideration of a potential promise inherent in the statement or announcement’. | The Court (Dixon CJ, Williams, Webb, Fullagar and Kitto JJ). | CORRECT. A unilateral-contract frame, used for AMPL's signing as the act; hedged ‘arguably’. |

### Part II, paragraph 9 (when the 12 months began)

| Answer | Source | Status | Verdict |
|---|---|---|---|
| ‘Construction is objective, and in New South Wales post-contractual conduct, such as Grace's interest payments or ‘I have until 8 April 2025’, cannot construe the term’ [42: Brambles 164 (Heydon JA)] | Rep 164 (cb 73 to 74; the [165] marker comes at the end of cb 74). Third principle (cb 73): ‘post-contractual conduct is not admissible on the question of what a contract means as distinct from the question of whether it was formed’. NSW limb (cb 74): ‘unless it is demonstrated that the later decisions of the Victorian Full Court and Court of Appeal against admissibility … are clearly wrong or they are overruled, they should be followed in New South Wales’. Fourth principle (cb 74): ‘the construction of a contract is an objective question for the court, and the subjective beliefs of the parties are generally irrelevant’. | Heydon JA. Ipp AJA: ‘For the reasons set out by Heydon JA, I agree that the July 1990 contract governed …’, and Mason P agreed with Ipp AJA. On construction these are therefore the Court's reasons, not minority obiter. | CORRECT in pin, speaker and substance. ‘Construction is objective’ fairly compresses the fourth principle. Status P1: cb 74 is outside the student's supplied extract and inside the guide's skip range. Facts: ‘I have until 8 April 2025’ is Grace's words to AMPL; the interest payments are the narrator's. |
| ‘if it is ambiguous, mutually known facts showing ‘the genesis of the transaction’ are admissible’ [43: Ibid 191 (Ipp AJA)] | Rep 191 (cb 82): ‘Where ambiguities exist, mutually known facts establishing the commercial purpose of the contract, the genesis of the transaction, the background and the context in which the parties are operating will be admissible’. These are Ipp AJA's own words; the indentation is a layout artefact following his ‘…construing the contract:’ and citation. | Ipp AJA; Mason P agreed with his reasons. | CORRECT. Status P2 (skip range); in-range swap to Heydon JA 163. Ipp AJA was construing an offer letter, not a concluded contract, a small mismatch the Heydon JA 163 swap also removes. |
| ‘AMPL argues it ran from the 27 February advance, which the agreement ‘recorded’; but ‘recorded’ equally governs the 4% rate’ | AMPL ‘argued that the Loan was advanced on 27 February, and thus the 12 months had begun then’. Narrator: ‘The loan was recorded as $1,150,000 (‘Loan’) with an interest rate of 4% per annum’; ‘repayable at the expiry of 12 months’. | AMPL; narrator. | CORRECT. |
| ‘Interest is shown paid only to 8 February 2025’ | ‘Between 8 April 2024 and 8 February 2025, Grace made appropriate monthly repayments of the interest’. | Narrator. | CORRECT. |

### Part II, paragraph 10 (‘once Grace repays’; duty to co-operate)

| Answer | Source | Status | Verdict |
|---|---|---|---|
| ‘a condition precedent to that obligation, not to the contract, which bound at once’ [44: Meehan 582] | Rep 582: ‘It is clear that the condition in Special Condition 1(b) is not a condition precedent to contract. Certain obligations under the contract attached immediately … Whether the condition is described as a condition precedent to completion, or as a condition subsequent, seems largely a matter of words.’ | Gibbs CJ. Mason J at 592 calls the precedent/subsequent label ‘artificial’. | CORRECT. |
| ‘read commercially, his own payment satisfies it’ [45: Upper Hunter 437] | ‘In the search for that intention, no narrow or pedantic approach is warranted, particularly in the case of commercial arrangements.’ | Barwick CJ. | CORRECT (as Rocky's argument). |
| ‘the duty to co-operate, to ‘do everything necessary on [its] part’’ [46: Beaton 185 (McHugh JA dissenting), citing Secured Income 607 (Mason J)] | Rep 185 (cb 107, between [185] and [186]): ‘The McDivitts have a contractual duty to do everything necessary on their part to enable the plaintiff to have the benefit of the contract: Secured Income … at 607 per Mason J.’ | McHugh JA dissenting; the words are his own, citing (not quoting) Mason J. | CORRECT. ‘[C]iting’ is right; ‘dissenting’ is labelled. The answer omits the purposive tail (‘to enable the plaintiff to have the benefit of the contract’) but applies it implicitly (the call ‘does not stop Grace repaying’). The term is the casebook heading ‘The duty to co-operate’. |

### Part II, paragraph 11 (exposure)

‘$1,150,000 once the Loan is due and unpaid: now, on a 27 February start; otherwise from 8 April 2025 … in damages, to AMPL or Pierre … No term requires him to pay early … Grace, who said he ‘might not pay at all’’. Grace said it to AMPL: ‘if you don't leave off, I might not pay at all!’. CORRECT, and consistent with R-AD and R-AE.

---

## 3. verify.py artefacts (for the record; none affects the answer)

- ‘be put into form’ was reported at rep[362]; it is at 363 (after the ‘[363] of similar import’ marker, cb 154).
- ‘practice to ensure’ was reported at rep[123]; the answer's use is at *Banque* 525 (cb 144).
- ‘a stranger to the consideration’ was reported at Coulls 478 only; it is also at *Trident* 115, split across a line at cb 343.
- ‘as agent’ was reported at ch03 and ch11 p 333; it is also at *Trident* 145, cb 355 line 1804.

---

## 4. The items the caller named

1. ***Pace* 151, ‘specified parameters’, and the Placer citation.** Both are verified at 151 (McHugh JA, majority). The sentence is used for Grace and answered with the passage's own range illustration. McHugh JA does cite Placer ‘at 356, [151] 360–1’, but against the sentence before the quoted definition. ‘[C]iting’ is a fair AGLC signal and not an error. Placer 356 is Kitto J (confirmed by Gibbs CJ in *Meehan* 581); 360–1 is Taylor and Owen JJ ([361] at cb 189). **CORRECT.**
2. ***Godecke* 642–3, Walsh J.** ‘[R]easonable in an objective sense’ is at 642, with [643] falling mid-sentence. Mason J agreed with Walsh J, which makes this the majority reasoning. **CORRECT.**
3. ***Empirnall*, ‘a reasonable opportunity to reject’.** These are McHugh JA's own words at 535, not Judge Levine's quoted words. **Substance CORRECT; citation CERTAIN ERROR C3** (no footnote on the sentence).
4. **The agency test sentence (fn 25).** **CERTAIN ERROR C1.** Deane J states neither ‘with its consent’ nor ‘rather than solely for himself’. Both are the editors' words at [11.32].
5. **‘Construction is objective’ at *Brambles* 164.** Pin, speaker and substance are **CORRECT** (Heydon JA's fourth principle, cb 74, before [165]). Heydon JA's construction principles were adopted by Ipp AJA, with Mason P agreeing. Status P1: cb 74 is in the skip range and missing from the supplied extract.
6. **Every ibid and (n X) after renumbering.** All 46 references run 1 to 46 in order. Every (n X) points at the right first full citation: Gibson 1, Empirnall 3, Beaton 4, Ermogenous 5, Masters 6, Meehan 9, Pace 11, Trident 15, Coulls 17, Brambles 22, Pao On 28, Upper Hunter 32. Ibids at 2, 8, 16, 18, 31, 35, 37 and 43 are each preceded by a single-source footnote for the same case. No ibid follows a multi-source footnote: 7 and 13 correctly avoid ibid, and so do 23, 33 and 36. **One failure: fn 10 (C2).** Inserting C3's footnote after fn 37 leaves every (n X) unchanged, because none points to 38 or above. The new fn 38 (‘Ibid 535 (McHugh JA).’) is preceded by fn 37 (Ibid 535–6, Empirnall), so it is valid.
7. **The .docx.** Text identical to ANSWER.md. The 46 footnotes are Word auto-numbered (internal ids 20 to 65, no custom marks). Body and headings are Times New Roman 12, double spaced; footnotes are Times New Roman 10, single spaced. Headings are bold. A PAGE field is in the footer. The comments part is empty. The core properties have no author. Defects: C5 (italic party name) and P10 (no explicit page size or margins).

---

## 5. Fixes, with exact text

### 5.1 C1, the agency sentence (choose one)

- **Option A (faithful to Deane J, minus 2 words).** ‘Who promised turns on agency: if Pierre contracted ‘as agent’ for AMPL, AMPL is ‘a party to the contract’.[^25]’ Footnote unchanged: `Trident (n 15) 145 (Deane J).` The next sentence's facts (‘Pierre controls AMPL … so he likely acted for AMPL’) still apply. Deane J's ‘ordinarily’ can be added at a cost of 1 word: ‘AMPL is ordinarily ‘a party to the contract’’.
- **Option B (keeps both elements, from a case; minus 1 word).** ‘Who promised turns on agency: Pierre bound AMPL if, with its authority, he contracted ‘as agent’ for it, not solely for himself.[^25]’ Footnote: `Trident (n 15) 145 (Deane J); Port Jackson Stevedoring Pty Ltd v Salmond & Spraggon (Aust) Pty Ltd (1978) 139 CLR 231, 240 (Barwick CJ dissenting).` Barwick CJ at 240 (cb 334) states Lord Reid's requisites: ‘(2) the carrier by the bill contracted for the stevedore's protection as well as for his own, (3) the authority of the carrier to act for the stevedore … whether antecedently or by ratification’. Barwick CJ was in the majority on the agency point (cb 333: the agency point was ‘rejected by the majority of the court: Barwick CJ, Mason and Jacobs JJ’) but dissented on the result, hence ‘dissenting’.
- Not recommended: citing the editors' [11.32]. Its paragraph number in the student's edition is unknown, because the 14th edition numbering differs from the reading guide's, and R-Z(3) makes the casebook a last resort.

### 5.2 C2: fn 10 becomes `Ibid 582 (Gibbs CJ).`

### 5.3 C3: after ‘the clause.’ in Part II paragraph 7, insert a footnote `Ibid 535 (McHugh JA).` and renumber 38 to 46 as 39 to 47 (renumber.py handles this). No (n X) changes.

### 5.4 Source swaps that stay within the reading guide's read range (optional but recommended)

- **Fn 43 (P2):** ‘but, if it is ambiguous, pre-contractual conduct showing ‘the genesis of the contract’ is admissible.[^43]’ with `Ibid 163 (Heydon JA).` This saves 1 word. Source (cb 73, in the extract): ‘pre-contractual conduct is only admissible on questions of construction if the contract is ambiguous and if the pre-contractual conduct casts light on the genesis of the contract’. The 27 February advance is pre-contractual conduct.
- **Fn 42 (P1):** keep *Brambles* 164 for the in-extract third principle (cb 73). For ‘Construction is objective’, an in-range alternative at no word cost is *Pace* (n 11) 135 (Kirby P): ‘The meaning of the agreement between the parties must be discovered objectively.’ (cb 161, [135] marker; Kirby P in the majority). Using it means splitting the sentence's footnote in two (0 body words). The ‘in New South Wales’ limb exists only at cb 74; if it is kept, keep 164 and accept the status.
- **Fn 38 (P4):** `Trident (n 15) 115–16 (Mason CJ and Wilson J).`

### 5.5 C4 and P8 (fact fidelity)

‘Even had the email bound, the advance differed in amount, date and lender.’ (minus 1) ‘As Pierre ‘agreed to provide the money’ and the Loan Agreement named Rocky guarantor, …’ (plus 1).

### 5.6 C5 (.docx)

In build.py, stop italicising ‘Empirnall’ when it is followed by ‘being bound’, for example by marking that occurrence or post-editing. ‘Masters’, ‘Meehan’, ‘Godecke’, ‘Sundell’ and ‘Pao On’ in the body name cases and are rightly italic.

---

## 6. Terminology, voice and mechanics

### 6.1 Terminology (the answer's term against the lecturer's)

| Answer's term | Lecturer or casebook source | Verdict |
|---|---|---|
| invitation to treat | Slides 1A and 1B | Matches |
| external manifestation of assent | Empirnall 534 | Matches (the source's words) |
| counter-offer | Slide 1B; Brambles 176 | Matches (uncited, P9) |
| bilateral contract | Slide 1A; Brambles 177 | Matches |
| preliminary agreement; Masters' first and third class | Slide 3A ‘preliminary agreements’; Masters 360 ‘three classes’ | Matches |
| intention to create legal relations (in full); presumptions; onus | Slide 3A; Ermogenous [26] | Matches |
| letter of comfort | Slide 3A; casebook heading | Matches |
| illusory; ‘specified parameters’; ‘subsidiary matters’ | Casebook heading ‘ILLUSORY PROMISES’; Pace 151; Godecke 647 | Matches |
| existing legal duty rule; exception for promises to third parties | Slide 2B: ‘Existing Legal Duty Rule’; ‘3 exceptions to the rule: … promises to third parties (Pao On v Lau Yiu Long)’ | Matches |
| past consideration | Slide 2A: ‘Past consideration’; ‘Exception to past consideration rule’ | Matches |
| privity; stranger to the consideration; joint promisee | Slide 4A; Trident 115; casebook [11.30] ‘joint promisee doctrine’ | Matches |
| agency, ‘as agent’ | Slide 4A ‘Agency’; casebook [11.32] | Matches |
| post-contractual conduct | Brambles 164 (the source's term); slide 1B says ‘post-formation conduct’ | Acceptable (the source's term) |
| condition precedent | Meehan 582 | Matches |
| duty to co-operate | Beaton, casebook heading ‘The duty to co-operate’ | Matches |
| silence | Slide 1B | Matches |

No proxy or invented label was found.

### 6.2 Voice and mechanics

- **No dashes, double quotation marks or contractions** (all apostrophes are possessives). No meta language and no invented abbreviations. Longest sentence: 45 words (‘Otherwise its advance is past consideration …’), at the limit. Next longest: 42, 42, 41.
- **One-clause sentences** (Yusuf ‘despises’ them): ‘Acceptance requires an external manifestation of assent.’ (it opens a paragraph); ‘Naming no start, it is arguably ambiguous.’; ‘Thus Rocky has no present claim against Grace.’; ‘Silence while a clause is included is generally not acceptance.’ Each can be joined to its neighbour with a semicolon at no word cost. Examples: ‘Acceptance requires an external manifestation of assent;[^3] ‘Confirmed’ arguably …’; ‘… are admissible;[^43] naming no start, it is arguably ambiguous.’
- **Elliptical clause (clarity, possible zeugma):** in ‘…‘have dealt only with major matters’; though no formal document was contemplated, so did the email’, ‘so did the email’ borrows ‘have dealt’ from ‘parties’. Clearer: ‘…; though no formal document was contemplated, the email likewise dealt only with major matters.’ (plus 4 words, affordable after 5.1A, 5.4 and 5.5).
- **Ambiguous list:** ‘Rocky could say his 12 February email records discussions, its other points, ‘Potential’ and ‘wait and see’, promising nothing.’ This can be read as three items. Clearer: ‘… merely records discussions, and that its other points, ‘Potential’ and ‘wait and see’, promise nothing.’ (plus 3 words).
- **No fragments after semicolons** (every post-semicolon segment has a finite main verb).

---

## 7. Facts and speakers (complete list of quoted or used facts)

| Fact as used | Problem's words | Speaker | Verdict |
|---|---|---|---|
| 5 February call | ‘proposed that Rocky offer Grace a ‘$1 million dollar working capital loan …’’ | Narrator reporting Grace | OK |
| ‘records discussions’, ‘Potential’, ‘wait and see’, ‘I will lend’, ‘subject to satisfactory conditions’, ‘subject to success of Hail Mary Project’, ‘this morning’, ‘confirm agreement’ | Email text | Rocky | OK |
| ‘Confirmed’ | ‘Mr Rocky, Confirmed. Best, Grace.’ | Grace | OK |
| ‘project developers’ | ‘both project developers’ | Narrator | OK |
| ‘asked’ | ‘Rocky asked A-Maize Pty Ltd’ | Narrator | OK |
| ‘agreed to provide the money’ | same words | Narrator | OK |
| advance ‘differed in … rate’ | no rate stated for 27 February | — | C4 |
| ‘AMPL named Rocky guarantor’ | ‘The Loan Agreement also included a clause’ | Narrator | P8 |
| 5 March demand ‘under the Loan Agreement’ | ‘requiring repayment of the principal amount under the Loan Agreement with AMPL’ | Narrator | OK |
| ‘I never signed anything with you’ | same | Grace to Rocky, 7 March | OK |
| ‘if the Project made a profit’ | same | Narrator (clause description) | OK; P7 on ‘minimal’ |
| Pierre's expectation; ‘all payments’; ‘promptly’ | ‘Pierre expressed … that he expected Rocky to ensure that Grace made all payments under the Loan Agreement promptly’ | Narrator reporting Pierre | OK |
| ‘I will do that if you also promise’; ‘to me directly’; ‘once Grace repays the Loan’ | same | Rocky | OK |
| ‘agreed’ (Pierre) | ‘Pierre agreed’ | Narrator | OK |
| ‘repayment of the Loan’ | ‘a clause that Rocky personally guaranteed repayment of the Loan’ | Narrator (not necessarily the clause's text) | OK |
| ‘attended’ | ‘Rocky, Grace, and Pierre attended a meeting at AMPL's office’ | Narrator | OK |
| ‘provided by Rocky’ | ‘under the personal guarantee provided by Rocky’ | Narrator | OK |
| Pierre controls AMPL; cousin | ‘a company owned and controlled by Rocky's cousin, Pierre’ | Narrator | OK |
| ‘recorded’; 4%; 12 months | ‘The loan was recorded as $1,150,000 … 4% per annum … repayable at the expiry of 12 months’ | Narrator | OK |
| Interest to 8 February 2025 | ‘Between 8 April 2024 and 8 February 2025, Grace made appropriate monthly repayments of the interest’ | Narrator | OK |
| ‘I have until 8 April 2025’ | same | Grace to AMPL | OK |
| AMPL's 27 February argument | ‘AMPL argued that the Loan was advanced on 27 February’ | AMPL | OK |
| ‘might not pay at all’ | ‘if you don't leave off, I might not pay at all!’ | Grace to AMPL | OK |
| 9 March call | ‘on 9 March 2025 … AMPL called for payment of the Loan under the personal guarantee’ | Narrator | OK |

---

## 8. Overall fidelity verdict

Of roughly 75 traced propositions, 70 are CORRECT at source, with the right pin, speaker, status and hedge (save P5). The five new or changed items the caller named all check at source, except the agency test sentence. That sentence (C1) is the only substantive misattribution in the answer: it puts the editors' two-element agency test into Deane J's mouth. The remaining certain defects are mechanical: one ibid (C2), one uncited quotation (C3), one unsupported and self-contradicted derived fact (C4) and one italicised party name in the .docx (C5). All five can be fixed within the word cap; the recommended set lowers the count by 4 before the optional clarity edits.
