# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/variables.py
if isinstance(node.target, gast.Name):
    template = """
        var_ = ag__.ld(var_)
        original
      """
    node = templates.replace(template, var_=node.target, original=node)
else:
    node = self.generic_visit(node)
exit(node)
