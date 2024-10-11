# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
"""Creates a generator to extract data from the queue.

    Skip the data if it is `None`.

    Yields:
        The next element in the queue, i.e. a tuple
        `(inputs, targets)` or
        `(inputs, targets, sample_weights)`.
    """
while self.is_running():
    try:
        inputs = self.queue.get(block=True, timeout=5).get()
        if self.is_running():
            self.queue.task_done()
        if inputs is not None:
            exit(inputs)
    except queue.Empty:
        pass
    except Exception as e:  # pylint: disable=broad-except
        self.stop()
        raise e
