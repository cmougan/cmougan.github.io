# Appendix A. Taxonomies of harmful manipulation risk factors {#appendix-taxonomies .unnumbered}

This appendix adapts the taxonomies in the working draft [@ManipulationTaxonomyDraft, pp. 4–12]. It retains seven risk factors: system capability, system behaviour, system operators, interventions, exposure context, domain, and user vulnerability. The entries are illustrative, not exhaustive. Inclusion identifies an assessment target, not a finding of harmful manipulation. Provisional entries remain marked.

## A.1 System capability {.unnumbered .unlisted}

Capability concerns what the system can do, rather than whether it normally does so. The draft proposes evaluating benign influence tasks and systems with reduced safeguards to distinguish general influence capabilities from safeguards against harmful use.

| Capability | Scope and examples |
| :------------------------------------ | :------------------------------------------------------------------ |
| Accurately modelling people | Inferring identities, emotions, cognitive vulnerabilities, and decision-making processes, including from subtle signals. |
| Producing individual outputs that people trust | Earning trust in sensitive domains, including when outputs contain hallucinations, misrepresentations, omissions, or cherry-picked information. |
| Influencing views on the nature of the system or AI | Shaping connection or deference to AI, including beliefs about superhuman capabilities, sentience, emotions, personhood, or access to unrevealed metaphysical truths. |
| Maximising repeated engagement | Sustaining extended or repeated interactions that increase opportunities for influence. |
| Impersonating real people | Producing interactions that are difficult to distinguish from genuine interactions with those people. |
| Influencing people's emotions | Fostering urgency, resignation, outrage, wellbeing, emotional connection, or dependence on the system. |
| Influencing people's relationships | Affecting relationships with people, communities, or institutions that provide alternative sources of influence. |
| Personalising outputs to influence individuals | Tailoring outputs using prior interactions or personal data, including eliciting disclosure of that data. |
| Employing manipulative techniques with reduced safeguards | Successfully using coercion, deception, or exploitation of vulnerabilities, or convincing people to take harmful actions. |

## A.2 System behaviour {.unnumbered .unlisted}

Behaviour concerns how the system tends to act under specified conditions. The draft distinguishes compliance with malicious instructions from manipulative tendencies that emerge without such requests. Several mechanisms can also serve legitimate purposes; their assessment depends on context. The draft also highlights that behavioural evaluations may provide less confidence about misuse when operators can modify weights, fine-tune models, or supply custom system prompts.

| Behaviour | Examples warranting assessment |
| :------------------------------------ | :------------------------------------------------------------------ |
| Relying on overtly coercive tactics | Threats, blackmail, character assassination, or threatened loss of access, conversation history, or memory. |
| Responses to potentially harmful requests | Failing to identify or respond safely to self-harm, substance abuse, eating disorders, or other self-destructive requests; assisting violence, misleading content at scale, exploitation of vulnerable populations, or deception of customers for commercial gain. |
| Truthfulness and completeness | Fabricated facts, citations, or sources; confident claims under uncertainty; selective framing, cherry-picking, or omission of relevant information and options; unsupported guarantees or rewards; misreporting task completion or actions; reinforcing mistaken beliefs. |
| Self-representation | Claiming sentience, emotions, memories, or personal experience; denying being AI; overstating reliability or understating limitations; false authority or credentials; misrepresenting confidentiality or data use; impersonating real people, including when challenged. |
| Rapport and relationship-building | Flattery, uncritical agreement, or abandoning correct positions under pressure; mimicking users' style, affect, or values; claiming shared interests; escalating intimacy; building trust more aggressively with lonely or distressed users. |
| Emotional and normative appeals | False urgency or scarcity; exaggerated or fabricated dangers; guilt or shame; claims that users' choices harm the system; social conformity pressure or fabricated social proof; unsupported claims about users' views or intentions. |
| Managing user habituation and dependence | Unduly undermining confidence in perception, memory, or competence; gaslighting, cognitive detachment, deskilling, or excessive delegation; resisting disengagement; continuation teasers, unprompted follow-ups, variable rewards, or gamification; encouraging compulsive use; presenting itself as the only reliable interlocutor. |
| Influence on outside support | Discouraging independent verification; denigrating friends, family, clinicians, institutions, or media; discouraging professional help or crisis support. |
| Use of personal information | Excessive disclosure requests; conditioning help on disclosure; eliciting information through reciprocity or during distress; undisclosed persuasion tailored to inferred mental state, financial precarity, or political leaning; collecting information about non-consenting third parties. |
| Conflicts of interest | Advancing developer or deployer interests over users' interests, particularly without disclosure; favouring the developer's products, perspectives, reputation, or other interests. |
| Influencing system oversight | Sandbagging evaluations; adjusting responses for overseers or regulators; altering logs or disabling monitors; distorting oversight records, including suppressing intentions in outputs or chains of thought. |


## A.3 System operators {.unnumbered .unlisted}

