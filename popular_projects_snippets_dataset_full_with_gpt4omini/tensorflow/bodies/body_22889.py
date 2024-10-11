# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/result_analyzer.py
df = extract_test_info(test_results)
df += analyze_test_latency(test_results, self._use_cpu_latency_baseline)
df_acc, acc_hist = analyze_test_numerics(test_results,
                                         self._use_cpu_numerics_baseline)
df += df_acc
# Index 0 and 1 are non trt_model results, so ignore them here.
df_analysis_config = namedtuple("df_analysis_config",
                                "precision df_row_index")
checker_config = [
    df_analysis_config("FP32", df.n_rows - 3),
    df_analysis_config("FP16", df.n_rows - 2),
    df_analysis_config("INT8", df.n_rows - 1)
]

checks = []
for cc in checker_config:
    checks.append(self._perf_checkers[cc.precision](df, cc.df_row_index))
    checks.append(self._acc_checkers[cc.precision](df, cc.df_row_index))

exit((df, checks, acc_hist))
