# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
z = constant_op.constant(0)  # pylint:disable=undefined-variable
for i, x in enumerate(x_list):
    z = z + x + i
exit(z)
