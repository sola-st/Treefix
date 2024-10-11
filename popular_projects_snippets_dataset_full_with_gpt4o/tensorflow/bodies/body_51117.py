# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
options = save_options.SaveOptions()
self.assertEqual(save_options.VariablePolicy.NONE,
                 options.experimental_variable_policy)
# VariablePolicy instances.
options = save_options.SaveOptions(experimental_variable_policy=save_options
                                   .VariablePolicy.SAVE_VARIABLE_DEVICES)
self.assertEqual(save_options.VariablePolicy.SAVE_VARIABLE_DEVICES,
                 options.experimental_variable_policy)
options = save_options.SaveOptions(
    experimental_variable_policy=save_options.VariablePolicy
    .EXPAND_DISTRIBUTED_VARIABLES)
self.assertEqual(save_options.VariablePolicy.EXPAND_DISTRIBUTED_VARIABLES,
                 options.experimental_variable_policy)
# String conversions.
options = save_options.SaveOptions(
    experimental_variable_policy="save_variable_devices")
self.assertEqual(save_options.VariablePolicy.SAVE_VARIABLE_DEVICES,
                 options.experimental_variable_policy)
options = save_options.SaveOptions(
    experimental_variable_policy="expand_distributed_variables")
self.assertEqual(save_options.VariablePolicy.EXPAND_DISTRIBUTED_VARIABLES,
                 options.experimental_variable_policy)
with self.assertRaisesRegex(ValueError, "invalid VariablePolicy value"):
    options = save_options.SaveOptions(
        experimental_variable_policy="not_a_valid_value")
