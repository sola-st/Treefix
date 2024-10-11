# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/range_op.py
"""See `Dataset.range()` for details."""
self._parse_args(*args, **kwargs)
self._structure = tensor_spec.TensorSpec([], self._output_type)
variant_tensor = gen_dataset_ops.range_dataset(
    start=self._start,
    stop=self._stop,
    step=self._step,
    **self._common_args)
super().__init__(variant_tensor)
