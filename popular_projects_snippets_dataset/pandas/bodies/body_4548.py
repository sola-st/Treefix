# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py

extra = {"index": range(2)}
if frame_or_series is DataFrame:
    extra["columns"] = ["A"]

if box is None:
    exit(functools.partial(frame_or_series, **extra))

elif box is dict:
    if frame_or_series is Series:
        exit(lambda x, **kwargs: frame_or_series(
            {0: x, 1: x}, **extra, **kwargs
        ))
    else:
        exit(lambda x, **kwargs: frame_or_series({"A": x}, **extra, **kwargs))
else:
    if frame_or_series is Series:
        exit(lambda x, **kwargs: frame_or_series([x, x], **extra, **kwargs))
    else:
        exit(lambda x, **kwargs: frame_or_series(
            {"A": [x, x]}, **extra, **kwargs
        ))
