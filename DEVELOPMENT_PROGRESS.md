2. Keep V1 completely frozen
Do not make any more changes to the V1 backup.

We have:

V1
│
├── Local ZIP backup
├── Private GitHub archive
└── Locked baseline

Our V2 working copy is:

D:\Coding\Trading-Dashboard

3. Tomorrow's first step should NOT be coding
When you come back, simply tell me something like:

"Let's start Trading Dashboard Version 2."

I will first use the documents you've provided to establish the context, then inspect the current source code.

Our sequence will be:

V1 Documentation
       ↓
Project Structure
       ↓
Development Environment
       ↓
Current Source Code
       ↓
Performance Baseline
       ↓
Identify Actual Bottlenecks
       ↓
V2 Optimization

We should not immediately start rewriting code.

4. One thing I specifically want to avoid
I don't want us to make architectural decisions based only on our earlier assumptions.

Tomorrow, I'll compare the V2 requirements against the actual current V1 code.

For example, if we said:

"This part probably does a linear search."

I'll verify the actual implementation first.

If it does, we'll optimize it.

If it doesn't, we'll optimize whatever the actual bottleneck is.

That keeps the work evidence-based rather than theoretical.

Our V2 starting contract
This is effectively what we've locked in:

Source:

D:\Coding\Trading-Dashboard

V1:

LOCKED

Local Git:

Not installed / not used

Primary goal:

Performance + RAM efficiency

Priority:

1. Crosshair
2. Data loading
3. Timeframe processing
4. Memory usage
5. Python ↔ JavaScript communication
6. QWebEngine/chart rendering
7. Drawing performance

Constraint:

The laptop has limited RAM, so performance improvements must not simply trade CPU usage for excessive memory consumption.

Development philosophy:

Measure → optimize → test → compare → keep/revert.

V1 functionality:

Must remain intact.

New features:

Not during the initial optimization phase.

That's enough context to start properly tomorrow. We don't need another requirements round.
