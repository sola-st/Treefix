# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
"""A function that regularly checks messages from parent process."""
# TODO(rchao): Remove this once parent uses SIGKILL to terminate subprocess.
while True:
    try:
        message = self._resources.parent_to_sub_queue.get(block=False)

        # Currently the only possible message is termination.
        if not message.startswith('terminate'):
            raise ValueError('Unrecognized message: {}'.format(message))

        if message == 'terminate {} {}'.format(task_type, task_id):
            break
        else:
            # If the message is not targeting this process, put it back to the
            # queue.
            self._resources.parent_to_sub_queue.put(message)
            time.sleep(1)
    except Queue.Empty:
        time.sleep(0.1)
self._resources.process_status_queue.put(
    _ProcessStatusInfo(
        task_type=task_type,
        task_id=task_id,
        is_successful=True,
        exc_info=None,
        return_value=None))
# `os._exit(1)` is used to more reliably terminate a subprocess.
os._exit(1)  # pylint: disable=protected-access
