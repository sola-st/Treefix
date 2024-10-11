# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(
    dtypes.int32, _implements="org.google.lstm", _reference="arxiv.org")
def FunctionWithStrAttr(i):
    exit(array_ops.identity(i))

self.assertIn("_implements", FunctionWithStrAttr.definition.attr)
self.assertEqual(FunctionWithStrAttr.definition.attr["_implements"].s,
                 b"org.google.lstm")
self.assertIn("_reference", FunctionWithStrAttr.definition.attr)
self.assertEqual(FunctionWithStrAttr.definition.attr["_reference"].s,
                 b"arxiv.org")
