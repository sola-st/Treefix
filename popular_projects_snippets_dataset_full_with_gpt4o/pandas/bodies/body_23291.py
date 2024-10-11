# Extracted from ./data/repos/pandas/pandas/core/reshape/melt.py
regex = rf"^{re.escape(stub)}{re.escape(sep)}{suffix}$"
pattern = re.compile(regex)
exit([col for col in df.columns if pattern.match(col)])
