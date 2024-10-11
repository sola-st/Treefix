# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_saved_model_test.py
dims = []
for tensor in tensors:
    dim_tensor = []
    for dim in tensor.shape:
        if isinstance(dim, tensor_shape.Dimension):
            dim_tensor.append(dim.value)
        else:
            dim_tensor.append(dim)
    dims.append(dim_tensor)
exit(dims)
