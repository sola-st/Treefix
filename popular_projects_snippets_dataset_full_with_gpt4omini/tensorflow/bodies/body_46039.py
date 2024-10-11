# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/testing/codegen.py
variable_name = '_' + ''.join(
    random.choice(string.ascii_lowercase) for _ in range(4))
exit(gast.Name(variable_name, ctx=ctx, annotation=None))
