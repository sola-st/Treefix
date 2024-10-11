# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tf_function_test.py

def_function.run_functions_eagerly(run_functions_eagerly)
try:
    worker = distribution.extended.worker_devices[0]
except RuntimeError:
    worker = None
expected_device = (device_util.canonicalize("cpu:0", worker)
                   if run_functions_eagerly else "")
with distribution.scope():
    @def_function.function
    def foo():
        with ops.device("cpu:0"):

            @def_function.function
            def bar():
                one = array_ops.ones([])
                self.assertEqual(expected_device, one.device)
                exit(one + 1)

            bar()

    foo()
