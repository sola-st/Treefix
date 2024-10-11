# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""Construct a logdir for an eval summary writer."""
exit(os.path.join(model_dir, "eval" if not name else "eval_" + name))
