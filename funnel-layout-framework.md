# Funnel Layout Framework — Free Masterclass → High-Ticket Offer

> **Purpose:** A reusable blueprint for laying out a paid-traffic masterclass /
> webinar funnel. Read this before designing any new funnel of this type. It
> covers what pages exist, what each page's *one job* is, what blocks go on each
> page, in what order, and why that order is the order.
>
> **Archetype covered:** cold paid traffic (Meta/IG ad) → free masterclass
> registration page → confirmation page → reminder sequence → masterclass →
> application/call → enrollment in a high-ticket program.
>
> This is the funnel shape behind almost every `[offer]masterclass.com` /
> `[offer]workshop.com` style dedicated-domain landing page you see in the feed.
> Section 13 covers how to adapt it for low-ticket and self-checkout offers.

---

## 1. The governing principle

Everything in this framework comes from one idea:

> **One page. One decision. One belief closed at a time.**

A visitor coming off an ad is not deciding whether to buy your $5,000 program.
They are deciding *one much smaller thing*: "do I give up my email and an hour
of my life?" The entire registration page exists to win **that** decision and
nothing else.

The page sells the **masterclass**, not the program.
The masterclass sells the **program**.

Getting this backwards is the single most common funnel design failure. If the
registration page starts pitching the $5k offer, prices, payment plans, or
"apply now" language, it is doing the masterclass's job and it will convert
worse.

### The belief ladder (why sections are in the order they're in)

Page sections are not decoration. Each block exists to close one specific
objection, laid out **in the order a real visitor forms those objections**:

| # | The visitor's silent question | The block that answers it |
|---|---|---|
| 1 | "Am I in the right place?" | Eyebrow + headline (message match to the ad) |
| 2 | "What exactly is this and what does it cost me?" | Format line: free, live, date, time, duration |
| 3 | "Do I even want this outcome?" | Subhead + the "is this you?" pain block |
| 4 | "Is this outcome actually achievable?" | The 3 Secrets / what-you'll-learn block |
| 5 | "Who are you to teach it?" | Host authority block |
| 6 | "Has it worked for people like *me*?" | Social proof block |
| 7 | "What's the catch / what do I risk?" | Objection + FAQ block |
| 8 | "Why now and not later?" | Scarcity / urgency mechanism |
| 9 | "Fine — how do I get in?" | Final CTA |

**Rule:** never answer question 6 before you've answered question 3. Testimonials
placed above the pain block are wasted — the reader doesn't yet care.

If you only remember one thing from this document: **lay out sections in
objection order, not in "what looks nice" order.**

---

## 2. The funnel map

Six assets. Build them in this order; do not launch traffic until all six exist.

```
  META AD (image/video + long-form copy)
        │  message match must survive this jump
        ▼
  ① REGISTRATION PAGE ──────── job: capture name/email/phone
        │
        ▼
  ② CONFIRMATION PAGE ──────── job: lock in attendance + first micro-yes
        │
        ▼
  ③ REMINDER SEQUENCE ──────── job: get them to actually show up
     (email + SMS, ~6-9 touches)
        │
        ▼
  ④ THE MASTERCLASS ────────── job: shift beliefs, then make the offer
        │
        ▼
  ⑤ APPLICATION + BOOKING ──── job: qualify and schedule
        │
        ▼
  ⑥ CALL CONFIRMATION + ────── job: reduce no-shows, pre-frame the call
     NURTURE / REPLAY
```

**Each asset gets exactly one conversion event.** Write it down before you design
the page. If you can't name the single event, the page isn't designed yet.

**Dedicated domain, not a subpage.** This archetype almost always lives on its
own exact-match domain (`speakmoremakemoremasterclass.com`) rather than
`yoursite.com/masterclass`. Reasons, in order of importance:

1. **No escape hatches.** A dedicated domain has no header nav, no blog, no
   "About" link, no store. Every exit is the CTA or the back button.
2. **Message match.** The domain itself continues the ad's promise. The visitor
   reads the URL as confirmation they landed in the right place.
3. **Clean tracking.** Pixel/CAPI events, UTM data, and lookalike-source traffic
   aren't contaminated by organic site visitors.
4. **Reputation isolation.** If the domain gets flagged in ad review, the main
   business site isn't caught in it.

