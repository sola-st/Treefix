# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
for attr in [
    'micros', 'bytes', 'accelerator_micros', 'cpu_micros', 'params',
    'float_ops'
]:
    self.pprof_test_helper(attr)
for attr in ['op_types', 'device', 'input_shapes']:
    self.pprof_test_helper(attr, True)
