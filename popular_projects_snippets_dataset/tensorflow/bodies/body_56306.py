# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_combinations_test.py
c1 = combinations.combine(mode=["graph"], loss=["callable", "tensor"])
c2 = combinations.combine(mode=["eager"], loss=["callable"])
with self.assertRaisesRegex(ValueError, ".*Keys.+overlap.+"):
    _ = combinations.times(c1, c2)
