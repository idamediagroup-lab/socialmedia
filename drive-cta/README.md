# CREDIT SCRIPTS — bulk CTA update

Changes every comment/DM call-to-action in the CREDIT SCRIPTS Drive folder to:

    Comment "SCORE" to learn more

## Why a script

The Google Drive connector can read, search, create and move files, but it
cannot edit the body of an existing Google Doc — its update call takes only a
title and a parent folder. With 210+ docs to change, a script that runs inside
the Drive account is the only route that actually edits them.

## How to run

1. Go to script.google.com → New project
2. Paste in `update-ctas.gs`
3. Run `dryRun()` — changes nothing. View → Logs shows every CTA it found,
   what it would become, and which docs have no CTA at all.
4. Read the log. If it looks right, run `applyChanges()`.

Authorise when prompted. It only touches folder 1tFVZXcmZull85ZZX2YwgRMcwP8wPbRY9.

## What it matches

| Pattern in the docs | Result |
|---|---|
| `Comment "FUNDING" if you want…` | `Comment "SCORE" to learn more` |
| `COMMENT "MENTEE" TO JOIN THIS TRIBE` | `Comment "SCORE" to learn more` |
| `Comment MENTEE to learn how` (unquoted) | `Comment "SCORE" to learn more` |
| `Comment the word "ONE" below` | `Comment "SCORE" to learn more` |
| `DM the word UNIONS for the free ebook` | `Comment "SCORE" to learn more` |
| `DM me "APPLE" and I'll send it over.` | `Comment "SCORE" to learn more` |

Skipped on purpose: CTAs already saying SCORE, and ordinary prose such as
"I commented on his post yesterday."

## Not matched

Non-trigger CTAs are left alone, because they ask for a different action:
"Tag a friend", "Vote below", "Read caption", "Join our waitlist".
If you want those swapped too, say so and I'll extend the patterns.

## Trigger words found so far
MENTEE · CLASS · ONE · LOAN · FUND · FUNDING · CHARGE · APPLE · UNIONS
