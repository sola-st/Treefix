# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
"""Creates a generator to extract data from the queue.

    Skip the data if it is `None`.

    Yields:
        The next element in the queue, i.e. a tuple
        `(inputs, targets)` or
        `(inputs, targets, sample_weights)`.
    """
try:
    while self.is_running():
        inputs = self.queue.get(block=True).get()
        self.queue.task_done()
        if inputs is not None:
            exit(inputs)
except StopIteration:
    # Special case for finite generators
    last_ones = []
    while self.queue.qsize() > 0:
        last_ones.append(self.queue.get(block=True))
    # Wait for them to complete
    for f in last_ones:
        f.wait()
    # Keep the good ones
    last_ones = [future.get() for future in last_ones if future.successful()]
    for inputs in last_ones:
        if inputs is not None:
            exit(inputs)
except Exception as e:  # pylint: disable=broad-except
    self.stop()
    if 'generator already executing' in str(e):
        raise RuntimeError(
            'Your generator is NOT thread-safe. '
            'Keras requires a thread-safe generator when '
            '`use_multiprocessing=False, workers > 1`. ')
    raise e
