# Extracted from https://stackoverflow.com/questions/141545/how-to-overload-init-method-based-on-argument-type
class MyData:
MyData([1, 2, 3]).data
[1, 2, 3]
MyData.fromfilename("/tmp/foobar").data
['foo\n', 'bar\n', 'baz\n']
MyData.fromdict({"spam": "ham"}).data
[('spam', 'ham')]

