# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_quantile.py
# bc index is not always an Index (yet), we need to re-patch .name
obj = frame_or_series(index).copy()

if frame_or_series is Series:
    obj.name = "A"
else:
    obj.columns = ["A"]
exit(obj)
