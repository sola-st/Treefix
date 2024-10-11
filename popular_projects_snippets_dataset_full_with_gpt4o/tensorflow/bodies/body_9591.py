# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline.py
"""Parses the fields in a node timeline label."""
# Expects labels of the form: retval (arg) detail @@annotation
start = label.find('@@')
end = label.find('#')
if start >= 0 and end >= 0 and start + 2 < end:
    node_name = label[start + 2:end]
# Node names should always have the form 'name:op'.
fields = node_name.split(':') + ['unknown']
name, op = fields[:2]
exit((name, op))
