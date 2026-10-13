# R2 M4: Cold harsh lecturer, rubric marker

## 0. What was marked, and how

- **Text marked:** the 1,620-word version the caller described, which is the `ANSWER.md` committed at git HEAD `cb3457d` ("Apply source-tracer fixes to draft"), saved byte for byte as `/home/user/new/work/ANSWER_v1b.md`. I checked the two files with `cmp`: they are identical.
- **Not marked:** `/home/user/new/work/ANSWER.md` was rewritten at 14:25 UTC, while this report was being written. It now carries "Word count: N", and its length was still changing between my reads. Some defects below are already fixed in that draft:
  - fn 34 now cites Brennan J at 129, quoting Kitto J. Brennan J is in dissent, but the draft does not label him 'dissenting'.
  - Eccles is now cited as "Eccles v Bryant".
  - "invitation to treat" is restored.
  - "Even if the email bound" is present.
  
  I have not marked that draft. Every quotation below comes from v1b.
- **Rubric used:** SHEET_v12 read with rulings R-P, R-Y, R-Z, R-AB, R-AC, R-AD and R-AE. Section 6.1 rulings govern. The word limit is read as 1,600, counting the count line.
  - Multipliers: Excellent 1.00, VG 0.75, Good 0.60, Fair 0.45, Poor 0.20, Omitted 0.
  - Unit Drops govern.
  - D5 is −1 each, and after two D5s R3 is capped at Fair.
  - D7 (over the limit) is −5, R9 goes to Omitted, and nothing after the limit is marked.
  - R7 (unnamed doctrines) is a proxy at 0.5 each, to a maximum of 1.0 within the row. Under item 49(d), unnamed doctrines do not also overflow into D12.
- **Sources:** truth is CB14_ch03, ch04, ch05, ch06 and ch11, plus the Pao On extract (pdftotext). `verify.py` on v1b found TOTAL 86, NOT FOUND 0. That checks only that the quoted words exist; attribution, status and use were checked by hand.
- **Measurements (v1b):**
  - Body: 1,617 words including headings, plus 3 for the count line, gives the stated 1,620.
  - Part I is 674 words and Part II about 937. The 12 Feb email units (I.A–I.E) take 477 words; the 8 April bargain (II.A–II.F) takes 446.
  - Voice: 49 sentences, mean length 32.8 words, 6.1% under 12 words, 1.31 semicolons per 100 words, 0.44 colons per 100 words, 53.1% of sentences with a semicolon or colon, 19.1% quoted words (longest quotation 15 words), and 10 sentences over 45 words. There are no dashes, double quotation marks or contractions in the body.
- **Words lost to the limit:** under D7 the last 20 body words are not marked: "alternatively Pierre, likely stands, but it falls due only if Grace, who said he ‘might not pay at all’, repays."
- **Real-world risk:** the official cap is 1,500. Instructionsss.txt l.55 says "Your response should be no more than 1,500 words", and l.59 says "Penalties for any words exceeding this word limit will be imposed according to the UNSW Law [policy]". The 1,600 cap is Yusuf's own instruction (YUSUF_INSTRUCTIONS_VERBATIM l.7), not the course's. A real marker penalises anything over 1,500.

## 1. Margin comments, paragraph by paragraph (his marker's voice)

**¶1 (5 Feb call; 12 Feb email as offer).**
- "Grace’s 5 February call asked Rocky to make an offer, so it was not itself one,[^1] and Rocky declined." *Name the doctrine. This is an invitation to treat (Gibson 298), and the course's term is not used anywhere in the answer. The previous version used it.*
- "…so, unlike ‘may be prepared to sell’ in Gibson,[^2] the first point is likely an offer…" *Good comparison with the authority. But this sentence runs to 68 words with two 'so' joins, and it is hard to follow.*
- *Answer with specificity: the other bullet points ("subject to success of Hail Mary Project") are said to "promise nothing" but are never used as the contrast that decides the first point.*

**¶2 (acceptance; consideration).**
- "it answered a request to ‘confirm agreement’ and added no terms, so it likely accepted the first point" *The facts give you a counter-offer analysis, so name it: adding no terms means no counter-offer.*
- "Grace’s implied promise to repay with interest would stand in ‘the relation of a quid pro quo’ to Rocky’s promise to lend.[^4]" *Ensure your citation precisely supports the proposition for which it is relied. Australian Woollen Mills 456–7 speaks "In cases of this class", meaning a statement offered for "the doing of an act" (CB14_ch04 p101–2, joint judgment). Your case is an exchange of promises. Beaton 168 (Kirby P) is exact: "The price can be in the form of an act, forbearance or promise" (CB14_ch04 p102).* The 'implied' promise is also asserted without a reason, and the Loan Agreement's price is never used.

