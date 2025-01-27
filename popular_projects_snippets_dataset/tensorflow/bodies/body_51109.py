# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
self.assertEqual(save_options.VariablePolicy.NONE,
                 save_options.VariablePolicy.from_obj(None))
self.assertEqual(
    save_options.VariablePolicy.SAVE_VARIABLE_DEVICES,
    save_options.VariablePolicy.from_obj(
        save_options.VariablePolicy.SAVE_VARIABLE_DEVICES))
self.assertEqual(
    save_options.VariablePolicy.EXPAND_DISTRIBUTED_VARIABLES,
    save_options.VariablePolicy.from_obj(
        save_options.VariablePolicy.EXPAND_DISTRIBUTED_VARIABLES))
self.assertEqual(
    save_options.VariablePolicy.SAVE_VARIABLE_DEVICES,
    save_options.VariablePolicy.from_obj("save_variable_devices"))
self.assertEqual(
    save_options.VariablePolicy.SAVE_VARIABLE_DEVICES,
    save_options.VariablePolicy.from_obj("SaVe_VaRiAbLe_DeViCeS"))
self.assertEqual(
    save_options.VariablePolicy.EXPAND_DISTRIBUTED_VARIABLES,
    save_options.VariablePolicy.from_obj("expand_distributed_variables"))
self.assertEqual(
    save_options.VariablePolicy.EXPAND_DISTRIBUTED_VARIABLES,
    save_options.VariablePolicy.from_obj("eXpAnD_dIsTrIbUtEd_VaRiAbLeS"))
for invalid in ["not_a_valid_value", 2.0, []]:
    with self.assertRaisesRegex(ValueError, "invalid VariablePolicy value"):
        save_options.VariablePolicy.from_obj(invalid)
