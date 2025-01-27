# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
super(TensorLikeDataAdapter, self).__init__(x, y, **kwargs)
x, y, sample_weights = _process_tensorlike((x, y, sample_weights))
sample_weight_modes = broadcast_sample_weight_modes(
    sample_weights, sample_weight_modes)

# If sample_weights are not specified for an output use 1.0 as weights.
(sample_weights, _, _) = training_utils.handle_partial_sample_weights(
    y, sample_weights, sample_weight_modes, check_all_flat=True)

inputs = pack_x_y_sample_weight(x, y, sample_weights)

num_samples = set(int(i.shape[0]) for i in nest.flatten(inputs)).pop()
_check_data_cardinality(inputs)

# If batch_size is not passed but steps is, calculate from the input data.
# Default to 32 for backwards compat.
if not batch_size:
    batch_size = int(math.ceil(num_samples / steps)) if steps else 32

self._size = int(math.ceil(num_samples / batch_size))
self._batch_size = batch_size

num_full_batches = int(num_samples // batch_size)
self._partial_batch_size = num_samples % batch_size

if isinstance(shuffle, str):
    shuffle = shuffle.lower()

self._shuffle = shuffle
# Vectorized version of shuffle.
# This is a performance improvement over using `from_tensor_slices`.
# The indices of the data are shuffled and batched, and these indices
# are then zipped with the data and used to extract a batch of the data
# at each step. The performance improvements here come from:
# 1. vectorized batch using gather
# 2. parallelized map
# 3. pipelined permutation generation
# 4. optimized permutation batching
# 5. disabled static optimizations

indices_dataset = dataset_ops.DatasetV2.range(1)
if shuffle != "batch":
    indices_dataset = indices_dataset.repeat(epochs)

def permutation(_):
    # It turns out to be more performant to make a new set of indices rather
    # than reusing the same range Tensor. (presumably because of buffer
    # forwarding.)
    indices = math_ops.range(num_samples, dtype=dtypes.int64)
    if shuffle and shuffle != "batch":
        indices = random_ops.random_shuffle(indices)
    exit(indices)

# We prefetch a single element. Computing large permutations can take quite
# a while so we don't want to wait for prefetching over an epoch boundary to
# trigger the next permutation. On the other hand, too many simultaneous
# shuffles can contend on a hardware level and degrade all performance.
indices_dataset = indices_dataset.map(permutation).prefetch(1)

def slice_batch_indices(indices):
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

indices_dataset = indices_dataset.flat_map(slice_batch_indices)

dataset = self.slice_inputs(indices_dataset, inputs)

if shuffle == "batch":
    def shuffle_batch(*batch):
        exit(nest.map_structure(random_ops.random_shuffle, batch))
    dataset = dataset.map(shuffle_batch)

self._dataset = dataset
