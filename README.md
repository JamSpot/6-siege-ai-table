# 6: Siege AI Table

A progressive learning guide for **6: Siege – The Board Game**, with a long-term goal of building a physical-table AI opponent.

## Start here

**Recommended first game:** [Consulate — Control (Beginner)](./tutorial/first-learning-scenario.md). This uses the published beginner mission setup; it is the main route for learning a complete game.

- [Tutorial home](./tutorial/README.md)
- [Lesson 1 — Your First Game](./tutorial/01-your-first-game.md)
- [Lesson 2 — Movement, Facing & Line of Sight](./tutorial/02-movement-facing-line-of-sight.md)
- [Lesson 3 — Activation & Actions](./tutorial/03-activation-and-actions.md)
- [Lesson 4 — Combat](./tutorial/04-combat.md)
- [Optional three-round practice drill — Clear the Room](./tutorial/05-first-learning-scenario.md) (project-created exercise, not an official mission)
- [First-game checklist](./tutorial/first-game-checklist.md)
- [First-game session sheet](./tutorial/first-game-session-sheet.md)

## Project goals

1. Teach the game progressively, from the battlefield and core actions through to a complete game.
2. Build a precise digital representation of the board and game state.
3. Develop a rules engine that determines legal actions.
4. Develop an AI player that chooses actions for one side.
5. Use an overhead camera to recognise the physical board, Operators, facing and game-state changes.
6. Have the human player physically move the AI's pieces, with the system checking the resulting board state.

## Development philosophy

The physical game remains the source of truth. The computer should assist the human rather than replace the tabletop.

Planned architecture:

Camera → Board State → Rules Engine → Legal Actions → AI Decision → Human Instruction → Camera

## Current status

- Tutorial lessons 1–4 are committed.
- The published Consulate beginner setup is the recommended first complete game.
- A separate project-created three-round drill is available for focused movement, LOS and combat practice.
- The beginner tutorial still needs a rules-verified end-to-end play-through before it can be called a complete playable milestone.
- The rules engine and camera prototype are future development steps; neither is claimed to be working yet.

## Next milestone

Verify the beginner setup, Operator choices, round sequence, legal actions and victory conditions against the current official rulebook and mission material. Then play through the scenario step by step and correct any gaps.

## Repository

https://github.com/JamSpot/6-siege-ai-table