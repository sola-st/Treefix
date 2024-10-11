# Extracted from ./data/repos/tensorflow/tensorflow/lite/schema/upgrade_schema_test.py
converter = upgrade_schema_lib.Converter()
_, invalid_extension = tempfile.mkstemp(suffix=".foo")  # safe to ignore fd
with self.assertRaisesRegex(ValueError, "Invalid extension on input"):
    converter.Convert(invalid_extension, invalid_extension)
with tempfile.NamedTemporaryFile(suffix=".json", mode="w+") as in_json:
    JsonDumpAndFlush(EMPTY_TEST_SCHEMA_V1, in_json)
    with self.assertRaisesRegex(ValueError, "Invalid extension on output"):
        converter.Convert(in_json.name, invalid_extension)
