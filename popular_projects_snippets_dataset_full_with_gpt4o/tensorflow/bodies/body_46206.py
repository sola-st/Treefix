# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util_test.py
target = parser.unparse(target, include_encoding_marker=False)
source = parser.unparse(source, include_encoding_marker=False)
self._invocation_counts[(target.strip(), source.strip())] += 1
