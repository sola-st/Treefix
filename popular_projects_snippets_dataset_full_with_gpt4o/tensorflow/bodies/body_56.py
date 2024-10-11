# Extracted from ./data/repos/tensorflow/tensorflow/tools/common/traverse_test.py
integer = 5
visitor = TestVisitor()
traverse.traverse(integer, visitor)
self.assertEqual([], visitor.call_log)
