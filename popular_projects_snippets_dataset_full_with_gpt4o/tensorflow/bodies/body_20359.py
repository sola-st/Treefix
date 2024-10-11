# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
x = x + 1.0
if x < 5:
    scalar_summary_v2.scalar("x", x, step=0)
    x = x * 2.0
exit(x + 1.0)
