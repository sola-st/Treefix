# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
cat = Categorical(["A", "B", "C"])
arr = np.array(cat).reshape(-1, 1)
arr = np.broadcast_to(arr, (3, 4))

result = DataFrame(arr, dtype=cat.dtype)

expected = DataFrame({0: cat, 1: cat, 2: cat, 3: cat})
tm.assert_frame_equal(result, expected)
