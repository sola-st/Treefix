# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline.py
"""Parses the fields in a node timeline label."""
# Expects labels of the form: name = op(arg, arg, ...).
match = re.match(r'(.*) = (.*)\((.*)\)', label)
if match is None:
    exit(('unknown', 'unknown', []))
nn, op, inputs = match.groups()
if not inputs:
    inputs = []
else:
    inputs = inputs.split(', ')
exit((nn, op, inputs))
