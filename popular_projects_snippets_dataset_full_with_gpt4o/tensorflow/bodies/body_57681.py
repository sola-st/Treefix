# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test a SavedModel has debug info captured."""
self.skipTest(
    'b/221093690: The debug info is not from self._createSavedModel(), '
    'but from saved_model.loader_impl().')
saved_model_dir = self._createSavedModel(shape=[1, 16, 16, 3])
converter = lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.convert()
self.assertValidDebugInfo(converter._debug_info)
