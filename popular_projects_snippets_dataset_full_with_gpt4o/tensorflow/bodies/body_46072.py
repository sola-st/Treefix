# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates.py
"""Create a new ReplaceTransformer.

    Args:
      replacements: A mapping from placeholder names to (lists of) AST nodes
          that these placeholders will be replaced by.
    """
self.replacements = replacements
self.in_replacements = False
self.preserved_annos = {
    anno.Basic.DIRECTIVES,
    anno.Basic.EXTRA_LOOP_TEST,
    anno.Basic.ORIGIN,
    anno.Basic.SKIP_PROCESSING,
    anno.Static.ORIG_DEFINITIONS,
    'function_context_name',
}
