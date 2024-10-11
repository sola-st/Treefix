# Extracted from ./data/repos/tensorflow/tensorflow/lite/schema/upgrade_schema_test.py
"""Given a data dictionary, test upgrading to current version.

    Args:
        data_old: TFLite model as a dictionary (arbitrary version).
        data_expected: TFLite model as a dictionary (upgraded).
    """
converter = upgrade_schema_lib.Converter()
with tempfile.NamedTemporaryFile(suffix=".json", mode="w+") as in_json, \
            tempfile.NamedTemporaryFile(
            suffix=".json", mode="w+") as out_json, \
            tempfile.NamedTemporaryFile(
            suffix=".bin", mode="w+b") as out_bin, \
            tempfile.NamedTemporaryFile(
            suffix=".tflite", mode="w+b") as out_tflite:
    JsonDumpAndFlush(data_old, in_json)
    # Test JSON output
    converter.Convert(in_json.name, out_json.name)
    # Test binary output
    # Convert to .tflite  and then to .bin and check if binary is equal
    converter.Convert(in_json.name, out_tflite.name)
    converter.Convert(out_tflite.name, out_bin.name)
    self.assertEqual(
        open(out_bin.name, "rb").read(),
        open(out_tflite.name, "rb").read())
    # Test that conversion actually produced successful new json.
    converted_schema = json.load(out_json)
    self.assertEqual(converted_schema, data_expected)
