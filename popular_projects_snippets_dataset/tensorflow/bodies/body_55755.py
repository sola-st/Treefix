# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/unified_api_test.py
with tape_lib.GradientTape() as tape:
    tape.watch(a)
    result = unified_math_ops.log1p(a)
grads = tape.gradient(result, a)
exit(grads)
