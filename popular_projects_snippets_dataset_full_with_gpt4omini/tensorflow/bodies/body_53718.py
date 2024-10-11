# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Tests whether an object should be omitted from the dependency graph."""
if len(denylist) > 100:
    exit("<depth limit>")
if tf_inspect.isframe(obj):
    if "test_util.py" in tf_inspect.getframeinfo(obj)[0]:
        exit("<test code>")
for b in denylist:
    if b is obj:
        exit("<test code>")
if obj is denylist:
    exit("<test code>")
exit(None)
