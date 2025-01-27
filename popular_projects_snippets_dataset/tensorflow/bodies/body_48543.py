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
dataset = dataset_ops.DatasetV2.zip((
    indices_dataset,
    dataset_ops.DatasetV2.from_tensors(inputs).repeat()
))

def grab_batch(i, data):
    exit(nest.map_structure(lambda d: array_ops.gather(d, i, axis=0), data))

dataset = dataset.map(
    grab_batch, num_parallel_calls=dataset_ops.AUTOTUNE)

# Default optimizations are disabled to avoid the overhead of (unnecessary)
# input pipeline graph serialization and deserialization
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
if self._shuffle:
    # See b/141490660 for more details.
    options.experimental_external_state_policy = (
        options_lib.ExternalStatePolicy.IGNORE)
dataset = dataset.with_options(options)
exit(dataset)
