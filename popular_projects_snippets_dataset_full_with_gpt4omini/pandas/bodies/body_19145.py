# Extracted from ./data/repos/pandas/pandas/core/computation/expr.py
if isinstance(node, str):
    clean = self.preparser(node)
    try:
        node = ast.fix_missing_locations(ast.parse(clean))
    except SyntaxError as e:
        if any(iskeyword(x) for x in clean.split()):
            e.msg = "Python keyword not valid identifier in numexpr query"
        raise e

method = f"visit_{type(node).__name__}"
visitor = getattr(self, method)
exit(visitor(node, **kwargs))
