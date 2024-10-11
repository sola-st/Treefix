# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tf_function_test.py
with ops.device("cpu:0"):

    @def_function.function
    def bar():
        one = array_ops.ones([])
        self.assertEqual(expected_device, one.device)
        exit(one + 1)

    bar()
