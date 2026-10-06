# Lesson 4 — Combat

This lesson introduces the basic attack workflow. Keep the relevant Operator cards beside the board and resolve each step from the current rules rather than trying to memorise every weapon interaction.

## 1. Before attacking

Check all of these before declaring the attack:
1. The attacker is activated and can perform the action.
2. The chosen weapon is available to that Operator.
3. The target is a legal target.
4. The attacker has the required line of sight.
5. Range and any weapon restrictions are satisfied.
6. The target's position, stance and protection are taken into account.

If any prerequisite fails, choose a different action or position.

## 2. Build the attack

Use the attacker's profile card and the current weapon information to determine the appropriate attack dice and modifiers.

Do not guess the dice pool. The weapon/profile determines it.

Then resolve the attack using the game's combat procedure.

## 3. Resolve the result

After rolling, apply the relevant result according to the current rules and the target's protection.

Then update the physical board:
- damage/health state;
- removed or placed markers;
- changed position or status;
- any effect caused by the attack.

The important learning habit is:

> **Resolve the result completely before starting the next action.**

## 4. Cover and protection

Protection is not just a cosmetic feature of the terrain.

Before firing, ask:

> What is protecting the target?

Check the target's position, stance and the terrain between the two Operators. Use the official protection/LOS rules and reference material for the exact interaction.

We will give cover and protection their own focused lesson because they are central to good tactical play.

## 5. Combat practice

Set up two Operators with a clear line of sight.

### Drill A — Clear shot
1. Activate the attacker.
2. Confirm range.
3. Confirm LOS.
4. Check the weapon.
5. Resolve the attack.
6. Apply the result.
7. Record the new board state.

### Drill B — Change position
Move the attacker to another legal position.

Repeat the attack and compare:
- range;
- protection;
- available actions;
- resulting position.

### Drill C — Change the target's protection
Move the defender behind a different piece of terrain.

Check LOS and protection again before attacking.

The point is not to maximise damage yet. It is to learn how **position creates or removes attack opportunities**.

## 6. The AI-table connection

Combat gives us another important rules-engine boundary.

The camera should report facts such as:

    attacker position
    attacker facing
    target position
    target facing
    terrain
    stance
    damage state

The rules engine should then determine:

    Can attack?
    Which weapons are legal?
    Which targets are legal?
    What attack data applies?
    What protection applies?
    What outcomes are possible?

The AI should make the tactical choice **after** the rules engine has generated legal possibilities.

That separation prevents the AI from inventing illegal moves.

## 7. First mini-battle

Now combine Lessons 1–4.

Give each side one Operator.

For each activation:
1. Move.
2. Check LOS.
3. Choose a legal action.
4. Attack when an attack is available.
5. Apply the result.
6. Continue until the activation ends.

Do not introduce every advanced rule yet. The objective is to make the basic loop comfortable:

**position → LOS → action → combat result → new position**

Once this feels natural, we can add protection, gadgets, special abilities and the full mission rules.

## Next

**Lesson 5 — Cover, Protection & Advanced Positioning**.

After that, the tutorial will have enough core mechanics to build a controlled first learning scenario and begin testing the rules-engine representation against actual board states.