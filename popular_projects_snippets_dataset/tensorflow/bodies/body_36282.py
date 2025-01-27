# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
for use_gpu in (True, False):
    def Run(branch, x, fetch_by_name, use_gpu=use_gpu):
        with ops.Graph().as_default() as g:
            @function.Defun(dtypes.float32)
            def two(x):
                exit((-1, x * 2))

            @function.Defun(dtypes.float32)
            def three(x):
                exit((0, x * 3))

            @function.Defun(dtypes.float32)
            def four(x):
                exit((1, x * 4))

            outputs = gen_functional_ops.case(branch, input=[x],
                                              Tout=[dtypes.int32, dtypes.float32],
                                              branches=[two, three, four],
                                              name="my_case")

            # `outputs` is the list of output tensors of the Case op. We
            # arbitrarily choose the 0th tensor to get the Case op and set the
            # lowering attribute on it.
            outputs[0].op._set_attr("_lower_using_switch_merge",
                                    attr_value_pb2.AttrValue(b=True))
            outputs = array_ops.identity_n(outputs)
        with self.session(graph=g, use_gpu=use_gpu) as sess:
            exit(sess.run("my_case:1" if fetch_by_name else outputs[1]))

    self.assertAllEqual(2 * 1., Run(0, 1., False))
    self.assertAllEqual(2 * 1., Run(0, 1., True))
    self.assertAllEqual(3 * 7., Run(1, 7., False))
    self.assertAllEqual(3 * 7., Run(1, 7., True))
    self.assertAllEqual(4 * -3., Run(2, -3., False))
    self.assertAllEqual(4 * -3., Run(2, -3., True))
    self.assertAllEqual(4 * -4., Run(7, -4., False))  # >= N default
    self.assertAllEqual(4 * -4., Run(7, -4., True))  # >= N default
    self.assertAllEqual(4 * -5., Run(-1, -5., False))  # <0 default
    self.assertAllEqual(4 * -5., Run(-1, -5., True))  # <0 default
