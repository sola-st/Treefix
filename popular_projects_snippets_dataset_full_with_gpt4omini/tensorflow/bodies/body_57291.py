# Extracted from ./data/repos/tensorflow/tensorflow/lite/schema/upgrade_schema_test.py
converter = upgrade_schema_lib.Converter()
_, non_existent = tempfile.mkstemp(suffix=".json")  # safe to ignore fd
with self.assertRaisesRegex(IOError, "No such file or directory"):
    converter.Convert(non_existent, non_existent)
