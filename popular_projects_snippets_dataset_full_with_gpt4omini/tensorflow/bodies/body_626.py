# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/fenced_doctest_test.py
parser = fenced_doctest_lib.FencedCellParser(fence_label='python')

example_tuples = []
for example in parser.get_examples(string, name=self._testMethodName):
    source = example.source.rstrip('\n')
    want = example.want
    if want is not None:
        want = want.rstrip('\n')
    example_tuples.append((source, want))

self.assertEqual(expected_example_tuples, example_tuples)
