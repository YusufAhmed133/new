# R5 · M5 · Opposing counsel and authenticity critic: ANSWER.md v4

Target: /home/user/new/work/ANSWER.md (v4). Body 1,596, stated 1,599, against a cap of 1,600 including the 3-word count line, so at most 1 word is spare. Every addition below names an exact cut of equal or greater length. I checked the arithmetic by applying the full package to a scratch copy and running stats.py: body 1,597, stated 1,600.

## Read for this report
- MARKERS_PROMPT.md: the common protocol and ROLE 5.
- YUSUF_INSTRUCTIONS_VERBATIM.md.
- The problem (ACTUAL TASKKK.txt), Instructionsss.txt and ReadingGuide.txt.
- RUBRIC_RULINGS_SHEET_v12 section 6.1 (R-P to R-AE).
- Slides 2A, 2B, 3A, 3B and 4A in full, and 1B. Slide 1A was not read.
- CB14 ch05 and ch06 in full. Ch04 [4.05] to [4.175] in full. Ch11, all of Coulls, the editors' notes, Trident (Mason CJ and Wilson J) and the Deane J and Brennan J passages relied on. Ch03 Gibson 296–9, Empirnall in full, and Brambles 155–7 and 161–4, 176–8 and 184–96.
- Part A of his LAWS1061 answer, for voice.
- The output of verify.py.

As instructed, I read no earlier reports. That covers every R2/R3/R4, MARK and CAL file, and the marker feedback on the previous version. I did not open submission.txt either. Casebook pages below are CB14 printed pages. Report pins are the bracketed page markers in the judgments.

---

## 1. Certain defects (proved from the text)

**D1. Internal contradiction in the consideration paragraph (para "On consideration…").**
- The answer says: "However, the rule applies 'at least when' the promise is made to the promisee under an existing contract, and none existed: … the clause, arguably included after Pierre 'agreed', bound no one before signing … Rocky likely gave consideration unless the clause preceded the bargain."
- Source: Wigan v Edwards 47 ALJR 586, 594 (Mason J; Walsh and Gibbs JJ agreeing on this point), CB p 129: "The general rule is that a promise to perform an existing duty is no consideration, at least when the promise is made by a party to a pre-existing contract, when it is made to the promisee under that contract…".
- Fact (narrator): "the clause was included in the Loan Agreement before it was signed by Grace and AMPL."
- On the answer's own reasoning, the rule needs an existing duty. A clause that "bound no one before signing" creates none, whenever it was drafted. Signing followed Pierre's agreement. The "unless" therefore contradicts the sentence before it.
- Fix: cut "unless the clause preceded the bargain" (−6).

**D2. Garbled clause in the intention paragraph.**
- The answer says: "Rocky would invoke the third class, where parties 'have dealt only with major matters'; though no formal document was contemplated, so did the email."
- "so did the email" has no verb it can take back, so the reader cannot work out that it means the email also dealt only with major matters.
- Fix: replace with "the email, though contemplating no formal document, did likewise." (−1).

**D3. The exposure paragraph does not match the answer's own findings, which R-AD(1) forbids.**
- The consideration-for-the-guarantee paragraph finds that the clause has consideration only "if AMPL made" the $10,000 promise, and otherwise "may lack consideration". The exposure paragraph then says: "if Rocky assented to the clause, he is liable for $1,150,000". That drops the consideration condition.
- The guarantee-clause paragraph concludes: "He is likely bound by his oral undertaking". The exposure paragraph then treats oral liability as an alternative: "If bound only orally, he is liable in damages…". On the answer's own findings, the oral undertaking binds in any event. It covers "all payments", including any unpaid March instalment, which the clause ("repayment of the Loan") does not.
- Fix: "if Rocky assented to the clause and AMPL promised the $10,000, he is liable…" (+5), and "By his oral undertaking he is also liable in damages, to AMPL or Pierre, for any payment Grace misses." (+1).

