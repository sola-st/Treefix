# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# mixed casting
casted = mixed_float_frame.reindex(columns=["A", "B"]).astype("float32")
_check_cast(casted, "float32")

casted = mixed_float_frame.reindex(columns=["A", "B"]).astype("float16")
_check_cast(casted, "float16")
