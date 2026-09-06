#!/usr/bin/env python3
"""
Build the Score Machine webinar deck as annotated HTML for Canva import.

All on-screen copy is taken verbatim from ScoreMachineslidescript.md.
Speaker notes carry the Say:/Why:/warning prose from the same file.

Emits 16:9 (1920x1080) pages annotated with data-document-role="page"
so Canva's importer maps each one to a slide.
"""

import html
import re
import sys

# Act boundaries, keyed by the source script's slide numbers.
ACTS = [(1, 14, "ACT 1 — WHAT THIS IS REALLY ABOUT"),
        (15, 24, "ACT 2 — WHY YOU GOT DENIED"),
        (25, 35, "ACT 3 — ELIGIBILITY FIRST"),
        (36, 46, "ACT 4 — SIX WAYS PEOPLE USE THIS"),
        (47, 63, "ACT 5 — THE OFFER"),
        (64, 64, "THE SECOND ASK"),
        (65, 65, "Q&A")]


def act_for(label, previous):
    """Act name for a slide. Asks and inserts inherit the act they sit in."""
    m = re.match(r"S(\d+)", label)
    if m:
        n = int(m.group(1))
        for lo, hi, name in ACTS:
            if lo <= n <= hi:
                return name
    if label.startswith("Social proof"):
        return "SOCIAL PROOF"
    if label.startswith("Demo"):
        return "DEMO — LIVE SOFTWARE"
    return previous


def topic_for(s):
    if s["layout"] == "question":
        return "Audience ask"
    label = s["label"]
    return label.split("—", 1)[1].strip() if "—" in label else label

# Raw base for background images. Pinned to a commit SHA at build time.
BG_BASE = sys.argv[1] if len(sys.argv) > 1 else "ASSET_BASE_PLACEHOLDER"

LIGHT = "light"
DARK = "dark"

S = []  # slide list


def slide(label, bg, layout, notes="", **kw):
    S.append(dict(label=label, bg=bg, layout=layout, notes=notes, **kw))


def ask(label, kicker, text, notes="", own_slide=False):
    """An audience ask.

    Most asks are spoken over the slide already on screen, so they fold into that
    slide's speaker notes. Only the four asks that carry real weight get a
    full-screen prompt of their own.
    """
    if own_slide:
        S.append(dict(label=label, bg=DARK, layout="question",
                      kicker=kicker, text=text, notes=notes))
        return
    prev = S[-1]
    block = f'ASK — say out loud, stay on this slide:\n"{text}"'
    if notes:
        block += "\n" + notes
    prev["notes"] = (prev["notes"] + "\n\n" + block).strip()


# ─────────────────────────────────────────────────────────────
# ACT 1 — WHAT THIS IS REALLY ABOUT
# ─────────────────────────────────────────────────────────────

slide("S1 — Title", DARK, "title",
      title="THE SCORE MACHINE",
      sub="Why you got denied — and what to do about it",
      notes="Say: Ninety minutes. By the end of tonight you're going to know exactly why your "
            "last denial happened, and exactly what your file needs before you apply to anything again.")

ask("Q1 — Ask 1 (after S1)", "TYPE IN THE CHAT",
    "Before we start — type YES in the chat if you can see my screen and hear me clearly.",
    "Why: The first ask must be trivially easy and it must succeed. It teaches the room that typing "
    "in the chat is what we do here. If the chat stays quiet, stop and fix it now — every later ask "
    "depends on this one landing.")

slide("S2 — The hook", LIGHT, "statement",
      text="You didn't get turned down for the reason you think.",
      notes="Say: Nothing. Three full seconds of silence. Let it sit before you move.")

slide("S3 — The house", LIGHT, "lines",
      lines=["You found the house.", "You got pre-approved.", "Then you weren't."],
      notes="Say: Some of you know exactly what that phone call sounds like.")

slide("S4 — The car", LIGHT, "lines",
      lines=["You need the car to get to work.",
             "The job is what feeds your family.",
             "The denial costs you both."],
      notes="Say: Slow down here. This is the slide people feel. Nobody applies for a car loan because "
            "they want a car loan — they want to stop asking for rides, stop losing shifts, get home "
            "before their kids are asleep. Do not rush this slide.\n\n"
            "PACING: One of only two slow slides in Act 1. Never cut this slide.")

ask("Q2 — Ask 2 (after S4)", "TYPE IN THE CHAT",
    "Type YES if a denial has ever cost you something that mattered more than the money.",
    "Why: First emotional yes. Wait for it. Read two or three names out loud — that's what teaches "
    "the room that answering gets acknowledged.")

slide("S5 — The contract", LIGHT, "lines",
      lines=["The contract was yours.",
             "You didn't have the capital to staff it.",
             "So you watched someone else take it."],
      notes="Say: And for the business owners in here — same feeling, different shape. You weren't "
            "short on skill. You were short on cash for ninety days.")

slide("S6 — The reframe", LIGHT, "statement",
      text="NOBODY WANTS A CREDIT SCORE.",
      sub="They want what it unlocks.",
      notes="Say: Nobody has ever laid in bed at night wishing their score was higher for its own sake. "
            "You want the house. You want the truck. You want the line of credit. The score is just the door.")

slide("S7 — What this class actually is", LIGHT, "lines",
      lines=["This isn't a class about credit.", "It's a class about approvals."],
      notes="PACING: Cuttable if running long.")

slide("S8 — Let's see if I'm describing your situation", LIGHT, "bullets",
      bullets=["Denied — and the letter never really told you why",
               "Your score is “fine.” 640. 700. Still denied.",
               "Solid card, still stuck at a $500 limit, calling it progress",
               "You have cards. You still aren't fundable."],
      notes="Say: [Wait. Do not move until the chat fills.] That's most of the room.")

ask("Q3 — Ask 3 (after S8)", "TYPE IN THE CHAT",
    "Type YES if even one of those four is you.",
    "Why: Highest-volume yes of the night. The wall of YES is the point, not the answer — it proves "
    "to every person that they aren't the only one.", own_slide=True)

slide("S9 — Both rooms", LIGHT, "lines",
      lines=["Some of you are here for personal credit.",
             "Some of you are here for business funding.",
             "Same file. Same rules. Same machine."],
      notes="Say: Nobody's in the wrong room tonight. Underwriting doesn't read a file differently "
            "because of what you want at the end of it.")

ask("Q4 — Ask 4 (after S9)", "TYPE IN THE CHAT",
    "Type 1 if you're here for personal credit, 2 if you're here for business funding, 3 if it's both.",
    "Why: Diagnostic, not agreement — it tells you the room mix so you can weight your examples for "
    "the next hour. Say the split out loud once you see it.")

slide("S10 — Who I am", LIGHT, "lines",
      lines=["[Your name]", "Owner — Get AI Leads Now", "",
             "I'm not a credit repair company.",
             "I'm a business owner who uses this software."],
      notes="Say: Quick word on who's talking to you. I run a marketing company — Get AI Leads Now. "
            "Credit isn't my industry. I'm on this call because of what this tool did inside my business "
            "and my clients' businesses, and I want to show it to you from the business owner's side of "
            "the desk, not the software company's side.\n\n"
            "LANGUAGE DISCIPLINE FOR THE WHOLE NIGHT: always “they” and “Score Machine.” "
            "Never “we,” “our software,” “our team.” You're a customer telling the room what "
            "the product did for you. That's the position, and one slip into “we” costs it.\n\n"
            "PACING: Never cut this slide.")

slide("S11 — The three ways I make money with it", LIGHT, "numbered",
      items=["<b>On my own file</b> — I know where I stand before I ever apply",
             "<b>For my clients</b> — I help them get funded, and I charge for that",
             "<b>By referring it</b> — I earn when people I send use it. Including tonight."],
      notes="Say: I want to be straight with you about all three, especially the last one. I get paid "
            "when someone signs up through my link — including anybody who signs up tonight. I'm telling "
            "you that up front because I'd rather you hear it from me than wonder about it later, and "
            "honestly, it's the whole point: number three is a business model, and it's available to "
            "every person on this call.\n\n"
            "WHY THIS SLIDE MATTERS: the disclosure is required if you earn on referrals, and delivering "
            "it yourself, early, in your own words converts a liability into proof. You're not hiding the "
            "affiliate model — you're demonstrating it live. This also plants Act 4's second tier fifteen "
            "minutes before it arrives.\n\n"
            "ON THE MARKETING RELATIONSHIP: you don't need to volunteer that your company does marketing "
            "work — that's simply not what tonight is about, and no rule requires you to narrate your whole "
            "client list. But don't deny it either. If someone asks you point-blank in Q&A whether you work "
            "with Score Machine, answer plainly and move on: “My company does marketing work in this space, "
            "yes — and everything I showed you tonight is something I actually use.” A brief honest answer "
            "costs you nothing. A denial that later surfaces costs you the room and the relationship.\n\n"
            "PACING: Slow slide. Never cut.")

