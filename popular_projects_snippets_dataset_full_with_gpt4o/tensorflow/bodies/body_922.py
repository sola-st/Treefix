# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/clustering_test.py
val1 = np.array([4, 3, 2, 1], dtype=np.float32)
val2 = np.array([5, 6, 7, 8], dtype=np.float32)
expected = val1 + val2
with self.session():
    with self.test_scope():
        input1 = constant_op.constant(val1, name="const1")
        input2 = constant_op.constant(val2, name="const2")
        output = math_ops.add(input1, input2)
    result = self.evaluate(output)
self.assertAllClose(result, expected, rtol=1e-3)
