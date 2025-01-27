# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape.py
"""Notifies all tapes in the stack that a variable has been accessed.

  Args:
    variable: variable to be watched.
  """
strategy, context = (
    distribution_strategy_context.get_strategy_and_replica_context())
if context:
    variables = [strategy.extended.value_container(variable)]
else:
    variables = strategy.experimental_local_results(variable)
for var in variables:
    pywrap_tfe.TFE_Py_TapeVariableAccessed(var)
    pywrap_tfe.TFE_Py_VariableWatcherVariableAccessed(var)
