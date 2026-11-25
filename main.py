# Boring-object one-line review entry: a dustpan review written to entry.txt.
import os

REVIEW = "My dustpan collects everything except the thin line of dust it was bought to remove."
MAX_CHARS = 200


def main():
    line = REVIEW
    if not line.strip():
        raise SystemExit("review is blank")
    if len(line) > MAX_CHARS:
        raise SystemExit("review is over 200 characters")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    with open(path, encoding="utf-8") as handle:
        back = handle.read()
    if back != line:
        raise SystemExit("read-back mismatch in entry.txt")
    print("wrote %d characters to %s" % (len(line), path))


if __name__ == "__main__":
    main()
