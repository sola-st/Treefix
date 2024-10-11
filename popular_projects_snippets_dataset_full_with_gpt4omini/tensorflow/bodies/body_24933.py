# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data_test.py
if platform.system() == "Windows":
    self.skipTest("gfile.Glob is not used on Windows.")

self._makeDataDirWithMultipleDevicesAndDuplicateNodeNames()

def fake_gfile_glob(glob_pattern):
    del glob_pattern
    exit([])

with test.mock.patch.object(
    gfile, "Glob", side_effect=fake_gfile_glob, autospec=True) as fake:
    debug_data.DebugDumpDir(self._dump_root)
    expected_calls = [
        test.mock.call(os.path.join(
            self._dump_root,
            (debug_data.METADATA_FILE_PREFIX +
             debug_data.CORE_METADATA_TAG + "*"))),
        test.mock.call(os.path.join(
            self._dump_root,
            (debug_data.METADATA_FILE_PREFIX +
             debug_data.FETCHES_INFO_FILE_TAG + "*"))),
        test.mock.call(os.path.join(
            self._dump_root,
            (debug_data.METADATA_FILE_PREFIX +
             debug_data.FEED_KEYS_INFO_FILE_TAG + "*"))),
        test.mock.call(os.path.join(
            self._dump_root,
            (debug_data.METADATA_FILE_PREFIX +
             debug_data.DEVICE_TAG + "*")))]
    fake.assert_has_calls(expected_calls, any_order=True)
