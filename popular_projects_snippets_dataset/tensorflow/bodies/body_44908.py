# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py
object_ids_before = {id(o) for o in gc.get_objects()}
f()
gc.collect()
objects_after = tuple(
    o for o in gc.get_objects() if id(o) not in object_ids_before)
self.assertEmpty(
    tuple(o for o in objects_after if isinstance(o, TestResource)))
