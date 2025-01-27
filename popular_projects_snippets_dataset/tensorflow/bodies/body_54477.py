# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
strs = [
    "hidden1/hidden1/weights",  # Same prefix. Should strip.
    "hidden1///hidden1/weights",  # Extra "/". Should strip.
    "^hidden1/hidden1/weights",  # Same prefix. Should strip.
    "loc:@hidden1/hidden1/weights",  # Same prefix. Should strip.
    "hhidden1/hidden1/weights",  # Different prefix. Should keep.
    "hidden1"
]  # Not a prefix. Should keep.
expected_striped = [
    "hidden1/weights", "hidden1/weights", "^hidden1/weights",
    "loc:@hidden1/weights", "hhidden1/hidden1/weights", "hidden1"
]
expected_prepended = [
    "hidden2/hidden1/weights", "hidden2/hidden1/weights",
    "^hidden2/hidden1/weights", "loc:@hidden2/hidden1/weights",
    "hidden2/hhidden1/hidden1/weights", "hidden2/hidden1"
]
name_scope_to_strip = "hidden1"
name_scope_to_add = "hidden2"
for es, ep, s in zip(expected_striped, expected_prepended, strs):
    striped = ops.strip_name_scope(s, name_scope_to_strip)
    self.assertEqual(es, striped)
    self.assertEqual(ep, ops.prepend_name_scope(striped, name_scope_to_add))
