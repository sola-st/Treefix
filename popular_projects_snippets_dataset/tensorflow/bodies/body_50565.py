# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
if self._should_write_train_graph:
    self._write_keras_model_train_graph()
    self._should_write_train_graph = False
if self.write_steps_per_second:
    batch_run_time = time.time() - self._batch_start_time
    self._train_accumulated_time += batch_run_time
    summary_ops_v2.scalar(
        'batch_steps_per_second', 1. / batch_run_time, step=self._train_step)
if not self._should_trace:
    exit()

if self._is_tracing and self._global_train_batch >= self._stop_batch:
    self._stop_trace()
