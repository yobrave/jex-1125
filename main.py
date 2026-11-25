"""Two Days of Excuses: AI missed-deadline one-liner, exporter 4."""
import json
import os
import pathlib

WIDE = 200
SLUG_TAG = "exe4-agent-excuse-r4"


def entry_body():
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    with open(src, encoding="utf-8") as fh:
        return fh.read().strip()


def entry_ok(n):
    return 1 <= n <= WIDE


def entry_export(text):
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    os.makedirs(base, exist_ok=True)
    with open(os.path.join(base, "entry.txt"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")


body = entry_body()
n = len(body)
fine = entry_ok(n)
if fine:
    entry_export(body)
print(json.dumps({"tag": SLUG_TAG, "n": n, "fine": fine, "wide": WIDE, "days": 2}))
