# First Learning Scenario — Consulate Control

This scenario is designed to get you playing rather than studying.

## Use the official beginner setup

For the first full learning game, use **Consulate — Control (Beginner)** from the mission material.

The beginner setup is specifically intended for a first game: it can be played without a timer/app, or using the Beginner speed setting. The published beginner mission material uses a predefined set of Operators and does not use Hidden Operator tokens for this introduction.

### Attackers

- Thermite
- Ash
- IQ
- Sledge
- Blitz

### Defenders

- Smoke
- Castle
- Bandit
- Mute
- Pulse

Do not substitute Operators for this first learning game. The point is to learn the game system before introducing team-building decisions.

## Learning mode

For your first attempt:

- **Do not use the timer.**
- Use the mission's beginner setup.
- Use the listed Operators.
- Follow the mission deployment exactly.
- Keep the Operator cards beside the board.
- Keep the LOS tool, dice and reference material beside the board.
- Stop whenever you are unsure and resolve the rule before continuing.

This is deliberately a training game, not a speed test.

## What you are trying to learn

By the end of the first game you should have experienced:

- an Attacker activation;
- a Defender activation;
- movement;
- facing;
- line of sight;
- shooting;
- cover/protection;
- using a gadget;
- the Control objective;
- the end-of-round procedure.

You do **not** need to master every Operator ability.

## Suggested teaching order

### Round 1 — Learn the board

Concentrate on movement, line of sight and the objective.

### Round 2 — Add combat decisions

Start deliberately positioning Operators to create good firing opportunities.

### Round 3 — Add gadgets

Use the Operators' gadgets when the situation naturally calls for them.

### Later rounds — Play normally

Now stop explaining every decision and let the game flow.

## Win condition

Use the mission's actual Control scoring and victory conditions. Do not replace the mission objective with a made-up kill-everyone training condition.

The overall game can be won by completing the mission objective or eliminating the opposing team; the exact objective procedure depends on the mission type.

## After the game

Write down only three things:

1. What rule felt confusing?
2. What action felt most useful?
3. What did you wish the tutorial had explained?

Those answers will guide the next revision of the tutorial and eventually the rules-engine test cases.

## Why this scenario matters to the AI project

This is our first candidate for a **known-state AI test environment**.

Because the beginner scenario removes much of the hidden-information complexity, we can eventually record a board state after every activation:

```text
round
phase
operator
team
position
facing
health
status
terrain
gadgets
objective state
```

The AI can then be tested against the same position repeatedly.

That is much safer than trying to build a general-purpose AI before we have a verified, playable rules model.
