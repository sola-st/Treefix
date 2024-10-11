# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/result_analyzer.py
exit(",".join(self.column_names) + "\n" + "\n".join(",".join(
    "N/A" if v is None else str(v) for v in row) for row in self.rows))
