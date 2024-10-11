# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops_test.py
handle = client.call(
    "read_var", output_specs=[tensor_spec.TensorSpec([], dtypes.int64)])
status_or_handle = handle._status_or
handle.get_value()
exit(status_or_handle)
