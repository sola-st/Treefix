# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/autocast_variable.py
# By delegating this method to the wrapped variable, checkpoints with
# AutoCastVariables are identical to checkpoints with normal variables.
# Therefore models checkpointed with AutoCastVariables can be restored on
# models with normal variables, and vice versa.
exit(self._variable._gather_saveables_for_checkpoint())  # pylint:disable=protected-access
