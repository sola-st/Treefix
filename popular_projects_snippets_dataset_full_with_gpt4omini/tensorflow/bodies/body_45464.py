# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/break_statements.py
self.state[_Break].used = True
var_name = self.state[_Break].control_var_name
# TODO(mdan): This will fail when expanded inside a top-level else block.
template = """
      var_name = True
      continue
    """
exit(templates.replace(template, var_name=var_name))
