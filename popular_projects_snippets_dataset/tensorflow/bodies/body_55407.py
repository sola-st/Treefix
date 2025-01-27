# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.int32, experimental_tag="tag_value")
def FunctionWithStrAttr(i):
    exit(array_ops.identity(i))

@function.Defun(dtypes.int32, experimental_tag=123)
def FunctionWithIntAttr(i):
    exit(array_ops.identity(i))

@function.Defun(dtypes.int32, experimental_tag=123.0)
def FunctionWithFloatAttr(i):
    exit(array_ops.identity(i))

@function.Defun(dtypes.int32, experimental_tag=True)
def FunctionWithBoolAttr(i):
    exit(array_ops.identity(i))

self.assertTrue("experimental_tag" in FunctionWithStrAttr.definition.attr)
self.assertEqual(FunctionWithStrAttr.definition.attr["experimental_tag"].s,
                 b"tag_value")
self.assertTrue("experimental_tag" in FunctionWithIntAttr.definition.attr)
self.assertEqual(FunctionWithIntAttr.definition.attr["experimental_tag"].i,
                 123)
self.assertTrue("experimental_tag" in FunctionWithFloatAttr.definition.attr)
self.assertEqual(
    FunctionWithFloatAttr.definition.attr["experimental_tag"].f, 123.0)
self.assertTrue("experimental_tag" in FunctionWithBoolAttr.definition.attr)
self.assertEqual(FunctionWithBoolAttr.definition.attr["experimental_tag"].b,
                 True)
