# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Convert a Tensor of indices into a dataset of batched indices.

      This step can be accomplished in several ways. The most natural is to
      slice the Tensor in a Dataset map. (With a condition on the upper index to
      handle the partial batch.) However it turns out that coercing the Tensor
      into a shape which is divisible by the batch size (and handling the last
      partial batch separately) allows for a much more favorable memory access
      pattern and improved performance.

      Args:
        indices: Tensor which determines the data order for an entire epoch.

      Returns:
        A Dataset of batched indices.
      """
num_in_full_batch = num_full_batches * batch_size
first_k_indices = array_ops.slice(indices, [0], [num_in_full_batch])
first_k_indices = array_ops.reshape(
    first_k_indices, [num_full_batches, batch_size])

flat_dataset = dataset_ops.DatasetV2.from_tensor_slices(first_k_indices)
if self._partial_batch_size:
    index_remainder = dataset_ops.DatasetV2.from_tensors(array_ops.slice(
        indices, [num_in_full_batch], [self._partial_batch_size]))
    flat_dataset = flat_dataset.concatenate(index_remainder)

if shuffle == "batch":
    # 1024 is a magic constant that has not been properly evaluated
    flat_dataset = flat_dataset.shuffle(1024).repeat(epochs)
exit(flat_dataset)
