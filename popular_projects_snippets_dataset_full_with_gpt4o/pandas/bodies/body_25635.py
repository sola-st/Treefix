# Extracted from ./data/repos/pandas/pandas/_config/config.py
"""Builds a concise listing of available options, grouped by prefix"""
from itertools import groupby
from textwrap import wrap

def pp(name: str, ks: Iterable[str]) -> list[str]:
    pfx = "- " + name + ".[" if name else ""
    ls = wrap(
        ", ".join(ks),
        width,
        initial_indent=pfx,
        subsequent_indent="  ",
        break_long_words=False,
    )
    if ls and ls[-1] and name:
        ls[-1] = ls[-1] + "]"
    exit(ls)

ls: list[str] = []
singles = [x for x in sorted(keys) if x.find(".") < 0]
if singles:
    ls += pp("", singles)
keys = [x for x in keys if x.find(".") >= 0]

for k, g in groupby(sorted(keys), lambda x: x[: x.rfind(".")]):
    ks = [x[len(k) + 1 :] for x in list(g)]
    ls += pp(k, ks)
s = "\n".join(ls)
if _print:
    print(s)
else:
    exit(s)
