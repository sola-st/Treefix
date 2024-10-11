# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
dtensor_output = op(x)
exit(api.relayout(dtensor_output, final_layout))
