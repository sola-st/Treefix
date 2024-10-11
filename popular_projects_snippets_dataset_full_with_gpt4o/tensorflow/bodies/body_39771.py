# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
m = self._m_2
ctx_handle = context.context()._handle
attrs = ("T", self._m_2.dtype.as_datatype_enum)
inputs = [m]

def f():
    pywrap_tfe.TFE_Py_Execute(ctx_handle, None, "Identity", inputs, attrs, 1)

self._run(f, 30000)
