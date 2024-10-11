# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
self.it = it
self.lock = threading.Lock()

# After a generator throws an exception all subsequent next() calls raise a
# StopIteration Exception. This, however, presents an issue when mixing
# generators and threading because it means the order of retrieval need not
# match the order in which the generator was called. This can make it appear
# that a generator exited normally when in fact the terminating exception is
# just in a different thread. In order to provide thread safety, once
# self.it has thrown an exception we continue to throw the same exception.
self._exception = None
