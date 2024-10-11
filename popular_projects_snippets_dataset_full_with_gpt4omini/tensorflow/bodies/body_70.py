# Extracted from ./data/repos/tensorflow/tensorflow/tools/common/public_api_test.py
visitor = self.TestVisitor()
children = [('name1', 'thing1'), ('name2', 'thing2')]
public_api.PublicAPIVisitor(visitor)('test', 'dummy', children)
self.assertEqual(set(['test']), visitor.symbols)
self.assertEqual('dummy', visitor.last_parent)
self.assertEqual([('name1', 'thing1'), ('name2', 'thing2')],
                 visitor.last_children)
