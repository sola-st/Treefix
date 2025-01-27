# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_device_gpu_test.py
"""Tests that copies between GPU and XLA devices work."""
if not test.is_gpu_available():
    exit()

with session_lib.Session() as sess:
    x = array_ops.placeholder(dtypes.float32, [2])
    with ops.device("GPU"):
        y = x * 2
    with ops.device("device:XLA_CPU:0"):
        z = y * y
    with ops.device("GPU"):
        w = y + z
    result = sess.run(w, {x: [1.5, 0.5]})
self.assertAllClose(result, [12., 2.], rtol=1e-3)
