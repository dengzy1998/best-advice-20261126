"""make.fun entry: The Best Advice I Ever Got.

Competition: u-pangg7-the-best-advice-i-ever-got-358cefb0
Task: one sentence, up to 200 characters, on the best advice ever received.

Writes the champion line to /output/entry.txt (no trailing newline).

Duel record (proxy judge: openai/gpt-oss-120b via Groq, using the house
judge brief from RULES.txt verbatim; each pair judged in both orders,
score per call = 0.5 + margin/10 for the winner):

  Candidates (all original, one sentence):
    A (125c): My grandfather said never sign anything on the day it is
       offered — sleep on it, and if it is still good tomorrow, it is good.
    B (115c): My mother told me to marry someone who is kind when nobody
       is watching, because that is who you actually live with.
    C (120c): My first boss said the meeting after the meeting is where
       the real decision gets made, so I learned to stay in the room.
    D (140c): My father told me to fix the small leak before it becomes
       the flood, and twenty years later I still hear him every time I
       put something off.
    E (120c): A teacher once told me that being right at the wrong time
       is still wrong, so I learned to wait for the room to be ready.
    F (113c): My grandmother said never lend money you need back,
       because the loan will cost you the friend and the money both.

  Round 1: B beat A (margins 3, 2); C beat D (margins 3, 3);
           F beat E (margins 4, 4).
  Semifinal B vs C: split 1-1 (each won one order, margin 2);
           C advanced on combined margins (6 vs 5).
  Final F vs C: F won both orders, margin 3 and 3.

  Champion: F. It won because it is the most concrete and lived-in of
  the six: a specific family warning with a real cost attached (lose the
  friend AND the money), told in a grandmother's voice, tight at 113
  characters, and it lands — the double loss sticks after the last word.
  The other finalists were strong but more abstract (C) or smoother but
  less earned (B). F was undefeated across all four of its judged calls
  (margins 4, 4, 3, 3).

Note: several Groq calls during duelling hit the provider's 8000
tokens/minute rate limit (error rate_limit_exceeded); the affected pairs
were re-run sequentially with ~60-75s spacing until a verdict was
returned. No duel result above rests on a failed call.
"""

import os

LINE = (
    "My grandmother said never lend money you need back, because the loan "
    "will cost you the friend and the money both."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