**D4. Footnote 25 (Deane J) does not contain the words paraphrased into it.** Words certain; whether the paraphrase may rest on this footnote is contestable.
- The answer says: "Pierre bound AMPL if, with its consent, he contracted 'as agent' for it rather than solely for himself.[^25]" Footnote 25 is Trident 145 (Deane J).
- What Deane J says at 145 (CB p 355): "If the promisee contracts as agent for a disclosed or undisclosed principal, the principal will ordinarily himself be, for the purposes of the requirement of privity, a party to the contract."
- The consent element and "not solely on his or her own behalf" come from the editors at [11.32] (CB pp 332–3): "the principal expressly or impliedly consented to the agent acting on his or her behalf … the agent was purporting to act on behalf of the principal and not solely on his or her own behalf."
- Deane J also speaks of the *promisee* as agent. That fits Part I (AMPL as promisee-agent for Rocky) and AMPL's claim to the benefit of Rocky's undertaking. It does not, in terms, fit the *burden* of the $10,000, where Pierre is the promisor.
- R-Y(2) prefers Deane J for the burden aspect, so I do not demand a change of source. The reviser should know that the consent words are the editors', not Deane J's. One answer is to keep the paraphrase and accept the risk. The other is to drop "with its consent" and "rather than solely for himself", which costs the test its elements.

---

## 2. Every conclusion attacked

Status key: **MET** (the answer meets the counter), **PARTLY** (it does so thinly), **UNMET**.

### Part I. Rocky v Grace

