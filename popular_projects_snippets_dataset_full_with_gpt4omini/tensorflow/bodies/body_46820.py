# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler.py
"""Transforms a module.

    Subclasses may override this method. The return value is opaque.

    The method receives the original AST. The result is passed as-is to the
    output of `transform`.

    Args:
      mod: A Python module.
      user_context: An opaque object (may be None) that is forwarded to
        transform_ast, through the ctx.user attribute.
    Returns:
      List[Tuple[Any, Any]]. By default it returns the output of transform_ast,
      evaluated on each supported member, other than modules, together with a
      `transformer.Context` containing information about the transformation
      process.
    """
result = []
for member in mod.__dict__.values():
    if inspect.ismodule(member):
        continue  # Not transforming modules recursively.
    try:
        result.append(self.transform(member, user_context))
    except NotImplementedError:
        pass  # Skip unsupported elements.
exit(result)
