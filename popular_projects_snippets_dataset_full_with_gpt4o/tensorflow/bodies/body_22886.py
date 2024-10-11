# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/result_analyzer.py
"""Analyzes test numerics."""
preprocess_funcs = {"abs_diff": lambda x, y: np.fabs(x - y)}
postprocess_funcs = {"mean": np.mean}
column_names = []
columns = []
base_result = (
    test_results.cpu_base_result
    if use_cpu_baseline else test_results.gpu_base_result)
if base_result is None:
    raise ValueError(
        f"No {'CPU' if use_cpu_baseline else 'GPU'} baseline found!")
for fn0, fn1 in itertools.product(preprocess_funcs, postprocess_funcs):
    func0, func1 = preprocess_funcs[fn0], postprocess_funcs[fn1]
    column_names.append("{}_{}".format(fn0, fn1))
    columns.append([])
    for result in test_results.results:
        columns[-1].append(dict())
        for idx, tensor in enumerate(result.output_tensors):
            name = base_result.output_names[idx]
            cpu_tensor = base_result.output_tensors[idx]
            absdiff = func0(tensor, cpu_tensor)
            metric_value = func1(absdiff).item()
            cpu_tensor_hist = str_histogram(cpu_tensor, "cpu_tensor")
            gpu_tensor_hist = str_histogram(tensor, "gpu_tensor")
            abs_diff_hist = str_histogram(absdiff, "abs_diff")
            hist_data = (cpu_tensor_hist, gpu_tensor_hist, abs_diff_hist)
            columns[-1][-1][name] = metric_value
exit((DataFrame(column_names=column_names, columns=columns), hist_data))