slide("S12 — What changed in my business", LIGHT, "lines",
      lines=["Before: a client asked me about funding and I had nothing to hand them.",
             "Now: I read their file in minutes and tell them exactly where they stand.",
             "",
             "New service. Same clients.",
             "",
             "If you own a business that touches people with credit problems —",
             "you're closer to this than you think."],
      notes="Say: I didn't have to become a credit expert. I didn't have to go get certified in anything. "
            "I already had the clients — what I didn't have was something useful to say when they brought "
            "me a funding problem. Now I do, and it's a line of revenue that didn't exist in my business a "
            "year ago. And that's the last I'll say about me. I only told you that because most of the room "
            "is going to spend tonight thinking about their own credit file — and some of you should be "
            "thinking about both.\n\n"
            "⚠️ FILL THIS WITH YOUR OWN TRUE SPECIFICS BEFORE STAGE — what you actually offer clients "
            "now, and what actually changed. Do not put a revenue figure on this slide. “A line of revenue "
            "that didn't exist” is honest and persuasive; a dollar amount is an earnings claim and invites a "
            "very different set of problems.\n\n"
            "Why: The host block must end pointed at them, not at you. Three slides about you is credibility; "
            "a fourth is a detour. This is the hard stop — the second half of this slide is the handoff back "
            "to the room.\n\n"
            "PACING: Cut this slide first if the host block runs long — but never 10 or 11.")

slide("S13 — Let me be straight with you", LIGHT, "twocol",
      col_a_head="What this is:",
      col_a=["Exactly how underwriting reads your file",
             "The software that does it in about a minute"],
      col_b_head="What this isn't:",
      col_b=["A promise of an approval", "A promise of a number"],
      notes="Say: I'm not going to stand up here and guarantee you an approval or tell you your score is "
            "going up 100 points. Nobody honest can promise you that. What I can do is show you the ten "
            "questions every lender is asking about your file, and then show you your own answers.")

slide("S14 — The chain", LIGHT, "numbered",
      items=["You got denied",
             "Because inquiries quietly lowered your ceiling",
             "Because you applied without knowing if you were eligible",
             "Eligibility can be known <b>before</b> you apply",
             "If you're not eligible — the file gets fixed",
             "Once you are — the bank and the bureau decide where you apply"],
      notes="Say: That's the whole ninety minutes on one slide. Screenshot it. Everything from here just "
            "fills it in.\n\nPACING: Needs silence after it.")

# ─────────────────────────────────────────────────────────────
# ACT 2 — WHY YOU GOT DENIED
# ─────────────────────────────────────────────────────────────

slide("S15 — The pivot", LIGHT, "statement",
      text="A score is not an approval.",
      notes="Say: A score gets you considered. It does not get you approved. Those are two different "
            "events and almost nobody is taught the difference.")

slide("S16 — Three files", LIGHT, "lines",
      lines=["You don't have a credit score.", "You have three files.", "",
             "Experian · Equifax · TransUnion", "",
             "Different data. Different scores."])

slide("S17 — The question", LIGHT, "statement",
      text="Which one did they pull?",
      notes="Say: Think about your last denial. Right now. Which bureau did that lender pull? "
            "[Pause. Let it be uncomfortable.]\n\nPACING: Needs silence after it. Never cut this slide.")

ask("Q5 — Ask 5 (after S17)", "TYPE IN THE CHAT",
    "Type YES if you have no idea which bureau your last denial pulled.",
    "Why: Near-universal, and it's an admission rather than an agreement — which is stronger. Once "
    "they've typed it they've told themselves they have a gap. Follow with: “That's not your fault. "
    "Nobody ever told you it mattered.”")

slide("S18 — Why it matters", LIGHT, "lines",
      lines=["Your best file doesn't get you approved.", "The one they pulled does."],
      notes="PACING: Cuttable if running long.")

slide("S19 — Credit decay", LIGHT, "lines",
      lines=["Every application leaves an inquiry.",
             "Every inquiry lowers what a bank will extend you.", "",
             "This is called <b>credit decay.</b>"],
      notes="Say: This is the part nobody tells you. It's not just that inquiries ding your score a few "
            "points. Inquiries lower the dollar amount a bank is willing to hand you — and that happens "
            "quietly, whether you got approved or not.")

ask("Q6 — Ask 6 (after S19)", "TYPE IN THE CHAT",
    "Type YES if nobody has ever explained credit decay to you before tonight.",
    "Why: Establishes you as the one who told them. This is the authority beat of Act 2.")

slide("S20 — What decay looks like", LIGHT, "statfocus",
      kicker="Real file. 14 inquiries.",
      stat="Approval odds: −$5,000",
      notes="Say: Negative five thousand. This person isn't getting a smaller approval — they're not "
            "getting anything, from anyone, and their credit score never told them that. They'd have "
            "kept applying.\n\nPACING: Never cut this slide.")

slide("S21 — The line", LIGHT, "statement",
      text="Forget about points.",
      sub="It's about money.")

slide("S22 — So what actually happened", LIGHT, "lines",
      lines=["You applied.", "You didn't know if you qualified.", "You got denied.",
             "And the inquiry made the next one harder."],
      notes="PACING: Cuttable if running long.")

slide("S23 — The spiral", LIGHT, "lines",
      lines=["Denied → inquiry → lower ceiling →",
             "denied → inquiry → lower ceiling →",
             "denied"],
      notes="Say: This is why it feels like it's getting worse even though you're trying harder. You are "
            "trying harder. Every attempt is costing you the next one.")

ask("Q7 — Ask 7 (after S23)", "TYPE IN THE CHAT",
    "Type YES if that's been your experience.",
    "Why: They're now agreeing to your diagnosis of their own history. Everything after this is built "
    "on that yes.")

slide("S24 — The turn", LIGHT, "statement",
      text="There is a way to know first.")

# ─────────────────────────────────────────────────────────────
# ACT 3 — ELIGIBILITY FIRST
# ─────────────────────────────────────────────────────────────

slide("S25 — Eligibility is the whole game", LIGHT, "lines",
      lines=["The question is never “what's my score?”", "",
             "The question is <b>“should I apply at all?”</b>"])

slide("S26 — How it starts", LIGHT, "lines",
      lines=["Upload your credit report.", "No forms. No typing.",
             "Five AIs read every line of it."])

slide("S27 — The Blueprint", LIGHT, "statement",
      text="THE UNDERWRITING BLUEPRINT",
      sub="Ten questions.<br>Every lender asks them.<br>Almost nobody has ever seen them written down.")

slide("S28 — The legend", LIGHT, "legend",
      rows=[("#D7191C", "RED = STOP"),
            ("#B07A00", "YELLOW = PROCEED WITH CAUTION"),
            ("#1A7A3C", "GREEN = GO")],
      notes="Say: Like a traffic light. If you can drive a car, you can read a credit file. That's not me "
            "being cute — that's genuinely the whole skill.")

ask("Q8 — Ask 8 (after S28)", "TYPE IN THE CHAT",
    "Type YES if you can read a traffic light.",
    "Why: Deliberately easy and a little funny. Resets the energy after eight heavy minutes and plants "
    "the belief that this is learnable — before you show them the ten lines.")

slide("S29 — The ten lines", LIGHT, "tenlines",
      items=["700 credit score?",
             "Under 30% utilization?",
             "Five open primary cards, two years of good history?",
             "Three primary cards, three years old, $5,000 limit?",
             "More than four unsecured accounts in the last 12 months?",
             "Under four inquiries?",
             "Collections?",
             "Charge-offs?",
             "Late payments?",
             "Bankruptcy?"],
      notes="Say: Ten. That's it. That's what stands between you and every approval you've been denied.\n\n"
            "PACING: The longest single slide in the deck. Never cut.")

ask("Q9 — Ask 9 (after S29)", "TYPE IN THE CHAT",
    "Type YES if you've never seen these ten questions written down anywhere before.",
    "Why: The value moment. They just received something they didn't have — get them to say so out loud.\n\n"
    "⚠️ Line 5 direction must be locked before stage — see the framework doc.")

slide("S30 — The question it answers", LIGHT, "statement",
      text="→ Are you eligible?")

slide("S31 — Let's read one together", LIGHT, "lines",
      lines=["Let's read a real file.", "You call it."],
      notes="Say: I'm going to read you the line. You tell me red, yellow, or green. Don't be shy — you "
            "already know how to do this, you just haven't been allowed to before.")

slide("S32 — The file (red)", LIGHT, "placeholder",
      text="[Ten lines, marked red/yellow/green from a real anonymized file]",
      notes="Say: Walk it one line at a time. Let the room answer each one out loud. Do not answer for them.\n\n"
            "ASK (spoken, not typed — Yes Ladder #10): Red, yellow, or green? — line by line. Gets "
            "participation out loud rather than in the chat.\n\n"
            "⚠️ Drop the real anonymized file art onto this slide before stage.")

slide("S33 — The verdict", LIGHT, "lines",
      lines=["Not eligible.", "And now you know exactly why.", "",
             "Not “your credit is bad.”", "Four specific lines."],
      notes="Say: That's the difference between how you felt walking in here and how you feel now. "
            "“Bad credit” is a feeling. Four red lines is a to-do list.\n\nPACING: Never cut this slide.")

slide("S34 — What green looks like", LIGHT, "lines",
      lines=["A real approved file:", "", "1 inquiry", "0 collections", "2% utilization",
             "<b>Every line green</b>"],
      notes="Say: Same ten questions. Completely different life.")

ask("Q10 — Ask 10 (after S34)", "TYPE IN THE CHAT",
    "Type YES if you want your file to look like that.",
    "Why: The pivot from agreeing to wanting. Most important ask before the offer — the first time they "
    "state a desire instead of confirming a fact. Do not skip it, do not rush it.", own_slide=True)