---

## 3. Asset ① — The registration page, block by block

This is the page most of your design time goes into. Here is the full stack.

### 3.0 Wireframe

```
┌──────────────────────────────────────────────┐
│ [A] ANNOUNCEMENT BAR — free · live · date    │  ← ~40px, high contrast
├──────────────────────────────────────────────┤
│ [B] HERO                                     │
│     eyebrow: FREE ONLINE MASTERCLASS         │
│     H1: outcome + timeframe + mechanism      │  ← THE FOLD
│     subhead: who it's for + what they leave  │     everything above
│     with                                     │     this line must
│     ▸ date · time · duration · "live"        │     load in <2s
│     [ ██ PRIMARY CTA BUTTON ██ ]             │
│     micro-copy: 100% free · limited seats    │
│     (host photo or 30-60s promo video)       │
├──────────────────────────────────────────────┤
│ [C] CREDIBILITY STRIP — logos / numbers      │
├──────────────────────────────────────────────┤
│ [D] "IS THIS YOU?" — 3-5 pain bullets        │
├──────────────────────────────────────────────┤
│ [E] WHAT YOU'LL LEARN — the 3 Secrets        │
│     [ CTA #2 ]                               │
├──────────────────────────────────────────────┤
│ [F] HOST AUTHORITY — story, not résumé       │
├──────────────────────────────────────────────┤
│ [G] SOCIAL PROOF — 3-6 specific results      │
│     [ CTA #3 ]                               │
├──────────────────────────────────────────────┤
│ [H] OBJECTIONS / FAQ — 4-6 items             │
├──────────────────────────────────────────────┤
│ [I] URGENCY — seats / cohort date / timer    │
├──────────────────────────────────────────────┤
│ [J] FINAL CTA — restate promise + button     │
├──────────────────────────────────────────────┤
│ [K] FOOTER — legal, disclaimers, privacy     │
└──────────────────────────────────────────────┘
        + STICKY MOBILE CTA BAR (appears after
          the user scrolls past the hero)
```

### 3.1 [A] Announcement bar

- One line, full width, highest-contrast color on the page.
- Contains the three facts that set the frame: **free**, **live**, **when**.
- Example: `FREE LIVE MASTERCLASS · THURSDAY 7PM ET · LIMITED SEATS`
- Do not put a CTA here. Its job is framing, not conversion.

### 3.2 [B] Hero — the only block that must be perfect

Roughly 80% of visitors who bounce never scroll past the hero. Budget your
effort accordingly.

**Eyebrow (2-5 words).** Categorizes the page instantly: `FREE ONLINE
MASTERCLASS`. This kills the "is this a sales page?" hesitation before the
headline is even read.

**H1 headline.** The formula that works most reliably:

> **How to [specific desirable outcome] in [timeframe] — without [the thing
> they dread / the obvious-but-wrong method]**

Rules:
- Name a **specific, measurable outcome**, not a feeling. "Book 3 paid speaking
  gigs in 90 days" beats "Become a confident speaker."
- Include a **timeframe**. It makes the claim concrete and creates urgency
  without a countdown.
- Include the **"without"**. This is where your differentiation lives — it names
  the mechanism by exclusion and pre-frames why their previous attempts failed.
- 8–16 words. Longer reads as a paragraph; shorter loses specificity.
- Mobile type size: 28–34px. Test it on a phone before anything else.

**Subhead (1–2 sentences).** Two jobs: **name the audience explicitly**
("For coaches and consultants who…") and **state what they walk away with**.
The audience callout is a qualifier — it should make the wrong people leave.
That's a feature, not a leak.

**Format line.** Date, day, time *with timezone*, duration, and the word
"live" if it's live. Explicit duration ("90 minutes") materially raises
registration and show-up rates because the reader can price the commitment.

**Primary CTA button.** See 3.3.

**Risk-reducer micro-copy** directly under the button, small type:
`100% free · No pitch until the end · Replay not guaranteed`. Every word here
removes a specific fear.

**Hero visual.** Either a photo of the host (looking *toward* the CTA — eye
direction measurably pulls attention) or a 30–60 second promo video. If you use
video: never autoplay with sound, always a visible play button, and **the page
must convert with the video ignored**. Video is a booster, not the mechanism.