| Conclusion | Strongest counter, with source (verbatim, pin, speaker) | Status / fix |
|---|---|---|
| The 5 February call was an invitation to treat | No real counter. Grace "proposed that Rocky offer", and Rocky declined a "long-term loan". | MET. Uncontested; one sentence is right under R-AB(2). |
| The email's first point was likely an offer | **Rocky:** the email is "Confirming discussions", and its other points ("Potential", "wait and see") promise nothing. **Grace:** that contrast helps her, because Rocky could write non-committal points and chose "I will lend" with amount, date, term and rate. Gibson 298 (Lord Diplock, CB p 42): "may be prepared to sell" is "fatal" to an offer. "I will lend" is the opposite. | MET. The answer puts both sides. Optional clarity rewrite at 0 words: "Rocky could say his 12 February email, 'Confirming discussions', promised nothing, like its 'Potential' and 'wait and see' points." |
| "Confirmed" accepted the point, qualifier included | **Rocky:** "Confirmed" vouches for accuracy, not agreement. **Answer:** it answered "Please confirm agreement". Empirnall 534 (McHugh JA, CB p 71) requires "an external manifestation of assent". | MET. |
| Grace's implied promise to repay is consideration | Beaton 168 (Kirby P, CB p 102): "The price can be in the form of an act, forbearance or promise." | MET. |
| Intention: the onus | **Grace:** BBL 141–2 (Rogers CJ, at first instance, quoting Megaw J in Edwards v Skyways, CB pp 141–2) says the onus "rests with the party 'who asserts that no legal effect is intended, and the onus is a heavy one'". On that view Rocky, who denies intention, would carry a heavy onus. **Reply:** Ermogenous 106 (Gaudron, McHugh, Hayne and Callinan JJ, CB p 135) says presumptions at best "invite attention to identifying the party who bears the onus of proof". Grace, who would allege the contract, must show it. | PARTLY. The answer states the High Court position ("the alleging party bearing the onus") but does not confront Skyways. That is acceptable because the High Court prevails. No change. |
| Is the email a "preliminary agreement" at all, and do the Masters classes apply? | **Grace:** Masters 360 (the Court, CB p 153) classifies cases where the parties "also agree that the matter of their negotiation shall be dealt with by a formal contract". No formal contract was contemplated, so the classes do not apply. On that view the email is a concluded loan subject to a condition (Meehan). **Reply:** the editors at [5.05] (CB p 133) define the preliminary-agreement question as whether parties "intend to be bound immediately, or not until … they have finalised some outstanding issues *or* recorded their agreement in a more formal manner". The email's "conditions" are outstanding issues. Winn v Bull, quoted in Masters 363 (CB p 154), states the construction question for agreements not expressly made subject to a formal contract, and the answer uses it. | MET in substance. D2 garbles the bridging clause; fix as above. |
| Masters' fourth category, and lending "by 15 February" | **Grace's best unused argument.** The editors' note [5.105] (CB p 155), quoting McLelland J (at first instance) in Baulkham Hills, describes a fourth class: parties "content to be bound immediately and exclusively by the terms which they had agreed upon whilst expecting to make a further contract … containing, by consent, additional terms". Slide 3A names it. Grace adds that lending "by 15 February", three days later, left no time for a new agreement. **Reply:** "subject to" carries its natural sense of an overriding condition (Masters 362–3), and "satisfactory" to Rocky is not "by consent". | **UNMET.** It cannot be funded without losing an argument (cost 33 words). Second-ranked unfunded item (section 5). |
| The conditions are further loan terms left to Rocky, so Meehan is distinguishable | **Grace:** Meehan 581 (Gibbs CJ, CB p 181): the Placer principle "does not apply where the discretion … relates, not to the performance of the contractual obligations themselves, but only to the fulfilment of a condition". "Subject to satisfactory conditions" reads like "subject to … finance on satisfactory terms", which bound in Meehan, with honest judgment implied (Gibbs CJ 581; Mason J 588–9, CB pp 182–3). **Reply (in the answer):** the email's own contrast, "unlike 'subject to success of Hail Mary Project', name no external event", so the conditions are terms, not events. | MET. This is the strongest reasoning in the answer. |
| Grace's McHugh JA "honestly/reasonably" reply fails | **Rocky's better rebuttal, unused:** McHugh JA's inference at Pace 151 (CB p 164) is confined to "a commercial or employment agreement under which the promisee provides services" and "a firm promise to pay or remunerate the promisee in return for his services". Grace provided no services before the conditions. Kirby P at Pace 135 (CB p 161), with the majority on the result: "the court will not accept for itself a discretion which the parties have, by their agreement, reserved to one or other of them." | PARTLY. The answer's "which neither standard can supply and no range confines" gives the point but not its source. Unfunded (section 5). |
| Godecke and Gibbs J's "Perhaps" | **Grace:** Gibbs J 646–7 (CB p 187): "Perhaps it may be different where agreement has been reached on all essential terms but the determination of subsidiary matters has been left to one of the parties." The amount, date, term and rate (the essentials, "price" in his words) are fixed, and the conditions are subsidiary. Gibbs J also says "there can be no concluded bargain if a vital matter (such as price or rental) has been left" to one party, and price is not left here. **Reply (in the answer):** Gibbs J then rejects Bray CJ's view that Sweet & Maxwell would have stood without "reasonably", because that court "placed considerable reliance on the fact that the parties had imported the familiar and objective standard of reasonableness". He also left the matter open: "it is unnecessary to express any concluded opinion" (647–8). | MET, and the hedge is kept ("obiter", "[p]erhaps"). The sentence is a four-fragment quote-mosaic (section 4). It cannot be compressed without blurring that the Walsh J majority and Gibbs J reasoned differently, so leave it. |
| The email bound neither party | **Rocky's strongest unused support:** Brambles 164 (Heydon JA, CB p 73; Ipp AJA agreeing "for the reasons set out by Heydon JA" on that contract, 184): "post-contractual conduct is admissible on the question of whether a contract was formed". Planted facts: Rocky instead "asked" AMPL, and Grace contracted with AMPL at 4% for 12 months. Todd v Nicol (Mayo J, CB p 145) says the same for intention. | **UNMET.** Top-ranked unfunded item (section 5). |
| AMPL's advance did not perform Rocky's promise; no agency | **Rocky:** Deane J 145 (CB p 355): if the promisee contracts "as agent for a disclosed or undisclosed principal", the principal is a party. **Reply (in the answer):** Pierre "agreed to provide the money", and AMPL named Rocky guarantor, "which no lender acting for him would need". | MET. Good reasoning from the facts. |
| Privity defeats Rocky's 5 March demand | **Rocky:** Trident's plurality relaxed privity. Mason CJ and Wilson J at 115 (CB p 343) say only that "This court has *hitherto* accepted that a third party cannot sue upon a contract". At 123 (CB p 348) the question they decided was "whether the old rules apply to a policy of insurance", and they held McNiece "entitled to succeed" (124). Rocky arguably benefits from Grace's repayment, which discharges his guarantee and triggers his $10,000. | PARTLY. The quote drops "hitherto" and the plurality's departure. Fix at +2: "faces privity: outside insurance, 'a third party cannot sue upon a contract'". Fund it by dropping "12 February" from the X6 rewrite (−2). That is lossless, because para 3 still dates the email by context ("the February dealings", "this morning"). |
| "I never signed anything with you" is right in result, wrong in reason | Empirnall 535–6 (bound unsigned); Coulls 487 (Taylor and Owen JJ, CB p 327): "the mere fact that her signature appears does not make her a party". | MET. Excellent use. |
| Rocky has "no present claim" against Grace; Development Agreement profit "none yet shown" | **Rocky:** the narrator says Rocky and Grace realised "the profit from the Project would be minimal" and that Grace was unlikely to profit "due to the terms of their Development Agreement". A profit was expected, and the clause repays Rocky "in priority". That is his one real contractual claim against Grace, and the question asks for "any contractual claims he could make". | PARTLY. Fix at −2: "Thus Rocky's only claim against Grace lies under the Development Agreement, repaying him first 'if the Project made a profit', expected though 'minimal'. Grace never promised to reimburse what he pays AMPL." |

