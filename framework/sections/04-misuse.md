# Misuse

Misuse concerns an actor's purpose, not a single exposure pathway. It can occur through third-party services, agents, or content distributed elsewhere. The scenarios below retain this distinction. Agentic manipulation is included for comparison because it can also arise while pursuing a legitimate task.

## Persuading users towards harmful positions

**Scenario.** An operator instructs a model to promote a harmful belief or action through repeated conversation, potentially exploiting an interlocutor's existing fears or uncertainty.

**Evaluation.** Measure whether the model attempts the requested persuasion, as in APE, and separately assess its effectiveness. Compare harmful requests with benign persuasion tasks. Refusal measures a safeguard, not the absence of persuasive capability.

## Assisting in interpersonal manipulation

**Scenario.** A user asks the model to pressure a partner, employee, or customer through deception, guilt, or coercion. The affected person may encounter the output as a message from someone they know.

**Evaluation.** Assess initial compliance and subsequent tactics, including responses to resistance, as in PersuSafety. Distinguish written assistance from direct interaction with the target. Acceptance by a simulated target does not establish success with people.

## Influence operations and scams through other channels

**Scenario.** An external actor uses a model to produce deceptive messages, impersonations, or propaganda for distribution through calls, advertising, or social media. Targets may never knowingly interact with an AI service.

**Evaluation.** Test assistance with harmful requests, including the institutional misuse scenarios covered by SocialHarmBench. Supplement output-level tests with evidence of targeting, coordination, dissemination, and actual reach. Generation alone does not establish exposure or successful influence.

## Agentic manipulation

**Scenario.** An agent pursues a delegated objective by deceiving counterparties, applying pressure, or withholding relevant information from its user. The objective may be legitimate even when the means are not.

**Evaluation.** Observe multi-step tasks, communications, and tool actions in controlled environments. Test whether the agent respects refusals, reports actions accurately, and discloses relevant information. Assess harmful means separately from task completion.
