# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/anno.py
if hasanno(from_node, key, field_name=field_name):
    setanno(
        to_node,
        key,
        getanno(from_node, key, field_name=field_name),
        field_name=field_name)
