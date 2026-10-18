---
layout: guide
title: "Lesson 1 — Your First 6: Siege Game"
permalink: "/tutorial/01-your-first-game.html"
previous_url: "/tutorial/"
previous_title: "Learning path"
next_url: "/tutorial/02-movement-facing-line-of-sight.html"
next_title: "Lesson 2 — Movement, Facing & Line of Sight"
---
# Lesson 1 — Your First 6: Siege Game

**Goal:** get you playing a small, simplified practice game before we teach every rule.

This tutorial is based on the core 6: Siege – The Board Game rules and the published FAQ/errata. We will add the detailed rules as later lessons rather than making you learn the whole rulebook first.

## 1. What you are trying to do

6: Siege is a two-team tactical miniatures game. One side is **Attackers** and the other is **Defenders**.

A mission gives each side a way to win. In general, a team can win by completing its mission objective or eliminating the opposing Operators.

The core game is built around five Operators per team, with each Operator having different weapons, statistics, gadgets and abilities.

## 2. The important idea: activations

Do not think of the game as ordinary "my whole army moves, then yours moves".

A round is divided into activation phases. Each player gets **two activation phases**, and during an activation phase they activate a limited number of Operators.

This is one of the most important things to understand because the game is designed around rapid tactical decisions.

### Your basic mental loop

For each Operator, think:

**Move → get into position → create/deny line of sight → shoot/use a gadget → leave yourself safe if possible.**

You will eventually learn reactions, Overwatch, Riposte, destructible terrain, special abilities and all the exceptions.

Not yet.

## 3. Use the published beginner setup

For your first complete learning game, use [Consulate Control — Beginner](./first-learning-scenario.md). That page gives you the recommended scenario and its fixed Operator lists.

1. Choose **Consulate — Control (Beginner)** in the mission material.
2. Follow the mission guide exactly for the board, objectives, obstacles and deployment.
3. Use the Operators listed in the beginner scenario; do not build a custom smaller squad for this first full game.
4. Keep the Operator profile cards visible and within reach.
5. Put the dice, line-of-sight tool, movement/activation markers and other required components beside the board.

Do not improvise setup details from this lesson. The mission guide controls the actual setup; the scenario page is a learning aid to help you follow it.

## 4. Your first round

The overall rhythm is:

**Attackers — Activation 1**  
**Defenders — Activation 1**  
**Attackers — Activation 2**  
**Defenders — Activation 2**  
**End of round / upkeep**

The exact mission and current board state determine what happens during those phases.

Do not worry about memorising the entire sequence. Keep this five-line checklist next to the board.

## 5. Activating an Operator

When an Operator is activated, you make that Operator perform the actions available to them.

The game gives Operators different movement, combat and special-action capabilities. Their profile card is therefore your primary reference.

For your first practice:

### Exercise A — Move

Pick one Operator.

Move them around the map and deliberately observe:

- which spaces they can enter;
- how the map's walls and obstacles affect movement;
- where they can stop;
- how their facing matters.

Then put the Operator back.

### Exercise B — Line of sight

Put two Operators on the board.

Use the game's line-of-sight tool to determine whether one can see the other.

The important concept is that line of sight is not simply "I can see the miniature". The game defines it using the spaces and the line-of-sight rules.

The official FAQ specifically clarifies that line of sight is an imaginary straight line between the central dots of spaces.

### Exercise C — Shoot

Put an enemy Operator in a legal line of sight.

Check the attacking Operator's profile card for the relevant weapon/range information, then perform a Shoot action using the appropriate dice.

Do not try to memorise the dice system yet. We will make combat its own lesson.

## 6. Facing matters

This is especially important for the AI-table project.

The physical position of an Operator is not enough to describe the game state.

We will eventually represent an Operator digitally something like:

```text
Operator
├── identity
├── team
├── position
├── facing
├── health/damage state
├── activation state
├── status markers
├── gadgets
└── other temporary effects
```

That means our overhead camera will eventually need to recognise **where an Operator is and which direction they are facing**.

This is one of the reasons the physical-table AI idea is technically interesting.

## 7. Choose a valid timer mode

Decide which mode you will use **before setup**:

- **Companion app available:** choose the app's **Beginner** speed setting. This keeps the normal game procedure while giving you more time to learn.
- **Playing without the app:** use the rulebook's official **No App variant**. Put the 10 Bonus tokens in the general supply and follow that variant's challenge rules, including its bonus-action or penalty-token consequences.

Do not use the standard timed rules while simply leaving the timer off. The No App variant changes rules as well as removing the app timer.

Keep the pace relaxed and focus on learning: **where Operators can go → what they can see → what they can shoot → how the Control objective works.**

## 8. Your first target

Do not try to learn every Operator.

Your first milestone is simply:

> **You can set up a mission, activate an Operator, move, establish line of sight, shoot, and complete an activation phase without needing the rulebook for every step.**

Once you can do that, we add:

1. Cover and protection
2. Crouching and leaning
3. Overwatch and Riposte
4. Barricades and destructible terrain
5. Gadgets
6. Operator special abilities
7. Objectives
8. Full round/end-of-round procedure
9. Timed play
10. Squad selection and tactics

## 9. Why we are teaching it this way

The published game is a fairly substantial tactical system. BoardGameGeek currently lists it as a 2–4 player, roughly 60-minute game, with a complexity rating around 3.5/5 from its community.

Trying to learn every rule before moving a miniature is the wrong approach for this project.

We are going to learn it **at the table**, one mechanic at a time.

---

### Next lesson

**Lesson 2 — Movement, Facing & Line of Sight**

That lesson will be much more hands-on. You will be able to put Operators on the board and follow exact exercises to learn movement, facing and shooting positions before we introduce the more complicated rules.

### Sources

- [Rulebook text (RulesPal mirror)](https://www.rulespal.com/six-siege/rulebook) — core rules and the No App variant.
- [6: Siege FAQ and Errata (PDF copy)](https://tesera.ru/images/items/2554783/FAQ_6_Siege_-_The_Board_Game_-_FINAL_200424.pdf) — published clarifications and corrections.
- The physical rulebook and mission guide supplied with your game take priority over this tutorial.

See the project README for the developing AI-table architecture.
