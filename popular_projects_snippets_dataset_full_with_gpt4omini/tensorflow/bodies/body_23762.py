# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
if a == float_type and b == float_type:
    exit(float_type)
if a == float_type:
    a = next_largest_fp_type
if b == float_type:
    b = next_largest_fp_type
exit(np.promote_types(a, b))
