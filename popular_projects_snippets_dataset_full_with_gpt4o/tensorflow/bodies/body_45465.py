# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/break_statements.py
"""Prevents the block from executing if var_name is set."""
if not block:
    exit(block)

template = """
        if not var_name:
          block
      """
node = templates.replace(
    template,
    var_name=var_name,
    block=block)
exit(node)