slide("S35 — Transition", LIGHT, "lines",
      lines=["The software does all of this", "in about a minute.", "",
             "And that's only the first of six things people use it for."],
      notes="Say: I'm going to show it to you live before we're done tonight. But first I need you to "
            "understand what this actually is, because most of the room only knows about one-sixth of it.")

# ─────────────────────────────────────────────────────────────
# ACT 4 — SIX WAYS PEOPLE USE THIS
# (source doc mislabels these 48–56; correct range is 36–46)
# ─────────────────────────────────────────────────────────────

slide("S36 — The six", LIGHT, "statement",
      text="Six ways people use this.",
      sub="Three on yourself.<br>Three to get paid.",
      notes="Say: Some of you came here tonight for the first three. Nobody told you the last three existed.")

ask("Q11 — Ask 11 (after S36)", "TYPE IN THE CHAT",
    "Type the number you came here for tonight — 1, 2, or 3.",
    "Why: Primes them to hunt for their own number, which keeps all six avatars watching the rest of the act.")

slide("S37 — Tier one", LIGHT, "heading",
      text="FIRST — USE IT ON YOURSELF")

slide("S38 — #1 Analyze", LIGHT, "usecase",
      num="1. ANALYZE YOUR PROFILE",
      sub="Know your factors — not your score.",
      lines=["What's actually on all three bureaus.",
             "What's helping. What's holding you back.",
             "Whether you should apply at all."],
      notes="Say: This is the one everybody needs and nobody has. Your score is a summary. Your factors "
            "are the reasons. Lenders read the reasons.")

slide("S39 — #2 Improve", LIGHT, "usecase",
      num="2. IMPROVE YOUR PROFILE",
      sub="Dispute with the latest AI.",
      lines=["Custom letters written per account — not templates",
             "Printed and mailed for you",
             "Every removal tracked"],
      notes="Say: Template letters get template responses. The bureaus have seen the same letter ten "
            "thousand times — that's how you end up with stall letters. These are written per account, "
            "per bureau, per situation.")

slide("S40 — #3 Funding recommendations", LIGHT, "usecase",
      num="3. KNOW WHERE TO APPLY",
      sub="Which banks. Which bureau they pull. What order.",
      lines=["Not “apply and hope.”"],
      notes="Say: Remember slide seventeen — you couldn't tell me which bureau your last denial pulled. "
            "This is the slide that fixes that permanently.")

slide("S41 — The turn", LIGHT, "statement",
      text="Now — here's what most people in this room don't know.",
      notes="Say: Beat. Then move.\n\nPACING: Gets a beat.")

slide("S42 — Tier two", LIGHT, "heading",
      text="THEN — USE IT TO GET PAID",
      sub="The same tool that fixes your file<br>is a business.")

ask("Q12 — Ask 12 (after S42)", "TYPE IN THE CHAT",
    "Type YES if you'd want to get paid doing this for other people.",
    "Why: Opens the second tier and measures how operator-minded the room is. Big YES wall — slow down "
    "on the next two slides. Thin — move through them and spend the time on the funding-business slide.")

slide("S43 — #4 Credit repair business", LIGHT, "usecase",
      num="4. LAUNCH A CREDIT REPAIR BUSINESS",
      lines=["Pull a client's report. Read their ten lines.",
             "Show them the red on their own screen.",
             "Let the software write and mail the letters."],
      notes="Say: The consultation sells itself. You don't have to convince anyone they need help — you "
            "show them their own file and ask one question: do you want help with this?\n\n"
            "⚠️ Be straight about what this takes: credit repair is a regulated business with state "
            "requirements. The software is the engine, not the license. Say it out loud on this slide.")

slide("S44 — #5 Funding business", LIGHT, "usecase",
      num="5. LAUNCH A FUNDING BUSINESS",
      lines=["Qualify the client before you ever apply.",
             "Know the banks, the bureaus, the order.",
             "Get paid a percentage of what you get funded."],
      notes="Say: This is what people charge ten and fifteen percent for. The hard part was never the "
            "paperwork — it was knowing whether the file could get approved before you burned an inquiry "
            "finding out.\n\n"
            "⚠️ No earnings claims. If you show the arithmetic of a percentage fee, say plainly that "
            "it's arithmetic on an example, not a typical result.")

slide("S45 — #6 Refer it", LIGHT, "usecase",
      num="6. REFER IT",
      lines=["Your own referral link.", "Share the software.",
             "Earn on it — every month it stays active."],
      notes="Say: You don't have to run a single client file to benefit from this. If all you ever do is "
            "send it to the people in your circle who keep getting denied, that's a real thing.\n\n"
            "⚠️ The referral program is a referral program. Describe how it works. Don't project what "
            "anyone will earn from it.")

slide("S46 — All six", LIGHT, "numbered",
      items=["Analyze your profile", "Improve it with AI disputes", "Know where to apply",
             "Launch a credit repair business", "Launch a funding business", "Refer it and earn"],
      footer="One login.",
      notes="Say: Find yourself on this list. Most of you are on it twice.\n\nPACING: Never cut this slide.")

ask("Q13 — Ask 13 (after S46)", "TYPE IN THE CHAT",
    "Type every number that applies to you. Not one — all of them.",
    "Why: Someone typing “1, 3, 6” is telling you and themselves that this is worth more than one "
    "thing to them. That multiplies perceived value right before the stack.")

# ─────────────────────────────────────────────────────────────
# ACT 5 — THE OFFER
# ─────────────────────────────────────────────────────────────

slide("S47 — The two files", LIGHT, "placeholder",
      text="[Red file] · [Green file]",
      sub="Same ten questions.",
      notes="⚠️ Drop the two file comparisons onto this slide before stage.")

slide("S48 — The question", LIGHT, "statement",
      text="Which one are you?",
      notes="Say: Be honest with yourself. Most of this room is the file on the left. That's not a "
            "character flaw — it's a starting point, and now it's a measurable one.")

slide("S49 — The good news", LIGHT, "lines",
      lines=["The gap between those two files", "isn't willpower.", "",
             "It's a checklist and a tool."])

slide("S50 — Three levers", LIGHT, "numbered",
      items=["Pay down what's high — often $7–8 a week",
             "Remove what shouldn't be there",
             "Only apply where you're actually eligible"],
      notes="Say: Three levers. The third one is free — it just requires knowing something you didn't "
            "know an hour ago.")

ask("Q14 — Ask 14 (after S50)", "TYPE IN THE CHAT",
    "Type YES if $8 a week is doable for you.",
    "Why: The last micro-yes before money enters the room. They've just agreed the fix is affordable — "
    "that's the frame you want them holding when the price appears four slides later.")

slide("S51 — Back to why", LIGHT, "lines",
      lines=["The house.", "The car.", "The capital.", "", "Or a business of your own."],
      notes="Say: Because that's what this was always about. Not the score.")

slide("S52 — What you get", LIGHT, "statement",
      text="All six.",
      sub="One login.")

ask("Q15 — Ask 15 (after S52)", "TYPE IN THE CHAT",
    "Type YES if you'd want all six of those in one place.",
    "Why: Agreement on the bundle before it has a price. Now the stack is answering “how much,” "
    "not “whether.”")

slide("S53 — The value stack", LIGHT, "chart",
      rows=[("Full AI Credit File Analysis — five AIs read your report", 297),
            ("The Underwriting Blueprint — know before you apply", 197),
            ("Bank + Bureau Matching — who pulls what, and in what order", 197),
            ("AI Dispute Letter Engine — custom letters, not templates", 97),
            ("Letter Print + Certified Mail", 97),
            ("Progress Report + Score Timeline", 67),
            ("Client Summary PDF", 45)],
      notes="Say: Name each line as it appears and tie it back to the use case it powers. Nothing here "
            "should be new information by now.\n\n"
            "⚠️ The script calls for this to build one line at a time. The import lands it as one "
            "chart — duplicate this slide seven times in Canva and delete bars upward if you want the build back.")

# The four price slides — identical layout, only the number changes.
slide("S54 — The total", DARK, "price", strike="", big="$997", sub="",
      notes="Say: Let it sit. Say nothing for a beat.\n\n"
            "PACING: Slides 54–57 are one motion — no pause except after this one.")

slide("S55 — $497", DARK, "price", strike="$997", big="$497", sub="",
      notes="PACING: One motion with 54, 56, 57. No pause.")

slide("S56 — $247", DARK, "price", strike="$497", big="$247", sub="",
      notes="PACING: One motion with 54, 55, 57. No pause.")

slide("S57 — The offer", DARK, "price", strike="$247", big="$1 TO GET STARTED",
      sub="7 days, then $97/month",
      notes="Say: One dollar to get started. Seven days. After that it's $97 a month — your card gets "
            "charged $97 on [state the exact date]. No surprises, no small print. If it's not for you, "
            "cancel inside the seven days.\n\nPACING: Never cut this slide.")

ask("Q16 — Ask 16 (after S57)", "TYPE IN THE CHAT",
    "Type YES if you're getting started tonight.",
    "Why: The commitment ask. Every yes before this one was practice for this one. Wait through the "
    "silence — it always feels longer than it is.", own_slide=True)

slide("S58 — What happens in those 7 days", LIGHT, "lines",
      lines=["Tonight: upload your report", "Tonight: run the Blueprint", "Tonight: see your ten lines",
             "", "This week: know whether you're eligible —", "before you apply to anything else."],
      notes="Say: The trial isn't “poke around and see.” You have one job in seven days: find out what "
            "your own ten lines actually say.")

