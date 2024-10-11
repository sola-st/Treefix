# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/barrier_ops_test.py
try:
    sess.run([insert_0_ops[i], insert_1_ops[i]])
except errors_impl.CancelledError:
    pass
