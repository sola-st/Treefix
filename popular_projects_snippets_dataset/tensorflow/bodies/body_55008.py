# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_dispatcher_test.py
checker = dispatch.MakeInstanceChecker(tuple)
MyTuple = collections.namedtuple('MyTuple', ['a', 'b'])  # Subclass of tuple

self.assertEqual(checker.cache_size(), 0)
self.assertEqual(checker.Check(5), NO_MATCH)
self.assertEqual(checker.cache_size(), 1)  # cache miss
self.assertEqual(checker.Check(12), NO_MATCH)
self.assertEqual(checker.cache_size(), 1)  # cache hit
self.assertEqual(checker.Check(1.3), NO_MATCH)
self.assertEqual(checker.cache_size(), 2)  # cache miss
self.assertEqual(checker.Check([1]), NO_MATCH)
self.assertEqual(checker.cache_size(), 3)  # cache miss
self.assertEqual(checker.Check((1,)), MATCH)
self.assertEqual(checker.cache_size(), 4)  # cache miss
self.assertEqual(checker.Check((1, 2, 3)), MATCH)
self.assertEqual(checker.cache_size(), 4)  # cache hit
self.assertEqual(checker.Check(MyTuple(1, 2)), MATCH)
self.assertEqual(checker.cache_size(), 5)  # cache miss
self.assertEqual(checker.Check(MyTuple(3, 4)), MATCH)
self.assertEqual(checker.cache_size(), 5)  # cache miss
self.assertEqual(checker.Check(()), MATCH)
self.assertEqual(checker.cache_size(), 5)  # cache hit
