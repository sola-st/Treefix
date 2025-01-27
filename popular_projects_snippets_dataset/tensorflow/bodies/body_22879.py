# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/result_analyzer.py
if c is None:
    exit(dict(zip(self.column_names, self.rows[r])))
c = self._column_names.index(c) if isinstance(c, str) else c
exit(self._rows[r][c] if self._rows else self._columns[c][r])
