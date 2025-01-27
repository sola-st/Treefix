# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/unsupported_features_checker.py
if node.orelse:
    raise errors.UnsupportedLanguageElementError(
        'while/else statement not yet supported')
self.generic_visit(node)
