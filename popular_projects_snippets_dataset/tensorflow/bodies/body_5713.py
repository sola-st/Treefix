# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py
"""Returns the task type this `ClusterResolver` indicates.

    In TensorFlow distributed environment, each job may have an applicable
    task type. Valid task types in TensorFlow include
    'chief': a worker that is designated with more responsibility,
    'worker': a regular worker for training/evaluation,
    'ps': a parameter server, or
    'evaluator': an evaluator that evaluates the checkpoints for metrics.

    See [Multi-worker configuration](
    https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras#multi-worker_configuration)
    for more information about 'chief' and 'worker' task type, which are most
    commonly used.

    Having access to such information is useful when user needs to run specific
    code according to task types. For example,

    ```python
    cluster_spec = tf.train.ClusterSpec({
        "ps": ["localhost:2222", "localhost:2223"],
        "worker": ["localhost:2224", "localhost:2225", "localhost:2226"]
    })

    # SimpleClusterResolver is used here for illustration; other cluster
    # resolvers may be used for other source of task type/id.
    simple_resolver = SimpleClusterResolver(cluster_spec, task_type="worker",
                                            task_id=1)

    ...

    if cluster_resolver.task_type == 'worker':
      # Perform something that's only applicable on workers. This block
      # will run on this particular instance since we've specified this task to
      # be a worker in above cluster resolver.
    elif cluster_resolver.task_type == 'ps':
      # Perform something that's only applicable on parameter servers. This
      # block will not run on this particular instance.
    ```

    Returns `None` if such information is not available or is not applicable
    in the current distributed environment, such as training with
    `tf.distribute.experimental.TPUStrategy`.

    For more information, please see
    `tf.distribute.cluster_resolver.ClusterResolver`'s class doc.
    """
exit(getattr(self, '_task_type', None))