### 3.3 The registration mechanism

Two viable patterns:

**Two-step (recommended default).** The hero shows a button, not a form.
Clicking opens a modal with the fields. This usually outperforms an inline form
on cold traffic because the button click is a costless micro-commitment, and
people finish what they start.

**One-step inline form.** Fields sit directly in the hero. Better for warm
traffic, retargeting, and audiences who already know you.

**Field count:** every field costs conversion rate.
- **Name + Email** — highest conversion, weakest follow-up.
- **Name + Email + Phone** — the standard for this archetype, because SMS
  reminders are the single biggest lever on show-up rate. The trade is worth it.
- **Anything more** on a *free* registration is almost always a mistake. Save
  qualifying questions for the application step (Asset ⑤), where the prospect is
  motivated enough to answer them.

**Button copy:** first person, outcome-flavored, never "Submit."
- `Save My Free Seat` · `Yes — Reserve My Spot` · `Send Me The Link`
- Add the price frame *in the button* if the offer is free: `Register Free →`

**Consent:** if you collect a phone number, put explicit SMS consent language
adjacent to the button. This is both a legal requirement in most jurisdictions
and a deliverability protection.

### 3.4 [C] Credibility strip

Immediately below the fold. A thin band of borrowed authority: press logos,
brands worked with, or a hard number (`4,200+ students trained`,
`$18M in client revenue`). Only use what's true and verifiable. Its job is to
buy you the next 10 seconds of attention.

### 3.5 [D] "Is this you?" — the pain block

3–5 bullets, written **in the reader's own words**, present tense, first person.
Each one should be so specific that the right reader thinks "how do they know
that?"

- Weak: "You struggle with visibility."
- Strong: "You've spoken for free four times this year and still haven't been
  paid once."

Format as a checklist with checkmarks or a light icon. Keep bullets under 15
words each — this block is scanned, not read.

End the block with a bridging line: `If you nodded at any of those, this
masterclass was built for you.`

### 3.6 [E] "What you'll learn" — the 3 Secrets

The load-bearing content block. The convention is **exactly three** items —
enough to feel substantial, few enough to remember, and it mirrors the
three-part structure of the masterclass itself.

Each of the three should follow this shape:

> **Secret #1: [Curiosity-driving name] — how to [outcome] without [objection],
> even if [their specific disqualifying belief].**

The three should map to the three beliefs that must break for someone to buy:

1. **The vehicle belief** — "this method/approach actually works."
2. **The internal belief** — "I personally can do this."
3. **The external belief** — "my circumstances won't stop me."

That's not a copywriting flourish; it's the architecture. If your three items
are just "topics," rewrite them until each one attacks one of those beliefs.

**Do not fully teach here.** Name the outcome, not the how. Curiosity is what
gets the registration; resolution is what the masterclass delivers.

Place **CTA #2** at the end of this block. This is the highest-intent scroll
depth on the page.

### 3.7 [F] Host authority

A résumé does not convert. A **transformation story** does. Structure:

1. **Where I was** — the relatable low point (specific and unflattering).
2. **What changed** — the discovery/mechanism, stated in one line.
3. **Where I am now** — proof, with numbers.
4. **Why I teach it** — the mission line that makes it not-about-money.

4–6 short paragraphs, one photo, first person. Credentials belong here as a
supporting line, never as the lead.

### 3.8 [G] Social proof

3–6 testimonials. Quality bar, in descending order of power:

1. **Video** testimonials (30–60s).
2. **Screenshots** of real messages/DMs/results dashboards.
3. **Photo + full name + specific numeric result.**
4. Text + first name only. ← weakest; treat as filler.

Every testimonial should contain a **number or a before/after state**. "Amazing
program, changed my life" is decorative. "Went from $0 to three $5k keynote
bookings in 11 weeks" is evidence.

Choose testimonials that mirror your **audience's starting point**, not your
best-ever result. The reader is asking "someone like me," not "someone
impressive."

Place **CTA #3** here.

### 3.9 [H] Objections / FAQ

4–6 items. Answer the real objections, not softballs. For this archetype the
standing four are almost always:

- "Is this actually free?" → Yes, and say what you'll offer at the end. Naming
  the pitch honestly increases both registration and show-up quality.
