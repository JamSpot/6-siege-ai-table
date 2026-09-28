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

## 3. Set up only what we need

For your first learning session:

1. Choose one map from the core box.
2. Choose a simple Control mission.
3. Put the mission components on the map as instructed by the mission guide.
4. Choose a small team of Operators for each side rather than trying to learn the entire roster.
5. Put the Operator profile cards where both players can see them.
6. Put dice, the line-of-sight tools, movement/activation markers and other commonly used components beside the board.
7. Do the normal deployment for the chosen mission, but **do not worry about playing at full speed yet**.

The real game also uses a timed system. There is an official companion app with different speed settings, including Beginner, Chill, Standard and Extreme. For learning, use the least stressful setting and concentrate on understanding the sequence first.

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

## 7. Don't use the timer yet

For your first learning game, leave the pressure of the real-time system aside.

First learn:

**where pieces can go → what they can see → what they can shoot → how objectives work.**

Then introduce the timer.

The official game supports different timer speeds, so we can progressively move you from learning mode to proper timed play.

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

- Steamforged Games — current publisher/project information.
- BoardGameGeek — game overview and gameplay structure.
- Official 6: Siege FAQ/Errata — rule clarifications.

See the project README for the developing AI-table architecture.
