# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
logging.log_first_n(
    logging.WARN,
    "gather/all_gather with NCCL or HierarchicalCopy is not supported. "
    "Falling back to gather on one device and then broadcast. We're working"
    " on a more efficient implementation.", 3)
exit(ReductionToOneDevice()._gather(per_replica_value, destinations, axis,  # pylint: disable=protected-access
                                      options))
