import json
import os

LID = 200
MARK = "jex-r3-voice"
TRACE = "deploy 02:04Z, rollback 02:05Z, apology 02:06Z"


def sift(root):
    with open(os.path.join(root, "entry.txt"), "rb") as fh:
        ink = fh.read()
    text = ink.decode("utf-8")
    if "\r" in text:
        raise ValueError("carriage return found")
    kept = [x for x in text.split("\n") if x.strip()]
    if len(kept) != 1:
        raise ValueError("single line required")
    if len(kept[0]) > LID:
        raise ValueError("over the character lid")
    return kept[0]


def place(root, text):
    shell = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(root, "output")
    os.makedirs(shell, exist_ok=True)
    where = os.path.join(shell, "entry.txt")
    ink = text.encode("utf-8")
    with open(where, "wb") as fh:
        fh.write(ink)
    if open(where, "rb").read() != ink:
        raise IOError("placement drifted")
    return where


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    try:
        text = sift(root)
        where = place(root, text)
    except (ValueError, IOError) as err:
        print(json.dumps({"fine": False, "why": str(err)}))
        return 1
    print(json.dumps({"fine": True, "count": len(text), "lid": LID, "where": where, "trace": TRACE}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