slide("S59 — Who this is for", LIGHT, "bullets",
      bullets=["You've been denied and never got a real answer",
               "You're about to apply for something that matters",
               "You're fixing your file and want the work tracked",
               "You want to start a credit repair business",
               "You want to start a funding business",
               "You want to refer it and earn"],
      notes="Say: Read all six out loud, slowly. Every person in the room should hear their own line. "
            "This is the slide where the six avatars each decide it's for them.")

slide("S60 — Who this isn't for", LIGHT, "bullets",
      bullets=["Anyone looking for a guaranteed approval",
               "Anyone who wants someone else to care about their file more than they do"],
      notes="Say: I'd rather you not start than start expecting a miracle. This is a tool. A very good "
            "one. It isn't magic, and it isn't a license — if you're building a business on it, you still "
            "have to build the business.")

slide("S61 — How to start", LIGHT, "numbered",
      items=["Click the link", "Create your account — $1", "Upload your report tonight"])

slide("S62 — The link", LIGHT, "placeholder",
      text="GET STARTED HERE",
      notes="Say: Say it out loud. Have someone drop it in chat now, and again in five minutes.\n\n"
            "⚠️ Add your live referral link to this slide before stage — type it under the "
            "heading, and drop it in the chat as well.")

ask("Q17 — Ask 17 (after S62)", "TYPE IN THE CHAT",
    "Type GOT IT when you see the link.",
    "Why: Two jobs at once — confirms the link actually reached people, and puts visible evidence in the "
    "chat that others are moving. That's the most persuasive thing on screen at this moment.")

slide("S63 — Close before the demo", DARK, "close",
      lines=["You were never bad with credit.", "You were playing a game",
             "nobody showed you the rules to."],
      big="$1 TO GET STARTED",
      sub="7 days, then $97/month",
      notes="Say: Get started now, and then watch me use the exact thing you just got. Everybody else — "
            "watch anyway, and decide at the end.\n\n"
            "⚠️ THIS SLIDE STAYS VISIBLE OR PINNED IN CHAT FOR THE ENTIRE 30-MINUTE DEMO. The link "
            "never leaves the screen.")

# ── DEMO ASKS — held in reserve, not part of the running order ──
ask("Q18 — Demo ask 1 (after demo beat 3)", "TYPE IN THE CHAT",
    "Type YES if you want to see your own ten lines.",
    "DEMO ASK — hold in reserve. Bring this up after demo beat 3 (the Blueprint live), then return to "
    "S63 so the offer and link are back on screen. Thirty minutes is a long time to watch someone "
    "else's screen; these keep the room from drifting.")

ask("Q19 — Demo ask 2 (after demo beat 6)", "TYPE IN THE CHAT",
    "Type YES if you thought that number would be higher.",
    "DEMO ASK — hold in reserve. Bring this up after demo beat 6 (the paydown calculator), then return "
    "to S63 so the offer and link are back on screen.")

ask("Q20 — Demo ask 3 (after demo beat 14)", "TYPE IN THE CHAT",
    "Type YES if that was helpful tonight.",
    "DEMO ASK — hold in reserve. Bring this up after demo beat 14 (the green file), then return to S63. "
    "This one warms the room for the second ask.")

slide("S64 — After the demo", DARK, "close",
      lines=["That's the whole thing."],
      big="$1 TO GET STARTED",
      sub="7 days, then $97/month",
      notes="Say: This is the ask that actually converts the room, so don't rush past it into questions. "
            "Everyone who was undecided forty-five minutes ago just watched it work. Say the price, say "
            "the rebill date, say the link, and give them fifteen seconds of silence to click before you "
            "take the first question.\n\nPACING: Never cut this slide.")

ask("Q21 — Ask 21 (after S64)", "TYPE IN THE CHAT",
    "Type YES if you're in.",
    "Why: The second ask. Fifteen seconds of silence after the link.", own_slide=True)

slide("S65 — Q&A holding slide", DARK, "qa",
      text="Questions.",
      blueprint=["700 credit score?", "Under 30% utilization?",
                 "Five open primary cards, two years of good history?",
                 "Three primary cards, three years old, $5,000 limit?",
                 "More than four unsecured accounts in the last 12 months?",
                 "Under four inquiries?", "Collections?", "Charge-offs?",
                 "Late payments?", "Bankruptcy?"],
      offer="$1 to get started · 7 days · then $97/month",
      notes="Say: Leave this up the entire time. Late arrivals can still read the Blueprint and still "
            "find the link.")



# ─────────────────────────────────────────────────────────────
# Visual upgrades + added slides
# ─────────────────────────────────────────────────────────────

def find(label_prefix):
    for i, sl in enumerate(S):
        if sl["label"].startswith(label_prefix):
            return i
    raise KeyError(label_prefix)


def mutate(label_prefix, **kw):
    S[find(label_prefix)].update(kw)


def insert_after(label_prefix, sl):
    S.insert(find(label_prefix) + 1, sl)


# -- financial iconography on the story slides --
mutate("S3 ", layout="iconlines", icons=["house"])
mutate("S4 ", layout="iconlines", icons=["car"])
mutate("S5 ", layout="iconlines", icons=["contract"])
mutate("S19 ", layout="iconlines", icons=["arrowdown"])
mutate("S26 ", layout="iconlines", icons=["report"])
mutate("S58 ", layout="iconlines", icons=["calendar"])

# -- the six use cases each get an icon --
for lbl, ic in [("S38 ", "report"), ("S39 ", "envelope"), ("S40 ", "bank"),
                ("S43 ", "people"), ("S44 ", "briefcase"), ("S45 ", "link")]:
    mutate(lbl, icon=ic)

# -- three bureaus as cards --
mutate("S16 ", layout="bureaus", names=["Experian", "Equifax", "TransUnion"],
       lines=["You don't have a credit score.", "You have three files.",
              "Different data. Different scores."])

# -- credit decay: 14 marks is the count the script already states --
mutate("S20 ", layout="decay", kicker="Real file. 14 inquiries.",
       marks=14, marks_label="Fourteen inquiries on one credit file",
       stat="Approval odds: −$5,000")

# -- the approved file, charted from the figures the script already gives --
mutate("S34 ", layout="statgrid", kicker="A real approved file:",
       tiles=[("1", "inquiry"), ("0", "collections"), ("2%", "utilization")],
       chips=10, chips_label="All ten Blueprint lines green",
       foot="Every line green")

# -- how to start as a flow --
mutate("S61 ", layout="flow",
       steps=["Click the link", "Create your account — $1", "Upload your report tonight"])

# -- the read-along file: a working slide the host marks live, not an empty placeholder --
mutate("S32 ", layout="blueprintlive",
       kicker="Call each line: red, yellow or green.",
       items=["700 credit score?",
              "Under 30% utilization?",
              "Five open primary cards, two years of good history?",
              "Three primary cards, three years old, $5,000 limit?",
              "More than four unsecured accounts in the last 12 months?",
              "Under four inquiries?",
              "Collections?",
              "Charge-offs?",
              "Late payments?",
              "Bankruptcy?"])

# -- the link slide, designed rather than a bare token on an empty page --
mutate("S62 ", layout="link",
       kicker="GET STARTED HERE",
       url="",
       foot="$1 today · 7 days · then $97/month")

# -- the two files, built from the counts the script already states --
mutate("S47 ", layout="compare",
       footer="Same ten questions.",
       panes=[dict(tone="bad", verdict="NOT ELIGIBLE",
                   chips=["r", "r", "r", "r", "n", "n", "n", "n", "n", "n"],
                   note="Four specific lines."),
              dict(tone="good", verdict="APPROVED",
                   chips=["g"] * 10,
                   note="Every line green.")])

# -- host bio --
insert_after("S10 ", dict(
    label="S10a — Bio", bg=LIGHT, layout="bio",
    name="[Your name]",
    paras=[
        "A serial entrepreneur and Founder of Get AI Leads Now LLC, builds AI-driven "
        "automation and marketing systems that help business owners scale revenue on autopilot.",
        "He has helped thousands achieve financial freedom through funding, credit, "
        "automation, and high-converting funnels.",
        "A Rochester native and former sound mixer on major shows like Cobra Kai and "
        "American Idol, he brings elite systems thinking, operational mastery, and proven "
        "growth strategies to entrepreneurs worldwide.",
    ],
    notes="Host bio, supplied verbatim. Drop your headshot into the framed slot on the left.\n\n"
          "⚠️ Two things to check before stage. First, this bio is third person while slides 10-12 "
          "are first person — read it in your own voice rather than reading it off the slide. "
          "Second, “helped thousands achieve financial freedom” is a results claim, and slide 13 "
          "promises the room no approval and no number. Decide which one you want the room to hear."))

