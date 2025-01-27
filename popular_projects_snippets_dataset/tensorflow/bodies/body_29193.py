# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/nest_test.py
# A nice messy mix of tuples, lists, dicts, and `OrderedDict`s.
named_tuple = collections.namedtuple("A", ("b", "c"))
mess = (
    "z",
    named_tuple(3, 4),
    {
        "c": (
            1,
            collections.OrderedDict([
                ("b", 3),
                ("a", 2),
            ]),
        ),
        "b": 5
    },
    17
)

flattened = nest.flatten(mess)
self.assertEqual(flattened, ["z", 3, 4, 5, 1, 2, 3, 17])

structure_of_mess = (
    14,
    named_tuple("a", True),
    {
        "c": (
            0,
            collections.OrderedDict([
                ("b", 9),
                ("a", 8),
            ]),
        ),
        "b": 3
    },
    "hi everybody",
)

unflattened = nest.pack_sequence_as(structure_of_mess, flattened)
self.assertEqual(unflattened, mess)

# Check also that the OrderedDict was created, with the correct key order.
unflattened_ordered_dict = unflattened[2]["c"][1]
self.assertIsInstance(unflattened_ordered_dict, collections.OrderedDict)
self.assertEqual(list(unflattened_ordered_dict.keys()), ["b", "a"])
