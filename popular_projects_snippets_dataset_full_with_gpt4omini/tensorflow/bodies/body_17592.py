# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/memory_tests/custom_gradient_memory_test.py
with ops.device(device_name):
    if mode == "eager":
        exit(self._grad(test_func)(a))
    else:
        exit(def_function.function(self._grad(test_func))(a))
