# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_string.py
dm = DataFrame(["\xc2"])
buf = StringIO()
dm.to_string(buf)
