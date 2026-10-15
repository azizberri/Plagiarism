# Jane Street "Probability & Markets" guide - what the firm itself says

Source: https://www.janestreet.com/probability-markets/ and the PDF https://www.janestreet.com/static/pdfs/trading-interview.pdf (read in full 2026-10-15; 12 pages). Jane Street says it is an intro, not required reading, and that people new to this are "in good company".

Sections: Randomness, Counting, Probabilities, Independence, Random Variables, Expected Value, Confidence Intervals, Conditional Probability, Making Markets, Adverse Selection, Problem Solving Tools (recursion, edge cases), Interview Thoughts.

Key content to study from it:
- **Making markets vocabulary**: bid/offer, size, "I'm 2 at 4, 10 up", hit/lift ("sold", "take 'em"), fills. Buy below expected value, sell above; balance trade likelihood against edge; consider downside vs your capital.
- **Practice prompts in the guide**: make markets on a d20; max of 3 d6; a d6 with a one-time reroll option (who decides to reroll?); temperature in an hour; 1,000,000 x a d6 (how would you feel if the bid is hit and it rolls 1?).
- **Adverse selection**: the trade you are given is worse than it looks; ask "conditional on my order being filled, what is the expected value now?"; be warier when the value is hard to determine. After a fill, update your fair value.
- **Confidence intervals / calibration**: people are overconfident (95% intervals contain the truth less than 95% of the time); practise on checkable facts (example: number of taxis in NYC), but don't overcorrect.
- **Conditional probability**: priors, updating, P[A|B]=P[A and B]/P[B]; example E[d6 | roll >= 4] = 5.
- **Recursion / memorylessness**: expected flips to first heads = 2 (1/p in general); expected flips for 3 heads in a row (exercise).
- **Edge cases and small cases**: test 0, 1, infinity; solve 2 players before 100.
- **Interview Thoughts (official myths debunked)**: you do not have to be really good at mental maths (numeracy and order-of-magnitude checks help; no one judges you for not multiplying two-digit numbers in 5 s); not complicated maths (they prefer the simple intuitive answer to esoteric theorems); you do not "fail" for a wrong answer (it is a collaboration; ask for clarification; how you take hints and respond to being wrong counts; getting it right is not enough, explain how); no required persona, it is fine to say you are unsure and take your time.

Unofficial companion (quantbrainteasers.com, 2026): sequence "fundamentals -> follow-up variants -> turn calculations into decisions (what would you pay?)"; avoid memorising questions and avoid staying silent. Its suggested 2-week plan: probability, EV, optimal stopping, strategic games, market making, mixed review.
