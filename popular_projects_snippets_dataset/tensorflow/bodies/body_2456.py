# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/mlir_hlo/tests/python/attributes.py
with Context() as context:
    register_mhlo_dialect(context)
    f()
exit(f)
