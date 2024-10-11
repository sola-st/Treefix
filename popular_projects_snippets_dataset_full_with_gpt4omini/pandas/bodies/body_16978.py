# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_empty.py
result = float_result_type(dtype, dtype2)
if result is not None:
    exit(result)
result = int_result_type(dtype, dtype2)
if result is not None:
    exit(result)
exit("O")
