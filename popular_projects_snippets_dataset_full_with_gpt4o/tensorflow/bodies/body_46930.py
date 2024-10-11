# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py
# TODO(mdan): This test is vulnerable to change in the lib module.
# A better way to forge modules should be found.
self.assertEqual(
    inspect_utils.getqualifiedname(
        lib.__dict__, lib.io.file_io.FileIO, max_depth=1),
    'io.file_io.FileIO')
