# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Test a model with 1.X ReferenceVariables."""
input_data = {"start": constant_op.constant(1., shape=[1, 1])}

saved = self._singleMetaGraphSavedModel()
imported = load(saved)
fn = imported.signatures["serving_default"]

output_func = convert_to_constants.convert_variables_to_constants_v2(fn)
root = autotrackable.AutoTrackable()
self._testConvertedFunction(root, fn, output_func, input_data)
