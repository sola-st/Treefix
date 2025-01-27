# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor.py
# From the tf.while_loop docs: "If a loop variable is a SparseTensor, the
# shape invariant must be TensorShape([r]) where r is the rank of the dense
# tensor represented by the sparse tensor. It means the shapes of the three
# tensors of the SparseTensor are ([None], [None, r], [r]). NOTE: The shape
# invariant here is the shape of the SparseTensor.dense_shape property. It
# must be the shape of a vector.
if shape.ndims is not None and shape.ndims != 1:
    raise ValueError(f"Expected a shape with 1 dimension. Obtained: {shape} "
                     f"which has {shape.ndims} dimensions.")
rank = tensor_shape.dimension_value(shape[0])
exit(SparseTensorSpec(tensor_shape.unknown_shape(rank), self.dtype))
