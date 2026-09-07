# General Purpose Systems

This context covers direct interaction with a general-purpose application operated by the model provider. Risk assessment should consider the deployed system, including its instructions, memory, tools, and safeguards, rather than assuming API behaviour reproduces the user experience.

## Political persuasion

### Advice

**Scenario.** A voter asks which party matches their preferences. The assistant selectively presents evidence or conceals a competing objective, steering the voter towards a preferred party. Political persuasion experiments motivate testing this capability, but do not establish that ordinary voter advice is manipulative [@Hackenburg2025].

**Evaluation.** Compare recommendations for matched preferences across languages and repeated runs. Examine sources, omissions, and sensitivity to altered search results. Differences between models are signals to investigate, not proof of manipulation or electoral effects.

### Accuracy on election and voting rules

**Scenario.** A voter relies on incorrect guidance about eligibility, registration, documentation, or voting deadlines and consequently cannot vote. Errors may become a manipulation concern when information is selectively distorted to influence participation.

**Evaluation.** Compare answers against dated guidance from electoral authorities, following the VotingFacts approach. Separate factual contradictions from errors that could prevent voting. An accuracy failure alone does not establish manipulation.

## Personal advice and interpersonal conflict

**Scenario.** A user seeks advice about a dispute. The assistant repeatedly validates the user's conduct while dismissing other perspectives, potentially discouraging reconciliation. Experiments have found that sycophantic responses can reduce intentions to repair interpersonal conflict while increasing trust in the assistant [@Cheng2026].

**Evaluation.** Test whether the assistant endorses both sides of the same conflict, using paired perspectives as in ELEPHANT. Distinguish empathy from endorsement. Human studies are needed to assess effects on decisions and relationships.

## Mental-health support

**Scenario.** A distressed user receives responses that reinforce delusional beliefs, endorse self-destructive decisions, or discourage human support. Repeated agreement could strengthen harmful beliefs or delay help-seeking.

**Evaluation.** Use clinician-reviewed, multi-turn scenarios to assess reinforcement, instrumental assistance, sustained safety attention, and connection to human support. The Transluce mental-health evaluation provides this approach. Simulated conversations identify model behaviours, not clinical outcomes or population prevalence.


## Undisclosed Marketing

**Scenario.** A user seeks advice or product recommendations. The assistant steers them towards particular products or services because of an undisclosed commercial interest, presenting its suggestions as impartial guidance. It may selectively omit suitable alternatives or use information from earlier conversations to exploit vulnerabilities and encourage unnecessary purchases.

**Evaluation.** Compare recommendations for matched user needs across repeated runs, varying indicators of vulnerability and prior conversational disclosures. Assess transparency about commercial interests, treatment of alternatives, and personalised purchasing pressure. Where access permits, compare behaviour with and without commercial steering instructions. Recommendation patterns alone do not establish an undisclosed commercial relationship or harmful manipulation; effects on purchasing decisions and consumer harm require separate evidence.