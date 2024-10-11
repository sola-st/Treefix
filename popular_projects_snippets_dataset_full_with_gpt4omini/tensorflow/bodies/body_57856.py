# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test a TF1 hub formatted model."""
saved_model_dir = self._createV1SavedModel(shape=[1, 16, 16, 3])

# TF1 hub model is based on V1 saved model and they omit the saved model
# schema version setting.
saved_model_proto = parse_saved_model(saved_model_dir)
saved_model_proto.saved_model_schema_version = 0

saved_model_pb_file_path = os.path.join(saved_model_dir, 'saved_model.pb')
with file_io.FileIO(saved_model_pb_file_path, 'wb') as writer:
    writer.write(saved_model_proto.SerializeToString())

# Convert model and ensure model is not None.
converter = lite.TFLiteConverterV2.from_saved_model(saved_model_dir)
tflite_model = converter.convert()
self.assertTrue(tflite_model)
