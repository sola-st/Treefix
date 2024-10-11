# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/multi_device_iterator_ops.py
# pylint: disable=protected-access
self._element_spec = per_device_dataset.element_spec
self._init_func = per_device_dataset._init_func
self._init_captured_args = self._init_func.captured_inputs

self._next_func = per_device_dataset._next_func
self._next_captured_args = per_device_dataset._next_captured_args
# The captured arguments to the next_func are string_handle, incarnation_id.
# We update the incarnation id to the new one.
self._next_captured_args[
    per_device_dataset._incarnation_id_index] = incarnation_id

self._finalize_func = per_device_dataset._finalize_func
self._finalize_captured_args = per_device_dataset._finalize_captured_args

variant_tensor = gen_dataset_ops.generator_dataset(
    self._init_captured_args,
    self._next_captured_args,
    self._finalize_captured_args,
    init_func=self._init_func,
    next_func=self._next_func,
    finalize_func=self._finalize_func,
    **self._flat_structure)
super(_ReincarnatedPerDeviceGenerator, self).__init__(variant_tensor)
