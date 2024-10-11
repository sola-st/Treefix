# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
"""Starts processes, one for each task in `cluster_spec`.

    Note that this is best effort by the applicable multiprocessing library,
    and it may take up to seconds for a subprocess to be successfully started.
    """
with self._process_lock:
    if self._processes:
        raise ValueError('MultiProcessRunner already started.')
    if self._joined:
        raise ValueError('cannot start new processes after'
                         'MultiProcessRunner.join() is called')

    for task_type, addresses in self._cluster_spec.items():
        for task_id, _ in enumerate(addresses):
            self._start_subprocess_and_reading_thread(task_type, task_id)

    # TODO(rchao): Remove the need of using SIGALRM if possible. At this time,
    # without this the tests become very flaky.
if self._max_run_time is not None:

    def handler(signum, frame):
        del signum, frame
        self.terminate_all()

    signal.signal(signal.SIGALRM, handler)
    signal.alarm(self._max_run_time)
