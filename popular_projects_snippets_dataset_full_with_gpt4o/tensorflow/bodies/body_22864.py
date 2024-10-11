# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
"""Test to make sure that save method respects options kwarg."""

# Create a model and save it.
input_saved_model_dir = self.mkdtemp()
root = self._GetModelForV2()
save.save(root, input_saved_model_dir,
          {_SAVED_MODEL_SIGNATURE_KEY: root.run})

# Run TRT conversion.
converter = self._CreateConverterV2(input_saved_model_dir)
converter.convert()

# Patch save function with mock.
with mock.patch.object(trt_convert, "save") as mock_save:
    mock_save.save = mock.MagicMock()
    # Save converted model with options.
    output_saved_model_dir = self.mkdtemp()
    options = save_options.SaveOptions(save_debug_info=True)
    converter.save(output_saved_model_dir, options=options)

    # Assert that the saved_model.save function was called with the given
    # save_options by TrtGraphConverterV2.save method.
    mock_save.save.assert_called_once_with(
        mock.ANY, mock.ANY, mock.ANY, options=options)
