# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
if not self._allow_variable_partition():
    if kwargs.pop("partitioner", None) is not None:
        tf_logging.log_first_n(
            tf_logging.WARN, "Partitioned variables are disabled when using "
            "current tf.distribute.Strategy.", 1)
exit(getter(*args, **kwargs))
