# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/mlir_hlo/tests/python/types.py
"""Check that the Token type is available."""
assert str(TokenType.get()) == "!mhlo.token"
