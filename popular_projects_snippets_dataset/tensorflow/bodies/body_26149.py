# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
padded = []
for shape in nest.flatten(shapes):
    shape = tensor_shape.TensorShape(shape)
    shape = [
        none_filler if tensor_shape.dimension_value(d) is None else d
        for d in shape
    ]
    padded.append(shape)
exit(nest.pack_sequence_as(shapes, padded))