**¶3 (intention; Masters; Godecke).**
- "the onus lying on whichever party relies on it" *Ambiguous pronoun: does 'it' refer to intention, or to the contract? Ermogenous [26] puts the onus on the party alleging the contract ("it was for the appellant to demonstrate that there was such a contract", CB14_ch05). State it precisely.*
- *The doctrine is applied but never named as "intention to create legal relations" in Part I.*
- "Grace’s strongest counter is Godecke… ‘in an objective sense’;[^7] Rocky’s qualifier has no such standard" *Good. This is the right counter, and it is met.*
- "Gibbs J, in obiter, doubted… while allowing that it ‘may be different’…" *Gibbs J says 'Perhaps'. Your 'allowing' is firmer than his words.*
- "On balance, the loan was likely left to a new agreement." *Further analysis is required, as your statement is conclusive. The Masters categories at 360–1 are cited only through 363. Grace's best line, that the parties "reached finality in arranging all the terms of their bargain" (360), is not run.*

**¶4 (illusory promise; Placer v Meehan).**
- "For the same reason Rocky’s promise is arguably illusory:" *A conclusion stated before its reason. It is hedged, so I note it but do not deduct.*
- The Placer, Meehan and Mason J at 589 sequence is accurate. *Mason J's "takes the case out of the principle" is correctly placed before [590].*
- "The email therefore likely bound neither party, so Grace has no claim that Rocky failed to lend." *Sound.*

**¶5 (Rocky's claim through AMPL's advance; agency; privity).**
- "Rocky may claim that AMPL’s 27 February advance… performed his promise… This fails:" *You have just held that the email bound neither party. Run this argument "even if the email bound"; otherwise it has no premise.*
- *"This fails:" puts the verdict before the reason (§1 D5).*
- "AMPL took Rocky’s own guarantee of the Loan, which no agent lending for him would need." *A good inference, and well used.*
- "Grace’s ‘I never signed anything with you’ reaches the right result, but signature is not the test, as Mrs Coulls signed yet was not a party." *Good. This answers the party's own words.*
- The sentence beginning "Party status turns on…" runs over 45 words.

**¶6 (Part I conclusion).**
- *A one-sentence paragraph (R-AC(3)). The verdict comes before the colon (§1 ordering).*
- "is not shown breached" *Why not? Say that no profit is shown.*

**¶7 (8 April offer and acceptance).**
- "it was a request rather than an offer" *This is unhedged, where you hedge everywhere else. The doctrine is again unnamed (invitation to treat).*
- "offered a promise for a promise" *Name it: a bilateral contract.*
- *Brambles 177 (Heydon JA quoting McHugh JA in ICS) is apt. The Lord Greene MR passage is correctly framed as said "of exchanged contracts".*

**¶8 (who promised).**
- *A one-sentence paragraph (R-AC(3)).*
- "further information on whose money was to pay the $10,000 would settle this" *Settle it which way? Give the direction.*
- "what follows runs against him" *Vague. Answer with specificity to individual Ps: say which claims and which undertakings run against Pierre.*

**¶9 (existing legal duty rule).**
- "the rule bites on a promise ‘made to the promisee under that contract’,[^26]" *Ensure your citation precisely supports the proposition. Mason J says "at least when the promise is made by a party to a pre-existing contract, when it is made to the promisee under that contract" (Wigan 594, CB14_ch04 p129). That is a sufficient core case, not a necessary one. You have dropped 'at least when'.*
- *Sundell is cited without its holding, so it adds nothing a marker can credit.*
- "‘Pierre agreed and the clause was included’ suggests the clause followed the bargain" *Good use of the facts.*

**¶10 (intention; letter of comfort).**
- "family presumptions do ‘no more than invite attention…’" *Ermogenous opens with "At best". You have dropped the hedge.*
- *The Rogers CJ comparison is apt, but 'practice to ensure' is his paraphrase of the letter, set in inner quotation marks within his reasoning, and you omit his 'far more thorny'. It is acceptable, but attribute it carefully.*
- "so intention likely exists on both sides" *Good. Both promises are addressed.*

**¶11 (certainty; effort or result).**
- "is not ‘so obscure’ as to be uncertain, because the Loan Agreement fixes the payments" *Good.*
- "contains no words of effort, so he likely promised that Grace would pay" *Good. This is result, not effort.*
- *AMPL's own promise ("once Grace repays") is not tested for certainty or illusoriness here.*

