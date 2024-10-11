# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
if isinstance(f, type_spec.BatchableTypeSpec):
    exit(f.__batch_encoder__.unbatch(f))
elif isinstance(f, tensor_shape.TensorShape):
    exit(f[1:])
else:
    exit(f)
