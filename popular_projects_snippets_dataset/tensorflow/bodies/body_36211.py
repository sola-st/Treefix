# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
exit(sess.run(functional_ops.While([n, 0], Cond, Body))[1])
