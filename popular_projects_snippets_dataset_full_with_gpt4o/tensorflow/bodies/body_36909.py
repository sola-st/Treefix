# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session() as sess:
    v1 = variables.Variable([1.0, 42.0])
    c = array_ops.placeholder(dtypes.int32, shape=[])
    pred = math_ops.less(c, 2)
    fn1 = lambda: array_ops.identity(v1)
    fn2 = lambda: array_ops.gather(v1, [1, 1])
    r = control_flow_ops.cond(pred, fn1, fn2)
    # The following `grad` is a Tensor since it is the aggregation of an
    # IndexedSlice and a Tensor. It is an `IndexedSlices` with control flow
    # v2.
    grad = gradients_impl.gradients(r, [v1])[0]
    self.evaluate(variables.global_variables_initializer())

    if control_flow_util.ENABLE_CONTROL_FLOW_V2:
        self.assertIsInstance(grad, indexed_slices.IndexedSlices)

    grad_value = sess.run(grad, feed_dict={c: 1})
    self.assertAllEqual(gradient_checker_v2._to_numpy(grad_value), [1.0, 1.0])

    grad_value = sess.run(grad, feed_dict={c: 3})
    self.assertAllEqual(gradient_checker_v2._to_numpy(grad_value), [0.0, 2.0])