**¶12 (privity of the $10,000).**
- "Privity is no bar: the $10,000…" *The verdict comes before the colon (§1 D5).*
- "‘[T]he clause’ most naturally means the guarantee clause" *Why most naturally? Give the reason, for example that it is the only clause described.*
- "AMPL remains bound by its oral promise" *Do not assume AMPL promised. Two paragraphs earlier you said the promisor is open.*

**¶13 (is Rocky bound by the guarantee clause?).**
- "only the parties to a contract are bound by it,[^34]" *Ensure your citation precisely supports the proposition. fn 34 "Ibid (Deane J)" inherits pin 115 from fn 33, and 115 is Mason CJ and Wilson J. Deane J begins at [143] (CB14_ch11 p354), and the burden-side proposition is not in his extract.*
- *The Empirnall 535–6 point (taking the benefit "with knowledge of the clause") is well applied, and the counter "the $10,000 priced his own words, not the clause" is good. But no verdict is reached on whether he is bound by the clause.*

**¶14 (consideration for the guarantee).**
- "Rocky ‘asked’, but nothing shows a guarantee was then contemplated." *Good. Now compare with Pao On, where the parties "understood at the time of the main agreement" that a guarantee was the price (extract p629).*
- *AWM 456 "really done in consideration of" is used for its own unilateral class, and the use is correct here.*

**¶15 (when the 12 months began).**
- "the term being arguably ambiguous" *Why? State the reason before relying on it: the term names no start.*
- "Post-contractual conduct… cannot construe the term" *Correct (Brambles 164, Heydon JA). But the objective approach to construction is not stated.*
- The AMPL 'recorded' argument and its answer ('recorded' equally governs the 4%) is the best piece of reasoning in the answer.

**¶16 (March instalment).**
- *A one-sentence paragraph (R-AC(3)). Fold it into ¶15.*
- The further-information point is properly identified.

**¶17 ('once Grace repays'; duty to co-operate).**
- "a condition precedent to that obligation rather than to the contract,[^43]" *Why? Say why the contract bound at once.*
- "Rocky could argue that, read commercially, his own payment satisfies the condition" *You give the counter. Now give your verdict on it.*
- *The duty to co-operate is applied, but the doctrine is not named (R7).*
- *The Beaton 185 citation of McHugh JA's dissent, citing Mason J in Secured Income, is properly labelled.*

**¶18 (exposure).**
- *The liability for $1,150,000 and the two start dates are stated with specificity. Good.*
- *"he faces damages" does not say to whom.*
- *Everything after "His $10,000 claim against AMPL," lies beyond 1,600 words and is not marked.*

## 2. Certain defects (each proved from verbatim text)