- "Will there be a replay?" → Answer strategically. "Replay only for live
  attendees" protects live attendance, which is where conversion happens.
- "How long is it?" → Exact duration.
- "Is this for me if I'm just starting / already experienced?" → Reassure the
  segment you actually want, and gently exclude the one you don't.

Accordion UI is fine here — this block is for the minority who need it, and
collapsing it keeps the page short for everyone else.

### 3.10 [I] Urgency mechanism

Urgency must be **real**. Fake countdown timers that reset on refresh are both a
trust risk and an ad-policy risk. Legitimate options:

- A genuine **cohort date** — the class happens Thursday; Thursday is the timer.
- A genuine **seat cap** tied to your platform's actual limit.
- **Registration close time** ("doors close 1 hour before we start").

If nothing is genuinely scarce, use the date and drop the timer. A calendar date
is honest urgency and works fine.

### 3.11 [J] Final CTA

Restate the headline promise in one line, restate the format line (date/time/
duration/free), and repeat the button. This is where scroll-to-the-bottom
skimmers convert. Never end a page on the FAQ.

### 3.12 [K] Footer

Minimal and legally complete:
- Copyright + business entity name
- Privacy Policy, Terms, and (if collecting phone) SMS terms
- **Earnings/results disclaimer** if any income or outcome is implied anywhere
  on the page
- **Platform disclaimer:** "This site is not part of, or endorsed by, Meta /
  Facebook / Instagram." Required for Meta advertising compliance in this niche.
- **No outbound links** other than the legal pages. No social icons — a social
  icon in the footer is an exit ramp you paid for.

### 3.13 CTA placement math

- **Minimum three** CTAs on any page longer than two screens; five is normal.
- One CTA roughly every **1.5 screen-heights** of scroll.
- **Every CTA on the page does the same thing.** One offer, one action, one
  destination. A secondary "learn more" or "book a call" button on a
  registration page splits intent and lowers total conversions.
- **Sticky mobile CTA bar** that appears once the hero scrolls out of view. On
  mobile-heavy paid traffic this is one of the highest-ROI single elements you
  can add.

---

## 4. Asset ② — The confirmation page

The most under-built page in most funnels. It has **five jobs**, in this order:

1. **Confirm** — "You're registered." Remove all doubt the form worked.
2. **Calendar** — an "Add to Calendar" button (Google/Apple/Outlook). Attendees
  who add the event to a calendar show up at a much higher rate.
3. **Set expectations** — where the link will arrive (email + text), when, and
   what to do if it doesn't.
4. **First micro-yes** — one small next action that deepens commitment: join the
   Facebook/WhatsApp group, follow on IG, watch a 3-minute pre-frame video, or
   download the workbook they'll use during the class.
5. **Optional monetization** — a self-liquidating offer ($27–$97) or an
   application/booking link for the impatient minority who are already sold.
   Keep it clearly *secondary*; it must not compete with job #2.

**Design note:** this page should feel like a receipt, not a sales page. Short,
clean, one obvious next action.

---

## 5. Asset ③ — The reminder sequence

Show-up rate is where masterclass funnels are won or lost. A great registration
page feeding a weak reminder sequence produces registrations, not revenue.

**Baseline cadence (live class on Thursday 7pm):**

| When | Channel | Content |
|---|---|---|
| Immediately | Email | Confirmation + link + calendar + what to bring |
| Immediately | SMS | "You're in. Save this link:" + link |
| T-24h | Email | Value/story email — reinforce *why* they registered |
| T-3h | Email | "Tonight" + link |
| T-1h | SMS | "Starting in 1 hour" + link |
| T-10min | SMS | "We're going live now" + link |
| T-0 | Email | "We're live" + link |
| T+2h (no-shows) | Email | Replay (if offering) or next session |
| T+24h (attendees) | Email | Recap + the offer's next step |

**Rules:**
- The **link is in every single message.** Never make someone search their inbox.
- SMS carries the near-time reminders; email carries the value and the long-lead
  touches.
- Segment sends by attendance the moment the class ends. Attendees and no-shows
  must never receive the same follow-up.

---

## 6. Asset ④ — The masterclass itself

The page layout only pays off if the class converts. Standard structure:

