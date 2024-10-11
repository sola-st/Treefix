# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
klass, dtype, method = combo
cls_funcs = request.node.session.items
exit(any(
    klass in x.name and dtype in x.name and method in x.name for x in cls_funcs
))
