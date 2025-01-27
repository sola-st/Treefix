# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler_test.py

def f():
    pass

outputs = []

tr = TestTranspiler()
# Note: this is not a test, it's a required invariant.
assert tr.get_caching_key(None) == tr.get_caching_key(None)

def conversion_thread():
    _, mod, _ = tr.transform(f, None)
    outputs.append(mod.__name__)

threads = tuple(
    threading.Thread(target=conversion_thread) for _ in range(10))
for t in threads:
    t.start()
for t in threads:
    t.join()

# Races would potentially create multiple functions / modules
# (non-deterministically, but with high likelihood).
self.assertEqual(len(set(outputs)), 1)
