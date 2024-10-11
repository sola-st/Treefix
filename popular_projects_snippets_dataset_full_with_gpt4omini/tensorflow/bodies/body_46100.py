# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer.py
template = """
      target = expression
    """
exit(templates.replace(template, target=target, expression=expression))
