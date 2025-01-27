# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_flags.py
if env:
    self._env = env
else:
    self._env = os.environ
self._validate_flag_names()
self.trace_mode = self._get_trace_mode()
self.submode = self._get_submode()
self.trace_dir = self._get_trace_dir()
self.report_file_path = self._get_report_filepath()
self.op_range = self._get_op_range()
self.excluded_opname_re_list = self._flag_value_to_re_list(
    FLAG_NAME_EXCLUDED_OPNAMES)
self.excluded_optype_re_list = self._flag_value_to_re_list(
    FLAG_NAME_EXCLUDED_OPTYPES)

self.included_opname_re_list = self._flag_value_to_re_list(
    FLAG_NAME_INCLUDED_OPNAMES)
self.included_optype_re_list = self._flag_value_to_re_list(
    FLAG_NAME_INCLUDED_OPTYPES)

self.trace_scalar_ops = self.is_flag_on(FLAG_NAME_TRACE_SCALAR_OPS)
self.use_compact_trace = self.trace_mode in (TRACE_MODE_NAN_INF,
                                             TRACE_MODE_NORM,
                                             TRACE_MODE_HISTORY,
                                             TRACE_MODE_MAX_ABS,
                                             TRACE_MODE_SUMMARY)
self.use_temp_cache_var = self.is_flag_on(FLAG_NAME_TEMP_CACHE_VAR)
self.inspect_trace = self.is_flag_on(FLAG_NAME_INSPECT_TRACE)
self.use_fingerprint_subdir = self.is_flag_on(FLAG_NAME_FINGERPRINT_DIR)

_, self.graph_dump_path = self.get_flag_value(
    FLAG_NAME_DUMP_BEFORE_AFTER_GRAPHS)
self.trace_level = self._get_flag_int_value(FLAG_NAME_TRACE_LEVEL,
                                            _TT_DEFAULT_TRACE_LEVEL)
self.summary_signatures = self._get_summary_signatures()
self.collect_summary_per_core = self.is_flag_on(FLAG_NAME_SUMMARY_PER_CORE)
# TODO(b/199284834): Will be resolved with referenced bug.
if self.collect_summary_per_core:
    logging.warning('Aggregate signatures are approximate for mean, variance'
                    ' and sparsity.')
self.flush_summaries_with_outside_compile = self.is_flag_on(
    FLAG_FLUSH_SUMMARY)
# Do not produce errors or warnings if Tensor Tracer is not enabled.
if self.is_enabled():
    self._check_flag_errors()
