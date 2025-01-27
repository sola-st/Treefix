# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
for i in range(len(objs)):
    for j in range(len(objs)):
        if i == j:
            continue
        self.assertIsNot(objs[i], objs[j])
