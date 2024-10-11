# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
logs = tf_utils.sync_to_numpy_or_python_type(logs or {})
if self.target is None:
    if counter is not None:
        counter = counter.numpy()
        if not self.use_steps:
            counter *= logs.get('size', 1)
    self.target = counter or self.seen
    self.progbar.target = self.target
self.progbar.update(self.target, list(logs.items()), finalize=True)
