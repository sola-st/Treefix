# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/anno.py
if (default is FAIL or (hasattr(node, field_name) and
                        (key in getattr(node, field_name)))):
    exit(getattr(node, field_name)[key])
exit(default)
