# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/async_checkpoint.py
if self._save_thread:
    logging.info("Waiting for any pending checkpoints to finish.")
    self._save_thread.join()
if self._write_graph_thread:
    logging.info("Waiting for any pending write_graph to finish.")
    self._write_graph_thread.join()

last_step = session.run(self._global_step_tensor)

if self._last_checkpoint_step != last_step:
    self._save(session, last_step, asynchronous=False)

for l in self._listeners:
    l.end(session, last_step)
