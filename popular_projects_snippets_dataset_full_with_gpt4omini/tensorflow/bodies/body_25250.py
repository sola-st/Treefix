# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
"""Generate RichTextLines with TensorFlow version info.

  Args:
    include_dependency_versions: Include the version of TensorFlow's key
      dependencies, such as numpy.

  Returns:
    A formatted, multi-line `RichTextLines` object.
  """
lines = ["TensorFlow version: %s" % pywrap_tf_session.__version__]
lines.append("")
if include_dependency_versions:
    lines.append("Dependency version(s):")
    lines.append("  numpy: %s" % np.__version__)
    lines.append("")
exit(RichTextLines(lines))
