# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Replaces `<<API_LIST>>` in target.__doc__ with the given list of APIs."""
lines = []
for func in api_list:
    name = tf_export_lib.get_canonical_name_for_symbol(
        func, add_prefix_to_v1_names=True)
    if name is not None:
        params = tf_inspect.signature(func).parameters.keys()
        lines.append(f"  * `tf.{name}({', '.join(params)})`")
lines.sort()
target.__doc__ = target.__doc__.replace("  <<API_LIST>>", "\n".join(lines))
