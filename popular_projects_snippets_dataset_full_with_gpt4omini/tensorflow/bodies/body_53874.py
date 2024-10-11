# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
exit(self.assertRaisesWithPredicateMatch(errors.OpError,
                                           expected_err_re_or_predicate))
