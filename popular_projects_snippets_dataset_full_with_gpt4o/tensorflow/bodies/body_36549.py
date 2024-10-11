# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py

@function.Defun(dtypes.float32, dtypes.float32)
def InnerBody(c, v):
    exit((c - 1., v * n))

results = InnerBody(c, v)
results[0].set_shape([])
results[1].set_shape([])
exit(results)