# -- social proof, placed after the bundle ask and before the value stack --
# One screenshot per slide with the quote set large, so the room can read it even
# when the phone screenshot is small on stream. Ordered safest first, so cutting
# from the bottom removes the riskiest slides.
TESTIMONIALS = [
    ("testimonial-3.png", "Gerren Hansley",
     "I love myself!!! Discovering you has made a life changing couple of events for me, "
     "it won't be overnight but over life!!!! Thanks for a better n clearer understanding!!!", ""),
    ("testimonial-4.png", "Rochelle Johnson",
     "It was great. A lot of good options for people who are new to credit or needing to fix "
     "their credit. I think it's fantastic. Thank for sharing it with me.", ""),
    ("testimonial-12.png", "David",
     "Hey Nick I just want to let you know I'm grateful since the first day I met you and the "
     "team, from Vegas till now you really helped change my mindset and my financial situation "
     "from the jump bro I was really down bad when we met", ""),
    ("testimonial-6.png", "TransUnion investigation result",
     "INVESTIGATION RESULTS - DELETED: The disputed item(s) was removed from your credit report.",
     ""),
    ("testimonial-1.png", "Client credit report",
     "Three prior inquiries returned as Deleted and removed from the credit report.",
     "⚠️ This screenshot also shows a public bankruptcy record that did NOT come off. The court "
     "reference number is blurred, but the record is still visible and it argues against the "
     "slide. Consider cropping to the three deleted inquiries, or cutting this one."),
    ("testimonial-2.png", "Ricardo Bey",
     "Still a work in progress but we getting RESULTS. All personal info updated with the "
     "bureaus. And 13 inquires removed with 2 credit builders added to the profile..it's UP "
     "from here",
     "⚠️ Two problems. The message credits “the MINTERSHIP”, not Score Machine — as proof for "
     "tonight's offer that is misleading. And “13 inquires removed” is a specific results claim "
     "against slide 13's promise of no number."),
    ("testimonial-7.png", "Keyana Matthews",
     "I struggled with removing a $24k collection from my account for about 2 years. I paid "
     "LexingtonLaw to remove it & they couldn't. Wealth builders has officially changed my "
     "life. All from following the blueprint",
     "⚠️ Highest-risk slide in the deck. It names a competitor as having failed, which carries "
     "defamation risk with no upside, and it credits “Wealth builders”, not Score Machine. The "
     "account and phone numbers in the screenshot are blurred. Recommend cutting it."),
    ("testimonial-8.jpg", "Tracy Small",
     "1 year anniversary with the wealth builders!!!!!! Got one of my dream whips ... WITH NO "
     "MONEY DOWN!!!!",
     "⚠️ Credits “the wealth builders”, not Score Machine. Licence plate is blurred; faces are "
     "still visible, so get permission."),
    ("testimonial-11.jpg", "Credit score: 826, Exceptional",
     "Someone just became a member of the 800 club",
     "⚠️ A specific score on screen, minutes after slide 13 promises the room no number."),
    ("testimonial-10.jpg", "Takirra Haley",
     "You have been approved. $25,000 credit limit, 8.99% APR, $0 annual fee.",
     "⚠️ A specific approval and limit on screen, against slide 13's promise of no approval."),
    ("testimonial-9.jpg", "Nicholas Minter",
     "Quick lil $120k today w/ 1 inquiry",
     "⚠️ A specific funding figure — the clearest earnings-style claim in the deck and the one "
     "most likely to draw scrutiny."),
    ("testimonial-5.png", "Client travel redemption",
     "A round trip booked on points — 62,000 miles plus $11.20.",
     "⚠️ An airline booking, not a credit or funding outcome. It proves nothing about the ten "
     "Blueprint lines. Record locator is blurred."),
]

# Trimmed for the three-up layout. The full quote stays in the speaker notes.
SHORT = {
    "Gerren Hansley": "Discovering you has made a life changing couple of events for me… "
                      "Thanks for a better n clearer understanding!!!",
    "Rochelle Johnson": "A lot of good options for people who are new to credit or needing to "
                        "fix their credit. I think it's fantastic.",
    "David": "You really helped change my mindset and my financial situation from the jump.",
    "TransUnion investigation result": "INVESTIGATION RESULTS — DELETED: the disputed item was "
                                       "removed from your credit report.",
    "Client credit report": "Three prior inquiries returned as Deleted.",
    "Ricardo Bey": "13 inquires removed with 2 credit builders added to the profile.. "
                   "it's UP from here",
    "Keyana Matthews": "I struggled with removing a $24k collection for about 2 years… "
                       "following the blueprint changed my life.",
    "Tracy Small": "Got one of my dream whips … WITH NO MONEY DOWN!!!!",
    "Credit score: 826, Exceptional": "Someone just became a member of the 800 club",
    "Takirra Haley": "You have been approved. $25,000 credit limit, 8.99% APR.",
    "Nicholas Minter": "Quick lil $120k today w/ 1 inquiry",
    "Client travel redemption": "A round trip booked on points — 62,000 miles plus $11.20.",
}

# Grouped safest-first, so cutting from the last slide drops the riskiest claims.
GROUPS = [
    ("Social proof — in their words",
     ["Gerren Hansley", "Rochelle Johnson", "David"]),
    ("Social proof — items removed",
     ["TransUnion investigation result", "Client credit report", "Ricardo Bey"]),
    ("Social proof — what changed",
     ["Keyana Matthews", "Tracy Small", "Credit score: 826, Exceptional"]),
    ("Social proof — approvals and funding",
     ["Takirra Haley", "Nicholas Minter", "Client travel redemption"]),
]
BY_WHO = {t[1]: t for t in TESTIMONIALS}

# -- the demo marker, so the switch to live software is unmistakable on screen --
insert_after("S63 ", dict(
    label="Demo — DEMO", bg=DARK, layout="demo",
    word="DEMO", sub="30 MINUTES · LIVE SOFTWARE",
    offer="$1 to get started · 7 days, then $97/month",
    notes="Hold this slide while you switch to the software, then keep the offer line "
          "visible or pinned in chat for the whole demo — the link never leaves the screen.\n\n"
          "BEAT ORDER: 1 upload a report · 2 full AI analysis · 3 the Blueprint on a real file · "
          "4 personals that don't match · 5 utilization at 101% · 6 the paydown calculator · "
          "7 negative items · 8 AI letters · 9 print and certified mail · 10 progress report · "
          "11 bank and bureau matching · 12 the client view · 13 the referral link · "
          "14 a green file. Call the use-case number out loud on each beat.\n\n"
          "THREE ASKS, SPACED OUT:\n"
          "After beat 3 — \"Type YES if you want to see your own ten lines.\"\n"
          "After beat 6 — \"Type YES if you thought that number would be higher.\"\n"
          "After beat 14 — \"Type YES if that was helpful tonight.\"\n\n"
          "RULES: no live pulls, files pre-pulled hours ahead. Full-resolution screenshots of "
          "every beat as backup. Everything anonymised. Never demo a module you know is broken. "
          "If the platform stalls, move to screenshots without announcing it. Cut beats from the "
          "end, never the Blueprint."))

# Two slides of four screenshots, matching the layout the host built by hand. The
# images themselves live in the Canva account already and are inserted after import;
# only these eight exist there, so the remaining four testimonials are not shown.
PROOF_SLIDES = [
    ("Social proof — messages and removals",
     ["Client credit report", "Ricardo Bey", "Gerren Hansley", "Rochelle Johnson"]),
    ("Social proof — what changed",
     ["Keyana Matthews", "TransUnion investigation result", "Client travel redemption",
      "Tracy Small"]),
]

for _title, _whos in reversed(PROOF_SLIDES):
    _detail = []
    for _w in _whos:
        _img, _who, _quote, _warn = BY_WHO[_w]
        _detail.append(f'{_who} — "{_quote}"' + (("\n" + _warn) if _warn else ""))
    _n = ("Four screenshots supplied by the host, shown full height.\n\n"
          "FULL QUOTES AND CHECKS:\n\n" + "\n\n".join(_detail)
          + "\n\nGENERAL: every one of these is another person's private message or account. "
            "Get written permission before showing them, and say plainly that individual "
            "results are not typical.")
    insert_after("S52 ", dict(label=_title, bg=DARK, layout="proofshots",
                              kicker="WHAT PEOPLE ARE SAYING", names=_whos, notes=_n))

# ─────────────────────────────────────────────────────────────
# Original vector iconography (no stock art, no third-party assets)
# ─────────────────────────────────────────────────────────────

