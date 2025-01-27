# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
# Keeps track of epoch for profiling.
if self.write_steps_per_second:
    self._previous_epoch_iterations = self.model.optimizer.iterations.numpy()
    self._train_accumulated_time = 0
