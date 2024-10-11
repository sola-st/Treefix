# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
# Create a 1D array of strings
x = np.asarray(["", "", "a", "", "", "b"])
self._compare(x, None, keepdims=False, zero=np.str_(""))
self._compare(x, [], keepdims=False, zero=np.str_(""))
self._compare(x, [0], keepdims=False, zero=np.str_(""))
self._compare(x, None, keepdims=True, zero=np.str_(""))
self._compare(x, [], keepdims=True, zero=np.str_(""))
self._compare(x, [0], keepdims=True, zero=np.str_(""))
