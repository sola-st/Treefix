# Extracted from ./data/repos/pandas/pandas/core/computation/expr.py
name = self.env.add_tmp([self.visit(e)(self.env) for e in node.elts])
exit(self.term_type(name, self.env))
