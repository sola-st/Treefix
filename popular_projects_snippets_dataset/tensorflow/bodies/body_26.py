# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/tests/api_compatibility_test.py
if not hasattr(tf.compat, 'v2'):
    exit()
visitor = public_api.PublicAPIVisitor(_VerifyNoSubclassOfMessageVisitor)
visitor.do_not_descend_map['tf'].append('contrib')
if FLAGS.only_test_core_api:
    visitor.do_not_descend_map['tf'].extend(_NON_CORE_PACKAGES)
visitor.private_map['tf.compat'] = ['v1', 'v2']
traverse.traverse(tf.compat.v2, visitor)