ICONS = {
 "house": '<path d="M12 56 L48 24 L84 56 V88 H60 V66 H36 V88 H12 Z"/>',
 "car": '<path d="M14 62 L22 40 H74 L82 62 V78 H70 V70 H26 V78 H14 Z"/>'
        '<circle cx="32" cy="76" r="8"/><circle cx="64" cy="76" r="8"/>',
 "contract": '<path d="M24 12 H62 L76 26 V88 H24 Z"/>'
             '<path d="M36 40 H64 M36 54 H64 M36 68 H54" stroke-width="5" fill="none"/>',
 "card": '<rect x="10" y="26" width="76" height="48" rx="6"/>'
         '<path d="M10 42 H86" stroke-width="8" fill="none"/>',
 "bank": '<path d="M48 14 L86 34 H10 Z"/><rect x="20" y="42" width="9" height="30"/>'
         '<rect x="43" y="42" width="9" height="30"/><rect x="66" y="42" width="9" height="30"/>'
         '<rect x="12" y="78" width="72" height="9"/>',
 "envelope": '<rect x="10" y="26" width="76" height="48" rx="5"/>'
             '<path d="M10 30 L48 56 L86 30" stroke-width="6" fill="none"/>',
 "report": '<rect x="20" y="12" width="56" height="76" rx="5"/>'
           '<rect x="32" y="56" width="8" height="18"/><rect x="44" y="44" width="8" height="30"/>'
           '<rect x="56" y="32" width="8" height="42"/>',
 "gauge": '<path d="M14 68 A34 34 0 0 1 82 68" stroke-width="9" fill="none"/>'
          '<path d="M48 68 L70 44" stroke-width="7" fill="none"/><circle cx="48" cy="68" r="7"/>',
 "arrowup": '<path d="M16 74 L38 50 L54 62 L82 28"  stroke-width="8" fill="none"/>'
            '<path d="M62 28 H82 V48"  stroke-width="8" fill="none"/>',
 "arrowdown": '<path d="M16 28 L38 52 L54 40 L82 74" stroke-width="8" fill="none"/>'
              '<path d="M62 74 H82 V54" stroke-width="8" fill="none"/>',
 "briefcase": '<rect x="12" y="32" width="72" height="50" rx="6"/>'
              '<path d="M36 32 V22 H60 V32" stroke-width="6" fill="none"/>',
 "people": '<circle cx="34" cy="34" r="13"/><circle cx="66" cy="38" r="10"/>'
           '<path d="M12 78 a22 22 0 0 1 44 0 Z"/><path d="M56 78 a16 16 0 0 1 32 0 Z"/>',
 "check": '<circle cx="48" cy="50" r="34"/>',
 "link": '<path d="M40 34 H30 a18 18 0 0 0 0 36 h10 M56 34 h10 a18 18 0 0 1 0 36 H56"'
         ' stroke-width="8" fill="none"/><path d="M34 52 H62" stroke-width="8" fill="none"/>',
 "calendar": '<rect x="12" y="24" width="72" height="62" rx="6"/>'
             '<path d="M12 42 H84" stroke-width="6" fill="none"/>'
             '<rect x="28" y="12" width="7" height="20" rx="3"/>'
             '<rect x="61" y="12" width="7" height="20" rx="3"/>',
}


def icon(name, cls="ic"):
    return (f'<svg class="{cls}" viewBox="0 0 96 100" aria-hidden="true">'
            f'<g>{ICONS[name]}</g></svg>')


def icon_row(names):
    return '<div class="icrow">' + "".join(icon(n) for n in names) + '</div>'


def stat_tiles(tiles):
    out = ['<div class="tiles">']
    for val, lab in tiles:
        out.append(f'<div class="tile"><div class="tval">{esc(val)}</div>'
                   f'<div class="tlab">{esc(lab)}</div></div>')
    out.append('</div>')
    return "".join(out)


def tally_marks(n, label):
    """n discrete marks - a count already stated in the script, drawn not invented."""
    w, gap, h = 22, 12, 74
    total = n * w + (n - 1) * gap
    out = [f'<svg class="tally" viewBox="0 0 {total} {h}" role="img" '
           f'aria-label="{esc(label)}">']
    for i in range(n):
        out.append(f'<rect x="{i*(w+gap)}" y="0" width="{w}" height="{h}" rx="4"/>')
    out.append('</svg>')
    return "".join(out)


def chip_row(n, label):
    out = [f'<div class="chiprow" role="img" aria-label="{esc(label)}">']
    for _ in range(n):
        out.append('<span class="gchip"></span>')
    out.append('</div>')
    return "".join(out)


def flow_steps(steps):
    out = ['<div class="flow">']
    for i, st in enumerate(steps):
        if i:
            out.append('<span class="farrow">&#9654;</span>')
        out.append(f'<div class="fstep"><span class="fnum">{i+1}</span>'
                   f'<span class="ftxt">{esc(st)}</span></div>')
    out.append('</div>')
    return "".join(out)


def bureau_cards(names):
    out = ['<div class="bureaus">']
    for n in names:
        out.append(f'<div class="bcard">{icon("report","ic bic")}'
                   f'<div class="bname">{esc(n)}</div></div>')
    out.append('</div>')
    return "".join(out)


# ─────────────────────────────────────────────────────────────
# Rendering
# ─────────────────────────────────────────────────────────────

def wrap_text(text, max_chars):
    """Break on word boundaries into lines of at most max_chars."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        cand = w if not cur else cur + " " + w
        if len(cand) <= max_chars:
            cur = cand
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def esc(t):
    return html.escape(t, quote=True)


VB_W, VB_H = 1440, 660


def chart_svg(rows):
    """Horizontal bar chart. Single series, magnitude -> bars, direct labels, no legend.

    No chart title and no total: neither appears on this slide in the source, and the
    $997 total is the reveal on the very next slide.
    """
    lab_end, x0, track = 760, 800, 520
    top, bar_h, gap = 30, 48, 38
    mx = max(v for _, v in rows)
    out = [f'<svg class="chart" viewBox="0 0 {VB_W} {VB_H}" role="img" '
           'aria-label="Value stack, seven components by dollar value">']
    for i, (lab, val) in enumerate(rows):
        y = top + i * (bar_h + gap)
        w = round(track * val / mx, 1)
        out.append(f'<text class="c-lab" x="{lab_end}" y="{y + bar_h/2 + 9}" text-anchor="end">{esc(lab)}</text>')
        out.append(f'<rect class="c-bar" x="{x0}" y="{y}" width="{w}" height="{bar_h}" rx="4"/>')
        out.append(f'<text class="c-val" x="{x0 + w + 18}" y="{y + bar_h/2 + 11}">${val}</text>')
    out.append('</svg>')
    return "\n".join(out)


def render(s):
    L, b = s["layout"], []
    if L == "title":
        b.append(f'<h1 class="t-title">{esc(s["title"])}</h1>')
        b.append(f'<p class="t-sub">{esc(s["sub"])}</p>')
    elif L == "statement":
        for ln in wrap_text(s["text"], 26):
            b.append(f'<h1 class="t-state">{esc(ln)}</h1>')
        if s.get("sub"):
            b.append(f'<p class="t-statsub">{s["sub"]}</p>')
    elif L == "heading":
        b.append(f'<h2 class="t-head">{esc(s["text"])}</h2>')
        if s.get("sub"):
            b.append(f'<p class="t-statsub">{s["sub"]}</p>')
    elif L == "lines":
        for ln in s["lines"]:
            if ln == "":
                b.append('<p class="t-line spacer">&nbsp;</p>')
            elif "<" in ln or len(ln) <= 46:
                b.append(f'<p class="t-line">{ln}</p>')
            else:
                for part in wrap_text(ln, 46):
                    b.append(f'<p class="t-line">{esc(part)}</p>')
    elif L == "bullets":
        b.append('<ul class="t-ul">' + "".join(f'<li>{esc(x)}</li>' for x in s["bullets"]) + '</ul>')
    elif L == "numbered":
        b.append('<ol class="t-ol">' + "".join(f'<li>{x}</li>' for x in s["items"]) + '</ol>')
        if s.get("footer"):
            b.append(f'<p class="t-footer">{esc(s["footer"])}</p>')
    elif L == "tenlines":
        b.append('<ol class="t-ten">' + "".join(f'<li>{esc(x)}</li>' for x in s["items"]) + '</ol>')
    elif L == "twocol":
        b.append('<div class="t-cols">')
        for head, items in ((s["col_a_head"], s["col_a"]), (s["col_b_head"], s["col_b"])):
            b.append(f'<div class="t-col"><h3>{esc(head)}</h3><ul>'
                     + "".join(f'<li>{esc(i)}</li>' for i in items) + '</ul></div>')
        b.append('</div>')
    elif L == "usecase":
        if s.get("icon"):
            b.append(icon_row([s["icon"]]))
        b.append(f'<h2 class="t-uc">{esc(s["num"])}</h2>')
        if s.get("sub"):
            b.append(f'<p class="t-ucsub">{esc(s["sub"])}</p>')
        for ln in s["lines"]:
            b.append(f'<p class="t-line">{esc(ln)}</p>')
    elif L == "legend":
        b.append('<div class="t-legend">')
        for color, label in s["rows"]:
            b.append(f'<div class="t-legrow"><span class="chip" style="background:{color}"></span>'
                     f'<span class="t-leglab">{esc(label)}</span></div>')
        b.append('</div>')
    elif L == "statfocus":
        b.append(f'<p class="t-kicker">{esc(s["kicker"])}</p>')
        b.append(f'<p class="t-stat">{esc(s["stat"])}</p>')
    elif L == "placeholder":
        b.append(f'<p class="t-ph">{esc(s["text"])}</p>')
        if s.get("sub"):
            b.append(f'<p class="t-line">{esc(s["sub"])}</p>')
    elif L == "chart":
        b.append(chart_svg(s["rows"]))
    elif L == "price":
        b.append(f'<p class="t-strike">{esc(s["strike"]) if s["strike"] else "&nbsp;"}</p>')
        b.append(f'<p class="t-big">{esc(s["big"])}</p>')
        b.append(f'<p class="t-pricesub">{esc(s["sub"]) if s["sub"] else "&nbsp;"}</p>')
    elif L == "close":
        for ln in s["lines"]:
            for part in wrap_text(ln, 44):
                b.append(f'<p class="t-closeline">{esc(part)}</p>')
        b.append(f'<p class="t-big close">{esc(s["big"])}</p>')
        b.append(f'<p class="t-pricesub">{esc(s["sub"])}</p>')
    elif L == "iconlines":
        b.append(icon_row(s["icons"]))
        for ln in s["lines"]:
            for part in wrap_text(ln, 46):
                b.append(f'<p class="t-line">{esc(part)}</p>')
    elif L == "statgrid":
        if s.get("kicker"):
            b.append(f'<p class="t-kicker">{esc(s["kicker"])}</p>')
        b.append(stat_tiles(s["tiles"]))
        if s.get("chips"):
            b.append(chip_row(s["chips"], s.get("chips_label", "")))
        if s.get("foot"):
            b.append(f'<p class="t-footer">{esc(s["foot"])}</p>')
    elif L == "decay":
        b.append(f'<p class="t-kicker">{esc(s["kicker"])}</p>')
        b.append(tally_marks(s["marks"], s["marks_label"]))
        b.append(f'<p class="t-stat">{esc(s["stat"])}</p>')
    elif L == "flow":
        b.append(flow_steps(s["steps"]))
    elif L == "bureaus":
        for ln in s["lines"]:
            if ln:
                b.append(f'<p class="t-line">{ln}</p>')
        b.append(bureau_cards(s["names"]))
    elif L == "bio":
        b.append('<div class="bio">')
        b.append(f'<img class="biophoto" src="{BG_BASE}/headshot.jpg" alt="Host portrait">')
        b.append('<div class="biotext">')
        b.append(f'<h2 class="bioname">{esc(s["name"])}</h2>')
        for para in s["paras"]:
            b.append(f'<p class="biopara">{esc(para)}</p>')
        b.append('</div></div>')
    elif L == "proofshots":
        # The four screenshots are inserted into this page after import, straight from
        # the assets already in the user's Canva account. The page carries the heading
        # and the attributions; the middle band is left clear for the images.
        b.append(f'<p class="q-kicker tk3">{esc(s["kicker"])}</p>')
        b.append('<div class="shotspacer"></div>')
        b.append('<div class="shotnames">')
        for who in s["names"]:
            b.append(f'<span class="shotname">{esc(who)}</span>')
        b.append('</div>')
    elif L == "testimonial":
        # Finished quote cards, not empty photo frames. The screenshots hold other
        # people's financial data and the repo feeding the importer is public, so they
        # are never committed; a card stands on its own and a screenshot can be dropped
        # behind it later in Canva without leaving a hole on the slide meanwhile.
        b.append('<div class="tgrid">')
        for c in s["cards"]:
            b.append('<div class="tcard">')
            b.append('<span class="tmark">&ldquo;</span>')
            b.append(f'<p class="tquote">{esc(c["quote"])}</p>')
            b.append('<span class="trule"></span>')
            b.append(f'<p class="twho">{esc(c["who"])}</p>')
            b.append('</div>')
        b.append('</div>')
    elif L == "link":
        b.append(f'<p class="linkkick">{esc(s["kicker"])}</p>')
        # An empty box would read as a blank slide, so the box only appears once a
        # real link is set; otherwise the heading and price line carry the slide.
        if s["url"]:
            b.append(f'<div class="linkbox">{esc(s["url"])}</div>')
        b.append(f'<p class="linkfoot">{esc(s["foot"])}</p>')
    elif L == "demo":
        b.append(f'<p class="demoword">{esc(s["word"])}</p>')
        b.append(f'<p class="demosub">{esc(s["sub"])}</p>')
        b.append(f'<p class="demooffer">{esc(s["offer"])}</p>')
    elif L == "blueprintlive":
        b.append(f'<p class="t-kicker">{esc(s["kicker"])}</p>')
        b.append('<div class="bpcols">')
        for start, col in ((1, s["items"][:5]), (6, s["items"][5:])):
            b.append(f'<ol class="bpcol" start="{start}">')
            # Plain list items: Canva's importer scatters inline spans inside <li>,
            # so the chips are spoken rather than drawn.
            for it in col:
                b.append(f'<li>{esc(it)}</li>')
            b.append('</ol>')
        b.append('</div>')
    elif L == "compare":
        b.append('<div class="cmp">')
        for pane in s["panes"]:
            b.append(f'<div class="cpane {pane["tone"]}">')
            b.append(f'<p class="cverdict">{esc(pane["verdict"])}</p>')
            b.append('<div class="cchips">')
            for tone in pane["chips"]:
                b.append(f'<span class="cchip {tone}"></span>')
            b.append('</div>')
            b.append(f'<p class="cnote">{esc(pane["note"])}</p>')
            b.append('</div>')
        b.append('</div>')
        b.append(f'<p class="t-footer">{esc(s["footer"])}</p>')
    elif L == "question":
        b.append(f'<p class="q-kicker">{esc(s["kicker"])}</p>')
        for ln in wrap_text(s["text"], 34):
            b.append(f'<p class="q-text">{esc(ln)}</p>')
    elif L == "qa":
        b.append(f'<h1 class="t-state qa">{esc(s["text"])}</h1>')
        b.append('<ol class="qa-bp">' + "".join(f'<li>{esc(x)}</li>' for x in s["blueprint"]) + '</ol>')
        b.append(f'<p class="qa-offer">{esc(s["offer"])}</p>')
    return "\n      ".join(b)


CSS = """


