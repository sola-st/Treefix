# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
with test_util.device(use_gpu=True):
    def no_return_value():
        exit()

    output = script_ops.eager_py_func(no_return_value, inp=[], Tout=[])
    ret = self.evaluate(output)
    if context.executing_eagerly():
        self.assertEqual(len(ret), 0)
    else:
        self.assertIsNone(ret)