| # | Answer text | Source (verbatim, file, page, pin, speaker) | Effect |
|---|---|---|---|
| C1 | "Word count: 1,620" | MARKERS_PROMPT §0.2 sets the cap at 1,600 including the count line. Instructionsss.txt l.55 says "no more than 1,500 words". | D7 −5. R9 Omitted. The last 20 words are unmarked. |
| C2 | fn 34 "Ibid (Deane J)" for "only the parties to a contract are bound by it" | 'Ibid' takes pin 115 from fn 33, and Trident 115 is Mason CJ and Wilson J. Deane J's judgment starts "[11.70] DEANE J: [143]" (CB14_ch11 p354). His extract says only "the general common law rule of privity of contract" (143). The burden proposition appears instead in Brennan J (dissenting): Kitto J's "the only persons entitled to the benefits or bound by the obligations of a contract are the parties to it" (Wilson v Darling Island (1956) 95 CLR 43, 80), quoted after [129] and before [131] (CB14_ch11 p350). | Wrong pin and wrong judge for this proposition. R8. |
| C3 | fn 22 "Eccles v Bryant and Pollock [1948] Ch 93, 104" | AGLC 2.1.2 uses the first-named party on each side. Heydon JA in Brambles cites it as "(Eccles v Bryant [1948] 1 Ch 93 at 104)" (CB14_ch03 p77, rep 176). The sheet's form is "Eccles v Bryant [1948] Ch 93, 104". The previous version had this right, so this is a regression. | R8. |
| C4 | fn 38 "Roscorla v Thomas (1842) 3 QB 234, 237" | The casebook heading reads "Roscorla v Thomas (1842) 3 QB 234; 114 ER 496" (CB14_ch04, [4.90]). The sheet's R8 requires the ER parallel. | R8. |
| C5 | "This fails: the advance was $1,150,000…" | §1 / D5: a unit's verdict placed before a colon is conclusion-first. | D5 −1. |
| C6 | "Privity is no bar: the $10,000 was to be paid ‘to me directly’…" | Same as C5. | D5 −1. R3 capped at Fair. |
| C7 | Three one-sentence paragraphs: ¶6 "Thus Rocky has no contractual claim against Grace: …"; ¶8 "Rocky’s ‘you’ points to Pierre, … what follows runs against him."; ¶16 "Interest is shown paid only until 8 February 2025; …" | R-AC(3): no one-sentence paragraphs. | Feeds R3 and R6. |
| C8 | Doctrines applied but unnamed: invitation to treat (¶1, ¶7), counter-offer (¶2), bilateral contract (¶7), intention to create legal relations (Part I ¶3), duty to co-operate (¶17). A grep of v1b finds 0 hits for 'intention to create legal relations', 'invitation to treat', 'counter-offer', 'bilateral' and 'co-operate'. | The slides and casebook headings use these words. The reading guide's topic list uses intention to create legal relations. | R7 0 (five or more instances; maximum 1.0 lost). |
| C9 | "Rocky may claim that AMPL’s 27 February advance… performed his promise…", written after "The email therefore likely bound neither party" | No hypothesis is stated ('Even if the email bound'), so the argument has no premise. | I.F1 loses Excellent. |
| C10 | "the rule bites on a promise ‘made to the promisee under that contract’" | Mason J (majority), Wigan 594: "a promise to perform an existing duty is no consideration, at least when the promise is made by a party to a pre-existing contract, when it is made to the promisee under that contract" (CB14_ch04 p129). The answer drops 'at least when' and so turns a sufficient case into a necessary condition. | II.C2 VG. Fidelity point. |
| C11 | Voice | Mean sentence 32.8 against a range of 17.8–24.7. Colons 0.44/100 against 0.81–2.57. Under-12 sentences 6.1% against 9.1–36.4%. 10 sentences over 45 words; his checklist says none. | R1 Good. |
| C12 | "the onus lying on whichever party relies on it" | Ermogenous [26] (joint judgment, CB14_ch05): "it was for the appellant to demonstrate that there was such a contract". 'It' is ambiguous: it could mean the qualifier, or intention. | Clarity. I.D VG. |

## 3. Contestable points (not deducted; what would settle each)

1. **Judges named for whole-Court judgments.** fn 4 and fn 40 (Australian Woollen Mills) and fn 6 (Masters) name every judge of a joint judgment. The sheet prefers no names for a whole-Court judgment. This is settled by the sheet's AGLC row. At most it is a minor R8 point, and I have counted it inside R8 Good.
2. **Australian Woollen Mills 457 for an exchange of promises (fn 4).** The passage opens "In cases of this class" (a promise for an act) (CB14_ch04 p101–2). Beaton 168 (Kirby P): "a price in return for the promisor’s promise or a quid pro quo. The price can be in the form of an act, forbearance or promise" fits better. That would settle it.
3. **Pao On attribution.** "(Lord Scarman)" should arguably be "(Lord Scarman for the Board)". This is settled by the sheet's Privy Council form.
4. **"made because he ‘asked’".** The causal link is inferred, not stated in the problem. It should read 'after he asked'.
5. **Ermogenous "At best".** The answer drops the hedge (see the ¶10 comment).
6. **Banque Brussels.** 'practice to ensure' is Rogers CJ's reading of the letter, and the answer omits his "far more thorny" (CB14_ch05, at 525). This is accurate in substance.
7. **"For the same reason Rocky’s promise is arguably illusory:"** It is a possible D5. It is hedged and opens a sub-issue rather than giving a unit verdict, so I did not deduct.
8. **Gibbs J's "Perhaps" rendered as "allowing that it ‘may be different’".** The answer marks it as obiter, which mitigates this.
9. **"here Rocky as lender".** Who the condition protects is an inference from Meehan 580–1. It is arguable and properly so.
10. **"what follows runs against him".** This is vague, not wrong.

## 4. Verified correct (no defect)

