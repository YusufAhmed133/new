# R4 M3: Fidelity, terminology and AGLC audit of ANSWER.md (v3)

Role 3 under MARKERS_PROMPT.md. The target is /home/user/new/work/ANSWER.md (identical to ANSWER_v3.md, checked by diff). Body is 1,597 words; the stated count is 1,600 (body plus 3, per R-P). I also checked the built document, /home/user/new/work/LAWS1150 Mid-Term T3 2026 - Rocky (v3).docx. I did not open any earlier report.

## 0. How I checked it

- I read in full: YUSUF_INSTRUCTIONS_VERBATIM.md; the problem (ACTUAL TASKKK.txt); Instructionsss.txt; ReadingGuide.txt; slide decks 1A, 1B, 2A, 2B, 3A and 4A, plus 3B on certainty and illusory promises.
- I read every extract the answer relies on, in full context, from the casebook text files:
  - CB14_ch03: Gibson; Felthouse; Empirnall; Brambles (whole extract, all three judges).
  - CB14_ch04: the Jenks and Pollock notes; Australian Woollen Mills; Beaton (all three judges); Roscorla; the existing legal duty rule note quoting Sundell; Pao On (whole extract); Wigan.
  - CB14_ch05: Ermogenous; Banque Brussels; Masters, with the [5.105] note.
  - CB14_ch06: the chapter note; Upper Hunter; Biotechnology v Pace (Kirby P, McHugh JA, Hope JA); Meehan (all judges); Godecke; Placer.
  - CB14_ch11: Coulls; Trident, covering Mason CJ and Wilson J, Brennan J and Deane J.
  - The Pao On one-page extract, read with pdftotext.
- Under the rulings sheet I read only R-F, R-K and the unit text needed to avoid contradicting binding rulings (skip-range register, 'Ipp AJA', the qualifier's antecedent, Pace '150 to 151', Wigan's hedge, 'promises to third parties').
- `verify.py`: 78 quoted spans, 0 not found. The tool does not check page markers by eye, so every pin below was checked by eye against the printed [nnn] report markers.

Status key:
- CORRECT: true at source in context.
- CERTAIN ERROR: proved from the verbatim text.
- POSSIBLE: contestable, with what would settle it.
- NOTE: register or style point, no deduction.

---

## 1. Certain defects (proved)

| # | Where | Defect | Proof (verbatim, file, casebook page, report pin, speaker) | Fix and word cost |
|---|---|---|---|---|
| C1 | fn 12, S18 | **Wrong pin.** Pace is cited at 150. The quoted words sit on report page **151**. | CB14_ch06.txt, casebook p 163, McHUGH JA under 'Was the consideration illusory?' (majority; Kirby P at 136: 'I differ and agree with McHugh JA'): '[6.45] [150] A contract made for a consideration which is illusory is unenforceable: Placer Development Ltd v Commonwealth at 356, **[151]** 360–1 and Meehan v Jones (1982) 149 CLR 571, 581. A consideration is illusory if its payment or fulfilment **depends upon an unfettered discretion vested in the promisor**.' The [151] marker is printed before the quoted sentence. The rulings sheet's own register also reads 'Pace 150 to 151'. | Change fn 12 to '…130, 151 (McHugh JA).' (or 150–1). 0 words. |
| C2 | Built .docx, fn 12 | **Case name not italicised.** The footnotes.xml run for 'Biotechnology Australia Pty Ltd v Pace' carries no `<w:i/>`. It is the only case name in the document left in roman. Cause: build.py's CASES list omits it. | docx footnote 12 (internal id 31) reads 'Biotechnology Australia Pty Ltd v Pace (1988) 15 NSWLR 130, 150 (McHugh JA).' with no italics, while every other case name is italic. The brief requires 'Every case name is italicised in text and footnotes.' | Add 'Biotechnology Australia Pty Ltd v Pace' to CASES in build.py and rebuild after the C1 fix. 0 words. |
| C3 | S7, S9, S18 | **'qualifier' has no antecedent.** The planted words 'subject to satisfactory conditions' are never quoted whole in the body: 0 occurrences, with only 'satisfactory' and 'conditions' quoted separately in S14. 'Qualifier' is the answer's own label, and its first use ('qualifier included', S7) points to nothing the reader can see. | Problem: 'I will lend $1 million to you by 15 February for 1 year at a rate of 5% interest **subject to satisfactory conditions**.' The rulings sheet (unit for 'Confirmed') says: '‘qualifier included’ must have an antecedent the reader can see in the unit or the cross-reference (R1).' Brief R4: no invented labels. | S7: 'likely accepted the first point, ‘subject to satisfactory conditions’ included.' S9 and S18 then read 'That qualifier…' / 'The qualifier…' with a visible antecedent. +3 words. To fund it: drop 'merely' in S3 (−1), 'just' in S50 (−1) and 'already' in S65 (−1). The count stays 1,600. |

No other proposition in the answer is proved wrong at source. The three paraphrases you asked about are traced in section 3. All are CORRECT; the Pao On one should be strengthened.

---

## 2. Every sentence traced (S1 to S71)

Speaker and status come from the casebook judge heading and the bench count. The table lists facts only where the wording matters. Section 4 checks every fact word by word.

### Part I

