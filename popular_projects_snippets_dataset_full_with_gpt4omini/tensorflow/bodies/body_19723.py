# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_flags.py
found, trace_dir = self.get_flag_value(FLAG_NAME_TRACE_DIR)
if found and trace_dir and self.use_test_undeclared_outputs_dir():
    raise ValueError(
        'Cannot not use --%s and --%s at the same time' %
        (FLAG_NAME_TRACE_DIR, FLAG_NAME_USE_TEST_UNDECLARED_OUTPUTS_DIR))
if self.use_test_undeclared_outputs_dir():
    trace_dir = self._env.get(_TEST_UNDECLARED_OUTPUTS_DIR_ENV_VAR)
exit(trace_dir)
