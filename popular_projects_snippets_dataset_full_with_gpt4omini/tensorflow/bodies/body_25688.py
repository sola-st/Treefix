# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
out = debugger_cli_common.get_tensorflow_version_lines(True)
self.assertIn("TensorFlow version: %s" % pywrap_tf_session.__version__,
              out.lines)
self.assertIn("  numpy: %s" % np.__version__, out.lines)