| S | Sentence (abridged) | Proposition and source in full context | Status |
|---|---|---|---|
| S1 | The first issue is whether the February dealings formed a loan contract… | Issue framing; no law. | CORRECT |
| S2 | Grace's 5 February call asked Rocky to make an offer and promised nothing; likely an invitation to treat [1], which Rocky declined | Gibson 298, Lord Diplock (the leading speech; Lord Edmund-Davies, Lord Russell, Lord Fraser and Lord Keith agreed in the result). The words '“may be prepared to sell” are fatal…; so is the invitation, not… to accept the offer, but “to make formal application to buy”' (CB ch03 p 42). Lord Diplock does not use the phrase 'invitation to treat'; slide 1A defines it: 'An invitation for others to make an offer or enter into a negotiation.' The use is analogical and sound. On the facts: the problem says Grace 'proposed that Rocky offer Grace' a loan. 'Asked… to make an offer' is a fair paraphrase. 'Declined' is fair: Rocky 'was not interested in offering Grace a long-term loan but proposed that they meet'. | CORRECT |
| S3 | Rocky could say his email merely records discussions… 'Potential' and 'wait and see' | Facts: 'Confirming discussions from our meeting this morning'; 'Potential project'; 'wait and see at present'. | CORRECT |
| S4 | 'I will lend' fixes the amount, date, term and rate; the email seeks agreement | Facts: '$1 million', 'by 15 February', 'for 1 year', '5% interest'; 'Please confirm agreement.' | CORRECT |
| S5 | Unlike 'may be prepared to sell', those words are promissory [2] | Gibson 298 (Ibid). Lord Diplock contrasts the first paragraph with the 'indicative mood in such expressions as “the interest rate will change”', which 'might have been understood… as indicating a firm offer'. | CORRECT |
| S6 | Acceptance requires an external manifestation of assent [3] | Empirnall 534, McHugh JA (Samuels JA agreed; Kirby P 'to substantially the same effect'): 'The objective theory of contract requires an external manifestation of assent to an offer.' | CORRECT (one-clause sentence: §6) |
| S7 | 'Confirmed' arguably vouched only for accuracy; but it answered a request to 'confirm agreement' without new terms, so no counter-offer… qualifier included | Facts: 'Mr Rocky, Confirmed. Best, Grace.' 'Counter-offer' is the course term (S1B: 'What is the legal effect of a counter-offer?'). No case is cited for the counter-offer point; the rubric accepts this form. | CORRECT on the law. **C3** on 'qualifier'. |
| S8 | Grace's implied promise to repay would arguably be consideration, since a promise can be the price of a promise [4] | Beaton 168, Kirby P: 'consideration must be satisfied in the form of a price in return for the promisor's promise or a quid pro quo. **The price can be in the form of an act, forbearance or promise.**' See §3(a). 'Implied promise' is a derived fact, hedged with 'arguably'. | CORRECT |
| S9 | The qualifier raises whether this preliminary agreement showed an intention to create legal relations | Course terms ('preliminary agreements', S3A; 'intention to create legal relations' in full). | CORRECT (C3 antecedent) |
| S10 | judged objectively, the alleging party bearing the onus [5]; status as 'project developers' favours it | Ermogenous [25]: 'requires an objective assessment of the state of affairs between the parties'; 'the status of the parties to it'. [26]: 'it was for the appellant to demonstrate that there was such a contract'. Joint judgment of Gaudron, McHugh, Hayne and Callinan JJ. Paragraph [26] is confirmed by slide 3A, which prints '26. In this context of [ICLR]…'. [25] is the paragraph immediately before it ('Because the inquiry…'). Facts: narrator, 'Mr Grace and Mr Rocky are both project developers'. | CORRECT |
| S11 | As nothing was made 'subject to a formal contract', the question is whether the terms were merely to 'be put into form' or left to 'a new agreement' [6] | Masters 363. The Court (Dixon CJ, McTiernan and Kitto JJ) quotes Winn v Bull 32 (Jessel MR): 'When it is not expressly stated to be subject to a formal contract it becomes a question of construction, whether the parties intended that the terms agreed on should be put into form, or whether they should be subject to a new agreement…'. The [363] marker precedes the quote. The footnote attribution ('quoting… (Jessel MR)') is right. | CORRECT |
| S12 | Grace: 'reached finality', Masters' first class [7] | Masters 360, the Court: 'It may be one in which the parties have reached finality in arranging all the terms of their bargain…'. The next marker is [361]. | CORRECT. NOTE: the three classes presuppose that 'the matter of their negotiation shall be dealt with by a formal contract' (360). S13 concedes that premise for Rocky, but Grace's first-class argument carries the same caveat. |
| S13 | Rocky: third class, 'have dealt only with major matters' [8]; though no formal document was contemplated… | Masters 361: 'because they have dealt only with major matters **and contemplate that others will or may be regulated by provisions to be introduced into the formal document**'. The confining words are acknowledged by 'though no formal document was contemplated'. The hedge is kept. | CORRECT |
| S14 | 'conditions'… name no external event… further loan terms; 'satisfactory' leaves them to the protected party's judgment [9], here Rocky's as lender | Meehan 580–1, Gibbs CJ: 'its natural effect is to leave it to the purchaser to determine…' (580); 'Such a condition is generally entirely for the protection of the purchaser, and it is the satisfaction of the purchaser… that will satisfy the condition' (581). Transposing purchaser to lender is application, and it is marked as such ('here'). | CORRECT |
| S15 | Later conduct, admissible on formation [10], agrees, AMPL later lending on other terms | Brambles 164, Heydon JA: 'post-contractual conduct is admissible on the question of whether a contract was formed'. Ipp AJA adopted Heydon JA's reasons on the July 1990 contract ('For the reasons set out by Heydon JA, I agree…', 184–5) and Mason P agreed with Ipp AJA (155), so this is effectively unanimous. Register: this passage lies in RG 1B skip range [3.290]–[3.300] (pp73–76); R-F says register only. | CORRECT. NOTE: the conduct relied on is partly AMPL's, a non-party, though Rocky's request and Grace's receipt of $1,150,000 are the parties' own conduct. |
| S16 | On balance, the loan was likely left to a new agreement | Conclusion. | CORRECT |
| S17 | Were the conditions settled 'this morning'… Rocky's duty would arise only once they were met [11] | Meehan 582, Gibbs CJ: 'Once the condition is fulfilled… the contract becomes completely binding'; 'a condition on whose fulfilment the obligation to complete the contract depended'. | CORRECT |
| S18 | …illusory if it 'depends upon an unfettered discretion vested in the promisor' [12] | Pace, McHugh JA, **151** (see C1). The quote drops 'its payment or fulfilment' without distortion. | CORRECT proposition; **C1** pin |
| S19 | Grace may reply that, as in Meehan, Rocky must judge honestly, perhaps reasonably [13] | Meehan 581, Gibbs CJ: 'No doubt it may be implied that the purchaser will act honestly'. Meehan 589, Mason J: 'acting honestly, or honestly and reasonably' (the [589] marker is elided, but Kirby P in Pace pins the adjacent passage 'To say that clauses of this kind…' at 589). Mason J leaves it undecided at 590–1; Wilson J leans to honesty at 597–8. 'Perhaps reasonably' keeps the absence of a majority. | CORRECT |
| S20 | Meehan distinguishable: discretion 'only to the fulfilment of a condition', finance, within agreed terms [14] | Meehan 581–2, Gibbs CJ: 'relates, not to the performance of the contractual obligations themselves, but only to the fulfilment of a condition' (581); 'There is a concluded agreement as to the terms of the contract' (582). | CORRECT |
| S21 | Gibbs J's obiter '[p]erhaps'… 'all essential terms'… assumed 'the familiar and objective standard of reasonableness' [15] | Godecke 647, Gibbs J (separate concurring judgment; Mason J agreed with Walsh J): 'Perhaps it may be different where agreement has been reached on all essential terms but the determination of subsidiary matters has been left to one of the parties.' He then says Sweet & Maxwell 'placed considerable reliance on the fact that the parties had imported the familiar and objective standard of reasonableness', disagrees with Bray CJ's extension without 'reasonably', and adds 'it is unnecessary to express any concluded opinion'. Obiter status and hedge are kept. | CORRECT. POSSIBLE overstatement: 'assumed' compresses Gibbs J's reliance, through Sweet & Maxwell, on the reasonableness standard. 'Required, as he read Sweet & Maxwell,' is more exact (+3). Optional. |
| S22 | The email therefore likely bound neither party… | Conclusion. | CORRECT |
| S23 | Rocky may claim AMPL's advance, made because he 'asked', performed his promise | Fact: 'Rocky asked A-Maize Pty Ltd… to advance $1,150,000'. | CORRECT |
| S24 | …$1,150,000, after 15 February, by AMPL, recorded on 8 April at 4% | Facts exact (27 February; 'recorded as $1,150,000'; '4% per annum'). | CORRECT |
| S25 | As Pierre 'agreed to provide the money' and AMPL named Rocky guarantor… AMPL did not contract 'as agent' for him [16] | Trident 145, Deane J: 'If the promisee contracts as agent for a disclosed or undisclosed principal, the principal will ordinarily himself be, for the purposes of the requirement of privity, a party to the contract.' AMPL is the promisee of Grace's promises, so the dictum's position matches. | CORRECT |
| S26 | privity: 'a third party cannot sue upon a contract', nor can 'a stranger to the consideration' [17] | Trident 115, Mason CJ and Wilson J: 'This court has **hitherto** accepted that a third party cannot sue upon a contract and that a stranger to the consideration cannot maintain an action at law upon it'. Their departure is confined: 'the limited question we have to decide is whether the old rules apply to a policy of insurance' (123). For a loan contract the rule stands, so dropping 'hitherto' does not misstate it. | CORRECT |
| S27 | Party status turns on 'the written instrument itself' [18]; promises made to AMPL, not Rocky, even as joint promisee [19]; Rocky gave Grace nothing | Coulls 487, Taylor and Owen JJ (the majority with McTiernan J): 'the mere fact that her signature appears does not make her a party; this is a question to be resolved upon a consideration of the written instrument itself.' Coulls 486 (joint promisees). Fact: 'AMPL and Grace entered into a written loan agreement'. | CORRECT |
| S28 | 'I never signed anything with you'… signature not necessary, Empirnall bound unsigned [20], nor decisive, Mrs Coulls [21] | Empirnall 535–6 ('Eric does not sign contracts'… 'Empirnall had accepted the offer on those terms'); Coulls 487. The quote is Grace's, exact. | CORRECT |
| S29 | Thus Rocky has no present claim against Grace | Conclusion. | CORRECT. NOTE: it opens its paragraph with a conclusion (R6, §6). |
| S30 | Development Agreement repays him first only 'if the Project made a profit', none yet shown; Grace never promised to reimburse | Fact: 'if the Project made a profit, Rocky… would be repaid his investment and a portion of the profit in priority to Grace'. | POSSIBLE (facts). (i) The problem also says the parties 'realised that the profit from the Project would be **minimal**'. A small profit was expected, so 'none yet shown' is literally true but hides a planted fact that bears on Rocky's priority repayment. Fix: 'a ‘minimal’ profit was expected but none is shown made' (+5). (ii) 'Grace never promised' turns the problem's silence into a positive fact. Write 'nothing shows Grace promised' (+1). Z2. |

