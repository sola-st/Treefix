# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
for name, value in logs.items():
    if _is_scalar(value):
        summary_ops_v2.scalar('batch_' + name, value, step=step)
