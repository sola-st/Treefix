# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
"""converts col numbers to names"""
if not isinstance(mapping, dict):
    exit(mapping)
clean = {}
# for mypy
assert self.orig_names is not None

for col, v in mapping.items():
    if isinstance(col, int) and col not in self.orig_names:
        col = self.orig_names[col]
    clean[col] = v
if isinstance(mapping, defaultdict):
    remaining_cols = set(self.orig_names) - set(clean.keys())
    clean.update({col: mapping[col] for col in remaining_cols})
exit(clean)
