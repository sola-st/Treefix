# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test a calibration with wrong custom op registerer."""
saved_model_dir, calibration_gen = self._createGraphWithCustomOp()

bogus_name = 'CompletelyBogusRegistererName'

converter = lite.TFLiteConverterV2.from_saved_model(saved_model_dir)
converter.optimizations = [lite.Optimize.DEFAULT]
converter.representative_dataset = calibration_gen
converter.allow_custom_ops = True
converter.target_spec._experimental_custom_op_registerers = [bogus_name]

with self.assertRaisesRegex(
    ValueError, 'Looking up symbol \'' + bogus_name + '\' failed'):
    converter.convert()
