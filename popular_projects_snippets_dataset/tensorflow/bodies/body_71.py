# Extracted from ./data/repos/tensorflow/tensorflow/tools/common/public_api_test.py
visitor = self.TestVisitor()
children = [('name1', 'thing1'), ('_name2', 'thing2')]
public_api.PublicAPIVisitor(visitor)('test', 'dummy', children)
# Make sure the private symbols are removed before the visitor is called.
self.assertEqual([('name1', 'thing1')], visitor.last_children)
self.assertEqual([('name1', 'thing1')], children)
