# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_css.py
if relative_to is None:
    inherited = None
else:
    inherited = {"font-size": relative_to}
assert_resolves(f"font-size: {size}", {"font-size": resolved}, inherited=inherited)
