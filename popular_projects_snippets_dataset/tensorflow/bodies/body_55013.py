# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_dispatcher_test.py
for (canon_args, expected) in canon_expected_pairs:
    with self.subTest(f'{canon_args} -> {expected}'):
        self.assertEqual(checker.CheckCanonicalizedArgs(canon_args), expected)
