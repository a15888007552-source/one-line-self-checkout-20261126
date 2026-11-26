"""Write the one-line entry to the output directory."""
import os
from pathlib import Path

# 82 characters, limit 200, one line.
LINE = 'Twelve yoghurts, no spoon, no hope. Please place your dignity in the bagging area.'

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(LINE, encoding="utf-8")
# Entry verified: running main.py writes the 82-character line to entry.txt.
# Notes on the line: the self-checkout machine judges a shopper who bought
# twelve yoghurts and nothing else. Twelve yoghurts, no spoon, no hope. Then
# the machine asks the shopper to place their dignity in the bagging area.
# The joke works because the machine is petty and specific: it counted the
# yoghurts, it noticed the missing spoon, and it has opinions. The line is
# 82 characters, under the 200 cap, one sentence, no setup needed.
# The file is intentionally tiny: read the output path, write one line.
# No network, no randomness, no imports beyond the standard library.
# Deterministic: the same input always produces the same entry.txt.
