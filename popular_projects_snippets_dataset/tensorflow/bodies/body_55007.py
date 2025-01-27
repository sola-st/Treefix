# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_dispatcher_test.py
t = constant_op.constant([1, 2, 3])
rt = ragged_factory_ops.constant([[1, 2], [3, 4, 5]])

with self.subTest('int checker'):
    int_checker = dispatch.MakeInstanceChecker(int)
    self.assertEqual(int_checker.Check(3), MATCH)
    self.assertEqual(int_checker.Check(3.0), NO_MATCH)
    self.assertEqual(int_checker.Check(t), NO_MATCH)
    self.assertEqual(int_checker.cost(), 1)
    self.assertEqual(repr(int_checker), '<PyTypeChecker int>')

with self.subTest('tensor checker'):
    tensor_checker = dispatch.MakeInstanceChecker(ops.Tensor)
    self.assertEqual(tensor_checker.Check(t), MATCH)
    self.assertEqual(tensor_checker.Check(3), NO_MATCH)
    self.assertEqual(tensor_checker.Check(3.0), NO_MATCH)
    self.assertEqual(tensor_checker.cost(), 1)
    self.assertEqual(repr(tensor_checker), '<PyTypeChecker Tensor>')

with self.subTest('ragged checker'):
    ragged_checker = dispatch.MakeInstanceChecker(ragged_tensor.RaggedTensor)
    self.assertEqual(ragged_checker.Check(rt), MATCH_DISPATCHABLE)
    self.assertEqual(ragged_checker.Check(3), NO_MATCH)
    self.assertEqual(ragged_checker.Check(t), NO_MATCH)
    self.assertEqual(ragged_checker.cost(), 1)
    self.assertEqual(repr(ragged_checker), '<PyTypeChecker RaggedTensor>')

with self.subTest('int or float checker'):
    int_checker = dispatch.MakeInstanceChecker(int, float)
    self.assertEqual(int_checker.Check(3), MATCH)
    self.assertEqual(int_checker.Check(3.0), MATCH)
    self.assertEqual(int_checker.Check(t), NO_MATCH)
    self.assertEqual(int_checker.cost(), 2)
    self.assertEqual(repr(int_checker), '<PyTypeChecker int, float>')

with self.subTest('subclasses'):

    class A(object):
        pass

    class B(A):
        pass

    class C(object):
        pass

    class D(C, B):
        pass

    checker = dispatch.MakeInstanceChecker(A)
    self.assertEqual(checker.Check(A()), MATCH)
    self.assertEqual(checker.Check(B()), MATCH)
    self.assertEqual(checker.Check(C()), NO_MATCH)
    self.assertEqual(checker.Check(D()), MATCH)
