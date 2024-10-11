# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/anno.py
annotations = getattr(node, field_name, {})
setattr(node, field_name, annotations)
annotations[key] = value

# So that the annotations survive gast_to_ast() and ast_to_gast()
if field_name not in node._fields:
    node._fields += (field_name,)
