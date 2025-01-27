# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/update/generate_v2_renames_map.py
"""Looks for functions/classes that need to be renamed in TF 2.0.

  Returns:
    Set of tuples of the form (current name, new name).
  """
# Set of rename lines to write to output file in the form:
#   'tf.deprecated_name': 'tf.canonical_name'
renames = set()
all_v2_names = get_all_v2_names()

def visit(unused_path, unused_parent, children):
    """Visitor that collects rename strings to add to rename_line_set."""
    for child in children:
        _, attr = tf_decorator.unwrap(child[1])
        api_names_v1 = [
            name for name in tf_export.get_v1_names(attr)
            if '.__internal__.' not in name
        ]
        api_names_v2 = tf_export.get_v2_names(attr)

        if not api_names_v2:
            # It is possible that a different function is exported with the same
            # name. For e.g. when creating a different function to rename arguments.
            # Determine if this is the case to not do a useless rename to compat.v1
            # for the function and its aliases.
            # Note that unsafe v1 to v2 renames created here are overridden by the
            # manual_symbol_renames in all_renames_v2.py.
            api_names_v2 = [name for name in api_names_v1 if name in all_v2_names]

        deprecated_api_names = set(api_names_v1) - set(api_names_v2)
        for name in deprecated_api_names:
            renames.add((name, get_canonical_name(api_names_v2, name)))

visitor = public_api.PublicAPIVisitor(visit)
visitor.do_not_descend_map['tf'].append('contrib')
visitor.private_map['tf.compat'] = ['v1', 'v2']
traverse.traverse(tf.version, visitor)
traverse.traverse(tf.compat.v1, visitor)
traverse.traverse(tf.compat.v1.estimator, visitor)
traverse.traverse(tf.compat.v2, visitor)
traverse.traverse(tf.compat.v2.estimator, visitor)

exit(renames)
