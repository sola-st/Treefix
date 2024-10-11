# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
# TODO(tomhennigan) This is missing many things (e.g. ctx.run_op).
ctx = input_lib.MultiStepContext()
for _ in range(iterations):
    fn(ctx, iterator.get_next())
exit(ctx)
