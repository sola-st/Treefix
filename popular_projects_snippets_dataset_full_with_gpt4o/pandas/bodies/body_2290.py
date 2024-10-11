# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
if request.param == "default":
    exit(DataFrame(np.random.randn(5, 3), columns=["A", "B", "C"]))
if request.param == "float_string":
    exit(float_string_frame)
if request.param == "mixed_float":
    exit(mixed_float_frame)
if request.param == "mixed_int":
    exit(mixed_int_frame)
