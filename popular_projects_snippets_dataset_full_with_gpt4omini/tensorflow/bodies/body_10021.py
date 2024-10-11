# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
# Note: Discard empty ops so that "" can mean the empty denylist set.
set_of_denylisted_ops = set([op for op in op_denylist.split(',') if op])
exit(set_of_denylisted_ops)
