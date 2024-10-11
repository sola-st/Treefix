# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
with self.cached_session():
    scalar = constant_op.constant(2.0)
    scalar1 = array_ops.placeholder(dtype=dtypes.float32)

    vector = [0.3, 0.4, 0.5]
    vector1 = array_ops.placeholder(dtype=dtypes.float32, shape=[None])
    vector2 = array_ops.placeholder(dtype=dtypes.float32, shape=[None])

    multidimensional = [[0.3, 0.4], [0.2, 0.6]]
    multidimensional1 = array_ops.placeholder(
        dtype=dtypes.float32, shape=[None, None])
    multidimensional2 = array_ops.placeholder(
        dtype=dtypes.float32, shape=[None, None])

    # Scalar
    self.assertTrue(
        du.same_dynamic_shape(scalar, scalar1).eval({
            scalar1: 2.0
        }))

    # Vector

    self.assertTrue(
        du.same_dynamic_shape(vector, vector1).eval({
            vector1: [2.0, 3.0, 4.0]
        }))
    self.assertTrue(
        du.same_dynamic_shape(vector1, vector2).eval({
            vector1: [2.0, 3.0, 4.0],
            vector2: [2.0, 3.5, 6.0]
        }))

    # Multidimensional
    self.assertTrue(
        du.same_dynamic_shape(
            multidimensional, multidimensional1).eval({
                multidimensional1: [[2.0, 3.0], [3.0, 4.0]]
            }))
    self.assertTrue(
        du.same_dynamic_shape(
            multidimensional1, multidimensional2).eval({
                multidimensional1: [[2.0, 3.0], [3.0, 4.0]],
                multidimensional2: [[1.0, 3.5], [6.3, 2.3]]
            }))

    # Scalar, X
    self.assertFalse(
        du.same_dynamic_shape(scalar, vector1).eval({
            vector1: [2.0, 3.0, 4.0]
        }))
    self.assertFalse(
        du.same_dynamic_shape(scalar1, vector1).eval({
            scalar1: 2.0,
            vector1: [2.0, 3.0, 4.0]
        }))
    self.assertFalse(
        du.same_dynamic_shape(scalar, multidimensional1).eval({
            multidimensional1: [[2.0, 3.0], [3.0, 4.0]]
        }))
    self.assertFalse(
        du.same_dynamic_shape(scalar1, multidimensional1).eval(
            {
                scalar1: 2.0,
                multidimensional1: [[2.0, 3.0], [3.0, 4.0]]
            }))

    # Vector, X
    self.assertFalse(
        du.same_dynamic_shape(vector, vector1).eval({
            vector1: [2.0, 3.0]
        }))
    self.assertFalse(
        du.same_dynamic_shape(vector1, vector2).eval({
            vector1: [2.0, 3.0, 4.0],
            vector2: [6.0]
        }))
    self.assertFalse(
        du.same_dynamic_shape(vector, multidimensional1).eval({
            multidimensional1: [[2.0, 3.0], [3.0, 4.0]]
        }))
    self.assertFalse(
        du.same_dynamic_shape(vector1, multidimensional1).eval(
            {
                vector1: [2.0, 3.0, 4.0],
                multidimensional1: [[2.0, 3.0], [3.0, 4.0]]
            }))

    # Multidimensional, X
    self.assertFalse(
        du.same_dynamic_shape(
            multidimensional, multidimensional1).eval({
                multidimensional1: [[1.0, 3.5, 5.0], [6.3, 2.3, 7.1]]
            }))
    self.assertFalse(
        du.same_dynamic_shape(
            multidimensional1, multidimensional2).eval({
                multidimensional1: [[2.0, 3.0], [3.0, 4.0]],
                multidimensional2: [[1.0, 3.5, 5.0], [6.3, 2.3, 7.1]]
            }))
