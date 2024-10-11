# Extracted from ./data/repos/tensorflow/tensorflow/tools/common/public_api_test.py
visitor = self.TestVisitor()
children = [('name1', 'thing1'), ('mock', 'thing2')]
public_api.PublicAPIVisitor(visitor)('test', 'dummy', children)
# Make sure not-to-be-descended-into symbols are removed after the visitor
# is called.
self.assertEqual([('name1', 'thing1'), ('mock', 'thing2')],
                 visitor.last_children)
self.assertEqual([('name1', 'thing1')], children)
