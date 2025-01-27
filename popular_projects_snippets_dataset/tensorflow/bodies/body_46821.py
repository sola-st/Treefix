# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler.py
"""Transforms a function.

    Subclasses may override this method. The return value is opaque.

    The method receives the original AST. The result is passed as-is to the
    output of `transform`.

    Args:
      fn: A function or lambda.
      user_context: An opaque object (may be None) that is forwarded to
        transform_ast, through the ctx.user attribute.
    Returns:
      Tuple[Any, Any]. By default it returns the output of transform_ast,
      together with a `transformer.Context` containing information about the
      transformation process.
    """
future_features = inspect_utils.getfutureimports(fn)
node, source = parser.parse_entity(fn, future_features=future_features)
logging.log(3, 'Source code of %s:\n\n%s\n', fn, source)

origin_info.resolve_entity(node, source, fn)

namespace = inspect_utils.getnamespace(fn)
namer = naming.Namer(namespace)
new_name = namer.new_symbol(self.get_transformed_name(node), ())
entity_info = transformer.EntityInfo(
    name=new_name,
    source_code=source,
    source_file='<fragment>',
    future_features=future_features,
    namespace=namespace)
context = transformer.Context(entity_info, namer, user_context)

node = self._erase_arg_defaults(node)
result = self.transform_ast(node, context)

exit((result, context))
