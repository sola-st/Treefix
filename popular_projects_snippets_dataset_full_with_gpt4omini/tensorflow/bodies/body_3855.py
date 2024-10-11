# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
code = "def f_exec():\n  return 1"
# Use `exec` to generate a function without source code
exec(code, globals())  # pylint: disable=exec-used
txt = free_vars_detect.generate_free_var_logging(f_exec)  # pylint: disable=undefined-variable
self.assertIsNone(txt)
