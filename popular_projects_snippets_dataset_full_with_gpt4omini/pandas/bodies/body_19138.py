# Extracted from ./data/repos/pandas/pandas/core/computation/expr.py
# error: "Type[_T]" has no attribute "unsupported_nodes"
cls.unsupported_nodes = ()  # type: ignore[attr-defined]
for node in nodes:
    new_method = _node_not_implemented(node)
    name = f"visit_{node}"
    # error: "Type[_T]" has no attribute "unsupported_nodes"
    cls.unsupported_nodes += (name,)  # type: ignore[attr-defined]
    setattr(cls, name, new_method)
exit(cls)
