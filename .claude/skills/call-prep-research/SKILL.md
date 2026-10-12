---
name: call-prep-research
description: Research a person's professional background (given their name, company and role) and draft personalised questions plus talking points for a call or informational interview. Use when asked to prepare for a call, research someone before a meeting, or draft questions for a professional.
---

# Call prep research

Input needed from the user: **full name, company, role**, plus (ask if missing, one short question) the user's own background, the industry they are exploring, and the call's goal (e.g. informational interview, mentorship, job lead). Do not invent the user's background.

## Scope
Professional, public information only: career history, education, publications, talks, podcasts, interviews, patents, projects, company news, opinions the person has published. Skip family, home address, personal social accounts, health, or anything not meant for professional audiences. Mention people with the same name only to rule them out.

## Research (use WebSearch + WebFetch; run searches in parallel)
1. **Identity check**: confirm the right person via company site, LinkedIn-style bio, conference pages. State confidence; if ambiguous, ask the user.
2. **Career arc**: prior employers, roles, dates, pivots, education. Note *why* moves likely happened (acquisitions, industry shifts) and label inference as inference.
3. **Own words**: interviews, podcasts, talks, articles, posts. Quote or paraphrase with source URL. These produce the best personalised questions.
4. **Company context**: recent funding, launches, strategy, competitors, and where this person's role fits.
5. **Industry context**: 2-3 current trends/debates in the field the user wants to enter.
6. Use extended search mode if standard results are thin. Every factual claim gets a source link; unverified items are marked "unverified". Never fabricate.

## Output (write to `call-prep/<person-name>.md`)
1. **Snapshot**: 5-line summary and confidence in identity.
2. **Timeline** of roles with sources.
3. **Themes & hooks**: things they care about, with sources.
4. **Questions (8-12)**, grouped: career path/pivots, day-to-day, industry outlook, advice for entering. Each question must reference something specific about them (not answerable by a generic template). Order from warm-up to deeper. Include a few that sound like real thinking-in-progress, e.g. "I've been weighing X vs Y; how did you think about that when you moved from A to B?" — only if it truthfully reflects the user's situation.
5. **For each question**: why you're asking, a likely answer from their public record, and a good follow-up.
6. **Your side**: a 30-second intro and 3 honest reasons for interest in the industry, built from what the user told you (flag gaps to fill in, don't make them up). Confidence comes from specifics and preparation, not overstated claims.
7. **Questions they may ask you** with suggested talking points.
8. **Sources** list.

Keep the final chat reply to a short summary plus the file path.
