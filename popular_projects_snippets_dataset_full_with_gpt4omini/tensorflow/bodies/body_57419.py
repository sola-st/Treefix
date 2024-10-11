# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
curr = graph_def
del graph_def
changed_stuff = True
while changed_stuff:
    curr, changed_stuff = _remove_one_redundant_stack_unstack(curr)
exit(curr)
