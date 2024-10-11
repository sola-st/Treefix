# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client.py
assert use_tfrt
exit(_xla.get_tfrt_cpu_client(asynchronous=True))
