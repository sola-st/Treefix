# Extracted from ./data/repos/tensorflow/tensorflow/tools/common/traverse_test.py
visitor = TestVisitor()
traverse.traverse(TestVisitor, visitor)
self.assertEqual(TestVisitor,
                 visitor.call_log[0][1])
# There are a bunch of other members, but make sure that the ones we know
# about are there.
self.assertIn('__init__', [name for name, _ in visitor.call_log[0][2]])
self.assertIn('__call__', [name for name, _ in visitor.call_log[0][2]])
