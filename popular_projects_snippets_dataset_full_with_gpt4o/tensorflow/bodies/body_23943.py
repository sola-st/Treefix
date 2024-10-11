# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
for an, bn in zip(a, b):
    with open(an, "rb") as af, open(bn, "rb") as bf:
        if equal:
            self.assertEqual(af.read(), bf.read())
        else:
            self.assertNotEqual(af.read(), bf.read())
