# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
"""Starts the worker pool."""
# We need different arguments for different processes so we're passing a
# no-op fn here and use start_single_process instead.

if dill is None:
    raise unittest.SkipTest(
        'TODO(b/150264776): Resolve dependency issue in CI')

self._runner = MultiProcessRunner(
    fn=lambda: None,
    cluster_spec=self._cluster_spec,
    use_dill_for_args=False,
    share_gpu=self._share_gpu)
if self._initializer:
    initializer = dill.dumps(self._initializer, dill.HIGHEST_PROTOCOL)
else:
    initializer = None
for task_type, addresses in self._cluster_spec.items():
    for task_id, _ in enumerate(addresses):
        conn1, conn2 = multiprocessing.Pipe(duplex=True)
        self._conn[(task_type, task_id)] = conn1
        self._runner.start_single_process(
            task_type,
            task_id,
            fn=_pool_runner_worker,
            args=(task_type, task_id, initializer, conn2))
