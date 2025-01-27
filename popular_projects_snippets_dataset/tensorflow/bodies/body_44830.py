# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/unsupported_features_checker.py
if (node.attr is not None
    and node.attr.startswith('__') and not node.attr.endswith('__')):
    raise errors.UnsupportedLanguageElementError(
        'mangled names are not yet supported')
self.generic_visit(node)
