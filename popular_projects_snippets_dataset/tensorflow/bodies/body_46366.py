# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
existing_types = anno.Static.CLOSURE_TYPES.of(ast_node, None)

if existing_types is None:
    existing_types = {}
    anno.Static.CLOSURE_TYPES.add_to(ast_node, existing_types)

for k, v in types.types.items():
    if k in existing_types:
        existing_types[k].update(v)
    else:
        existing_types[k] = set(v)