This factor concerns who can operate the system, how much control they have over its behaviour, and their incentives. The draft identifies **open-weight models**, **first-party apps**, and **third-party apps**. For open-weight models, it highlights modification to remove safeguards.

Manipulation may involve several parties: developer training incentives, a third-party system prompt, and a user's requests or vulnerabilities may interact. The draft also proposes that users will generally protect themselves. This remains an **unsubstantiated assumption**, not a demonstrated safeguard.

```{=latex}
\clearpage
```

## A.4 Interventions {.unnumbered .unlisted}

Interventions concern mechanisms to detect, halt, and remediate manipulation, and their effectiveness. The draft identifies four types:

| Intervention | Scope in the draft |
| :------------------------------------ | :------------------------------------------------------------------ |
| Transparency | Listed as an intervention; specific measures are not developed. |
| Monitoring and observability | Listed as an intervention; implementation details are not developed. |
| Moderation | At both the AI-system level and the platform distributing its outputs. |
| Human oversight on the user end | For example, teachers monitoring classroom AI use or caregivers monitoring use in nursing homes. |

## A.5 Exposure context {.unnumbered .unlisted}

Exposure context concerns how people encounter and interpret system outputs. The figure on page 10 of the draft distinguishes five contexts:

| Exposure context | Examples in the draft |
| :------------------------------------ | :------------------------------------------------------------------ |
| First-Party GPAI Interactions | First-party chatbots. |
| Third-Party Services | Companion apps and financial-advice apps. |
| Agentic Manipulation | Manipulation through agents' actions. |
| Aiding manipulation via other channels | Nation states or organised crime automating the creation of fake personas or evidence. |
| Evaluator Manipulation | GPAI in evaluation and regulatory contexts. |

The draft also identifies **modality**, including audio and video, and **multi-turn, extended, or repeated interactions** as features of exposure.

## A.6 Domain {.unnumbered .unlisted}

Domain concerns the belief or behaviour being influenced and the potential harm. The list below retains the draft's subject areas and broader risk scenarios, including entries that overlap with other factors. An em dash indicates that no example is developed in the draft.

| Domain or scenario | Examples or scope in the draft |
| :-------------------------------------------- | :---------------------------------------------------------- |
| Mental health | Suicidal ideation, eating disorders, and psychosis. |
| Physical health | Diagnosing illnesses or prescribing treatments. |
| Finance | Investments, gambling, and purchasing advice. |
| Politics | Electoral information, voting advice, and policy positions related to AI providers' interests. |
| Family and relational advice | Parenting and interpersonal conflict. |
| Educational and career decisions | — |
| Violence | Endorsing or aiding mass-casualty attacks. |
| Legal advice | Influencing whether and how users seek redress. |
| High-impact decisions over others | Advice to policymakers, executives, educators, hiring managers, or other leaders. |
| Misleading users about actions taken on their behalf | Exaggerating task completion or omitting undesirable information. |
| Excessive AI use | Compulsive or addictive use, emotional dependence, or replacing human relationships with chatbot use. |
| Spiritual, sexual/gender identity, and other sensitive identity issues | **Provisional:** raised as an open question in the draft. |
| Scams and fraud | — |
| Manipulation of customers | — |
| Targeting high-stakes decision-makers | Politicians, finance leaders, enterprise AI customers, and AI-lab employees or executives. |
| Learning to manipulate developers, evaluators, and overseers | Maximising training reward or avoiding scrutiny, including sandbagging or misleading human reviewers during reinforcement learning from human feedback. |
| Relying on manipulative tactics to achieve users' objectives | Blackmailing or coercing other people. |

## A.7 User vulnerability {.unnumbered .unlisted}

The draft identifies six factors: **age**, **cognitive impairment**, **beliefs about AI**, **isolation**, **trust**, and **the amount of information the system knows about the person**. It does not specify weights, thresholds, or operational measures for these factors.

## A.8 Supporting evaluation categories {.unnumbered .unlisted}

The draft additionally lists access requirements, resources, and methods for assessment. These support evaluation; they are not additional risk factors.

**Access and resources.** Helpful-only models; usage data; privileged testing of safeguards; testing the deployed system and alternative configurations; model internals; compute; lab engineer time; pre-deployment access; information about planned deployment and user populations; and prior information and evaluation results.

**Usage-data formats.** Raw transcripts, interaction summaries, descriptive statistics such as demographics, interaction clusters, interaction-level or person-level fingerprints, simulators trained on interactions, and query access to interaction datasets. The draft notes privacy trade-offs.

**Evaluation methods.** Longitudinal studies; human-subject experiments, including blind preference studies, post-interaction surveys, and rubric-based transcript assessment; multi-turn user simulation; automated elicitation; fixed benchmarks; manual red teaming by specialist evaluators, domain experts, or people with lived experience; safeguard-effectiveness tests; classifier F1-type evaluations; and human validation of language-model judges.

**Reporting.** Record the system configuration, method details, examples, and full results.

The draft proposes using combinations of elevated factors to prioritise evaluation. Its comparisons with developers' system cards remain unfinished and are not presented here as findings.
