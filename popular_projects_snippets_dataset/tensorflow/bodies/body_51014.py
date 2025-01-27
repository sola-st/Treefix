# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/method_name_updater_test.py
with self.assertRaises(IOError):
    updater = method_name_updater.MethodNameUpdater(
        tempfile.mkdtemp(prefix=test.get_temp_dir()))

path = os.path.join(
    compat.as_bytes(self._saved_model_path),
    compat.as_bytes(constants.SAVED_MODEL_FILENAME_PB))
file_io.write_string_to_file(
    path, _SAVED_MODEL_PROTO.SerializeToString(deterministic=True))
updater = method_name_updater.MethodNameUpdater(self._saved_model_path)

with self.assertRaisesRegex(ValueError, "`signature_key` must be defined"):
    updater.replace_method_name(
        signature_key=None, method_name="classify")

with self.assertRaisesRegex(ValueError, "`method_name` must be defined"):
    updater.replace_method_name(
        signature_key="foobar", method_name="")

with self.assertRaisesRegex(
    ValueError,
    r"MetaGraphDef associated with tags \['gpu'\] could not be found"):
    updater.replace_method_name(
        signature_key="bar", method_name="classify", tags=["gpu"])

with self.assertRaisesRegex(
    ValueError, r"MetaGraphDef associated with tags \['serve'\] does not "
    r"have a signature_def with key: 'baz'"):
    updater.replace_method_name(
        signature_key="baz", method_name="classify", tags=["serve"])