### Part II. Rocky v AMPL, alternatively Pierre

| Conclusion | Strongest counter, with source | Status / fix |
|---|---|---|
| Pierre's expectation was an invitation to treat; Rocky offered; Pierre accepted | Uncontested. | MET. |
| A contract formed orally before signing | **AMPL:** the parties meant the written Loan Agreement to be the record, so nothing bound before it. Masters 362 (CB p 154): "depends upon the intention disclosed by the language". **Answer:** "Rocky reserved no right to withdraw pending a document signed only by Grace and AMPL". | MET. Footnote 24's "361–2" should be 362: the sentence follows the [362] marker. That pin is for Role 3. |
| Pierre acted for AMPL, so AMPL owes the $10,000 | **AMPL:** "you" means Pierre, AMPL's Loan Agreement records no $10,000, and the promise is Pierre's own. **Rocky's unused point:** AMPL called on "the personal guarantee provided by Rocky" (9 March). It adopts the bargain's benefit, and the editors at [11.32] note that agency can be "ratification … adoption or confirmation". AMPL cannot take Rocky's undertaking through Pierre and disown its price. | PARTLY. Fix at +6: "…and spoke at its office about its loan, and AMPL later invoked Rocky's guarantee, so he likely acted for AMPL." |
| The existing legal duty rule does not apply | **AMPL:** "also" presupposes an existing guarantee. Sundell 327 (court, in the editors' note, CB p 111). **Answer:** Wigan 594 (no existing contract), "all payments promptly" goes beyond the guarantee, and the third-party exception applies (Pao On 632, Lord Scarman for the Board, CB p 126: "a promise to perform, or the performance of, a pre-existing contractual obligation to a third party can be valid consideration"). | MET, apart from D1. On practical benefit (Musumeci 747, Santow J, CB p 121): element (i) needs a contract "to do work for, or to supply goods or services to, B in return for the payment". A guarantee is neither, so the exception is rightly not run. |
| Intention: cousin, onus on Rocky, "appropriately promissory" | **Pierre:** family, so a presumption against intention. **Answer:** Ermogenous 106, and BBL 523 (Rogers CJ, CB p 142). | MET. |
| Not a mere letter of comfort | **Rocky's own escape route:** "ensure" in a comfort letter. BBL 525 (Rogers CJ, CB p 144): "I see no relevant difference between that and saying that 'we promise to ensure that' Spedley will … be in a position to repay". | MET. It is good that the answer gives Rocky bad news here (R9). |
| "I will do that" promised a result, not effort | **Rocky:** his "check in consistently … via email" conduct shows the parties understood a monitoring role. **Reply:** Brambles 164 (Heydon JA, CB p 73): "post-contractual conduct is not admissible on the question of what a contract means". | **UNMET.** A planted fact goes unused, contrary to R-AD(2). Fix at +7: "His 'I will do that' contains no words of effort, and 'check in' emails cannot construe it:[^Brambles (n 22) 164 (Heydon JA)] it likely promised…". |
| AMPL's promise is not illusory | Meehan 582 (Gibbs CJ, CB p 181): "leaves no discretion". | MET. |
| Privity: Rocky is the promisee of the $10,000; "the clause" is ambiguous | **AMPL:** if "the clause" is the $10,000 term, it sits in a written instrument between AMPL and Grace. Coulls 487: party status turns on "the written instrument itself". **Answer:** "either way, Rocky relies on the oral promise", which formed before signing (para 17). | PARTLY, but correct. The link to para 17 is implicit. No funded fix. |
| The guarantee clause binds Rocky only if he saw its words | **AMPL:** Empirnall 535–6: an offeree "knowing of the terms … has exercised a choice and taken the benefit". Rocky "attended", bargained, and later demanded "under the Loan Agreement". **Rocky's stronger authority, unused:** Brambles 195 (Ipp AJA, Mason P agreeing on disposition, CB p 85), quoting Lord Hatherley in Brogden 686: conduct accepts only if "of such a character as necessarily to lead to the inference … that the agreement had been accepted". This is the majority's test, and it is stricter than Empirnall's "open to the tribunal of fact". In Brambles, Brambles charged the very fees the offer stipulated. Rocky's attendance performs nothing in the clause. The answer's "nothing shows 'a reasonable opportunity to reject'" is weak, because Rocky was in the room. | PARTLY. Fix at +2: "However, conduct accepts only if it 'necessarily' implies assent,[^Brambles (n 22) 195 (Ipp AJA), quoting Brogden v Metropolitan Railway Co (1877) 2 App Cas 666, 686 (Lord Hatherley)] and the benefit he took, AMPL's promise, priced his own words, not the clause." |
| Consideration for the guarantee: past consideration and Pao On | **AMPL:** Pao On 630 (CB p 125): whether a requested act "raises an implication of promised remuneration or other return is simply one of the construction of the words of the contract in the circumstances of its making". A lender advancing $1,150,000 to a stranger at Rocky's request expects security. **Answer:** "unlike Pao On, where a return was understood 'at the time of the main agreement', nothing shows a guarantee was then contemplated". | MET. Pao On's three conditions are kept apart from its 632 holding, as the checklist requires. |
| The 12 months ran from 8 April, so the call was premature | **AMPL:** Brambles 191 (Ipp AJA, CB p 82): where there is ambiguity, "the shared beliefs of the parties as to their respective rights as they existed immediately before the contract" are admissible, and everyone knew Grace had held AMPL's money since 27 February. "Recorded" describes an existing loan. **Answer:** "'recorded' equally governs the 4% rate, which nothing shows predated 8 April". **Rocky's contestable extra:** the narrator calls Grace's payments from 8 April "appropriate". That is a stipulated fact, not post-contractual conduct, and arguably fixes the cycle at 8 April. | MET. The "appropriate" point is contestable: the word may describe only the amount. Not funded. |
| The March instalment | **AMPL:** Grace's "you won't see a cent before then" (7 March) arguably shows the 8 March instalment went unpaid, so the oral undertaking is broken now on either start date. | PARTLY. The answer says "if the March instalment went unpaid". The D3 fix carries the consequence into the exposure paragraph. Quoting the 7 March words would cost +7 and is not funded. |
| "Once Grace repays" is a condition precedent to that obligation | **Rocky:** Upper Hunter 437 (Barwick CJ, CB p 159): "no narrow or pedantic approach … commercial arrangements", so his own payment repays the Loan. **Answer:** "the words name Grace, and the $10,000 priced his promise that Grace would pay." | MET. |
| No breach of the duty to co-operate | **Rocky:** AMPL's pressure ("contacted Grace directly") provoked "I might not pay at all", which hinders fulfilment of the condition. Beaton 185 (McHugh JA, dissenting in the result, CB p 107): "do everything necessary on their part to enable the plaintiff to have the benefit of the contract". **Answer:** "its call does not stop Grace repaying." | MET. The duty is to do what is necessary, not to forgo lawful demands. |
| Exposure | See D3. **Unfunded refinement:** if Pierre alone was promisee, Rocky's undertaking runs to Pierre for AMPL's benefit. Trident 118 (Mason CJ and Wilson J, CB p 345): "ordinarily the promisee is entitled to nominal damages only because non-performance by the promisor … causes no damage to the promisee". At 119 they accept Windeyer J that more is recoverable on proof of the promisee's own loss. | D3 fix needed. Nominal damages are unfunded (section 5). |

### Consistency between Parts I and II
- Agency: the same test is applied both ways. Part I says AMPL was not Rocky's agent; Part II says Pierre was AMPL's agent. This is consistent, subject to D4.
- Intention: Part I decides intention under Masters and never applies Rogers CJ's "appropriately promissory" test, though it calls "I will lend" "promissory". Part II applies Rogers CJ. Grace would say the answer uses BBL only where it helps. The answers differ because "subject to satisfactory conditions" is, in Rogers CJ's words, an indication that the parties were not yet bound. The answer never says so; it is a small asymmetry and is not funded.
- Exposure: as drafted, it contradicts the consideration-for-the-guarantee paragraph and the guarantee-clause paragraph (D3).

---

## 3. The specific tests

- **Whose onus.** Correct in both Parts (Grace in Part I, Rocky in Part II). Skyways is not confronted, which is acceptable under Ermogenous.
- **The email's other bullet points and "Confirming discussions".** Used for Rocky, and against him through the "Hail Mary" contrast. Grace's inference from the contrast is implicit.
- **The Masters categories and whether the email is a preliminary agreement at all.** Handled through Winn v Bull, but the bridging sentence is garbled (D2). The fourth category is UNMET.
- **Godecke and Gibbs J's "Perhaps".** MET, with the hedge kept.
- **Placer versus Meehan.** MET, through the "only to the fulfilment of a condition" distinction.
- **Agency of AMPL and of Pierre.** MET on the facts; see D4 on the source.
- **Whether "the clause" could be the $10,000 term.** PARTLY; the answer is correct.
- **"I will do that": result or effort.** MET, except for the unused check-in conduct (fix offered).
- **The existing legal duty rule both ways.** MET, apart from D1.
- **The guarantee clause and assent by conduct.** PARTLY; Brambles 195 is the stronger authority for Rocky.
- **Past consideration and Pao On's three conditions.** MET.
- **The start of the 12 months both ways.** MET.
- **The March instalment.** PARTLY.
- **"Once Grace repays" and the duty to co-operate.** MET.
- **Exposure stated exactly.** NO (D3).
- **Consistency between Parts I and II.** One defect (D3) and one asymmetry (BBL).

---

## 4. Authenticity (a senior academic's read, ignoring the rubric)

**Strengths.**
- It reasons chronologically from Rocky's goals.
- It works the client's own words hard. The "Hail Mary" contrast, "recorded" also governing the 4% rate, "no lender acting for him would need", and the signature point in Coulls and Empirnall are each a real lawyer's move.
- Authorities are mostly used for what they decided, and hedges and dissents are flagged.

**Weaknesses.**
- **Quote-mosaic.** The Godecke sentence strings four fragments together. The privity sentence ("'a third party cannot sue upon a contract', nor can 'a stranger to the consideration'") quotes historical background, "hitherto accepted", as if it were the plurality's own holding.
- **Compression that hides the step.** "which neither standard can supply and no range confines" works only for a reader who knows McHugh JA 151's two limbs. "even as joint promisee" is ambiguous. "either way, Rocky relies on the oral promise" asserts rather than shows the link to para 17.
- **A logic slip a practitioner would notice** (D1), and a bottom line that does not follow from the analysis above it (D3). In real advice the exposure paragraph is what the client reads, so D3 matters most.
- **No box-ticking headings, no meta language and no proxy terms were found.** The voice matches his LAWS1061 Part A in density, semicolon use and "On balance … likely".

---

## 5. Additions ranked by marks per word

**Funded package (net +1; tested on a scratch copy: body 1,597, stated 1,600).**

| # | Edit (exact) | Words |
|---|---|---|
| 1 | D1: delete "unless the clause preceded the bargain" | −6 |
| 2 | D3a: "if Rocky assented to the clause" → "if Rocky assented to the clause and AMPL promised the $10,000" | +5 |
| 3 | D3b: "If bound only orally, he is liable in damages, to AMPL or Pierre, for any payment Grace misses." → "By his oral undertaking he is also liable in damages, to AMPL or Pierre, for any payment Grace misses." | +1 |
| 4 | D2: "though no formal document was contemplated, so did the email." → "the email, though contemplating no formal document, did likewise." | −1 |
| 5 | Brambles 195, Ipp AJA's majority test (text in section 2) | +2 |
| 6 | AMPL invoked the guarantee, as evidence of agency (text in section 2) | +6 |
| 7 | Check-in emails cannot construe the undertaking (Brambles 164; text in section 2) | +7 |
| 8 | Development Agreement claim rewrite (text in section 2) | −2 |
| 9 | Cut "arguably assuming a 27 February start," (lossless: nothing depends on it) | −6 |
| 10 | "If he said he would pay personally" → "If he promised personally" | −3 |
| 11 | "Grace's 5 February call asked Rocky to make an offer and promised nothing; it was likely an invitation to treat." → "Grace's 5 February call, asking Rocky to make an offer and promising nothing, was likely an invitation to treat." | −1 |
| 12 | Pierre's expectation sentence: "so it was likely" → "so was likely" | −1 |
| 13 | "Rocky could say his 12 February email records discussions, its other points, 'Potential' and 'wait and see', promising nothing." → "Rocky could say his 12 February email, 'Confirming discussions', promised nothing, like its 'Potential' and 'wait and see' points." (clarity) | 0 |
| 14 | Optional Trident hedge: "faces privity: outside insurance, 'a third party cannot sue upon a contract'", funded by dropping "12 February" from #13 | +2 / −2 |

New footnotes, which are not counted: Brambles (n 22) 195 (Ipp AJA), quoting Brogden v Metropolitan Railway Co (1877) 2 App Cas 666, 686 (Lord Hatherley); and Brambles (n 22) 164 (Heydon JA).

**Unfunded.** No lossless cut of the required length is left in the package. Each item below is ranked; to add one, the reviser must drop a lower-value funded item of equal length.
1. **Post-formation conduct on formation, Part I.** After "On balance, the loan was likely left to a new agreement.": "Later conduct, admissible on formation,[^Brambles (n 22) 164 (Heydon JA)] agrees: Grace took AMPL's loan on other terms." (+13). This is worth more than #6 and #7 combined (13 words). I recommend that swap if the reviser accepts losing the check-in and agency-adoption points.
2. **Masters' fourth category and "by 15 February" for Grace** (+33).
3. **Trident 118, nominal damages on the Pierre branch:** "to Pierre, ordinarily only nominal damages unless he proves his own loss" (+12).
4. **Pace 135 (Kirby P) and McHugh JA's services limit**, sharpening the answer to the illusory-promise point (+15 to 20).
5. **The March instalment and "you won't see a cent before then"** (+7).

**Concessions.** The 4% / "recorded" argument and Meehan's distinction are as strong as the readings allow. No conclusion in the answer needs to change. Only the exposure statement (D3) and the consideration "unless" (D1) are wrong as drafted.

---

## 6. Holistic mark

**84 / 100** as it stands. The answer is accurate and closely reasoned, with sophisticated use of the facts. It loses marks for D1 to D3, a mosaic or compressed sentence in places, and two strong opposing arguments left unmet: post-formation conduct and the fourth category.

With the funded package, about **87 to 88**. Reaching 90 would need the top unfunded item (post-formation conduct) and the fourth-category answer. Within 1,600 words, that means giving up lower-value material the reviser must choose.
