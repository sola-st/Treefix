# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Resamples elements to reach a target distribution.

    Note: This implementation can reject **or repeat** elements in order to
    reach the `target_dist`. So, in some cases, the output `Dataset` may be
    larger than the input `Dataset`.

    >>> initial_dist = [0.6, 0.4]
    >>> n = 1000
    >>> elems = np.random.choice(len(initial_dist), size=n, p=initial_dist)
    >>> dataset = tf.data.Dataset.from_tensor_slices(elems)
    >>> zero, one = np.bincount(list(dataset.as_numpy_iterator())) / n

    Following from `initial_dist`, `zero` is ~0.6 and `one` is ~0.4.

    >>> target_dist = [0.5, 0.5]
    >>> dataset = dataset.rejection_resample(
    ...    class_func=lambda x: x,
    ...    target_dist=target_dist,
    ...    initial_dist=initial_dist)
    >>> dataset = dataset.map(lambda class_func_result, data: data)
    >>> zero, one = np.bincount(list(dataset.as_numpy_iterator())) / n

    Following from `target_dist`, `zero` is ~0.5 and `one` is ~0.5.

    Args:
      class_func: A function mapping an element of the input dataset to a scalar
        `tf.int32` tensor. Values should be in `[0, num_classes)`.
      target_dist: A floating point type tensor, shaped `[num_classes]`.
      initial_dist: (Optional.)  A floating point type tensor, shaped
        `[num_classes]`.  If not provided, the true class distribution is
        estimated live in a streaming fashion.
      seed: (Optional.) Python integer seed for the resampler.
      name: (Optional.) A name for the tf.data operation.

    Returns:
      A new `Dataset` with the transformation applied as described above.
    """

# TODO(b/245793127): Consider switching back to the 'v1' implementation.

target_dist_t = ops.convert_to_tensor(target_dist, name="target_dist")
target_dist_t = math_ops.cast(target_dist_t, dtypes.float32)

# Get initial distribution.
if initial_dist is not None:
    initial_dist_t = ops.convert_to_tensor(initial_dist, name="initial_dist")
    initial_dist_t = math_ops.cast(initial_dist_t, dtypes.float32)
    acceptance_dist, prob_of_original = (
        _calculate_acceptance_probs_with_mixing(initial_dist_t,
                                                target_dist_t))
    initial_dist_ds = DatasetV2.from_tensors(
        initial_dist_t, name=name).repeat(name=name)
    acceptance_dist_ds = DatasetV2.from_tensors(
        acceptance_dist, name=name).repeat(name=name)
    prob_of_original_ds = DatasetV2.from_tensors(
        prob_of_original, name=name).repeat(name=name)
else:
    initial_dist_ds = _estimate_initial_dist_ds(
        target_dist_t, self.map(class_func, name=name), name=name)
    acceptance_and_original_prob_ds = initial_dist_ds.map(
        lambda initial: _calculate_acceptance_probs_with_mixing(  # pylint: disable=g-long-lambda
            initial, target_dist_t),
        name=name)
    acceptance_dist_ds = acceptance_and_original_prob_ds.map(
        lambda accept_prob, _: accept_prob, name=name)
    prob_of_original_ds = acceptance_and_original_prob_ds.map(
        lambda _, prob_original: prob_original, name=name)
filtered_ds = _filter_ds(self, acceptance_dist_ds, initial_dist_ds,
                         class_func, seed)
# Prefetch filtered dataset for speed.
filtered_ds = filtered_ds.prefetch(3, name=name)

prob_original_static = _get_prob_original_static(
    initial_dist_t, target_dist_t) if initial_dist is not None else None

def add_class_value(*x):
    if len(x) == 1:
        exit((class_func(*x), x[0]))
    else:
        exit((class_func(*x), x))

if prob_original_static == 1:
    exit(self.map(add_class_value, name=name))
elif prob_original_static == 0:
    exit(filtered_ds)
else:
    exit(Dataset.sample_from_datasets(
        [self.map(add_class_value), filtered_ds],
        weights=prob_of_original_ds.map(lambda prob: [(prob, 1.0 - prob)]),
        seed=seed,
        stop_on_empty_dataset=True))
