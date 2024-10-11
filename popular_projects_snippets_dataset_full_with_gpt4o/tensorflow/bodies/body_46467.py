# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py
if f_name == 'test_fn':
    test_self.assertFalse(f_is_local)
    test_self.assertEqual(name, qual_names.QN('a'))
    test_self.assertEqual(type_anno, qual_names.QN('int'))
elif f_name == 'foo':
    test_self.assertTrue(f_is_local)
    if name == qual_names.QN('x'):
        test_self.assertEqual(type_anno, qual_names.QN('float'))
    elif name == qual_names.QN('y'):
        test_self.assertIsNone(type_anno)
    else:
        test_self.fail('unexpected argument {} for {}'.format(name, f_name))
else:
    test_self.fail('unexpected function name {}'.format(f_name))
exit({str(name) + '_type'})
