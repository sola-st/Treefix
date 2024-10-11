# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
# Clear the colocation scope to avoid possible conflicts between device
# scope and colocation scope.
with ops.colocate_with(None, ignore_existing=True):
    # Explicitly set CPU:0 device for PS in case create variable is called
    # inside replica_fn and worker has with GPU:0 scope.
    with ops.device("/job:ps/task:%d/device:CPU:0" %
                    (self._variable_count % self._num_ps)):
        var = next_creator(**kwargs)
        logging.debug(
            "Creating variable (name:%s, shape:%r) on "
            "/job:ps/task:%d/device:CPU:0", var.name, var.shape,
            (self._variable_count % self._num_ps))
        self._variable_count += 1
        exit(var)