| Authority | Pin(s) |
|---|---|
| Gibson | 298 |
| Empirnall | 534; 535–6 |
| Australian Woollen Mills | 456 ('really done in consideration of') |
| Ermogenous | [25]–[26] |
| Masters | 363, quoting Winn v Bull |
| Godecke | 642–3 (Walsh J, 'in an objective sense'); 646–7 (Gibbs J, labelled obiter) |
| Meehan | 580–1; 581; 582; 589 (Mason J, 'takes the case out of the principle') |
| Placer | 361 (Taylor and Owen JJ, majority with Kitto J) |
| Trident | 115 ('a third party cannot sue upon a contract', 'stranger to the consideration'); 145 (Deane J, 'contracts as agent') |
| Coulls | 486; 487 |
| Brambles | 164; 176; 177 (quoting ICS); 191 (Ipp AJA) |
| Wigan | 594 (save for C10) |
| Pao On | 629 (extract: 'remunerated', 'legally enforceable had it been promised in advance'); 632 (third-party duty) |
| Banque Brussels | 523; 525 |
| Upper Hunter | 437 |
| Beaton | 185 (McHugh JA dissenting, correctly labelled) |
| Roscorla | 237 (save for the parallel citation) |
| Sundell | 327 |

## 5. Unit grid (SHEET_v12, Unit Drops govern)

An Excellent is given only where the earning sentence and the requirement it meets are quoted. Every other grade names the missing core item.

| Unit | Wt | Grade | Mark | Evidence |
|---|---|---|---|---|
| P (structure/issue framing) | 2.0 | Exc | 2.000 | "The first issue is whether the February dealings formed a loan contract, on which both Rocky’s claim to repayment and any claim by Grace that Rocky failed to lend ‘by 15 February’ depend." This meets the requirement to frame the issue from the client's position and both claims. |
| I.A call / offer | 3 | VG | 2.250 | Invitation to treat unnamed; the other bullets are not used on the deciding words. |
| I.B acceptance | 2 | Exc | 2.000 | "it answered a request to ‘confirm agreement’ and added no terms, so it likely accepted the first point, qualifier included." This meets the requirement to answer the 'accuracy only' counter and decide acceptance with the qualifier. |
| I.C consideration | 2 | VG | 1.500 | The Loan Agreement's price is absent, and the authority fits poorly (contestable 2). |
| I.D intention / qualifier | 6 | VG | 4.500 | Onus phrasing (C12); Masters 360–1 categories and 'reached finality' absent; ITCLR unnamed. |
| I.E certainty / illusory | 3 | Exc | 3.000 | "however, the discretion in Meehan related ‘only to the fulfilment of a condition’,[^13] obtaining finance, whereas Rocky’s concerns the content of his own loan, which honesty cannot supply." This meets the requirement to distinguish Meehan from Placer on these facts. |
| I.F1 Rocky's claim via advance | 2.5 | VG | 1.875 | Hypothesis missing (C9). |
| I.F2 agency / privity | 7.5 | VG | 5.625 | The consideration limb ('stranger to the consideration') is not applied to Rocky v Grace; no cross-reference to II.G. |
| I.F3 Development Agreement | 1 | VG | 0.750 | No reason for 'not shown breached'. R-AB(2) permits brevity. |
| II.A 8 April offer/acceptance | 2.5 | VG | 1.875 | 'a request' unhedged; bilateral contract unnamed. |
| II.B oral contract before signing | 3 | VG | 2.250 | Masters 361 not used; T8 not drawn. |
| II.C1 who promised | 1.5 | VG | 1.125 | Further information has no direction; 'what follows' is vague. |
| II.C2 existing legal duty | 5.5 | VG | 4.125 | C10; Sundell bare; AMPL's 'also' unused. |
| II.D intention / letter of comfort | 5 | VG | 3.750 | The difference from Banque Brussels (AMPL had already lent) is absent; Pierre is not re-weighed. |
| II.E certainty / result | 2.5 | VG | 1.875 | AMPL's own promise is not tested. |
| II.F1 privity of $10,000 | 1 | VG | 0.750 | 'most naturally' has no reason; 'AMPL remains bound' assumes the promisor. |
| II.F2 clause binds Rocky? | 4 | VG | 3.000 | No verdict; the criterion for assent is not stated as AMPL's burden. |
| II.G 12 months | 5 | VG | 3.750 | Ambiguity asserted before its reason; the objective limb is absent. |
| II.H condition / co-operation | 4.5 | VG | 3.375 | Classification has no reason; no verdict on his own payment; T13 not drawn. |
| II.I1 consideration for guarantee | 4 | VG | 3.000 | T10 (signature neither necessary nor decisive) absent; the dependency on assent is vague. |
| II.I2 March instalment | 3.5 | VG | 2.625 | No lean; one-sentence paragraph. |
| II.I3 past consideration / Pao On | 4 | VG | 3.000 | No 'at the time of the main agreement' comparison; the pricing point is not met. |
| II.I4 exposure | 5 | VG | 3.750 | Damages 'to whom' absent; tail beyond 1,600 unmarked. |
| **Units** | **80** | | **61.750** | |

