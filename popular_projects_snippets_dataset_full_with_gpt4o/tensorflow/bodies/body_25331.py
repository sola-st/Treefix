# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared_test.py
tf_error = errors.OpError(None, None, "Fake OpError", -1)
error_intro = cli_shared.get_error_intro(tf_error)
self.assertIn("Cannot determine the name of the op", error_intro.lines[3])
