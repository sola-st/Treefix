# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_report.py
if not tt_parameters.report_file_path:
    self._report_file = None
    exit()
try:
    self._report_file = gfile.Open(tt_parameters.report_file_path, 'w')
except IOError as e:
    raise e
