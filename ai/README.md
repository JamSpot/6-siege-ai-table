---
layout: guide
title: "AI Opponent"
permalink: "/ai/README.html"
previous_url: "/rules/README.html"
previous_title: "Rules engine"
next_url: "/vision/README.html"
next_title: "Board vision"
---
# AI Opponent

The AI opponent will eventually choose actions for one side of a physical game.

The AI should not be responsible for enforcing basic rules. A deterministic rules engine will first generate legal actions; the AI then evaluates those actions and selects one.

Planned pipeline:

Game State → Legal Actions → Evaluation → Selected Action → Human Instruction
