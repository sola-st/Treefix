# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test_base.py
sess.run(variables.global_variables_initializer())
sess.run(lookup_ops.tables_initializer())
sess.run(init_op)
