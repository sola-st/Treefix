# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/collection_test.py
x_const = constant_op.constant(ops.get_collection('x')[0])
y_const = constant_op.constant(ops.get_collection('y')[0])
z = math_ops.add(x_const, y_const)
ops.add_to_collection('z', 7)
exit(z)
