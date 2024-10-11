# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_dispatcher_test.py
int_checker = dispatch.MakeInstanceChecker(int)
tensor_checker = dispatch.MakeInstanceChecker(ops.Tensor)
ragged_checker = dispatch.MakeInstanceChecker(ragged_tensor.RaggedTensor)
np_int_checker = dispatch.MakeInstanceChecker(np.integer)

t = constant_op.constant([1, 2, 3])
rt = ragged_factory_ops.constant([[1, 2], [3, 4, 5]])
a = [1, 2, 3]
b = ['a', 2, t]
c = [t, t * 2, t - 2]
d = [t, rt]
e = []
f = (1, 2, 3)
g = (rt,)
h = {1: 2, 3: 4}
i = np.array([1, 2, 3])

with self.subTest('List[int]'):
    checker = dispatch.MakeListChecker(int_checker)
    self.assertEqual(checker.Check(a), MATCH)
    self.assertEqual(checker.Check(b), NO_MATCH)
    self.assertEqual(checker.Check(c), NO_MATCH)
    self.assertEqual(checker.Check(d), NO_MATCH)
    self.assertEqual(checker.Check(e), MATCH)
    self.assertEqual(checker.Check(f), MATCH)
    self.assertEqual(checker.Check(iter(a)), NO_MATCH)
    self.assertEqual(checker.Check(iter(b)), NO_MATCH)
    self.assertEqual(checker.Check(reversed(e)), NO_MATCH)
    self.assertEqual(checker.Check(h), NO_MATCH)
    self.assertEqual(checker.Check(i), NO_MATCH)
    self.assertEqual(checker.cost(), 10)
    self.assertEqual(repr(checker), '<PyTypeChecker List[int]>')

with self.subTest('List[Tensor]'):
    checker = dispatch.MakeListChecker(tensor_checker)
    self.assertEqual(checker.Check(a), NO_MATCH)
    self.assertEqual(checker.Check(b), NO_MATCH)
    self.assertEqual(checker.Check(c), MATCH)
    self.assertEqual(checker.Check(d), NO_MATCH)
    self.assertEqual(checker.Check(e), MATCH)
    self.assertEqual(checker.cost(), 10)
    self.assertEqual(repr(checker), '<PyTypeChecker List[Tensor]>')

with self.subTest('List[Union[Tensor, RaggedTensor]]'):
    checker = dispatch.MakeListChecker(
        dispatch.MakeUnionChecker([tensor_checker, ragged_checker]))
    self.assertEqual(checker.Check(a), NO_MATCH)
    self.assertEqual(checker.Check(b), NO_MATCH)
    self.assertEqual(checker.Check(c), MATCH)
    self.assertEqual(checker.Check(d), MATCH_DISPATCHABLE)
    self.assertEqual(checker.Check(e), MATCH)
    self.assertEqual(checker.Check(f), NO_MATCH)
    self.assertEqual(checker.Check(g), MATCH_DISPATCHABLE)
    self.assertEqual(checker.cost(), 30)
    self.assertEqual(
        repr(checker), '<PyTypeChecker List[Union[Tensor, RaggedTensor]]>')

with self.subTest('List[Union[int, np.integer]]'):
    # Note: np.integer is a subtype of int in *some* Python versions.
    checker = dispatch.MakeListChecker(
        dispatch.MakeUnionChecker([int_checker, np_int_checker]))
    self.assertEqual(checker.Check(a), MATCH)
    self.assertEqual(checker.Check(np.array(a)), NO_MATCH)
    self.assertEqual(checker.Check(np.array(a) * 1.5), NO_MATCH)
