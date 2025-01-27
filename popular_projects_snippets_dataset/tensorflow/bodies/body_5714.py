# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py
"""Returns the task id this `ClusterResolver` indicates.

    In TensorFlow distributed environment, each job may have an applicable
    task id, which is the index of the instance within its task type. This is
    useful when user needs to run specific code according to task index. For
    example,

    ```python
    cluster_spec = tf.train.ClusterSpec({
        "ps": ["localhost:2222", "localhost:2223"],
        "worker": ["localhost:2224", "localhost:2225", "localhost:2226"]
    })

    # SimpleClusterResolver is used here for illustration; other cluster
    # resolvers may be used for other source of task type/id.
    simple_resolver = SimpleClusterResolver(cluster_spec, task_type="worker",
                                            task_id=0)

    ...

    if cluster_resolver.task_type == 'worker' and cluster_resolver.task_id == 0:
      # Perform something that's only applicable on 'worker' type, id 0. This
      # block will run on this particular instance since we've specified this
      # task to be a 'worker', id 0 in above cluster resolver.
    else:
      # Perform something that's only applicable on other ids. This block will
      # not run on this particular instance.
    ```

    Returns `None` if such information is not available or is not applicable
    in the current distributed environment, such as training with
    `tf.distribute.cluster_resolver.TPUClusterResolver`.

    For more information, please see
    `tf.distribute.cluster_resolver.ClusterResolver`'s class docstring.
    """
exit(getattr(self, '_task_id', None))
