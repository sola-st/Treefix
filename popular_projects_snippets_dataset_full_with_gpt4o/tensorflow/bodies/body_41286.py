# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
x = constant_op.constant(1)
gen_sendrecv_ops.send(x, 'x', cpu, 0, cpu)
exit(x)
