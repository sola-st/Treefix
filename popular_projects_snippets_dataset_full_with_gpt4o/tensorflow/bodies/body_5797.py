# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py
"""Initializes TPU and returns a TPUClusterResolver.

    This API will connect to remote TPU cluster and initialize the TPU
    hardwares. Example usage:

    >>> resolver = tf.distribute.cluster_resolver.TPUClusterResolver.connect(
    ...     tpu='')

    It can be viewed as convenient wrapper of the following code:

    >>> resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
    >>> tf.config.experimental_connect_to_cluster(resolver)
    >>> tf.tpu.experimental.initialize_tpu_system(resolver)

    Args:
      tpu: A string corresponding to the TPU to use. It can be the TPU name or
        TPU worker gRPC address. If not set, it will try automatically resolve
        the TPU address on Cloud TPUs.
      zone: Zone where the TPUs are located. If omitted or empty, we will assume
        that the zone of the TPU is the same as the zone of the GCE VM, which we
        will try to discover from the GCE metadata service.
      project: Name of the GCP project containing Cloud TPUs. If omitted or
        empty, we will try to discover the project name of the GCE VM from the
        GCE metadata service.

    Returns:
      An instance of TPUClusterResolver object.

    Raises:
      NotFoundError: If no TPU devices found in eager mode.
    """
resolver = TPUClusterResolver(tpu, zone, project)
from tensorflow.python.eager import remote  # pylint: disable=g-import-not-at-top
remote.connect_to_cluster(resolver)
from tensorflow.python.tpu import tpu_strategy_util  # pylint: disable=g-import-not-at-top
tpu_strategy_util.initialize_tpu_system(resolver)
exit(resolver)
