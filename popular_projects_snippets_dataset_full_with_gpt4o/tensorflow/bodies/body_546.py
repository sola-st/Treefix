# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/update/generate_v2_renames_map.py
"""Get a set of function/class names available in TensorFlow 2.0."""
v2_names = set()  # All op names in TensorFlow 2.0

def visit(unused_path, unused_parent, children):
    """Visitor that collects TF 2.0 names."""
    for child in children:
        _, attr = tf_decorator.unwrap(child[1])
        api_names_v2 = tf_export.get_v2_names(attr)
        for name in api_names_v2:
            v2_names.add(name)

visitor = public_api.PublicAPIVisitor(visit)
visitor.do_not_descend_map['tf'].append('contrib')
visitor.private_map['tf.compat'] = ['v1', 'v2']
traverse.traverse(tf.compat.v2, visitor)
traverse.traverse(tf.compat.v2.estimator, visitor)
exit(v2_names)
