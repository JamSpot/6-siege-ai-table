# Lesson 2 — Movement, Facing & Line of Sight

This is the first hands-on mechanics lesson. Put the board in front of you and physically move the Operators as you work through the exercises.

## The three things to learn

1. **Movement** — an Operator normally has a movement allowance of five squares.
2. **Facing** — where the Operator is facing matters when checking attacks and protection.
3. **Line of sight (LOS)** — LOS is checked between the central dots of the relevant spaces.

The official FAQ clarifies that LOS is an imaginary straight line linking the central dots of two spaces. An Operator cannot target their own space with an action that requires LOS.

## 1. Moving

When an Operator is activated, their normal movement is up to **five squares**. The Operator profile's Run value tells you how far that particular Operator can move when using the Run action.

Movement and actions can be interleaved. For example:

- move 2 squares;
- Shoot;
- move 3 more squares;
- Watch.

Each action must be legal at the point it is performed.

### Exercise 1 — Five-square movement

Take one Attacker.

1. Start at an entry point.
2. Move one square.
3. Count the remaining movement.
4. Continue until you have used five movement points.
5. Reset the Operator.
6. Try a different route.

Now repeat the exercise while deliberately moving around obstacles.

**Important:** obstacles can increase the movement cost when entering their square.

## 2. Facing

Treat facing as part of the Operator's physical state.

For the future AI system, a board position without a facing direction is incomplete.

After moving an Operator, deliberately rotate them and observe how their orientation changes the tactical situation.

We will cover the detailed facing/protection interactions separately.

## 3. Line of sight

The simplest reliable way to learn LOS is to use the game's LOS tool.

Put Operator A in one space and Operator B in another.

Check the imaginary straight line between the **central dots** of their spaces.

Then repeat with:

- a clear route;
- a wall between them;
- a corner;
- an obstacle;
- a holed wall.

Walls are impassable for movement. A holed wall does not block LOS, so an Operator may perform actions through it that require LOS.

### Exercise 2 — LOS drill

Set up five pairs of spaces:

**A. Clear:** confirm LOS.

**B. Solid wall:** confirm that the wall blocks movement and LOS.

**C. Corner:** move one Operator around the corner and check how LOS changes.

**D. Holed wall:** check that the hole permits LOS while the wall remains impassable to movement.

**E. Same space:** confirm that an Operator cannot target their own space with an action requiring LOS.

## 4. Leaning

Leaning is one of the game's important positioning rules.

A crouched Operator can lean to look beyond a wall angle while retaining the protection provided by the adjacent space. Leaning and straightening cost movement points.

For now, practise the physical idea:

1. Put an Operator next to a wall angle.
2. Place an enemy where the Operator cannot see them normally.
3. Lean.
4. Re-check LOS.
5. Straighten.
6. Re-check LOS.

We will teach the exact protection consequences in the Cover & Protection lesson.

## 5. Why this matters to our AI

This lesson gives us the first pieces of the machine-readable board state.

A future camera frame should eventually become something like:

```text
Attacker: Ash
position: room/square X
facing: direction N
stance: crouched
lean: left
visible enemies: ...
```

The rules engine can then ask:

> Given this position, facing, stance and the current terrain, which actions are legal?

That is the bridge between the physical board and the AI.

## 6. Five-minute practice challenge

Without worrying about winning:

1. Put two Operators on the board.
2. Give each a clear starting position.
3. Move one Operator five squares.
4. Stop at a position where LOS is blocked.
5. Change position until LOS is available.
6. Rotate the Operator.
7. Lean around a wall angle.
8. Check LOS again.
9. Reset and repeat from a different route.

When you can do this without reaching for the rulebook every few seconds, you are ready for **Lesson 3 — Actions & Combat**.

## Research basis

This lesson was checked against the published 6: Siege FAQ/Errata and the current operator overview. The FAQ covers central-dot LOS and holed-wall interactions; the operator overview covers movement, Run, actions and leaning.
