# 6: Siege AI Table

A learning tutorial and experimental platform for playing **6: Siege – The Board Game**, with the long-term goal of building a physical-table AI opponent.

## Project goals

1. Teach the game progressively, from the battlefield and core actions through to a complete game.
2. Build a precise digital representation of the board and game state.
3. Develop a rules engine that can determine legal actions.
4. Develop an AI player that chooses actions for one side.
5. Use an overhead camera to recognise the physical board, Operators, facing and game-state changes.
6. Have the human player physically move the AI's pieces, with the system checking the resulting board state.

## Development philosophy

The physical game remains the source of truth. The computer should assist the human rather than replace the tabletop.

The intended architecture is:

Camera → Board State → Rules Engine → Legal Actions → AI Decision → Human Instruction → Camera

## Status

Early project setup. Tutorial and technical specifications will be added incrementally.

## Repository

https://github.com/JamSpot/6-siege-ai-table