1. **Hook + promise** (5 min) — restate exactly what they registered for.
2. **Credibility story** (10 min) — the same story as block [F], told long.
3. **Secret #1 → vehicle belief** (15 min)
4. **Secret #2 → internal belief** (15 min)
5. **Secret #3 → external belief** (15 min)
6. **Transition** (2 min) — "here's what it looks like to do this with help."
7. **The offer** (15 min) — what it is, who it's for, what happens next.
8. **Q&A** (15 min) — handle live objections; keep the CTA on screen.

Note the symmetry: **the three Secrets on the registration page are the same
three Secrets taught in the class.** The page is a table of contents for the
class. That consistency is what makes the whole funnel feel coherent, and it's
what makes the registration page easy to write — write the class first, then the
page.

---

## 7. Asset ⑤ — Application + booking

For a high-ticket offer, do **not** send masterclass attendees straight to an
open calendar. Sequence:

1. **Short sales/application page** — restates the program, then the form.
2. **Qualifying questions** — 5–10 fields. Now is when you ask about revenue,
   timeline, budget readiness, and biggest obstacle. Friction here is *good*: it
   filters, and it makes the call feel earned.
3. **Calendar** — shown only after the application submits.
4. **Confirmation page** — pre-frame the call: how long, who they'll speak with,
   what to prepare, and an explicit "show up or reschedule" ask.

---

## 8. Asset ⑥ — Follow-up

- **No-show sequence:** replay (time-limited) + next session invitation.
- **Attended, didn't apply:** 5–7 day sequence, one objection per email, each
  ending at the application link.
- **Applied, didn't book:** SMS within the hour. This is your hottest segment.
- **Booked, didn't show:** immediate reschedule link, not a re-sell.
- **Retargeting:** run separate ad sets for registered-but-didn't-attend and
  attended-but-didn't-apply. Their objections are different, so their ads must
  be different.

---

## 9. Cross-cutting mechanics

### 9.1 Message match
The ad's headline, imagery, and promise must be recognizable within the first
screen of the landing page. The strongest version literally repeats the ad's
hook as the H1. Most "bad landing page" diagnoses are actually message-match
failures: the click was earned by a promise the page doesn't visibly keep.

### 9.2 Mobile first, always
The majority of Meta traffic is mobile. Design the mobile layout first and let
desktop be the adaptation, not the reverse. Non-negotiables:
- Tap targets ≥ 44px tall
- Full-width buttons on mobile
- H1 legible without zoom
- Sticky CTA bar after the hero
- No horizontal scroll anywhere, ever

### 9.3 Speed
Target under 2.5 seconds to the hero being interactive on 4G. Compress every
image, lazy-load anything below the fold, don't load a video player above the
fold, and strip every script you can't name the purpose of. Speed is a
conversion feature, not an engineering detail.

### 9.4 Tracking
Before a dollar of traffic:
- Pixel **and** server-side Conversions API firing (browser-only tracking
  under-reports badly).
- `PageView` on the registration page, `Lead` on the confirmation page — fire
  conversion events on the **confirmation** page, not on button click.
- UTMs on every ad so registrations are attributable to ad set and creative.
- Pass UTMs through the form into the CRM so you can trace closed revenue back
  to the creative that produced it.

### 9.5 Compliance
- No income guarantees; use "results not typical" language and a visible
  earnings disclaimer wherever outcomes are implied.
- Meta/Facebook non-affiliation disclaimer in the footer.
- Explicit SMS consent language at the point of phone collection.
- Privacy policy and terms reachable from the footer.

---

## 10. Copy templates

**Headline**
> How to [specific outcome] in [timeframe] — without [dreaded thing].

**Subhead**
> A free [duration] live masterclass for [specific audience] who want to
> [outcome] — even if [primary disqualifying belief].

**Pain bullet**
> You've [specific repeated action] and still [specific absent result].

**Secret**
> Secret #[n]: [Named concept] — how to [outcome] without [objection], even if
> [disqualifier].

**Button**
> Save My Free Seat  ·  Yes — Reserve My Spot  ·  Register Free →

**Risk-reducer**
> 100% free · [duration] · Limited seats · No experience required

**Bridge after pain block**
> If you nodded at any of those, this masterclass was built for you.

---

## 11. Benchmarks and diagnostics

Directional planning numbers for cold Meta traffic to a free masterclass. Use
them to locate the broken step — your own historical data always overrides them.

