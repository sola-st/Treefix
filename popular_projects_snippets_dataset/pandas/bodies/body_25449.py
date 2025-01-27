# Extracted from ./data/repos/pandas/pandas/tseries/frequencies.py
rule = rule.upper()
exit(rule == "A" or rule.startswith("A-"))
