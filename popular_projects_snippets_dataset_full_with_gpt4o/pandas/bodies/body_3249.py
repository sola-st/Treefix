# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# mixed casting
mn = mixed_type_frame._get_numeric_data().copy()
mn["little_float"] = np.array(12345.0, dtype="float16")
mn["big_float"] = np.array(123456789101112.0, dtype="float64")

casted = mn.astype("float64")
_check_cast(casted, "float64")

casted = mn.astype("int64")
_check_cast(casted, "int64")

casted = mn.reindex(columns=["little_float"]).astype("float16")
_check_cast(casted, "float16")

casted = mn.astype("float32")
_check_cast(casted, "float32")

casted = mn.astype("int32")
_check_cast(casted, "int32")

# to object
casted = mn.astype("O")
_check_cast(casted, "object")
