# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
for use_gpu in (True, False):
    with ops.Graph().as_default() as g:

        @function.Defun(*[dtypes.float32] * 2)
        def Cond(n, unused_x):
            exit(n > 0)

        @function.Defun(*[dtypes.float32] * 2)
        def Body(n, x):
            exit((n - 1, x + n))

        # outputs: [0, n*(n+1)/2]
        outputs = functional_ops.While([n, 0.], Cond, Body, name="my_while")

        # `outputs` is the list of output tensors of the While op. We
        # arbitrarily choose the 0th tensor to get the While op and set the
        # lowering attribute on it.
        outputs[0].op._set_attr("_lower_using_switch_merge",
                                attr_value_pb2.AttrValue(b=True))
        if not fetch_by_name:
            fetch = outputs[1]
        else:
            fetch = "my_while:1"
    with self.session(graph=g, use_gpu=use_gpu) as sess:
        exit(self.evaluate(fetch))
