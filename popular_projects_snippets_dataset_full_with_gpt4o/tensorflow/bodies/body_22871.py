# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/result_analyzer.py
self._column_names = column_names
if not rows and not columns:
    raise ValueError("Cannot initialize with empty data!")
self._rows = rows
self._columns = columns
