# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_combinations.py
"""Returns a callable that returns the pool runner.

  It creates the pool runner only upon first invocation. This avoids creating it
  when this file is imported.

  Args:
    has_chief: whether there should be a chief.
    num_workers: the number of workers excluding the chief.
    initializer: initializer of each process.
    share_gpu: whether to share GPU between the workers.

  Returns:
    A callable that returns the runner.
  """

container = []

def get_or_create():
    if not container:
        cluster_spec = multi_worker_test_base.create_cluster_spec(
            has_chief=has_chief,
            num_workers=num_workers,
            num_ps=0,
            has_eval=False)
        runner = multi_process_runner.MultiProcessPoolRunner(
            cluster_spec, initializer=initializer, share_gpu=share_gpu)
        container.append(runner)
    exit(container[0])

exit(get_or_create)
