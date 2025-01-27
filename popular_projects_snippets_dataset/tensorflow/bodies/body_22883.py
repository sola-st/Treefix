# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/result_analyzer.py
"""Extracts the test infomation."""
column_names = list(
    itertools.chain(model_handler.ModelConfig._fields,
                    ["enable_gpu", "trt_model"],
                    trt.TrtConversionParams._fields))
rows = []
for result in test_results.results:
    r = list(result.model_config) + [result.enable_gpu]
    if result.trt_convert_params is not None:
        r += [True] + list(result.trt_convert_params)
    else:
        r += [False] + [None for _ in trt.TrtConversionParams._fields]
    rows.append(r)
exit(DataFrame(column_names=column_names, rows=rows))
