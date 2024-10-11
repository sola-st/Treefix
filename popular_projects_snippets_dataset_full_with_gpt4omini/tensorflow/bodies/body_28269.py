# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
found_warning = False
for warning in caught_warnings:
    if ("Explicitly set the seed in the function if this is not the "
        "intended behavior" in str(warning)):
        found_warning = True
        break
self.assertEqual(found_warning, expected_result)
