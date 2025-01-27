# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
out = debugger_cli_common.get_tensorflow_version_lines()
self.assertEqual(2, len(out.lines))
self.assertEqual("TensorFlow version: %s" % pywrap_tf_session.__version__,
                 out.lines[0])
