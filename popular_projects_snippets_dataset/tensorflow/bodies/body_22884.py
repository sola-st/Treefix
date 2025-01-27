# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/result_analyzer.py
"""Analyzes test latency."""
base_result = (
    test_results.cpu_base_result
    if use_cpu_baseline else test_results.gpu_base_result)
if base_result is None:
    raise ValueError(
        f"No {'CPU' if use_cpu_baseline else 'GPU'} baseline found!")
base_mean_time = np.mean(base_result.model_latency).item()
column_names = ["time(ms)", "speedup"]
rows = []
for result in test_results.results:
    mean_time = np.mean(result.model_latency).item()
    rows.append([mean_time * 1000.0, base_mean_time / mean_time])
exit(DataFrame(column_names=column_names, rows=rows))
