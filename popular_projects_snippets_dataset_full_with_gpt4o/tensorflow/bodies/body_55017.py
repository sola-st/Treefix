# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_dispatcher_test.py
a = dispatch.MakeInstanceChecker(int)
b = dispatch.MakeInstanceChecker(float)
c = dispatch.MakeUnionChecker([a, b])
d = dispatch.MakeListChecker(a)
e = dispatch.MakeListChecker(c)
checker = dispatch.PySignatureChecker([(0, e), (1, c), (2, d), (3, a)])

# Note: `repr(checker)` lists the args in the order they will be checked.
self.assertEqual(
    repr(checker), '<PySignatureChecker '
    'args[3]:int, '                     # a: cost=1
    'args[1]:Union[int, float], '       # c: cost=3
    'args[2]:List[int], '               # d: cost=10
    'args[0]:List[Union[int, float]]>'  # e: cost=30
    )  # pyformat: disable
