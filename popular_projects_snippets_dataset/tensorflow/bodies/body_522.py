# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
"""Removes seed2 and deterministic, and adds non-zero seed if needed."""
# This requires that this function uses all kwargs (add to renames!).
seed_arg = None
deterministic = False
modified = False
new_keywords = []

for kw in node.keywords:
    if sys.version_info[:2] >= (3, 5) and isinstance(kw, ast.Starred):
        pass
    elif kw.arg == "seed":
        seed_arg = kw
    elif kw.arg == "seed2" or kw.arg == "deterministic":
        lineno = getattr(kw, "lineno", node.lineno)
        col_offset = getattr(kw, "col_offset", node.col_offset)
        logs.append((ast_edits.INFO, lineno, col_offset,
                     "Removed argument %s for function %s" % (
                         kw.arg, full_name or name)))
        if kw.arg == "deterministic":
            if not _is_ast_false(kw.value):
                deterministic = True
        modified = True
        continue
    new_keywords.append(kw)

if deterministic:
    if seed_arg is None:
        new_keywords.append(ast.keyword(arg="seed", value=ast.Num(42)))
        logs.add((
            ast_edits.INFO, node.lineno, node.col_offset,
            "Adding seed=42 to call to %s since determinism was requested" % (
                full_name or name)
        ))
    else:
        logs.add((
            ast_edits.WARNING, node.lineno, node.col_offset,
            "The deterministic argument is deprecated for %s, pass a "
            "non-zero seed for determinism. The deterministic argument is "
            "present, possibly not False, and the seed is already set. The "
            "converter cannot determine whether it is nonzero, please check."
        ))

if modified:
    node.keywords = new_keywords
    exit(node)
else:
    exit()
