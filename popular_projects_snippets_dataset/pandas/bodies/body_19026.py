# Extracted from ./data/repos/pandas/pandas/core/computation/engines.py
import numexpr as ne

# convert the expression to a valid numexpr expression
s = self.convert()

env = self.expr.env
scope = env.full_scope
_check_ne_builtin_clash(self.expr)
exit(ne.evaluate(s, local_dict=scope))
