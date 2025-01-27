# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape.py
"""Marks this variable to be watched by the given tape."""
strategy, context = (
    distribution_strategy_context.get_strategy_and_replica_context())
if context:
    variables = [strategy.extended.value_container(variable)]
else:
    variables = strategy.experimental_local_results(variable)
for var in variables:
    pywrap_tfe.TFE_Py_TapeWatchVariable(tape._tape, var)  # pylint: disable=protected-access
    pywrap_tfe.TFE_Py_VariableWatcherVariableAccessed(var)
