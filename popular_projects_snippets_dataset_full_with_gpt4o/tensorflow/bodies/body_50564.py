# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
self._global_train_batch += 1
if self.write_steps_per_second:
    self._batch_start_time = time.time()
if not self._should_trace:
    exit()

if self._global_train_batch == self._start_batch:
    self._start_trace()
