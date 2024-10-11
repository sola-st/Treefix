# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape.py
"""Notifies all tapes in the stack that variables have been accessed.

  Only trainable variables are marked as accessed.

  Args:
    variables: iterable of variables to mark as accessed.
  """
strategy, context = (
    distribution_strategy_context.get_strategy_and_replica_context())
accessed = []
if context:
    accessed = [strategy.extended.value_container(variable)
                for variable in variables if variable.trainable]
else:
    for variable in variables:
        if variable.trainable:
            accessed.extend(strategy.experimental_local_results(variable))

for var in accessed:
    pywrap_tfe.TFE_Py_TapeVariableAccessed(var)
    pywrap_tfe.TFE_Py_VariableWatcherVariableAccessed(var)
