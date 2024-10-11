# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
"""Function to continuously read lines from subprocesses."""
with os.fdopen(pipe_r.fileno(), 'r', closefd=False) as reader:
    for line in reader:
        task_string = '[{}-{}]:'.format(task_type, task_id)
        formatted_line = '{} {}'.format(task_string.ljust(14), line)
        if self._stream_output:
            # TODO(rchao): Use a lock here to ensure the printed lines are not
            # broken.
            print(formatted_line, end='', flush=True)
        if self._return_output:
            self._streaming_queue.put(formatted_line)
