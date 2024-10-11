# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/lists.py
node = self.generic_visit(node)
template = """
      ag__.new_list(elements)
    """
exit(templates.replace_as_expression(template, elements=node))
