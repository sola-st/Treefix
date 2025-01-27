# Extracted from ./data/repos/pandas/pandas/_config/config.py
if len(args) % 2 != 0 or len(args) < 2:
    raise ValueError(
        "Need to invoke as option_context(pat, val, [(pat, val), ...])."
    )

self.ops = list(zip(args[::2], args[1::2]))
