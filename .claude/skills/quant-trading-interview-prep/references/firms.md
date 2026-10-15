# Firm-by-firm: what is reported to be tested

Compiled 2026-10-15. **Primary source (firm-official):** Jane Street's "Probability & Markets" guide (see `jane-street-official-guide.md`).
Everything else is **third-party, candidate-reported, and often from sites that sell prep** (quantt.co.uk, quantvault.org, techinterview.org,
tradermath.org, quantbrainteasers.com). Firms change formats between cycles without notice; sources conflict. Check your own invite.
Pages read in full via curl this session: quantt OA guide, techinterview SIG + Optiver, quantvault mental-math + books + market-making, tradermath HRT,
quantvault DRW, quantbrainteasers Jane Street. Not readable: quantnet (HTTP 403), reddit (blocked by the search tool).

| Firm | Reported process | What it weighs |
|---|---|---|
| **Optiver** | OA historically led by "80 in 8" (80 four-option arithmetic Qs, 8 min, +1/-1, no calculator, ~55 net reported pass line, 70+ competitive; Optiver publishes no cutoff). Also NumberLogic (sequences), Beat the Odds (probability), Zap-N games. 2026/27 invites reportedly add Likelihood-list, Intervals and Orderbooks modules and may drop the 80 in 8; retake limited to once per 8 months (Optiver Europe FAQ via quantt). Then phone (behavioural + 2-4 brainteasers), technical (probability + market making on an unknown number / sum of dice), Optiver Day with live trading game. | Speed + accuracy, EV, options market making, staying calm/coachable |
| **IMC** | Trader OA changes yearly: SHL 40-min inductive-reasoning (2027 US reports), BrainsFirst NeurOlympics games (2025), 15 math/prob Qs in 1h (2023); "24 in 18" number sequences reported elsewhere. Then trading game / options market-making sim; coding for traders. | Pattern reasoning, speed, pricing under pressure |
| **Jane Street** | Historically straight to phone interviews for trading, no standardised OA (some cycles/regions short quizzes). Phone: probability + EV; final: market-making game + strategy/betting games, estimation, some coding. Official guide covers probability, EV, confidence intervals, conditional probability, making markets, adverse selection, recursion. | Reasoning aloud, EV, market making, adapting to changed assumptions |
| **SIG** | OA by Mercer|Mettl: 17 Qs / 60 min "Problem Solving Assessment" (probability, EV, combinatorics, Bayes, Markov chains, a little calculus/logic; calculator allowed, counter-intuitive answers common). Phone: coin/dice EV, poker pot-odds ("30% to win, pot $100, opponent bets $50: call?"), "make a market on the number of dominoes". Onsite: back-to-back trader interviews, group trading game, poker/decision-theory discussion, behavioural. Trader training includes poker. | EV and decision-making under uncertainty, poker/game theory, options |
| **Citadel / Citadel Securities** | OA is usually HackerRank (2-3 problems, 60-90 min, LeetCode medium-hard; some research tracks add prob/stats MCQ). Phone/onsite: EV of asymmetric games, dice waiting times, project questions. | Coding bar is high for the OA; probability/EV in interviews |
| **DRW** | Trader/researcher OA: ~6 fill-in problems / 45 min, take-home timed: probability, statistics, Markov chains, linear algebra (matrix unknowns, covariance, CLT tails, dice EV), no speed arithmetic. Then probability + brainteasers (streaks, gambler's ruin, waiting times, order statistics), trading intuition + market making (estimation, options basics, pirate game, AKQ, Penney's game), onsite. | Probability depth, game theory, trading sense |
| **HRT** | OA: HackerRank 3 problems LeetCode med-hard, often simulation / timestamped-trade data processing. Phone: green-book-style probability + live coding (e.g. poker-hand simulation). Onsite ~5 rounds: coding, probability, EV/strategy games (derive strategy then validate by simulation), data analysis in a notebook. | Probability **and** strong coding, in the same round |
| **Akuna** | Trader probability test (30 fill-in Qs, ~12 min) + timed mental math block; Options 101 self-paced course/quiz is part of some funnels (the firm hands you the syllabus). Later: brainteasers, market-making games, derivatives basics. | Fast probability, options basics |
| **Flow Traders / Maven / Five Rings** | Arithmetic sprints (Flow ~8 min then ~25 min sequences, wrong answer costs a point; Maven ~50 Qs/5 min; Five Rings 17-20 fill-in Qs mixing arithmetic, probability, estimation, camera on). | Mental maths + sequences |
| Virtu / Two Sigma | HackerRank-style coding OAs (Two Sigma researcher tracks sometimes stats/prob MCQ). | Coding |

## Trader vs researcher
Trader loops: speed (firm-dependent), probability/EV, market-making and betting games, light-to-moderate coding.
Researcher loops: statistics/ML validation, take-home data challenge, solid Python. Jane Street (via quantbrainteasers) says do not prepare QT and QR identically.
Firm type often matters more than title: prop market makers (Optiver, SIG, IMC) vs engineering-first (HRT) vs multi-strat (Citadel).

## Prep-folklore vs the official guide
Prep sites stress mental-math speed for Jane Street; Jane Street's own guide says you need not be great at mental maths or complicated maths, and that a wrong answer is not an automatic fail. Speed is genuinely a filter at Optiver, Flow, Maven, Five Rings and IMC.
