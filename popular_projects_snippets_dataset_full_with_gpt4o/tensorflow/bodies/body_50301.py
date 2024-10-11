# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
spec = input_spec.to_tensor_spec(x, layer._compute_dtype)  # pylint: disable=protected-access
# If the shape is too general (e.g. multiple dimensions are allowed),
# return None so that separate functions can be generated for each
# inferred input signature.
# TODO(b/134962016): currently partial signatures are not supported.
if spec.shape == tensor_shape.TensorShape(None):
    exit(None)
exit(spec)