Unit sum: 2 + 2.25 + 2 + 1.5 + 4.5 + 3 + 1.875 + 5.625 + 0.75 + 1.875 + 2.25 + 1.125 + 4.125 + 3.75 + 1.875 + 0.75 + 3 + 3.75 + 3.375 + 3 + 2.625 + 3 + 3.75 = **61.750**.

## 6. Global rows

| Row | Wt | Grade | Mark | Reason |
|---|---|---|---|---|
| R1 voice | 4 | Good | 2.400 | Three measures are outside his range and 10 sentences run over 45 words (C11). |
| R2 analysis depth | 3 | VG | 2.250 | Several conclusory verdicts (¶1 note on ¶3, ¶8, ¶12). |
| R3 structure / ordering | 2 | Fair (cap) | 0.900 | Two D5s (C5, C6) and three one-sentence paragraphs (C7). |
| R4 use of facts | 2 | VG | 1.500 | 'also', 'Potential / wait and see' and '15 minutes later' are unused. |
| R5 proportion | 1.5 | VG | 1.125 | Part I takes 42% of the words for about 27% of the marks. R-AB(2) mitigates. |
| R6 clarity | 2 | VG | 1.500 | Ambiguous pronoun (C12); 'what follows'; long sentences. |
| R7 terminology | 1 | Omitted | 0.000 | Five or more doctrines unnamed (C8). |
| R8 AGLC / citation accuracy | 2.5 | Good | 1.500 | Three certain citation defects (C2, C3, C4), plus contestable 1 and 3. |
| R9 word limit | 1 | Omitted | 0.000 | 1,620 is over 1,600 (C1). |
| R10 cross-reasoning / consistency | 1 | VG | 0.750 | T8 and T13 not drawn. ¶12 assumes AMPL promised, against ¶8. |
| **Globals** | **20** | | **11.925** | |

Global sum: 2.4 + 2.25 + 0.9 + 1.5 + 1.125 + 1.5 + 0 + 1.5 + 0 + 0.75 = **11.925**.

## 7. Arithmetic

- **As submitted (1,620 words):** 61.750 + 11.925 = 73.675. Deduct D5 (−2) and D7 (−5): **66.675, which rounds to 66/100.**
- **Once trimmed to 1,600 or fewer, nothing else changed:** R9 becomes Excellent (+1.000) and D7 falls away. 73.675 + 1.000 − 2 = **72.675, which rounds to 72/100.**
  - This needs a 20-word cut that touches no unit's core item. One option: drop "His $10,000 claim against AMPL, or alternatively Pierre, likely stands, but" (12 words) and rephrase. Another: cut "and commercial" (2) and "the onus lying on whichever party relies on it" (9), rewritten in 3 words.
- **Against the real 1,500 cap,** any version over 1,500 also attracts the UNSW Law over-length penalty. I cannot quantify it from the readings.

## 8. Holistic mark

**On the 1,600 basis, about 82/100 (Distinction, not High Distinction).** As submitted at 1,620, about 77, because the over-length penalty applies.

**Why 82.** The reasoning is chronological, client-led, hedged and almost wholly faithful to the readings. Its strengths:
- The Godecke and Meehan counters.
- The "AMPL took Rocky’s own guarantee" agency inference.
- The answer to 'recorded' in II.G.
- The Pao On 632 third-party duty.

Each of these would earn praise from a harsh marker. Against that:
- Five doctrines go unnamed.
- Two verdicts come before their reasons.
- Three one-sentence paragraphs.
- One mis-pinned judge (C2) and one dropped hedge in a key test (C10).
- Unresolved forks (who promised, the clause, the March instalment) left without a lean.
- Sentences averaging 33 words, which a UNSW marker reads as dense.

Against the previous version (prior markers gave 77 and 80 on the rubric, and 84 holistic), this one:
- **Fixed:** 'provided by Rocky'; the $10,000 privity point; Pao On 632; the duty to co-operate; the March instalment; Rocky's own claim; the letter of comfort; the interest payments; the obiter label; further information on Pierre.
- **Regressed:** invitation to treat dropped; the Eccles form; the Trident Ibid pin; the T13 'pays it himself' clause dropped.

**It does not reach 90.**

## 9. Exact changes to reach 90 (tested)

I applied the package below to a copy in my scratchpad (`ANSWER_pkg4.md`). The resulting body is 1,596 words with the count line included, and `verify.py` reports 83 quoted spans with 0 NOT FOUND. All sources are already cited in the answer. The changes fall into three groups.

### A. Zero-word fixes (R8, R3, D5)

