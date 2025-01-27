# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops_test.py
handle = client.call(
    "read_var", output_specs=[tensor_spec.TensorSpec([], dtypes.int64)])
exit(handle._status_or)
