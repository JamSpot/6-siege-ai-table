# Lesson 3 — Activation & Actions

The aim of this lesson is to understand what an Operator can actually do during an activation.

## The core idea

Do not think of an activation as "move the miniature and then stop." An Operator can perform actions in sequence, provided each action is legal and the Operator has the required action points.

For learning, keep asking three questions:

1. **What actions does this Operator have available?**
2. **Is the action legal from the Operator's current position and facing?**
3. **What does performing it change on the board?**

## 1. Read the Operator card first

Before activating an Operator, put their profile card beside the board.

Identify:

- movement/Run information;
- weapons;
- special abilities;
- gadgets;
- any restrictions or costs.

Do not try to memorise the whole card.

## 2. Plan before moving

Pick one simple objective for the activation:

> "Move into a position where I can see the enemy."

Then work backwards.

1. Where do I want to finish?
2. How far away is that position?
3. Which route gets me there?
4. Will I still have the action I need after moving?
5. Does the new position expose me to an enemy?

This habit will become important when the AI starts evaluating legal actions.

## 3. Action sequence exercise

Place two opposing Operators on the board.

For your active Operator:

1. Choose a destination.
2. Move.
3. Re-check line of sight.
4. Choose a legal action.
5. Resolve it using the Operator card and current rules.
6. Record what changed.
7. Continue only if another action is available and legal.

Do not invent an action because it "looks right." The profile and rules determine what the Operator can do.

## 4. Movement is part of decision-making

A common beginner mistake is moving as far as possible simply because movement is available.

Instead ask:

> **What do I gain by spending this movement?**

Sometimes the best move is shorter because you want to preserve a useful position, maintain protection, or keep a line of sight.

## 5. The AI-table connection

This is where our physical-board project starts to become a rules problem.

A future digital state might look like:

```text
Round: 1
Active team: Attackers
Active operator: Ash
Position: B4
Facing: North
Remaining actions: ...
Visible enemies: ...
Available gadgets: ...
Terrain around operator: ...
```

The rules engine will eventually generate a list of legal actions from this state.

For example:

```text
LEGAL ACTIONS
- Move to B5
- Move to C4
- Shoot target X
- Use gadget Y
- Watch
```

The AI then evaluates those legal choices.

The camera does not decide what is legal. **The rules engine does.**

That separation is a key design decision for the project.

## 6. Practice challenge

Run three activations without worrying about winning.

For each activation, write down:

- starting position;
- starting facing;
- intended goal;
- movement;
- action chosen;
- resulting position;
- resulting facing;
- anything that changed.

Then ask:

> "Could another legal action have produced a better position?"

That question is the beginning of tactical AI.

## Next

**Lesson 4 — Combat** will turn the activation framework into a complete attack sequence. After that we can assemble the movement, LOS and combat lessons into a properly controlled first-game exercise.
