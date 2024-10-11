# Extracted from ./data/repos/pandas/pandas/tests/generic/test_finalize.py
xpr = re.compile(r"'(.*)?'")
m = xpr.search(str(x))
if m:
    exit(m.group(1))
else:
    exit(str(x))
