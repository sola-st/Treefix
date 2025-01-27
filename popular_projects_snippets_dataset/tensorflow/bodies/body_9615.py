# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
exit((e.op == c.op and e.op._original_op == b.op and
        e.op._original_op._original_op == a.op))
