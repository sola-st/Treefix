# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
with ops.control_dependencies(None):
    exit(array_ops.guarantee_const(
        getter(name, *args, **kwargs), name=name + "/GuaranteeConst"))
