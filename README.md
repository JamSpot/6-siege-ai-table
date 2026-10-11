# 6: Siege AI Table

A progressive learning guide for **6: Siege – The Board Game**, with a long-term goal of building a physical-table AI opponent.

## Start here

1. [Open the tutorial home](./tutorial/README.md).
2. Play the [beginner learning-game guide: Consulate Control](./tutorial/first-learning-scenario.md).
3. Keep the [first-game checklist](./tutorial/first-game-checklist.md) beside the board.
4. Use the [first-game session sheet](./tutorial/first-game-session-sheet.md) to record questions and board states.
5. Try the optional [Clear the Room mini-drill](./tutorial/05-first-learning-scenario.md) after the beginner game.

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
- A beginner-game guide, checklist and session sheet are available.
- The beginner materials still need a complete, rules-verified end-to-end play-through before the milestone can be called fully validated.
- The rules engine and camera prototype are future development steps; neither is claimed to be working yet.

## Next milestone

Play through the beginner guide step by step, record any unclear rules or missing setup details, and update the tutorial before building more AI features.

## Repository

https://github.com/JamSpot/6-siege-ai-table