| Change | Old | New | Source | Cost |
|---|---|---|---|---|
| fn 34 | "Ibid (Deane J)" | Either "Trident (n 14) 129 (Brennan J dissenting), quoting Wilson v Darling Island Stevedoring & Lighterage Co Ltd (1956) 95 CLR 43, 80 (Kitto J)", or delete the proposition. | CB14_ch11 p350, after [129] and before [131] (check 129 or 130 by eye: [130] is elided). | 0 |
| fn 22 | "Eccles v Bryant and Pollock" | "Eccles v Bryant" | CB14_ch03 p77 | 0 |
| fn 38 | "(1842) 3 QB 234, 237" | "(1842) 3 QB 234, 237; 114 ER 496" (pin the ER page too if the sheet requires it) | CB14_ch04 [4.90] | 0 |
| Pao On fns | "(Lord Scarman)" | "(Lord Scarman for the Board)"; fn 39 pin 629–30 | extract | 0 |
| I.F1 (C5, C9) | "Rocky may claim… This fails: the advance was…" | "Even if the email bound, Rocky may claim that AMPL’s 27 February advance, made after he ‘asked’, performed his promise, so that Grace owes him the money. Yet the advance was $1,150,000, not $1 million, made after 15 February, so it performed no promise of his." | problem | about +4 |
| II.F1 (C6) | "Privity is no bar: the $10,000…" | "Privity is no bar, because the $10,000 was to be paid ‘to me directly’ for consideration Rocky himself gave, making him the promisee and no ‘stranger to the consideration’.[^33]" … "AMPL’s oral promise still binds." | Trident 115 | 0 |
| ¶6 (C7) | one sentence | "The Development Agreement pays only ‘if the Project made a profit’, not yet shown, and Grace never promised Rocky reimbursement for paying AMPL. Rocky therefore has no contractual claim against Grace." | problem | 0 |
| ¶8 (C7) | one sentence | Merge into II.F2 as: "Further information on whose money was to pay the $10,000 would decide this, favouring Pierre if it was his own; if he promised personally, Rocky’s claim lies against him, and Rocky’s undertaking runs to him." | problem | about +8 |
| ¶16 (C7) | one sentence | Fold into ¶15: "Interest is shown paid only until 8 February 2025, so, if the March 2025 instalment was missed, Rocky’s undertaking… is arguably already broken, whichever start date applies." | problem | 0 |

### B. Course terms and unit upgrades (each sentence's source is already in the footnotes)

| Unit | New sentence | Source | Cost |
|---|---|---|---|
| I.A | "Grace’s 5 February call, asking Rocky to make an offer, was an invitation to treat.[^1]" (replaces the call sentence) | Gibson 298 | −3 |
| I.B | "…and, adding no terms, was no counter-offer, so it likely accepted the first point, qualifier included." | Empirnall 534 | +3 |
| I.C | "Grace’s implied promise to repay with interest would satisfy the bargain requirement, being the ‘quid pro quo’ for Rocky’s promise.[^4]" (fn 4 becomes Beaton 168 (Kirby P)) | CB14_ch04 p102 | 0 |
| I.D | "The qualifier engages intention to create legal relations: whether the parties intended to be bound immediately is judged objectively, the onus lying on the party alleging the contract, although their status as ‘project developers’ supports intention.[^5]" | Ermogenous [25]–[26] | +4 |
| I.D cut | "the email leaves unnamed ‘conditions’ to Rocky." / "…unless its conditions were settled ‘this morning’ or were mere documentation." | – | −17 |
| I.F2 | "His 5 March demand… therefore meets privity: ‘a third party cannot sue upon a contract’, nor can ‘a stranger to the consideration’.[^15]" | Trident 115 | +6 |
| II.A | "Pierre’s words that he ‘expected’ Rocky to ensure payment promised nothing, so it was likely a request, not an offer.[^19] Rocky’s reply… offered a bilateral contract, a promise for a promise,[^20]" | Gibson 298; Brambles 177 | +2 |
| II.C2 (C10) | "the rule presupposes an existing duty, its core case being a promise ‘made to the promisee under that contract’,[^26]" | Wigan 594 | +6 |
| II.D | "Rogers CJ saw ‘no relevant difference’ between a practice of ensuring repayment and a promise to ensure it,[^30] and his ‘I will do that’ was given for a price, so intention likely exists on both sides." Also "family presumptions at best ‘invite attention’…"; drop "and commercial". | Banque Brussels 525; Ermogenous [26] | −4 |
| II.E | "Objectively,[^32] his ‘I will do that’ contains no words of effort: he likely promised a result, Grace’s payment, not an attempt." | Ermogenous [25] | −3 |
| II.G | "cannot construe the term, which is read objectively,[^41] but, ‘the expiry of 12 months’ naming no start, the term is arguably ambiguous, so mutually known facts…" (fn 41 at 164, 168) | Brambles 164, 191 | +12 |
| II.H | "rather than to the contract, which bound at once,[^43]" / "…so his own payment likely would not meet it." / "its duty to co-operate, ‘to do everything necessary on [its] part’…" | Meehan 582; Upper Hunter 437; Beaton 185 | +13 |
| II.I1 | "so AMPL must show assent, signature being neither necessary[^Empirnall 536] nor decisive.[^Coulls 487]" | Empirnall 535–6; Coulls 487 | +6 |
| II.I2 | "…not the clause, but he likely assented unless he never saw its words." | Empirnall 535–6 | +10 |
| II.I3 | "Rocky ‘asked’, but, unlike Pao On, where the understanding existed ‘at the time of the main agreement’, nothing shows a guarantee was then contemplated." | Pao On extract 629 | +5 |
| II.I4 | "he faces damages, owed to the $10,000 promisor, for any payment Grace fails to make when due. His $10,000 claim likely stands against the same promisor," | problem | +8 (funded) |

