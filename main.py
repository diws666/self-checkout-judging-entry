#!/usr/bin/env python3
"""Self-checkout judging entry.

Writes the single judged line to /output/entry.txt (UTF-8, no trailing newline).
"""

OUTPUT_PATH = "/output/entry.txt"
LINE = "Unexpected item in the bagging area: your confidence. Please remove it and try again."


def main() -> None:
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
