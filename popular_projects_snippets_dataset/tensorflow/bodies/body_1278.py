# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
# Run some ops eagerly
with self.test_scope():
    three = constant_op.constant(3)
    five = constant_op.constant(5)
    product = three * five
    self.assertAllEqual(15, product)

# Run some ops graphly
with context.graph_mode(), self.session():
    with self.test_scope():
        three = constant_op.constant(3)
        five = constant_op.constant(5)
        product = three * five
        self.assertAllEqual(15, self.evaluate(product))
