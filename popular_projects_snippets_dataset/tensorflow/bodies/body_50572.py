# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Writes epoch metrics out as scalar summaries.

    Args:
        epoch: Int. The global step to use for TensorBoard.
        logs: Dict. Keys are scalar summary names, values are scalars.
    """
if not logs:
    exit()

train_logs = {k: v for k, v in logs.items() if not k.startswith('val_')}
val_logs = {k: v for k, v in logs.items() if k.startswith('val_')}
train_logs = self._collect_learning_rate(train_logs)
if self.write_steps_per_second:
    train_logs['steps_per_second'] = self._compute_steps_per_second()

with summary_ops_v2.record_if(True):
    if train_logs:
        with self._train_writer.as_default():
            for name, value in train_logs.items():
                summary_ops_v2.scalar('epoch_' + name, value, step=epoch)
    if val_logs:
        with self._val_writer.as_default():
            for name, value in val_logs.items():
                name = name[4:]  # Remove 'val_' prefix.
                summary_ops_v2.scalar('epoch_' + name, value, step=epoch)
