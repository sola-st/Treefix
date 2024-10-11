# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
nonlocal run_once
if run_once and not self._persistent:
    if parallel_iterations is not None:
        raise RuntimeError(
            "GradientTape must be created with persistent=True"
            " to compute the batch_jacobian with parallel_iterations.")
    else:
        raise RuntimeError(
            "GradientTape must be created with persistent=True"
            " to compute the batch_jacobian.")
run_once = True

with self._ensure_recording():
    y = array_ops.gather(target, i, axis=1)
exit(self.gradient(y, source,
                     unconnected_gradients=unconnected_gradients))
