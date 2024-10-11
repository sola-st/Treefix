# Extracted from ./data/repos/tensorflow/tensorflow/tools/common/traverse_test.py
visitor = TestVisitor()
traverse.traverse(test_module1, visitor)

called = [parent for _, parent, _ in visitor.call_log]

self.assertIn(test_module1.ModuleClass1, called)
self.assertIn(test_module2.ModuleClass2, called)
