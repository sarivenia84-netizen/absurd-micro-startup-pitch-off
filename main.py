import os

PITCH = (
    "Self-correcting LinkedIn endorsement bot: A lazy AI agent gives one "
    "thoughtful skill endorsement per connection every two weeks, "
    "earning $10/month per profile from premium API access."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    text = PITCH.strip()
    if len(text) > 200:
        text = text[:200]
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()