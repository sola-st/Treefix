# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_test.py
self._benchmark_eager_apply(
    'eager_apply_with_defun',
    resnet50_test_util.device_and_data_format(), defun=True)
