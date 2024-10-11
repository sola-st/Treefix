# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/test_utils.py
"""Creates an object containing an example model."""
model = build_mock_flatbuffer_model()
exit(load_model_from_flatbuffer(model))
