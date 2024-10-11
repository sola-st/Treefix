# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees_test.py
mock = MockConvertedCall()
tr = self.transform(
    f, (functions, call_trees),
    ag_overrides={'converted_call': mock})
exit((tr, mock))
