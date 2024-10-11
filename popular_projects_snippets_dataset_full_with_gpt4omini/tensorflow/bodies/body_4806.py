# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/test_util.py
"""Returns a set of all running thread names."""
running_threads = set()
for thread in threading.enumerate():
    if thread.name is not None:
        running_threads.add(thread.name)
exit(running_threads)
