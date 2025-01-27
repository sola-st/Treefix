# Extracted from ./data/repos/pandas/pandas/tseries/frequencies.py
rule = rule.upper()
exit(rule == "Q" or rule.startswith("Q-") or rule.startswith("BQ"))
