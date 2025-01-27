# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py
foo = object()

# We create a densely connected graph consisting of a relatively small
# number of modules and hide our symbol in one of them. The path to the
# symbol is at least 10, and each node has about 10 neighbors. However,
# by skipping visited modules, the search should take much less.
ns = {}
prev_level = []
for i in range(10):
    current_level = []
    for j in range(10):
        mod_name = 'mod_{}_{}'.format(i, j)
        mod = imp.new_module(mod_name)
        current_level.append(mod)
        if i == 9 and j == 9:
            mod.foo = foo
    if prev_level:
        # All modules at level i refer to all modules at level i+1
        for prev in prev_level:
            for mod in current_level:
                prev.__dict__[mod.__name__] = mod
    else:
        for mod in current_level:
            ns[mod.__name__] = mod
    prev_level = current_level

self.assertIsNone(inspect_utils.getqualifiedname(ns, inspect_utils))
self.assertIsNotNone(
    inspect_utils.getqualifiedname(ns, foo, max_depth=10000000000))
