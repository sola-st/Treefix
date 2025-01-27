# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
c = constant_op.constant(np.nan)
exit(x + c)