/* Navigation furniture: act name top-left, slide number top-right. */
.eyebrow{position:absolute;z-index:3;left:196px;top:132px;width:1200px;text-align:left;
  font-family:'Archivo Black',Arial,sans-serif;font-size:23px;letter-spacing:4px}
.pagenum{position:absolute;z-index:3;right:196px;top:132px;
  font-family:'Archivo Black',Arial,sans-serif;font-size:23px;opacity:.55}
.page.light .eyebrow{color:#8A8F96}
.page.light .pagenum{color:#8A8F96}
.page.dark .eyebrow{color:#FFB81C}
.page.dark .pagenum{color:#9AA0A8}

.linkkick{font-family:'Archivo Black',Arial,sans-serif;font-size:96px;letter-spacing:2px;
  color:#16181C;margin-bottom:34px}
.linkbox{width:1240px;padding:52px 40px;border-radius:20px;border:6px solid #16181C;
  font-family:'Archivo Black',Arial,sans-serif;font-size:76px;word-break:break-all}
.linkfoot{font-size:34px;font-weight:700;margin-top:38px;color:#3A3A3A}

.demoword{font-family:'Archivo Black',Arial,sans-serif;font-size:268px;line-height:.94;
  letter-spacing:14px;color:#FFFFFF}
.demosub{font-size:44px;font-weight:700;color:#FFB81C;letter-spacing:5px;margin-top:16px}
.demooffer{font-size:30px;font-weight:600;color:#C9CDD3;margin-top:56px}

.bpcols{display:flex;gap:80px;width:1440px;text-align:left}
.bpcol{width:680px;list-style:decimal;padding-left:44px}
.bpcol li{font-size:30px;line-height:1.35;margin:22px 0;font-weight:600}
.bpchip{display:inline-block;width:26px;height:26px;border-radius:50%;margin-right:16px;
  vertical-align:-3px;border:4px solid rgba(0,0,0,.34)}
.page.dark .bpchip{border-color:rgba(255,255,255,.45)}

.cmp{display:flex;gap:70px;width:1440px;justify-content:center}
.cpane{width:640px;padding:44px 36px;border-radius:22px;border:4px solid}
.cpane.bad{border-color:#D7191C;background:rgba(215,25,28,.07)}
.cpane.good{border-color:#1A7A3C;background:rgba(26,122,60,.07)}
.cverdict{font-family:'Archivo Black',Arial,sans-serif;font-size:46px}
.cpane.bad .cverdict{color:#C0161A}
.cpane.good .cverdict{color:#177036}
.cchips{display:flex;flex-wrap:nowrap;gap:12px;justify-content:center;margin:30px 0 24px}
.cchip{width:42px;height:42px;flex:none;border-radius:50%;border:3px solid rgba(0,0,0,.30)}
.cchip.r{background:#D7191C}
.cchip.g{background:#1A7A3C}
.cchip.n{background:#C6CBD1}
.cnote{font-size:30px;font-weight:600}

.ic{width:96px;height:100px;flex:none}
.page.light .ic{fill:#16181C;stroke:#16181C}
.page.dark  .ic{fill:#FFFFFF;stroke:#FFFFFF}
.icrow{display:flex;gap:64px;justify-content:center;margin-bottom:40px}
.tiles{display:flex;gap:40px;justify-content:center;margin:14px 0 26px}
.tile{width:400px;padding:30px 20px;border-radius:18px;
  background:rgba(0,0,0,.05);border:3px solid rgba(0,0,0,.14)}
.page.dark .tile{background:rgba(255,255,255,.07);border-color:rgba(255,255,255,.20)}
.tval{font-family:'Archivo Black',Arial,sans-serif;font-size:76px;line-height:1.05}
.tlab{font-size:30px;font-weight:600;margin-top:10px;opacity:.85}
.tally{width:1000px;height:74px;margin:8px 0 26px}
.page.light .tally rect{fill:#ED1C24}
.page.dark  .tally rect{fill:#ED1C24}
.chiprow{display:flex;gap:16px;justify-content:center;margin-top:8px}
.gchip{width:56px;height:56px;border-radius:50%;background:#00A03C;
  border:4px solid rgba(0,0,0,.30)}
.flow{display:flex;flex-wrap:wrap;gap:14px;justify-content:center;align-items:center;width:1400px}
.fstep{display:flex;align-items:center;gap:14px;padding:16px 22px;border-radius:14px;
  background:rgba(0,0,0,.06);border:3px solid rgba(0,0,0,.14);max-width:640px}
.page.dark .fstep{background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.22)}
.fnum{font-family:'Archivo Black',Arial,sans-serif;font-size:30px;color:#ED1C24;flex:none}
.ftxt{font-size:28px;font-weight:600;text-align:left;line-height:1.3}
.farrow{font-size:26px;opacity:.5}
.bureaus{display:flex;gap:56px;justify-content:center;margin-top:38px}
.bcard{width:380px;padding:30px 18px;border-radius:18px;background:rgba(0,0,0,.05);
  border:3px solid rgba(0,0,0,.14)}
.page.dark .bcard{background:rgba(255,255,255,.07);border-color:rgba(255,255,255,.20)}
.bic{width:70px;height:74px}
.bname{font-family:'Archivo Black',Arial,sans-serif;font-size:36px;margin-top:12px}
.bio{display:flex;gap:64px;align-items:center;width:1400px;text-align:left}
.biophoto{width:400px;height:533px;flex:none;border-radius:20px;object-fit:cover;
  box-shadow:0 0 0 4px rgba(0,0,0,.18)}
.biotext{flex:1}
.bioname{font-size:56px;margin-bottom:22px}
.biopara{font-size:31px;line-height:1.45;font-weight:600;margin-bottom:18px}
.q-kicker.tk3{width:1440px;text-align:center;margin-bottom:0;font-size:32px;letter-spacing:6px}
.shotspacer{height:640px}
.shotnames{display:flex;width:1440px;justify-content:space-between}
.shotname{width:323px;text-align:center;font-family:'Archivo Black',Arial,sans-serif;
  font-size:23px;color:#FFB81C}
.page.light .shotname{color:#B07A00}

.tgrid{display:flex;gap:52px;width:1440px;justify-content:center;align-items:stretch}
.tcard{width:445px;padding:44px 38px 40px;border-radius:20px;text-align:left;
  background:rgba(255,255,255,.07);border:3px solid rgba(255,255,255,.20);
  display:flex;flex-direction:column}
.page.light .tcard{background:rgba(0,0,0,.05);border-color:rgba(0,0,0,.14)}
.tmark{font-family:'Archivo Black',Arial,sans-serif;font-size:86px;line-height:.6;
  color:#FFB81C;display:block;margin-bottom:22px}
.page.light .tmark{color:#B07A00}
.tquote{font-size:27px;line-height:1.42;font-weight:600;flex:1}
.trule{display:block;width:70px;height:4px;background:#FFB81C;margin:26px 0 18px}
.page.light .trule{background:#B07A00}
.twho{font-family:'Archivo Black',Arial,sans-serif;font-size:24px;color:#FFB81C}
.page.light .twho{color:#B07A00}

:root{
  --ink:#0B0B0B; --ink-2:#3A3A3A; --paper:#FFFFFF;
  --red:#ED1C24; --gold:#FFB81C; --green:#00C637; --bar:#16181C;
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#20232A;font-family:'Inter','Helvetica Neue',Arial,sans-serif}
.page{position:relative;width:1920px;height:1080px;overflow:hidden;margin:0 auto 40px;background:var(--paper)}
.bg{position:absolute;inset:0;width:1920px;height:1080px;object-fit:cover;z-index:0}
.safe{position:absolute;z-index:2;left:240px;top:196px;width:1440px;height:700px;
  display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}
.page.light .safe{color:var(--ink)}
.page.dark .safe{color:#FFFFFF}
h1,h2,h3{font-family:'Archivo Black','Arial Black',Arial,sans-serif;font-weight:900;
  letter-spacing:-.5px;line-height:1.04}

.t-title{width:1400px;font-size:104px;text-transform:uppercase}
.t-sub{width:1440px;font-size:42px;margin-top:30px;color:#EDEDED;font-weight:600}
.t-state{width:1400px;font-size:76px;margin:2px 0}
.t-state.qa{width:1440px;font-size:76px;margin-bottom:26px}
.t-statsub{width:1400px;font-size:40px;line-height:1.35;margin-top:28px;font-weight:600}
.t-head{width:1400px;font-size:64px;text-transform:uppercase}
.t-line{width:1400px;font-size:44px;line-height:1.45;font-weight:600}
.t-line.spacer{height:24px}
.t-ul{width:1240px;text-align:left;padding-left:58px;list-style:disc}
.t-ul li{font-size:40px;line-height:1.4;margin:20px 0;font-weight:600}
.t-ol{width:1240px;text-align:left;padding-left:66px;list-style:decimal}
.t-ol li{font-size:38px;line-height:1.35;margin:18px 0;font-weight:600}
.t-ten{width:1300px;text-align:left;padding-left:66px;list-style:decimal}
.t-ten li{font-size:40px;line-height:1.3;margin:12px 0;font-weight:600}
.t-footer{width:1440px;font-family:'Archivo Black',Arial,sans-serif;font-size:54px;margin-top:32px}
.t-cols{display:flex;gap:100px;text-align:left;width:1440px}
.t-col{width:670px}
.t-col h3{font-size:42px;margin-bottom:24px}
.t-col ul{padding-left:46px;list-style:disc}
.t-col li{font-size:34px;line-height:1.35;margin:16px 0;font-weight:600}
.t-uc{width:1400px;font-size:56px;text-transform:uppercase}
.t-ucsub{width:1440px;font-size:44px;margin:20px 0 32px;font-weight:700;color:var(--ink-2)}
.t-legend{width:1180px;display:flex;flex-direction:column;gap:42px}
.t-legrow{display:flex;align-items:center;gap:38px}
.chip{width:72px;height:72px;border-radius:50%;flex:none;border:4px solid rgba(0,0,0,.85)}
.t-leglab{font-family:'Archivo Black',Arial,sans-serif;font-size:46px}
.t-kicker{width:1440px;font-size:46px;font-weight:700;margin-bottom:36px}
.t-stat{width:1400px;font-family:'Archivo Black',Arial,sans-serif;font-size:94px;color:var(--red)}
.t-ph{width:1240px;font-size:42px;font-weight:700;color:#8A8A8A;
  border:4px dashed #B9B9B9;border-radius:14px;padding:52px 64px}
.chart{width:1440px;height:660px}
.c-lab{font-family:'Inter',Arial,sans-serif;font-size:24px;font-weight:600;fill:#25282E}
.c-bar{fill:var(--bar)}
.c-val{font-family:'Archivo Black',Arial,sans-serif;font-size:32px;fill:#0B0B0B}
.t-strike{width:1440px;font-size:62px;font-weight:700;text-decoration:line-through;
  color:#9BA0A8;min-height:76px}
.t-big{width:1400px;font-family:'Archivo Black',Arial,sans-serif;font-size:146px;
  line-height:1.02;margin:16px 0}
.t-big.close{font-size:110px;margin-top:46px}
.t-pricesub{width:1440px;font-size:44px;font-weight:600;color:#E4E4E4;min-height:56px}
.t-closeline{width:1400px;font-size:46px;line-height:1.4;font-weight:600}
.q-kicker{width:1440px;font-family:'Archivo Black',Arial,sans-serif;font-size:38px;
  letter-spacing:6px;color:var(--gold);margin-bottom:48px}
.q-text{width:1400px;font-family:'Archivo Black',Arial,sans-serif;font-size:58px;line-height:1.22;margin:3px 0}
.qa-bp{width:1100px;text-align:left;padding-left:62px;list-style:decimal;margin-bottom:30px}
.qa-bp li{font-size:26px;line-height:1.4;margin:7px 0;font-weight:600}
.qa-offer{width:1440px;font-family:'Archivo Black',Arial,sans-serif;font-size:38px;color:var(--gold)}
"""


def main():
    pages, act = [], ACTS[0][2]
    for i, s in enumerate(S, 1):
        bgfile = "bg_dark.jpg" if s["bg"] == DARK else "bg_light.png"
        act = act_for(s["label"], act)
        topic = topic_for(s)
        # Canva lists this in its page navigator, so lead with the act and topic.
        page_title = f"{i:02d} · {act.split('—')[0].strip()} · {topic}"
        pages.append(
            f'  <section class="page {s["bg"]}" data-document-role="page"\n'
            f'           data-label="{esc(page_title)}"\n'
            f'           data-speaker-notes="{esc(s["notes"])}">\n'
            f'    <img class="bg" src="{BG_BASE}/{bgfile}" alt="">\n'
            f'    <p class="eyebrow">{esc(act)}</p>\n'
            f'    <p class="pagenum">{i}</p>\n'
            f'    <div class="safe">\n      {render(s)}\n    </div>\n'
            f'  </section>'
        )
    doc = ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
           "<title>The Score Machine — 90-Minute Webinar</title>\n"
           f"<style>{CSS}</style>\n</head>\n<body>\n" + "\n".join(pages) + "\n</body>\n</html>\n")

    out = sys.argv[2] if len(sys.argv) > 2 else "score-machine-deck.html"
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)

    q = sum(1 for s in S if s["layout"] == "question")
    print(f"pages={len(S)}  question_slides={q}  base_slides={len(S)-q}")
    print(f"dark={sum(1 for s in S if s['bg']==DARK)}  light={sum(1 for s in S if s['bg']==LIGHT)}")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
