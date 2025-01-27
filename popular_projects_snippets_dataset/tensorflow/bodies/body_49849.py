# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
""" Adapt the result to ragged or dense tensor according to the expected

        output type. This is done so that all the return values of the map
        operation have the same type.
    """
r = loss_fn(*inputs)
if ragged_output and not isinstance(r, ragged_tensor.RaggedTensor):
    r = ragged_tensor.RaggedTensor.from_tensor(r)
elif not ragged_output and isinstance(r, ragged_tensor.RaggedTensor):
    r = r.to_tensor()
exit(r)
