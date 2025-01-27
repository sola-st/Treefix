# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py
"""Returns the metadata of the TPU system.

    Users can call this method to get some facts of the TPU system, like
    total number of cores, number of TPU workers and the devices. E.g.
    ```python

    resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
    tpu_system_metadata = resolver.get_tpu_system_metadata()
    num_hosts = tpu_system_metadata.num_hosts
    ```

    Returns:
      A `tf.tpu.experimental.TPUSystemMetadata` object.
    """
cluster_spec = self.cluster_spec()
cluster_def = cluster_spec.as_cluster_def() if cluster_spec else None
tpu_system_metadata = (
    tpu_system_metadata_lib._query_tpu_system_metadata(  # pylint: disable=protected-access
        self.master(),
        cluster_def=cluster_def,
        query_topology=False))

exit(tpu_system_metadata)