| Step | Healthy range | Alarm |
|---|---|---|
| Ad CTR (link) | 1–3% | < 0.8% |
| Landing page → registration | 25–40% | < 15% |
| Registration → live attendance | 25–40% | < 20% |
| Attendee → application | 5–15% | < 3% |
| Application → booked call | 60–80% | < 40% |
| Booked → showed | 60–80% | < 50% |
| Call → close (high ticket) | 15–30% | < 10% |

**Diagnostic table — when a number is off, fix the cause, not the page you
happen to be looking at:**

| Symptom | Most likely cause | Fix |
|---|---|---|
| High CTR, low registration | Message match break | Rewrite H1 to mirror the ad hook |
| Low registration, high scroll depth | Weak CTA or too many fields | Two-step opt-in, cut fields, add sticky bar |
| Low registration, low scroll depth | Hero fails | Rewrite headline/subhead; check load speed |
| High registration, low show-up | Reminder sequence too thin | Add SMS at T-1h and T-10min; add calendar button |
| High show-up, low application | The class doesn't close the 3 beliefs | Restructure the class, not the page |
| High application, low booking | Calendar friction | Show calendar immediately on submit; SMS the link |
| High booking, low close | Wrong-fit leads | Tighten the audience callout in the subhead and the application questions |

Read that table upward. A weak close rate is usually caused by an audience
problem three steps earlier, not by the sales call.

---

## 12. Build checklist

**Before design**
- [ ] Offer, price, and delivery capacity confirmed
- [ ] The one conversion event named for each of the six assets
- [ ] The masterclass outline written **first**
- [ ] The three Secrets mapped to vehicle / internal / external beliefs

**Registration page**
- [ ] Dedicated domain, no nav, no outbound links
- [ ] Announcement bar with free · live · date
- [ ] H1 with outcome + timeframe + "without"
- [ ] Audience explicitly named in the subhead
- [ ] Date, time + timezone, duration visible above the fold
- [ ] Two-step opt-in; ≤3 fields
- [ ] Risk-reducer micro-copy under every button
- [ ] Credibility strip below the fold
- [ ] 3–5 pain bullets in the reader's language
- [ ] Exactly 3 Secrets
- [ ] Host story, not résumé
- [ ] 3–6 testimonials with numbers
- [ ] 4–6 FAQ items answering real objections
- [ ] Honest urgency mechanism
- [ ] ≥3 CTAs, all identical in action
- [ ] Sticky mobile CTA bar
- [ ] Footer: legal + earnings disclaimer + Meta non-affiliation
- [ ] Tested on a real phone

**Behind the page**
- [ ] Confirmation page doing all five jobs
- [ ] Calendar invite working on iOS and Android
- [ ] Email + SMS reminder sequence live and tested end to end
- [ ] Attendance segmentation splitting attendees from no-shows
- [ ] Application → calendar → confirmation chain tested
- [ ] Pixel + CAPI verified, `Lead` firing on the confirmation page
- [ ] UTMs passing through the form into the CRM
- [ ] Retargeting audiences built for each drop-off segment

---

## 13. Adapting the framework to other offer types

The block order is stable across offer types; what changes is what sits behind
the opt-in.

**Lead magnet / PDF funnel.** Same page, shorter. Drop the FAQ and urgency
blocks, cut the Secrets from three to three bullets, and expect a higher opt-in
rate with a lower-intent lead. The confirmation page's micro-yes matters more
here, because there's no scheduled event holding attention.

**Low-ticket / self-checkout.** Replace the masterclass with a sales page and
checkout. The belief ladder is identical, but blocks [E] through [I] must carry
the *whole* sale, so they get longer, and the page ends in a price + guarantee
block instead of a registration button. Margin comes from the order bump and
upsell, not the front end.

**Direct call booking (no class).** Skip Asset ④. The registration page becomes
an application page: the same layout, but with the qualifying questions moved
onto the main page and the CTA changed to "Apply." Expect a much lower page
conversion rate — that's correct, because each lead is worth far more.

**Challenge / multi-day event.** Same registration page, but the format line
carries multiple dates, and the reminder sequence repeats per day. Add a daily
"today's session" SMS. Attendance decay across days is the metric to watch.
