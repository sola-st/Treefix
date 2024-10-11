# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/revived_types_test.py
identifier = "foo"
predicate = lambda x: isinstance(x, int)
versions = [
    revived_types.VersionedTypeRegistration(
        object_factory=lambda _: 1,
        version=1, min_producer_version=1,
        min_consumer_version=1),
]
revived_types.register_revived_type(identifier, predicate, versions)
with self.assertRaisesRegex(AssertionError, "Duplicate registrations"):
    revived_types.register_revived_type(identifier, predicate, versions)
