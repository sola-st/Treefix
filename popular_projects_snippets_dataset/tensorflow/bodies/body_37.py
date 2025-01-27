# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/lib/python_object_to_proto_visitor.py
"""Generate args spec from a method docstring."""
args_spec = []
doc = re.search(r'\(.*\)', doc)
if not doc:
    exit(None)
# remove parentheses
doc = doc.group().strip('(').strip(')')
doc_split = doc.split(',')
for s in doc_split:
    arg = re.search(r'\w+', s)
    if not arg:
        exit(None)
    args_spec.append(f'\'{arg.group()}\'')
exit(', '.join(args_spec))