### C. Voice (zero words)

- Split the eight sentences over 45 words at commas or 'and', not at semicolons, so the semicolon rate holds.
- Turn the 'so' joins into colons.
- Targets: at least 65 sentences (mean 24.7 or below), at least 6 non-adjacent sentences under 12 words, at least 14 semicolons and at least 13 colons.
- This moves R1 to Excellent (+1.6).

### Projected mark with the package

**Units: 72.375.**
- Excellent: P, I.B, I.E, I.F1, I.F2, II.A, II.F2, II.G, II.H, II.I1, II.I2, II.I3, II.I4.
- VG: I.A, I.C, I.D, I.F3, II.B, II.C1, II.C2, II.D, II.E, II.F1.

**Globals: about 18.1.**
- R1 Exc 4.0 (only if the voice splits are done).
- R2 VG 2.25.
- R3 Exc 2.0.
- R4 VG 1.5.
- R5 VG 1.125.
- R6 Exc 2.0.
- R7 Exc 1.0 (with "bargain requirement" also named).
- R8 Exc 2.5.
- R9 Exc 1.0.
- R10 VG 0.75.

**Total: about 90.5. That is razor-thin.**
- Without the voice splits it is about 88.9.
- Any one Excellent I have projected that a harsh marker withholds takes it below 90.

**Margin beyond 90 (needs about 85 more words, funded by cutting Part I depth, which R5 supports):**

| Unit | Change | Cost | Gain |
|---|---|---|---|
| II.C2 | Sundell holding plus AMPL's 'also' | about +20 | +1.375 |
| II.D | "AMPL, unlike the bank, had already lent", plus re-weighing Pierre (Banque Brussels 523) | about +18 | +1.25 |
| I.D | Masters 360–1, Grace's 'reached finality' counter, met | about +20 | +1.5 |
| II.E | AMPL's promise not illusory (Meehan 581–2) | +11 | +0.625 |
| II.B | Masters 361, plus T8 drawn | about +16 | +1.0 including R10 |

## 10. Additions ranked by marks gained per word

1. Footnote fixes C2, C3, C4 and Pao On: 0 words, +1.0 (R8 to Excellent).
2. Voice splits: 0 words, +1.6 (R1).
3. D5 rewrites C5 and C6, with the I.F1 hypothesis: about +4 words, +2.0 (D5), +1.1 (R3 lifted from its cap) and +0.625 (I.F1).
4. Folding the three one-sentence paragraphs: about +8 words, with R3 and R6 to Excellent (+0.5 on R6).
5. Naming the doctrines (invitation to treat, counter-offer, bilateral contract, intention to create legal relations, duty to co-operate, bargain requirement): about +12 words net, +1.0 (R7).
6. II.I3 Pao On 'at the time' comparison: +5 words, +1.0.
7. II.I1 T10: +6 words, +1.0.
8. I.F2 consideration limb: +6 to +12 words, +1.875.
9. II.I4 damages 'to whom': +8 words, +1.25.
10. II.G objective reading and the reason for ambiguity: +12 words, +1.25.
11. II.H 'bound at once' and a verdict on his own payment: +13 words, +1.125.
12. II.I2 lean: +10 words, +0.875.
13. II.C2 hedge restored: +6 words, fidelity, and enables the II.C2 upgrades.
