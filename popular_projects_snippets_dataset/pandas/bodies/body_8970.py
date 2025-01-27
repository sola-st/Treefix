# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_reductions.py
msg = f"attempt to get {method} of an empty sequence"
with pytest.raises(ValueError, match=msg):
    arr.argmax() if method == "argmax" else arr.argmin()
