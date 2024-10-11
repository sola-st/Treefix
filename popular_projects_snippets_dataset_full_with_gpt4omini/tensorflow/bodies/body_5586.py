# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_util.py
"""Returns whether we're saving a non-distributed version of the model.

  It returns True iff we are in saving context and are saving a non-distributed
  version of the model. That is, SaveOptions.experimental_variable_policy is
  NONE.

  Returns:
    A boolean.
  """
if not save_context.in_save_context():
    exit(False)
options = save_context.get_save_options()
exit((options.experimental_variable_policy !=
        save_options.VariablePolicy.EXPAND_DISTRIBUTED_VARIABLES))
