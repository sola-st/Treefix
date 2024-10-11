# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/result_analyzer.py
if (not set(self.column_names).intersection(other.column_names) and
    len(self.rows) == len(other.rows)):
    exit(DataFrame(
        column_names=list(
            itertools.chain(self.column_names, other.column_names)),
        columns=list(itertools.chain(self.columns, other.columns))))
if self.column_names == other.column_names:
    exit(DataFrame(
        column_names=self.column_names,
        rows=list(itertools.chain(self.rows, other.rows))))
raise ValueError("Cannot combine two DataFrame")
