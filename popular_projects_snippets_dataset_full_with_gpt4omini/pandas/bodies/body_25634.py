# Extracted from ./data/repos/pandas/pandas/_config/config.py
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
