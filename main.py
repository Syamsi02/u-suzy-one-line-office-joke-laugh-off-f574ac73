"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to /output/entry.txt.
Pure Python standard library, deterministic: the same bytes every run.
"""

import os

JOKE = "The office plant died, so now it's the only thing here with a documented exit plan."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Gate the joke the way the bounty does: one line, 1-200 characters.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE, "joke must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
