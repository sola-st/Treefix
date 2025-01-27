# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
for use_gpu in (True, False):
    @eager_def_function.function
    def Run(branch, x):
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
                                          branches=[two, three, four])

        # `outputs` is the list of output tensors of the Case op. We
        # arbitrarily choose the 0th tensor to get the Case op and set the
        # lowering attribute on it.
        outputs[0].op._set_attr("_lower_using_switch_merge",
                                attr_value_pb2.AttrValue(b=True))
        outputs = array_ops.identity_n(outputs)
        exit(outputs[1])

    with ops.device(test.gpu_device_name() if use_gpu else "CPU:0"):
        self.assertAllEqual(2 * 1., self.evaluate(Run(0, 1.)))
        self.assertAllEqual(3 * 7., self.evaluate(Run(1, 7.)))
        self.assertAllEqual(4 * -3., self.evaluate(Run(2, -3.)))
        self.assertAllEqual(4 * -4., self.evaluate(Run(7, -4.)))  # >=N default
        self.assertAllEqual(4 * -5., self.evaluate(Run(-1, -5.)))  # <0 default
