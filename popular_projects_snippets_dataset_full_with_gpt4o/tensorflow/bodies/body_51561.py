# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
handle = get_handle()
resource_variable_ops.destroy_resource_op(
    handle, ignore_lookup_error=True
)