### Part II

| S | Sentence (abridged) | Proposition and source | Status |
|---|---|---|---|
| S31 | the questions are whether he can claim $10,000 and must pay AMPL | Framing. | CORRECT |
| S32 | Pierre's 'expected' promised nothing… invitation to treat [22] | Gibson 298 as in S2. On the facts, 'expected' is the **narrator's** word: 'Pierre expressed during the meeting that he expected Rocky to ensure…'. Pierre's actual words are not given. | POSSIBLE (speaker, Z2). Fix: 'Pierre's expressed expectation promised nothing' (0 words), or 'Pierre ‘expressed’ only what he ‘expected’' (+3). |
| S33 | 'I will do that if you also promise' offered a bilateral contract [23], which Pierre accepted when he 'agreed' [24] | Brambles 177, Heydon JA quoting ICS (McHugh JA, with Hope and Mahoney JJA concurring): 'In classical theory, the typical contract is a bilateral one and consists of an exchange of promises by means of an offer and its acceptance'. Empirnall 534. Course term 'bilateral contract' (S1A: 'contract is made by exchange of promises… eg Gibson'). | CORRECT; POSSIBLE pin (see A23) |
| S34 | AMPL: nothing bound before signing; but that 'depends upon the intention disclosed by the language' used [25]; Rocky reserved no right to withdraw… | Masters 362, the Court: 'The question depends upon the intention disclosed by the language the parties have employed' (after the [362] marker). The right-to-withdraw language is at 361 ('reserve to themselves a right to withdraw at any time until the formal document is signed'), so 361–2 covers both. Fact: 'before it was signed by Grace and AMPL'. | CORRECT |
| S35 | A contract likely formed orally, binding both promises | Conclusion. | CORRECT (one clause, §6) |
| S36 | Pierre bound AMPL if he contracted 'as agent' for it [26] | Trident 145, Deane J. NOTE: Deane J speaks of 'the promisee' contracting as agent. Pierre is promisee of Rocky's undertaking, so AMPL becomes 'a party to the contract' and is bound as well as entitled. Apt. | CORRECT |
| S37 | Rocky's 'you' points to Pierre; Pierre controls AMPL, had agreed to its 27 February advance, spoke at its office about its loan | Facts: 'owned and controlled by Rocky's cousin, Pierre'; 'Pierre agreed to provide the money to Grace and the $1,150,000 was advanced by AMPL'; 'meeting at AMPL's office'. 'Agreed to its advance' compresses 'agreed to provide the money'; it is acceptable. | CORRECT |
| S38 | If he said he would pay personally, he alone owes… AMPL cannot sue on the undertaking | Further information, conditional; follows from privity. | CORRECT |
| S39 | existing legal duty rule: 'also' arguably presupposes a guarantee already given; as in Sundell… adds nothing [27] | Sundell 327, the court, quoted in the editors' note [4.95]: '…would do what was necessary to ensure that the goods were delivered. But we are satisfied that the [defendant] was bound to do so under the original contract… every promise… was identical with a promise given under the original agreement.' No judge is named, which is correct. Course term 'existing legal duty rule' (S2B; casebook heading). | CORRECT |
| S40 | the rule applies 'at least when' the promise is made to the promisee under an existing contract [28], and none existed | Wigan 594, Mason J (Walsh and Gibbs JJ agreeing on the point): 'The general rule is that a promise to perform an existing duty is no consideration, at least when the promise is made by a party to a pre-existing contract, when it is made to the promisee under that contract…'. The hedge is kept, as the rubric requires. | CORRECT. NOTE: 'at least' marks the certain case, not an outer limit. The decisive reason is that no duty existed when Rocky promised, and the sentence states that ('none existed'). |
| S41 | ensuring 'all payments' 'promptly' exceeds guaranteeing 'repayment of the Loan'; if Pierre promised, the exception for promises to third parties applies [29] | Pao On 632, Lord Scarman for the Board. See §3(c). Facts: 'all payments', 'promptly' (narrator reporting Pierre's expression); 'Rocky personally guaranteed repayment of the Loan'. | CORRECT label; strengthen the rule (§3(c)) |
| S42 | Rocky likely gave consideration unless the clause preceded the bargain | Conclusion with further information. | CORRECT |
| S43 | Pierre is Rocky's cousin, but presumptions at most identify who bears the onus [30], here Rocky; …'appropriately promissory in character' [31] | Ermogenous [26]; Banque 523, Rogers CJ (sitting alone at first instance): 'If the statements are appropriately promissory in character, courts should enforce them when they are uttered in the course of business and there is no clear indication that they are not intended to be legally enforceable.' | CORRECT on the law; see §3(b). POSSIBLE (onus party): 'here Rocky' is right for the $10,000 promise, but the sentence ends (S45) 'both promises likely bind'. For Rocky's undertaking it is AMPL that alleges the contract, so AMPL bears the onus ([26]: 'it was for the appellant to demonstrate that there was such a contract'). Fix: 'here Rocky for the $10,000, AMPL for the undertaking' (+5), or 'the party alleging each promise' (+3 net). |
| S44 | Rogers CJ saw 'no relevant difference' between a 'practice to ensure'… and a promise 'to ensure' it [32] | Banque 525, Rogers CJ: 'The question whether the third paragraph… is promissory is **far more thorny**. However, in my view, if the paragraph is read as follows: “it is our practice to ensure that Spedley is at all times in a position to repay all loans…”, its promissory nature is much clearer. I see no relevant difference between that and saying that “we promise to ensure that” Spedley will at all times be in a position to repay'. | CORRECT. NOTE: the 'far more thorny' hedge and first-instance status are not stated. Low risk because the answer uses the words only to distinguish Rocky's plainer words. |
| S45 | Rocky's words were plainer and priced, so both promises likely bind | Application. | CORRECT (onus qualification at S43) |
| S46 | Loan Agreement fixes the payments Rocky must 'ensure', so not 'so obscure' as to be void [33] | Upper Hunter 437, Barwick CJ, quoting Scammell (Lord Wright): 'so obscure and so incapable of any definite or precise meaning that the court is unable to attribute to the parties any particular contractual intention'. The quoted source's pin 268 and the spelling 'G Scammell and Nephew Ltd' are verified in the readings: Meehan, Mason J at 587 (CB ch06 p 182) cites '(G Scammell and Nephew Ltd v Ouston [1941] AC 251 at 268)'. | CORRECT |
| S47 | 'I will do that' contains no words of effort: promised that Grace would pay | Application on Rocky's exact words. | CORRECT |
| S48 | AMPL's promise is not illusory, because once Grace repays it leaves AMPL 'no discretion' [34] | Meehan 582, Gibbs CJ: 'There is a concluded agreement as to the terms of the contract which, if the condition is satisfied, leaves no discretion in either party as to whether he shall carry them out.' | CORRECT. Mechanics: garden path ('once Grace repays it…' reads as 'repays it'). Add a comma after 'repays' (0 words). |
| S49 | $10,000 'to me directly' for consideration Rocky himself gave; promisee and no stranger to the consideration [35] | Trident 115 as in S26. Fact: '‘…to pay $10,000 to me directly…’'. | CORRECT |
| S50 | '[T]he clause' most naturally means the guarantee clause… | Fact: 'Pierre agreed and the clause was included'. | CORRECT |
| S51 | exposure turns next on whether the guarantee clause binds him | Framing. | CORRECT |
| S52 | A guarantee was 'provided by Rocky'… only 'the parties to it' are 'bound by the obligations of a contract' [36] | Trident, Brennan J **dissenting**, quoting Kitto J in Wilson v Darling Island at 80: 'the elementary general rule that the only persons entitled to the benefits or bound by the obligations of a contract are the parties to it'. Speaker and dissent are both disclosed. Fact: 'the personal guarantee provided by Rocky' (narrator). | CORRECT; POSSIBLE pin (see A36) |
| S53 | Silence while a clause is included is generally not acceptance [37] | Empirnall 534: 'the silent acceptance of an offer is generally insufficient to create any contract'. 'Generally' is kept. 'While a clause is included' folds the facts into the rule but does not alter it. | CORRECT |
| S54 | AMPL: Rocky 'attended' as the clause recording his bargain was included, taking the $10,000 promise knowing its terms [38], later invoked the Loan Agreement | Empirnall 535–6: 'taking the benefit of an offer with knowledge of its terms' (536); the ticket-case analogy at 535–6. Facts: 'attended a meeting'; 5 March letter 'under the Loan Agreement with AMPL'. | CORRECT |
| S55 | he has received nothing, and signature is no test for him either | Application of Empirnall and Coulls. | CORRECT |
| S56 | likely bound by his oral undertaking, and by the clause only if he saw its words | Conclusion with further information. | CORRECT |
| S57 | AMPL must show consideration moving from itself [39], which its $10,000 promise supplies if AMPL made it | Trident 115. | CORRECT |
| S58 | advance is past consideration [40], counting only if requested, understood to be remunerated, and enforceable if promised in advance; …unlike Pao On, return understood 'at the time of the main agreement' [41] | Roscorla 237, Lord Denman CJ for the Court: 'a consideration past and executed will support no other promise than such as would be implied by law'. Pao On 629, the Board (also the one-page extract): 'The act must have been done at the promisors' request: the parties must have understood that the act was to be remunerated…: and payment… must have been legally enforceable had it been promised in advance… The parties understood at the time of the main agreement that the restriction on selling must be compensated for…'. Both Pao On points are kept apart (629 versus 632), as the checklist requires. | CORRECT (45 words, at the limit) |
| S59 | AMPL signed after the clause's inclusion, arguably 'really done in consideration of' the guarantee [42] | AWM 456, the Court (Dixon CJ, Williams, Webb, Fullagar and Kitto JJ): 'that the act was really done in consideration of a potential promise inherent in the statement'. That is a promise-for-an-act analysis, and the position matches: AMPL's act, Rocky's promise. | CORRECT |
| S60 | premature depends on when the 12 months began | Fact: 'repayable at the expiry of 12 months'; '9 March 2025… AMPL called for payment'. | CORRECT |
| S61 | In NSW, post-contractual conduct… cannot construe the term [43]; if ambiguous, mutually known facts showing 'the genesis of the transaction' are admissible [44] | Brambles 164, Heydon JA: 'post-contractual conduct is not admissible on the question of what a contract means… they should be followed in New South Wales'. That is the source for 'In New South Wales'. Brambles 191, Ipp AJA (majority; Mason P agreeing): 'Where ambiguities exist, mutually known facts establishing… the genesis of the transaction… will be admissible'. Ipp AJA's own text, despite the block indent; it opens by completing his sentence with the Codelfa citation. 'Ipp AJA' is Mason P's form at 155; the casebook heading and reading guide say 'Ipp JA' (accepted under R-K). Register: 191 lies in RG 1B skip [3.330]–[3.360] (pp82–84), register only. | CORRECT |
| S62 | Naming no start, it is ambiguous | Application. | CORRECT (one clause, §6) |
| S63 | AMPL argues it ran from the 27 February advance, the agreement having 'recorded' a loan already made; but 'recorded' equally governs the 4% rate… | Fact: 'AMPL argued that the Loan was advanced on 27 February, and thus the 12 months had begun then.' The 'recorded' reasoning is the answer's construction of AMPL's case, not AMPL's stated words. The verb 'argues' is fair. | CORRECT |
| S64 | term arguably ran from 8 April 2024… unless the Loan Agreement says otherwise | Hedged conclusion with further information. | CORRECT |
| S65 | Interest shown paid only to 8 February 2025; if the March instalment went unpaid… | Fact: 'Between 8 April 2024 and 8 February 2025, Grace made appropriate monthly repayments of the interest'; 'Interest was to be paid by Grace monthly'. | CORRECT |
| S66 | payable 'once Grace repays the Loan', a condition precedent to that obligation, not to the contract [45] | Meehan 582, Gibbs CJ: 'It is clear that the condition in Special Condition 1(b) is not a condition precedent to contract. Certain obligations under the contract attached immediately'. | CORRECT |
| S67 | read commercially, his own payment satisfies it [46] | Upper Hunter 437, Barwick CJ: 'In the search for that intention, no narrow or pedantic approach is warranted, particularly in the case of commercial arrangements.' Said in construing to avoid uncertainty; used here for construction, which is fair. | CORRECT. Mechanics: 'read commercially' dangles, since grammatically it modifies 'his own payment'. 'On a commercial reading,' fixes it (+1). |
| S68 | AMPL does not breach the duty to co-operate, to 'do everything necessary on [its] part' [47] | Beaton 185, McHugh JA **dissenting** (the appeal was dismissed by Kirby P and Mahoney JA), citing Secured Income 607 (Mason J): 'The McDivitts have a contractual duty to do everything necessary on their part to enable the plaintiff to have the benefit of the contract'. 'Citing' is correct because the casebook gives McHugh JA's words, not Mason J's. 'Duty to co-operate' is the casebook heading. | CORRECT |
| S69 | if Rocky assented to the clause, liable for $1,150,000 once due and unpaid: now on a 27 February start; otherwise from 8 April 2025 | Arithmetic on the facts: 27 February 2025 is before the 9 March 2025 call. | CORRECT |
| S70 | If bound only orally, liable in damages, to AMPL or Pierre, for any payment Grace misses | Application. | CORRECT |
| S71 | paying likely forfeits the $10,000, payable only if Grace, who said he 'might not pay at all', repays | Fact: Grace, '…I might not pay at all!' The speaker is Grace. | CORRECT |

---

## 3. The three paraphrases you asked about

**(a) 'a promise can be the price of a promise' (S8, fn 4, Beaton 168, Kirby P).** CORRECT.
- Source: CB14_ch04 p 102. Kirby P: 'By that modern theory, consideration must be satisfied in the form of a price in return for the promisor's promise or a quid pro quo. The price can be in the form of an act, forbearance or promise.' He then quotes Pollock, 'is the price for which the promise of the other is bought'.
- The paraphrase is Kirby P's own sentence, not Pollock's quoted words, so attributing it to Kirby P without 'quoting' is right.
- Status: Kirby P found no consideration on the Beaton facts. Mahoney JA found a promise for an act. McHugh JA (dissenting) agreed with the bargain theory at 181–2 and himself quotes Pollock. The general proposition is uncontested across the bench, and the answer uses it only for the general proposition. No hedge is needed.

**(b) 'presumptions at most identify who bears the onus' (S43, fn 30, Ermogenous [26]).** CORRECT.
- Source: CB14_ch05 p 135, joint judgment of Gaudron, McHugh, Hayne and Callinan JJ (the paragraph number is confirmed by slide 3A, '26.'): 'For our part, we doubt the utility of using the language of presumptions in this context. At best, the use of that language does no more than invite attention to identifying the party who bears the onus of proof. In this case… it was for the appellant to demonstrate that there was such a contract.'
- 'At most' faithfully renders 'At best… no more than'. Compressing 'the use of that language… invite[s] attention to identifying' into 'presumptions… identify' is acceptable. The editors' introduction (CB p 133) also says 'Such presumptions determine who bears the onus of proof.'
- The one weakness is the application 'here Rocky' when both promises are in issue (S43 above).

**(c) Pao On third-party paraphrase, 'the exception for promises to third parties applies' (S41, fn 29, Pao On 632).** CORRECT in substance and in the lecturer's term; it should state the rule.
- Source: CB14_ch04 p 126, the Board (Lord Scarman delivering): 'Their Lordships do not doubt that a promise to perform, or the performance of, a pre-existing contractual obligation to a third party can be valid consideration.'
- Course framing: the casebook heading at [4.145] is 'Duty owed to a third party' ('consideration may be found in A's promise to B to perform a duty which A is already contractually obliged to perform for C'). Slide 2B lists '3 exceptions to the rule: … **promises to third parties (Pao On v Lau Yiu Long – class 2A)**'. The label is the lecturer's own, so it is not a proxy.
- Application check: on the hypothesis that Pierre personally promised and that the guarantee clause already bound Rocky to AMPL, Rocky (A) promises Pierre (B) to perform a duty already owed to AMPL (C). That is exactly the Pao On and [4.145] pattern, and the answer applies it correctly.
- Weakness: the label alone could be misread as 'a promise made to a third party', and it states no rule in the source's words (R1, R-AB). Recommended text: '…and if Pierre promised, ‘a promise to perform… a pre-existing contractual obligation to a third party’, AMPL, ‘can be valid consideration’.' Cost about +12 words net, if you replace 'the exception for promises to third parties applies' (−8) with the quoted words (+20). Fund it from the voice cuts in §6 or the S30 rewording. Optional.

---

## 4. Facts against the problem's exact words

All 30 quoted fact spans are found verbatim (verify.py). The points needing care:

| Fact use | Problem words and speaker | Verdict |
|---|---|---|
| 'project developers' (S10) | Narrator: 'Mr Grace and Mr Rocky are both project developers' | Correct, used as narrated status |
| 'asked Rocky to make an offer' (S2) | Narrator: Grace 'proposed that Rocky offer Grace a ‘$1 million dollar working capital loan for 2 years at 5% interest’' | Fair paraphrase |
| 'which Rocky declined' (S2) | 'Rocky told Grace he was not interested in offering Grace a long-term loan but proposed that they meet' | Fair |
| 'Potential', 'wait and see', 'I will lend', 'this morning', 'confirm agreement', 'subject to success of Hail Mary Project' | Rocky's email | Exact |
| 'Confirmed' (S7) | Grace: 'Mr Rocky, Confirmed. Best, Grace.' | Exact |
| 'subject to satisfactory conditions' | Rocky's email | **Never quoted whole (C3)** |
| 'asked' (S23, S40, S58) | Narrator: 'Rocky asked A-Maize Pty Ltd' | Exact |
| 'agreed to provide the money' (S25) | Narrator | Exact |
| 'expected' (S32) | Narrator: 'Pierre expressed during the meeting that he expected…' | **Narrator's word presented as Pierre's (POSSIBLE, Z2)** |
| 'all payments', 'promptly' (S41) | Narrator, reporting Pierre's expression | Correct (no speaker claimed) |
| 'I will do that if you also promise', 'to me directly', 'once Grace repays the Loan', 'you', 'also' | Rocky | Exact |
| 'agreed' (S33, S40) | Narrator: 'Pierre agreed and the clause was included… before it was signed by Grace and AMPL' | Exact |
| 'repayment of the Loan', 'provided by Rocky', 'recorded', 'attended' | Narrator | Exact |
| 'I never signed anything with you' (S28) | Grace to Rocky, 7 March | Exact |
| 'I have until 8 April 2025' (S61), 'might not pay at all' (S71) | Grace to AMPL | Exact; correct speaker |
| AMPL's 27 February argument (S63) | Narrator: 'AMPL argued that the Loan was advanced on 27 February, and thus the 12 months had begun then' | Correct; the 'recorded' gloss is the answer's construction |
| 'if the Project made a profit… none yet shown' (S30) | Narrator: '…realised that the profit from the Project would be minimal' | **POSSIBLE: planted 'minimal' omitted** |
| 'Grace never promised to reimburse' (S30) | Problem silent | **Derived fact stated as fact; write 'nothing shows'** |
| Interest 'to 8 February 2025' (S65) | Narrator | Exact |

---

## 5. Terminology

| Answer's term | Course source (quoted) | Verdict |
|---|---|---|
| invitation to treat | S1A: 'Invitation to treat: An invitation for others to make an offer or enter into a negotiation.' | Course term |
| external manifestation of assent | Empirnall 534 | Source's words |
| counter-offer | S1B: 'What is the legal effect of a counter-offer?' | Course term |
| consideration; 'price' | Beaton 168; S2A 'core elements of consideration' | Course term |
| preliminary agreement | S3A: 'What are preliminary agreements?' | Course term |
| intention to create legal relations (in full) | S3A; brief | Course term, never abbreviated |
| first class / third class | Masters 360–1 ('three classes'); S3A says 'Category 1… Category 3' | Both are course words; the answer uses the judgment's own term. NOTE: S3A's 'category' would match the slides exactly. |
| illusory | Casebook heading 'ILLUSORY PROMISES'; Pace 151 'illusory' | Course term |
| subsidiary matters / all essential terms | Godecke 647 | Source's words |
| bilateral contract | S1A 'Bilateral contract – contract is made by exchange of promises' | Course term |
| as agent; privity; stranger to the consideration; joint promisee | Trident 115, 145; S4A 'Privity'; casebook [11.30] 'joint promisee doctrine' | Course terms |
| existing legal duty rule | S2B 'Existing Legal Duty Rule'; casebook heading | Course term |
| exception for promises to third parties | S2B '3 exceptions to the rule… promises to third parties (Pao On…)'; casebook [4.145] 'Duty owed to a third party' | Course term (S2B). Rule not stated (§3(c)). |
| letter of comfort | S3A | Course term |
| certainty; 'so obscure' | S3B; Upper Hunter 437 | Course term |
| past consideration | S2A 'Past consideration'; casebook [4.85] | Course term |
| post-contractual conduct; genesis of the transaction | Brambles 164, 191. S1B uses 'post-formation conduct'. | Source's words; acceptable |
| condition precedent | Meehan 582 (casebook) | Source's words; no slide uses the term (rulings sheet notes this) |
| duty to co-operate | Beaton heading 'The duty to co-operate' | Source's words |
| **qualifier** | None; it is the answer's own label | **Invented label without a visible antecedent (C3)** |
| 'the first point' (email's first bullet) | Answer's own shorthand | Acceptable; refers to the visible bullet |

No proxy doctrine names otherwise. No doctrine is applied without being named in course words, except 'qualifier' (C3).

---

## 6. AGLC 4, footnote by footnote

| fn | Check | Verdict |
|---|---|---|
| 1 | Full citation; '(Lord Diplock)'; short title after the judge | CORRECT |
| 2 | 'Ibid.' (same source and pin, 298) | CORRECT |
| 3 | Empirnall full; 534; short title | CORRECT |
| 4 | Beaton 168 (Kirby P); short title | CORRECT |
| 5 | Ermogenous (2002) 209 CLR 95, [25]–[26]; paragraph pins in brackets, en dash | CORRECT. NOTE: the casebook prints CLR page markers (105–6) and slide 3A confirms [26]. Paragraph pins are acceptable. |
| 6 | Masters 363; short title placed before ', quoting'; Winn v Bull 32 (Jessel MR) | CORRECT |
| 7, 8 | Masters (n 6) 360; Ibid 361 | CORRECT |
| 9 | Meehan 580–1 (Gibbs CJ) | CORRECT |
| 10 | Brambles 164 (Heydon JA) | CORRECT. NOTE: no medium neutral citation ([2001] NSWCA 61), and none for Ermogenous ([2002] HCA 8). The casebook prints both. Not proved an AGLC error; consistent across the answer. |
| 11 | Meehan (n 9) 582 | CORRECT |
| **12** | Pace 150 | **C1: pin 151.** Name not italicised in the docx (**C2**). |
| 13, 14 | Meehan (n 9) 581 (Gibbs CJ), 589 (Mason J); Ibid 581–2 | CORRECT |
| 15 | Godecke 646–7 (Gibbs J) | CORRECT (647 alone is more exact; 646–7 is not wrong) |
| 16, 17 | Trident 145 (Deane J); Ibid 115 (Mason CJ and Wilson J) | CORRECT |
| 18, 19 | Coulls 487; Ibid 486; '&' as printed in the casebook | CORRECT |
| 20, 21, 22 | Empirnall (n 3) 535–6; Coulls (n 18) 487; Gibson (n 1) 298 | CORRECT |
| **23** | Brambles 177 (Heydon JA), quoting ICS 11,117 (McHugh JA) | POSSIBLE (A23). Heydon JA introduces the quote 'at 11,117–18'. The quoted 'bilateral' sentence's page within that range is not shown, and the casebook pins a different ICS passage 'at 11,117'. Settle against 5 BPR, or pin '11,117–18' (0 words). |
| 24, 25, 26 | Empirnall 534; Masters 361–2; Trident 145 | CORRECT |
| 27 | Sundell 327, no judge | CORRECT. NOTE: the body uses the short form 'Sundell' (S39), but the footnote defines no short title ('Sundell'). Add it (0 body words). |
| 28 | Wigan (1973) 47 ALJR 586, 594 (Mason J) | CORRECT (S2B prints the parallel 1 ALR 497, 512; the casebook's ALJR report is fine) |
| 29 | Pao On 632 (Lord Scarman for the Board); short title | CORRECT (R-P form) |
| 30 | Ermogenous (n 5) [26] | CORRECT |
| 31, 32 | Banque 523; Ibid 525 (Rogers CJ) | CORRECT |
| 33 | Upper Hunter 437 (Barwick CJ) ('Upper Hunter'), quoting G Scammell and Nephew Ltd v Ouston [1941] AC 251, 268 (Lord Wright) | CORRECT (268 and 'and' verified at Meehan 587, CB p 182) |
| 34, 35 | Meehan (n 9) 582; Trident (n 16) 115 | CORRECT |
| **36** | Ibid 129 (Brennan J dissenting), quoting Wilson v Darling Island 80 (Kitto J) | Form CORRECT. POSSIBLE pin (A36): the Kitto J quotation follows an editorial ellipsis after the [129] marker and comes before [131]; [130] is not printed. It may be 130. Settle against 165 CLR 129–30. |
| 37, 38, 39 | Empirnall 534; Ibid 535–6; Trident (n 16) 115 | CORRECT |
| 40 | Roscorla (1842) 3 QB 234, 237; 114 ER 496 (Lord Denman CJ) | CORRECT. NOTE: no ER pin for the parallel report (not printed in the readings). |
| 41 | Pao On (n 29) 629 | CORRECT |
| 42 | AWM 456 (whole bench named) | CORRECT (the casebook's '(Privy Council)' tag on 92 CLR is an editors' slip; the judgment is THE COURT of the High Court) |
| 43, 44 | Brambles (n 10) 164; Ibid 191 (Ipp AJA) | CORRECT |
| 45, 46 | Meehan (n 9) 582; Upper Hunter (n 33) 437 | CORRECT |
| 47 | Beaton (n 4) 185 (McHugh JA dissenting), citing Secured Income 607 (Mason J) | CORRECT ('citing', not 'quoting', is right) |

Across all footnotes:
- Every footnote ends with a full stop.
- Ibid is used only where the previous footnote is the same source.
- Pins follow a comma with no 'at'.
- Ranges use en dashes.
- 'Dissenting' appears where it applies (fn 36, fn 47).
- No discursive footnotes.

---

## 7. Voice and mechanics

- Sentences over 45 words: none. S58 is exactly 45.
- Dashes, double quotation marks, contractions: none in the body (checked by script).
- One-clause sentences, which Yusuf 'despises' (R8):
  - S6 'Acceptance requires an external manifestation of assent.'
  - S29 'Thus Rocky has no present claim against Grace.'
  - S35 'A contract likely formed orally, binding both promises.' (a participle tag only)
  - S62 'Naming no start, it is ambiguous.'
  - Merge S6 into S7 with a colon (0 words). Fold S62 into S61 ('…are admissible; naming no start, the term is'). Merge S35 into S34. Recast S29 (next point).
- Conclusion-first paragraph opener (R6): S29 'Thus Rocky has no present claim against Grace.' opens the paragraph before its reasons. Put it last: '…and nothing shows Grace promised to reimburse what he pays AMPL, so Rocky has no present claim against Grace.' (about 0 net).
- Ambiguity and garden path: S48 'once Grace repays it leaves AMPL' needs a comma after 'repays' (0 words).
- Dangling modifier: S67 'read commercially, his own payment satisfies it' should be 'on a commercial reading' (+1).
- Elliptical but grammatical: S59 'arguably ‘really done in consideration of’ the guarantee' reads as a fragment; 'its signing arguably ‘really done…’' fixes it (+2). Optional.
- Fragments after semicolons: none found. Each clause after a semicolon has its own subject and verb.
- Meta language: none beyond the issue framing, which is accepted.
- Invented abbreviations: none. 'AMPL' and 'Loan Agreement' come from the problem.

---

## 8. Built document check

- **Text fidelity.** I extracted document.xml and footnotes.xml and diffed them against ANSWER.md. The body is identical and all 47 footnotes are identical. Internal footnote ids 20 to 66 render as 1 to 47, so the '(n 6)' style cross-references resolve correctly.
- **Italics.** Every case name in the body and footnotes is italic except 'Biotechnology Australia Pty Ltd v Pace' in fn 12 (C2). The body short forms are italic: Masters, Meehan, Empirnall, Sundell, Pao On. 'Mrs Coulls' is correctly roman. Short titles inside ('…') are italic. 'Ibid' is roman, which is correct.
- **Format.**
  - Headings 'I. ROCKY v GRACE' and 'II. ROCKY v AMPL (ALTERNATIVELY PIERRE)' are bold.
  - Times New Roman 12 pt body, double spaced (line 480).
  - Footnotes 10 pt, single spaced.
  - The footer carries a PAGE field. No comments in comments.xml (0). No title page or cover sheet. Empty author metadata.
- **Word count.** The 'Word count: 1,600' line is present.
- **Page size.** sectPr has no pgSz or pgMar, so Word applies its default page size and 1-inch margins. NOTE: confirm A4 on opening. This is not a fidelity defect.
- **Disclosure.** Instructionsss.txt sets 'no more than 1,500 words'. The 1,600 stated follows Yusuf's own instruction. The statement is accurate, but it is 100 over the official cap, so the official penalty regime applies.

---

## 9. Register (no deduction)

- Brambles 164 (fn 10, fn 43) is in RG 1B 'Skip [3.290] – [3.300] (pp73-76)'.
- Brambles 191 (fn 44) is in RG 1B 'Skip [3.330]-[3.360] (the first part of Ipp JA's judgment; pp82-84)'.
- Under R-F these are register only, never required or deducted. Both statements are adopted or majority law.

---

## 10. Changes ranked by value per word

1. **C1** fn 12 pin 150 to 151. 0 words.
2. **C2** add Pace to build.py CASES; rebuild. 0 words.
3. **C3** S7 'qualifier included' becomes '‘subject to satisfactory conditions’ included'. +3, funded by cutting 'merely' (S3), 'just' (S50) and 'already' (S65).
4. S48 add a comma after 'repays'. 0.
5. S32 'Pierre's ‘expected’' becomes 'Pierre's expressed expectation' (narrator's word). 0.
6. S43 onus: 'here Rocky for the $10,000, AMPL for the undertaking'. +5.
7. S30 'a ‘minimal’ profit was expected but none is shown made'; 'nothing shows Grace promised'. About +6.
8. S29 moved to the end of its paragraph; merge S6 into S7, S35 into S34 and S62 into S61. About 0.
9. fn 23 pin '11,117–18'; fn 27 add ('Sundell'). 0 body words.
10. S41 quote Pao On 632's rule in place of the bare label. About +12; fund only if words free up.

Items 4 to 10 are optional. Items 6, 7 and 10 together cost about 23 words, which would need cuts elsewhere to stay at 1,600.
