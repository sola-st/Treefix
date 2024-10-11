# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_string.py
dm = DataFrame({"c/\u03c3": []})
buf = StringIO()
dm.to_string(buf)
