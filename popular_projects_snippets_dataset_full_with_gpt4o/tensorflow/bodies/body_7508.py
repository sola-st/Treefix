# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
"""Returns a `multiprocessing.Barrier` for `multi_process_runner.run`.

  `tf.__internal__.distribute.multi_process_runner.get_barrier()` returns
  a `multiprocessing.Barrier` object which can be used within `fn` of
  `tf.__internal__.distribute.multi_process_runner` to wait with
  `barrier.wait()` call until all other tasks have also reached the
  `barrier.wait()` call, before they can proceed individually.

  Note that all tasks (subprocesses) have to reach `barrier.wait()` call to
  proceed. Currently it is not supported to block on only a subset of tasks
  in the cluster.

  Example:
  ```python

  def fn():
    some_work_to_be_done_by_all_tasks()

    tf.__internal__.distribute.multi_process_runner.get_barrier().wait()

    # The barrier guarantees that at this point, all tasks have finished
    # `some_work_to_be_done_by_all_tasks()`
    some_other_work_to_be_done_by_all_tasks()

  result = tf.__internal__.distribute.multi_process_runner.run(
      fn=fn,
      cluster_spec=(
          tf.__internal__
          .distribute.multi_process_runner.create_cluster_spec(
              num_workers=2)))
  ```


  Returns:
    A `multiprocessing.Barrier` for `multi_process_runner.run`.
  """
if _barrier is None:
    raise ValueError(
        'barrier is not defined. It is likely because you are calling '
        'get_barrier() in the main process. get_barrier() can only be called '
        'in the subprocesses.'
    )
exit(_barrier)
