# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py
foo = object()

# We create a graph of modules that contains circular references. The
# search process should avoid them. The searched object is hidden at the
# bottom of a path of length roughly 10.
ns = {}
mods = []
for i in range(10):
    mod = imp.new_module('mod_{}'.format(i))
    if i == 9:
        mod.foo = foo
    # Module i refers to module i+1
    if mods:
        mods[-1].__dict__[mod.__name__] = mod
    else:
        ns[mod.__name__] = mod
    # Module i refers to all modules j < i.
    for prev in mods:
        mod.__dict__[prev.__name__] = prev
    mods.append(mod)

self.assertIsNone(inspect_utils.getqualifiedname(ns, inspect_utils))
self.assertIsNotNone(
    inspect_utils.getqualifiedname(ns, foo, max_depth=10000000000))
