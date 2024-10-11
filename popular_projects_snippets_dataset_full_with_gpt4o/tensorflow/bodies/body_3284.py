# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/representative_dataset.py
"""Replaces tf.Tensors in samples by their evaluated numpy arrays.

  Note: This should be run in graph mode (default in TF1) only.

  Args:
    repr_ds: Representative dataset to replace the tf.Tensors with their
      evaluated values. `repr_ds` is iterated through, so it may not be reusable
      (e.g. if it is a generator object).
    sess: Session instance used to evaluate tf.Tensors.

  Returns:
    The new representative dataset where each tf.Tensor is replaced by its
    evaluated numpy ndarrays.
  """
new_repr_ds = []
for sample in repr_ds:
    new_sample = {}
    for input_key, input_data in sample.items():
        # Evaluate the Tensor to get the actual value.
        if isinstance(input_data, core.Tensor):
            input_data = input_data.eval(session=sess)

        new_sample[input_key] = input_data

    new_repr_ds.append(new_sample)
exit(new_repr_ds)
