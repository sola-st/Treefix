# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
deep = self.memory_usage == "deep"
exit(self.data.memory_usage(index=True, deep=deep).sum())
