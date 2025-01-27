# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_dispatcher_test.py
int_checker = dispatch.MakeInstanceChecker(int)
float_checker = dispatch.MakeInstanceChecker(float)
str_checker = dispatch.MakeInstanceChecker(str)
none_checker = dispatch.MakeInstanceChecker(type(None))
tensor_checker = dispatch.MakeInstanceChecker(ops.Tensor)
ragged_checker = dispatch.MakeInstanceChecker(ragged_tensor.RaggedTensor)

t = constant_op.constant([1, 2, 3])
rt = ragged_factory_ops.constant([[1, 2], [3, 4, 5]])

with self.subTest('Union[int, float, str]'):
    checker = dispatch.MakeUnionChecker(
        [int_checker, float_checker, str_checker])
    self.assertEqual(checker.Check(3), MATCH)
    self.assertEqual(checker.Check(3.0), MATCH)
    self.assertEqual(checker.Check('x'), MATCH)
    self.assertEqual(checker.Check('x'), MATCH)
    self.assertEqual(checker.Check(None), NO_MATCH)
    self.assertEqual(checker.Check(t), NO_MATCH)
    self.assertEqual(checker.cost(), 4)
    self.assertEqual(repr(checker), '<PyTypeChecker Union[int, float, str]>')

with self.subTest('Optional[int] (aka Union[int, None])'):
    checker = dispatch.MakeUnionChecker([int_checker, none_checker])
    self.assertEqual(checker.Check(3), MATCH)
    self.assertEqual(checker.Check(3.0), NO_MATCH)
    self.assertEqual(checker.Check(None), MATCH)
    self.assertEqual(checker.Check(t), NO_MATCH)
    self.assertEqual(checker.cost(), 3)
    self.assertEqual(repr(checker), '<PyTypeChecker Union[int, NoneType]>')

with self.subTest('Union[Tensor, RaggedTensor]'):
    checker = dispatch.MakeUnionChecker([tensor_checker, ragged_checker])
    self.assertEqual(checker.Check(3), NO_MATCH)
    self.assertEqual(checker.Check(3.0), NO_MATCH)
    self.assertEqual(checker.Check(None), NO_MATCH)
    self.assertEqual(checker.Check(t), MATCH)
    self.assertEqual(checker.Check(rt), MATCH_DISPATCHABLE)
    self.assertEqual(checker.cost(), 3)
    self.assertEqual(
        repr(checker), '<PyTypeChecker Union[Tensor, RaggedTensor]>')
