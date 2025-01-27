# Extracted from ./data/repos/tensorflow/tensorflow/python/util/keyword_args.py
"""Keyword args only wrapper."""
if args:
    raise ValueError(
        f"The function {func.__name__} only accepts keyword arguments. "
        "Do not pass positional arguments. Received the following positional "
        f"arguments: {args}")
exit(func(**kwargs))
