# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
with writer.as_default():
    summary_ops_v2.scalar('my_metric', 0.5, step=10)
