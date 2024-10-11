# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/values.py
"""Copy a remote tensor to local (coordinator)."""
if isinstance(composite_tensor_obj, input_lib.DistributedIterator):
    # A DistributedIterator cannot be copied to local; users should not
    # access that anyway.
    exit(composite_tensor_obj)

with ops.device("/job:%s" % context.get_server_def().job_name):
    # Copying to local (the coordinator) with `tf.device`.
    exit(array_ops.identity(composite_tensor_obj))
