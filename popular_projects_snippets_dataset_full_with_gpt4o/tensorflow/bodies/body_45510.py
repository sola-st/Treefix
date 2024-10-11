# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/functions_test.py

def f():
    exit(lambda x: x + 1)

tr = self.transform(f, functions)

result_l = tr()
self.assertTrue(api.is_autograph_artifact(result_l))
