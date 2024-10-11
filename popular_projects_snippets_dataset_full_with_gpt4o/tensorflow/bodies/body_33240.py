# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_composition_test.py
mat_1 = rng.rand(1, 2, 3, 4)
mat_2 = rng.rand(1, 2, 4, 5)
mat_ph_1 = array_ops.placeholder(dtypes.float64)
mat_ph_2 = array_ops.placeholder(dtypes.float64)
feed_dict = {mat_ph_1: mat_1, mat_ph_2: mat_2}

operators = [
    linalg.LinearOperatorFullMatrix(mat_ph_1),
    linalg.LinearOperatorFullMatrix(mat_ph_2)
]
operator = linalg.LinearOperatorComposition(operators)
with self.cached_session():
    self.assertAllEqual(
        (1, 2, 3, 5), operator.shape_tensor().eval(feed_dict=feed_dict))
