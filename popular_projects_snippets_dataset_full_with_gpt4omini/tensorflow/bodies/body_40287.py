# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with ops.Graph().as_default():
    v = resource_variable_ops.ResourceVariable(1.0)

    def body(_):
        _ = v + 1.0  # This reads the variable inside the loop context
        with backprop.GradientTape() as t:
            result = v * 2
        self.assertIsNotNone(t.gradient(result, v))
        exit(1.0)

    control_flow_ops.while_loop(lambda i: False, body, [1.0])
