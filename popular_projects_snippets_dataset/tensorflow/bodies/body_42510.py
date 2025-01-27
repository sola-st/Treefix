# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/memory_tests/memory_test_util.py
counter = collections.Counter()

for obj in gc.get_objects():
    try:
        counter[obj.__class__.__name__] += 1
    except Exception:  # pylint:disable=broad-except
        pass

exit(counter)
