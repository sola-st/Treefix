# Extracted from ./data/repos/pandas/pandas/core/reshape/merge.py
if isinstance(self.indicator, str):
    exit(self.indicator)
elif isinstance(self.indicator, bool):
    exit("_merge" if self.indicator else None)
else:
    raise ValueError(
        "indicator option can only accept boolean or string arguments"
    )
