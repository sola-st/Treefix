# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
inputs = [m, m]
# pylint: disable=protected-access
ctx_handle = context.context()._handle
# pylint: enable=protected-access
device = context.context().device_name
attrs = ("transpose_a", False, "transpose_b", transpose_b, "T",
         m.dtype.as_datatype_enum)

def func():
    pywrap_tfe.TFE_Py_Execute(ctx_handle, device, "MatMul", inputs, attrs, 1)

self._run(func, num_iters)
