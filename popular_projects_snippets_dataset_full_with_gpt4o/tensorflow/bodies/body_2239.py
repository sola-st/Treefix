# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
for dtype in self.float_types:
    if dtype == dtypes.bfloat16.as_numpy_dtype:
        a = -1.01
        b = 4.1
    else:
        a = -1.001
        b = 4.01

    self._testBinary(
        lambda x, y: math_ops.approximate_equal(x, y, tolerance=0.0001),
        np.array([[[[-1, 2.00009999], [-3, b]]]], dtype=dtype),
        np.array([[[[a, 2], [-3.00009, 4]]]], dtype=dtype),
        expected=np.array([[[[False, True], [True, False]]]], dtype=dtype))

    self._testBinary(
        gen_math_ops.real_div,
        np.array([3, 3, -1.5, -8, 44], dtype=dtype),
        np.array([2, -2, 7, -4, 0], dtype=dtype),
        expected=np.array(
            [1.5, -1.5, -0.2142857, 2, float("inf")], dtype=dtype),
        rtol=1e-6,
        atol=1e-8)

    self._testBinary(
        math_ops.atan2,
        np.array([0, np.sqrt(2), 1, np.sqrt(2), 0], dtype),
        np.array([1, np.sqrt(2), 0, -np.sqrt(2), -1], dtype),
        expected=np.array([0, np.pi / 4, np.pi / 2, np.pi * 3 / 4, np.pi],
                          dtype=dtype))

    self._testBinary(
        gen_math_ops.reciprocal_grad,
        np.array([4, -3, -2, 1], dtype=dtype),
        np.array([5, -6, 7, -8], dtype=dtype),
        expected=np.array([-80, 54, -28, 8], dtype=dtype))

    self._testBinary(
        gen_math_ops.sigmoid_grad,
        np.array([4, 3, 2, 1], dtype=dtype),
        np.array([5, 6, 7, 8], dtype=dtype),
        expected=np.array([-60, -36, -14, 0], dtype=dtype))

    self._testBinary(
        gen_math_ops.rsqrt_grad,
        np.array([4, 3, 2, 1], dtype=dtype),
        np.array([5, 6, 7, 8], dtype=dtype),
        expected=np.array([-160, -81, -28, -4], dtype=dtype))

    self._testBinary(
        gen_math_ops.sqrt_grad,
        np.array([4, 3, 2, 1], dtype=dtype),
        np.array([5, 6, 7, 8], dtype=dtype),
        expected=np.array([0.625, 1, 1.75, 4], dtype=dtype))

    self._testBinary(
        gen_nn_ops.softplus_grad,
        np.array([4, 3, 2, 1], dtype=dtype),
        np.array([5, 6, 7, 8], dtype=dtype),
        expected=np.array([3.97322869, 2.99258232, 1.99817801, 0.99966466],
                          dtype=dtype),
        rtol=1e-4,
        atol=1e-8)

    self._testBinary(
        gen_nn_ops.softsign_grad,
        np.array([4, 3, 2, 1], dtype=dtype),
        np.array([5, 6, 7, 8], dtype=dtype),
        expected=np.array([0.11111111, 0.06122449, 0.03125, 0.01234568],
                          dtype=dtype),
        rtol=1e-6,
        atol=1e-8)

    self._testBinary(
        gen_math_ops.tanh_grad,
        np.array([4, 3, 2, 1], dtype=dtype),
        np.array([5, 6, 7, 8], dtype=dtype),
        expected=np.array([-75, -48, -21, 0], dtype=dtype))

    self._testBinary(
        gen_nn_ops.elu_grad,
        np.array([1, 2, 3, 4, 5, 6], dtype=dtype),
        np.array([-.6, -.4, -.2, 0, .2, .4], dtype=dtype),
        expected=np.array([0.4, 1.2, 2.4, 4, 5, 6], dtype=dtype))

    self._testBinary(
        gen_nn_ops.selu_grad,
        np.array([1, 2, 3, 4, 5, 6], dtype=dtype),
        np.array([-.6, -.4, -.2, .2, .4, .6], dtype=dtype),
        expected=np.array([
            1.158099340847, 2.7161986816948, 4.67429802254, 4.202803949422,
            5.2535049367774, 6.30420592413
        ],
                          dtype=dtype),
        rtol=1e-10,
        atol=1e-10)

    self._testBinary(
        gen_nn_ops.relu_grad,
        np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=dtype),
        np.array([0, 0, 0, 0, 0, 0.1, 0.3, 0.5, 0.7, 0.9], dtype=dtype),
        expected=np.array([0, 0, 0, 0, 0, 6, 7, 8, 9, 10], dtype=dtype))

    self._testBinary(
        gen_nn_ops.relu6_grad,
        np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], dtype=dtype),
        np.array([0, 0, 0, 0, 0, 0.1, 0.3, 0.5, 0.7, 0.9, 6.1, 10.0],
                 dtype=dtype),
        expected=np.array([0, 0, 0, 0, 0, 6, 7, 8, 9, 10, 0, 0], dtype=dtype))

    self._testBinary(
        gen_nn_ops.leaky_relu_grad,
        np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=dtype),
        np.array([0, 0, 0, 0, 0, 0.1, 0.3, 0.5, 0.7, 0.9], dtype=dtype),
        expected=np.array([0.2, 0.4, 0.6, 0.8, 1, 6, 7, 8, 9, 10],
                          dtype=dtype),
        rtol=1e-8,
        atol=1e-8)

    self._testBinary(
        gen_nn_ops.softmax_cross_entropy_with_logits,
        np.array([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=dtype),
        np.array([[0.1, 0.2, 0.3, 0.4], [0.4, 0.3, 0.2, 0.1]], dtype=dtype),
        expected=[
            np.array([1.44019, 2.44019], dtype=dtype),
            np.array([[-0.067941, -0.112856, -0.063117, 0.243914],
                      [-0.367941, -0.212856, 0.036883, 0.543914]],
                     dtype=dtype),
        ],
        equality_test=self.ListsAreClose,
        rtol=1e-4,
        atol=1e-8)

    # Check -inf logits doesn't create NaNs.
    self._testBinary(
        gen_nn_ops.sparse_softmax_cross_entropy_with_logits,
        np.array([[-np.inf, 0.]], dtype=dtype),
        np.array([1], dtype=np.int32),
        expected=[
            np.array([0.], dtype=dtype),
            np.array([[0., 0.]], dtype=dtype)
        ],
        equality_test=self.ListsAreClose,
        rtol=1e-4,
        atol=1e-8)

    # TODO(b/68813416): Fails with bfloat16.
    if dtype != dtypes.bfloat16.as_numpy_dtype:
        self._testBinary(
            gen_nn_ops.sparse_softmax_cross_entropy_with_logits,
            np.array([[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8],
                      [0.9, 1.0, 1.1, 1.2]],
                     dtype=dtype),
            np.array([2, 1, 7], dtype=np.int32),
            expected=[
                np.array([1.342536, 1.442536, np.nan], dtype=dtype),
                np.array([[0.213838, 0.236328, -0.738817, 0.288651],
                          [0.213838, -0.763672, 0.261183, 0.288651],
                          [np.nan, np.nan, np.nan, np.nan]],
                         dtype=dtype),
            ],
            equality_test=self.ListsAreClose,
            rtol=1e-5,
            atol=1e-8)

    # TF doesn't define these for bf16.
    if dtype != dtypes.bfloat16.as_numpy_dtype:
        self._testBinary(
            gen_math_ops.xdivy,
            np.array([0, 4, 3, 2, 1, 0], dtype=dtype),
            np.array([[0, 5, 6, 7, 8, float("NaN")]], dtype=dtype),
            expected=np.array([[0, 0.8, 0.5, 0.285714, 0.125, 0]], dtype=dtype),
            rtol=1e-6,
            atol=1e-6)

        self._testBinary(
            gen_math_ops.xlogy,
            np.array([0, 4, 3, 2, 1, 0], dtype=dtype),
            np.array([[0, 5, 6, 7, 8, float("NaN")]], dtype=dtype),
            expected=np.array([[0, 6.437752, 5.375278, 3.89182, 2.079442, 0]],
                              dtype=dtype),
            rtol=1e-4,
            atol=1e-6)

        self._testBinary(
            gen_math_ops.xlog1py,
            np.array([0, 4, 3, 2, 1, 0], dtype=dtype),
            np.array([[-1, 5, 6, 7, 8, float("NaN")]], dtype=dtype),
            expected=np.array([[0, 7.167038, 5.837730, 4.158883, 2.197225, 0]],
                              dtype=dtype),
            rtol=1e-4,
            atol=1e-6)
