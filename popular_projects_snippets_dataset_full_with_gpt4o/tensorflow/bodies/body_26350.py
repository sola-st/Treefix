# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_autograph.py
"""Registers the autograph specific overrides for dataset_ops."""
control_flow.for_loop_registry.register(
    dataset_ops.DatasetV2, _tf_ag_dataset_for_stmt
)
py_builtins.abs_registry.register(dataset_ops.DatasetV2, _tf_ag_dataset_abs)
py_builtins.len_registry.register(dataset_ops.DatasetV2, _tf_ag_dataset_len)
py_builtins.enumerate_registry.register(
    dataset_ops.DatasetV2, _tf_ag_dataset_enumerate
)
py_builtins.zip_registry.register(dataset_ops.DatasetV2, _tf_ag_dataset_zip)
py_builtins.map_registry.register(dataset_ops.DatasetV2, _tf_ag_dataset_map)
py_builtins.filter_registry.register(
    dataset_ops.DatasetV2, _tf_ag_dataset_filter
)
py_builtins.any_registry.register(dataset_ops.DatasetV2, _tf_ag_dataset_any)
py_builtins.all_registry.register(dataset_ops.DatasetV2, _tf_ag_dataset_all)
