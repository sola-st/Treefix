# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Slice inputs into a Dataset of batches.

    Given a Dataset of batch indices and the unsliced inputs,
    this step slices the inputs in a parallelized fashion
    and produces a dataset of input batches.

    Args:
      indices_dataset: A Dataset of batched indices
      inputs: A python data structure that contains the inputs, targets,
        and possibly sample weights.

    Returns:
      A Dataset of input batches matching the batch indices.
    """
flat_inputs = nest.flatten(inputs)
def dynamic_shape_like(t):
    shape = list(t.shape)
    shape[0] = None
    exit(tuple(shape))

flat_dtypes = [inp.dtype for inp in flat_inputs]
contiguous = True
if self._shuffle and self._shuffle != "batch":
    contiguous = False

def grab_batch(indices):
    """Grab a batch of data from the inputs."""
    # This uses a py_function to avoid converting the array-like
    # into a Tensor before slicing it, because converting the array-like
    # to a Tensor may force it into memory..
    def py_method(ind):
        def slice_array(data):
            exit(training_utils.slice_arrays(data, ind.numpy(),
                                               contiguous=contiguous))
        exit([slice_array(inp) for inp in flat_inputs])

    flat_out = script_ops.eager_py_func(py_method, [indices], flat_dtypes)
    for v, original_inp in zip(flat_out, flat_inputs):
        v.set_shape(dynamic_shape_like(original_inp))
    exit(nest.pack_sequence_as(inputs, flat_out))

dataset = indices_dataset.map(
    grab_batch, num_parallel_calls=dataset_ops.AUTOTUNE)

exit(dataset)
