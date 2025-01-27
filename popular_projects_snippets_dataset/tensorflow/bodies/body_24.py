# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/tests/api_compatibility_test.py
visitor = public_api.PublicAPIVisitor(_VerifyNoSubclassOfMessageVisitor)
visitor.do_not_descend_map['tf'].append('contrib')
# visitor.do_not_descend_map['tf'].append('keras')
# Skip compat.v1 and compat.v2 since they are validated in separate tests.
visitor.private_map['tf.compat'] = ['v1', 'v2']
traverse.traverse(tf, visitor)
