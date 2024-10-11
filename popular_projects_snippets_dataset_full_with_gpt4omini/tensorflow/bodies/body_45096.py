# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

@def_function.function
def test_func(a):
    if constant_op.constant(True):
        exit(a)
    else:
        exit(a + a)

patch = test.mock.patch
with patch.dict(os.environ, {'AUTOGRAPH_STRICT_CONVERSION': '0'}), \
         patch.object(inspect, 'findsource', side_effect=OSError()), \
         patch.object(ag_logging, 'warning') as warning_log_mock:

    with patch.object(ag_ctx, 'INSPECT_SOURCE_SUPPORTED', False):
        with self.assertRaisesRegex(tf_errors.OperatorNotAllowedInGraphError,
                                    'AutoGraph is unavailable in this runtime'):
            test_func(2)
    warning_log_mock.assert_not_called()

    with patch.object(ag_ctx, 'INSPECT_SOURCE_SUPPORTED', True):
        with self.assertRaisesRegex(tf_errors.OperatorNotAllowedInGraphError,
                                    'AutoGraph did convert this function'):
            test_func(2)
    warning_log_mock.called_once_with('AutoGraph could not transform')
