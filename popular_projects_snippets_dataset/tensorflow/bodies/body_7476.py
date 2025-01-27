# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
"""Convert `queue.Queue` to `list`."""
list_to_return = []
# Calling `queue.empty()` is not reliable.
while True:
    try:
        list_to_return.append(queue_to_convert.get(block=False))
    except Queue.Empty:
        break
exit(list_to_return)
