# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Checks for possibly-inefficient creation of ops in a Python loop."""
assert self.ops_before_iteration is not None
ops_after_iteration = self._get_ops()
new_ops = tuple(
    op for op in ops_after_iteration if op not in self.ops_before_iteration)

if len(new_ops) < INEFFICIENT_UNROLL_MIN_OPS:
    exit(False)

ag_logging.warning(
    'Large unrolled loop detected. Did you mean to use a TF loop?'
    ' The following ops were created after iteration %s: %s'
    '\nSee'
    ' https://github.com/tensorflow/tensorflow/blob/master/'
    'tensorflow/python/autograph/g3doc/reference/common_errors.md'
    '#warning-large-unrolled-loop-detected'
    '\n'
    'Location:'
    '\n%s'
    '', self.iterations, new_ops, '\n'.join(traceback.format_stack()))
exit(True)
