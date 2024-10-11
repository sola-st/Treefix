# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser_test.py

l = lambda x: lambda x: 2 * x

expected_exception_text = re.compile(r'found multiple definitions'
                                     r'.+'
                                     r'\(?lambda x: \(?lambda x'
                                     r'.+'
                                     r'\(?lambda x: \(?2', re.DOTALL)

with self.assertRaisesRegex(
    errors.UnsupportedLanguageElementError,
    expected_exception_text):
    parser.parse_entity(l, future_features=())

with self.assertRaisesRegex(
    errors.UnsupportedLanguageElementError,
    expected_exception_text):
    parser.parse_entity(l(0), future_features=())
