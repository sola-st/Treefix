# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client.py
exit([backend.buffer_from_pyval(v, d) for v, d in zip(pyvals, devices)])
