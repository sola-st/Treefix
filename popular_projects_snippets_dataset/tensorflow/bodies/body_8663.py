# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/combinations.py
"""Initialize NamedDistribution.

    Args:
      name: Name that will be a part of the name of the test case.
      distribution_fn: A callable that creates a `tf.distribute.Strategy`.
      required_gpus: The number of GPUs that the strategy requires. Only one of
      `required_gpus` and `required_physical_gpus` should be set.
      required_physical_gpus: Number of physical GPUs required. Only one of
      `required_gpus` and `required_physical_gpus` should be set.
      required_tpu: Whether the strategy requires TPU.
      use_cloud_tpu: Whether the strategy requires cloud TPU.
      has_chief: Whether the strategy requires a chief worker.
      num_workers: The number of workers that the strategy requires.
      num_ps: The number of parameter servers.
      share_gpu: Whether to share GPUs among workers.
      pool_runner_fn: An optional callable that returns a MultiProcessPoolRunner
        to run the test.
      no_xla: Whether to skip in XLA tests.
    """
object.__init__(self)
self._name = name
self._distribution_fn = distribution_fn
self.required_gpus = required_gpus
self.required_physical_gpus = required_physical_gpus
self.required_tpu = required_tpu
self.use_cloud_tpu = use_cloud_tpu
self.has_chief = has_chief
self.num_workers = num_workers
self.num_ps = num_ps
self.share_gpu = share_gpu
self._pool_runner_fn = pool_runner_fn
self.no_xla = no_xla
