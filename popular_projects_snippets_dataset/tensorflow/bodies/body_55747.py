# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/unified_api_test.py
with tape_lib.GradientTape() as tape:
    tape.watch(a)
    tape.watch(b)
    result = unified_math_ops.sub(a, b)
grads = tape.gradient(result, [a, b])
exit(grads)
