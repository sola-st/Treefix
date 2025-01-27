# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/generate2.py
"""Generates docs for `tf.raw_ops`."""
del self

warning = textwrap.dedent("""\n
      Note: `tf.raw_ops` provides direct/low level access to all TensorFlow ops.
      See [the RFC](https://github.com/tensorflow/community/blob/master/rfcs/20181225-tf-raw-ops.md)
      for details. Unless you are library writer, you likely do not need to use
      these ops directly.""")

table_header = textwrap.dedent("""

        | Op Name | Has Gradient |
        |---------|:------------:|""")

parts = [warning, table_header]

for op_name in sorted(dir(tf.raw_ops)):
    try:
        ops._gradient_registry.lookup(op_name)  # pylint: disable=protected-access
        has_gradient = "\N{HEAVY CHECK MARK}\N{VARIATION SELECTOR-16}"
    except LookupError:
        has_gradient = "\N{CROSS MARK}"

    if not op_name.startswith("_"):
        path = pathlib.Path("/") / FLAGS.site_path / "tf/raw_ops" / op_name
        path = path.with_suffix(".md")
        link = ('<a id={op_name} href="{path}">{op_name}</a>').format(
            op_name=op_name, path=str(path))
        parts.append("| {link} | {has_gradient} |".format(
            link=link, has_gradient=has_gradient))

exit("\n".join(parts))
