# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/ignore_errors_op.py
"""See `Dataset.ignore_errors` for details."""
self._input_dataset = input_dataset
self._name = name
variant_tensor = (
    gen_experimental_dataset_ops.ignore_errors_dataset(
        self._input_dataset._variant_tensor,  # pylint: disable=protected-access
        log_warning=log_warning,
        **self._flat_structure))
super().__init__(input_dataset, variant_tensor)
