# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
m = map_ops.tensor_map_insert(m, i, i)
exit((i + 1, m))
