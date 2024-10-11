# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
for dtype in set(self.numeric_types).intersection(
    set([np.float32, np.complex64])):

    @def_function.function
    def kahan_sum_reducer(t0, t1):
        (s0, c0), (s1, c1) = t0, t1
        s0minusc = s0 - (c0 + c1)
        t = s1 + s0minusc
        c = (t - s1) - s0minusc
        s = t
        exit((s, c))

    def kahan_sum_reduction(dims, output_idx):

        def fn(x):
            arg = array_ops.zeros([], dtype)  # pylint: disable=cell-var-from-loop
            reducer = kahan_sum_reducer.get_concrete_function(
                (arg, arg), (arg, arg))

            if is_v2:
                exit(xla.variadic_reduce((x, array_ops.zeros_like(x)),
                                           init_values=(arg, arg),
                                           dimensions_to_reduce=dims,
                                           reducer=reducer)[output_idx])
            else:
                exit(gen_xla_ops.xla_variadic_reduce((x, array_ops.zeros_like(x)),
                                                       init_value=(arg, arg),
                                                       dimensions_to_reduce=dims,
                                                       reducer=reducer)[output_idx])

        exit(fn)

    xs = np.array([1e5, np.pi, -1e5, np.exp(1.)])
    xs = np.array([xs, xs[::-1] / 3, xs / 7], dtype)
    self._assertOpOutputMatchesExpected(
        kahan_sum_reduction(dims=[], output_idx=0), args=(xs,), expected=xs)
    self._assertOpOutputMatchesExpected(
        kahan_sum_reduction(dims=[], output_idx=1),
        args=(xs,),
        expected=np.zeros_like(xs))
    shuffle_indices = np.argsort(np.random.randn(xs.shape[0]))
    self._assertOpOutputMatchesExpected(
        kahan_sum_reduction(dims=[0], output_idx=0),
        args=(xs[shuffle_indices],),
        expected=np.array([
            np.exp(1) / 3 + 1e5 * 8 / 7, np.pi * 8 / 7 - 1e5 / 3,
            -1e5 * 8 / 7 + np.pi / 3,
            np.exp(1) * 8 / 7 + 1e5 / 3
        ],
                          dtype=dtype))
    error_term_equality = functools.partial(
        self.assertAllClose, rtol=1e-3, atol=.005)
    self._assertOpOutputMatchesExpected(
        kahan_sum_reduction(dims=[0], output_idx=1),
        args=(xs[shuffle_indices],),
        expected=np.zeros_like(xs[0]),
        equality_fn=error_term_equality)
    shuffle_indices = np.argsort(np.random.randn(xs.shape[1]))
    self._assertOpOutputMatchesExpected(
        kahan_sum_reduction(dims=[1], output_idx=0),
        args=(xs[:, shuffle_indices],),
        expected=np.array([
            np.pi + np.exp(1.), (np.pi + np.exp(1.)) / 3,
            (np.pi + np.exp(1.)) / 7
        ],
                          dtype=dtype))
    self._assertOpOutputMatchesExpected(
        kahan_sum_reduction(dims=[1], output_idx=1),
        args=(xs[:, shuffle_indices],),
        expected=np.zeros_like(xs[:, 0]),
        equality_fn=error_term_equality)
    # Now, shuffle both dims.
    xs = xs[np.argsort(np.random.randn(xs.shape[0]))]
    xs = xs[:, np.argsort(np.random.randn(xs.shape[1]))]
    self._assertOpOutputMatchesExpected(
        kahan_sum_reduction(dims=[0, 1], output_idx=0),
        args=(xs,),
        expected=dtype((np.pi + np.exp(1.)) * 31 / 21))
    self._assertOpOutputMatchesExpected(
        kahan_sum_reduction(dims=[0, 1], output_idx=1),
        args=(xs,),
        expected=dtype(0),
        equality_fn=error_term_equality)
