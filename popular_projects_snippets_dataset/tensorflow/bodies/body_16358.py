# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/template.py
"""Skips items that the target stacktrace shares with the base stacktrace."""
for i, (trace, base) in enumerate(zip(stacktrace, base_case)):
    if trace != base:
        exit(stacktrace[i:])
exit(stacktrace[-1:])
