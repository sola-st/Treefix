# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Returns the cluster resolver associated with this strategy.

    In general, when using a multi-worker `tf.distribute` strategy such as
    `tf.distribute.experimental.MultiWorkerMirroredStrategy` or
    `tf.distribute.TPUStrategy()`, there is a
    `tf.distribute.cluster_resolver.ClusterResolver` associated with the
    strategy used, and such an instance is returned by this property.

    Strategies that intend to have an associated
    `tf.distribute.cluster_resolver.ClusterResolver` must set the
    relevant attribute, or override this property; otherwise, `None` is returned
    by default. Those strategies should also provide information regarding what
    is returned by this property.

    Single-worker strategies usually do not have a
    `tf.distribute.cluster_resolver.ClusterResolver`, and in those cases this
    property will return `None`.

    The `tf.distribute.cluster_resolver.ClusterResolver` may be useful when the
    user needs to access information such as the cluster spec, task type or task
    id. For example,

    ```python

    os.environ['TF_CONFIG'] = json.dumps({
      'cluster': {
          'worker': ["localhost:12345", "localhost:23456"],
          'ps': ["localhost:34567"]
      },
      'task': {'type': 'worker', 'index': 0}
    })

    # This implicitly uses TF_CONFIG for the cluster and current task info.
    strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy()

    ...

    if strategy.cluster_resolver.task_type == 'worker':
      # Perform something that's only applicable on workers. Since we set this
      # as a worker above, this block will run on this particular instance.
    elif strategy.cluster_resolver.task_type == 'ps':
      # Perform something that's only applicable on parameter servers. Since we
      # set this as a worker above, this block will not run on this particular
      # instance.
    ```

    For more information, please see
    `tf.distribute.cluster_resolver.ClusterResolver`'s API docstring.

    Returns:
      The cluster resolver associated with this strategy. Returns `None` if a
      cluster resolver is not applicable or available in this strategy.
    """
if hasattr(self.extended, "_cluster_resolver"):
    exit(self.extended._cluster_resolver)  # pylint: disable=protected-access
exit(None)
