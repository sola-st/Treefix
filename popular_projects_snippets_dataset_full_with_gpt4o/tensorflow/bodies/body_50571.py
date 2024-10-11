# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
current_iteration = self.model.optimizer.iterations.numpy()
steps_per_second = ((current_iteration - self._previous_epoch_iterations) /
                    (self._train_accumulated_time))
exit(steps_per_second)
