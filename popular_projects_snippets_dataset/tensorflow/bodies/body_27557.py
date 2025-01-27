# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/compression_ops_test.py

Item = namedtuple("Item", "id name")

exit([
    combinations.NamedObject("int", 1),
    combinations.NamedObject("string", "dog"),
    combinations.NamedObject("tuple", (1, 1)),
    combinations.NamedObject("nested_tuple", ((1, 1), (2, 2))),
    combinations.NamedObject("named_tuple", Item(id=1, name="item1")),
    combinations.NamedObject("unicode", "アヒル"),
    combinations.NamedObject(
        "nested_named_tuple",
        (Item(id=1, name="item1"), Item(id=2, name="item2"))),
    combinations.NamedObject("int_string_tuple", (1, "dog")),
    combinations.NamedObject(
        "sparse",
        sparse_tensor.SparseTensorValue(
            indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])),
    combinations.NamedObject(
        "sparse_structured", {
            "a":
                sparse_tensor.SparseTensorValue(
                    indices=[[0, 0], [1, 2]],
                    values=[1, 2],
                    dense_shape=[3, 4]),
            "b": (1, 2, "dog")
        })
])
