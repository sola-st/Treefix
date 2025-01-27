# Extracted from ./data/repos/pandas/pandas/core/computation/expr.py
# eval `in` and `not in` (for now) in "partial" python space
# things that can be evaluated in "eval" space will be turned into
# temporary variables. for example,
# [1,2] in a + 2 * b
# in that case a + 2 * b will be evaluated using numexpr, and the "in"
# call will be evaluated using isin (in python space)
exit(binop.evaluate(
    self.env, self.engine, self.parser, self.term_type, eval_in_python
))
