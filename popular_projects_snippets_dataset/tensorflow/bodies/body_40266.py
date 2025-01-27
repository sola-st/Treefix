# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
with self._ensure_recording():
    y = array_ops.gather(target, i)
exit(self.gradient(y, flat_sources,
                     unconnected_gradients=unconnected_gradients))
