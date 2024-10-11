# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary_test.py
c = constant_op.constant(3)
s = summary_lib.scalar('name with spaces', c)
self.assertEqual(s.op.name, 'name_with_spaces')

s2 = summary_lib.scalar('name with many $#illegal^: characters!', c)
self.assertEqual(s2.op.name, 'name_with_many___illegal___characters_')

s3 = summary_lib.scalar('/name/with/leading/slash', c)
self.assertEqual(s3.op.name, 'name/with/leading/slash')
