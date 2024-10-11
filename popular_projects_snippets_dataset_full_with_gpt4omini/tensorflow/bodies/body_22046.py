# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adagrad_test.py
with ops.Graph().as_default():
    for dtype in [dtypes.half, dtypes.float32, dtypes.float64]:
        with self.cached_session():
            var0 = variables.Variable([[1.0], [2.0]], dtype=dtype)
            var1 = variables.Variable([[3.0], [4.0]], dtype=dtype)
            grads0 = indexed_slices.IndexedSlices(
                constant_op.constant(
                    [0.1], shape=[1, 1], dtype=dtype),
                constant_op.constant([0]),
                constant_op.constant([2, 1]))
            grads1 = indexed_slices.IndexedSlices(
                constant_op.constant(
                    [0.01], shape=[1, 1], dtype=dtype),
                constant_op.constant([1]),
                constant_op.constant([2, 1]))
            ada_opt = adagrad.AdagradOptimizer(3.0, initial_accumulator_value=0.1)
            ada_update = ada_opt.apply_gradients(
                zip([grads0, grads1], [var0, var1]))
            self.evaluate(variables.global_variables_initializer())
            # Fetch params to validate initial values
            self.assertAllClose([[1.0], [2.0]], self.evaluate(var0))
            self.assertAllClose([[3.0], [4.0]], self.evaluate(var1))
            # Run 3 step of sgd
            for _ in range(3):
                ada_update.run()
            # Validate updated params
            self.assertAllCloseAccordingToType(
                np.array([[-1.6026098728179932], [2.0]]), self.evaluate(var0))
            self.assertAllCloseAccordingToType(
                np.array([[3.0], [3.715679168701172]]), self.evaluate(var1))
