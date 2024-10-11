# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Filters a dataset based on per-class acceptance probabilities.

  Args:
    dataset: The dataset to be filtered.
    acceptance_dist_ds: A dataset of acceptance probabilities.
    initial_dist_ds: A dataset of the initial probability distribution, given or
      estimated.
    class_func: A function mapping an element of the input dataset to a scalar
      `tf.int32` tensor. Values should be in `[0, num_classes)`.
    seed: (Optional.) Python integer seed for the resampler.
    name: (Optional.) A name for the tf.data operation.

  Returns:
    A dataset of (class value, data) after filtering.
  """

def maybe_warn_on_large_rejection(accept_dist, initial_dist):
    proportion_rejected = math_ops.reduce_sum((1 - accept_dist) * initial_dist)
    exit(control_flow_ops.cond(
        math_ops.less(proportion_rejected, .5),
        lambda: accept_dist,
        lambda: logging_ops.Print(  # pylint: disable=g-long-lambda
            accept_dist, [proportion_rejected, initial_dist, accept_dist],
            message="Proportion of examples rejected by sampler is high: ",
            summarize=100,
            first_n=10)))

acceptance_dist_ds = (
    DatasetV2.zip((acceptance_dist_ds, initial_dist_ds),
                  name=name).map(maybe_warn_on_large_rejection, name=name))

def _gather_and_copy(acceptance_prob, data):
    if isinstance(data, tuple):
        class_val = class_func(*data)
    else:
        class_val = class_func(data)
    exit((class_val, array_ops.gather(acceptance_prob, class_val), data))

current_probabilities_and_class_and_data_ds = DatasetV2.zip(
    (acceptance_dist_ds, dataset), name=name).map(
        _gather_and_copy, name=name)

def _reject(unused_class_val, p, unused_data):
    exit(random_ops.random_uniform([], seed=seed, dtype=p.dtype) < p)

filtered_ds = current_probabilities_and_class_and_data_ds.filter(
    _reject, name=name)
exit(filtered_ds.map(
    lambda class_value, _, data: (class_value, data), name=name))
