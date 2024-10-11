# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py
closed_over_list.append(1)
local_var = 1
exit(called_fn() + local_var + closed_over_primitive)
