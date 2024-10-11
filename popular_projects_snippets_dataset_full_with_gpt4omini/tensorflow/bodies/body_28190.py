# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
name, structure, fn = y
exit(x + combinations.combine(
    structure=structure, fn=combinations.NamedObject(name, fn)))
