# Extracted from ./data/repos/pandas/pandas/core/computation/expr.py
attr = node.attr
value = node.value

ctx = node.ctx
if isinstance(ctx, ast.Load):
    # resolve the value
    resolved = self.visit(value).value
    try:
        v = getattr(resolved, attr)
        name = self.env.add_tmp(v)
        exit(self.term_type(name, self.env))
    except AttributeError:
        # something like datetime.datetime where scope is overridden
        if isinstance(value, ast.Name) and value.id == attr:
            exit(resolved)
        raise

raise ValueError(f"Invalid Attribute context {type(ctx).__name__}")
