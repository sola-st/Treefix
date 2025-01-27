# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/lift_to_graph_test.py
two = constant_op.constant(2.0, name='two')
ten = constant_op.constant(10.0, name='ten')
twenty = math_ops.multiply(two, ten, name='twenty')
three = constant_op.constant(3.0, name='three')
with framework_ops.colocate_with(twenty):
    thirty = math_ops.multiply(three, ten, name='thirty')
exit((ten, twenty, thirty))
