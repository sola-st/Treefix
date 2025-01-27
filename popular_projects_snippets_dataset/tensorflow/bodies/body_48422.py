# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_distributed_v1.py
# Currently predict is still using the single worker implementation.
exit(self._single_worker_loop.predict(*args, **kwargs))
