# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
if isinstance(f, type_spec.BatchableTypeSpec):
    exit(f.__batch_encoder__.batch(f, batch_size))
elif isinstance(f, tensor_shape.TensorShape):
    exit([batch_size] + f)
else:
    exit(f)
