# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sample.py
# Fixes issue: 2419
# Check behavior of random_state argument
# Check for stability when receives seed or random state -- run 10
# times.

seed = np.random.randint(0, 100)
tm.assert_equal(
    obj.sample(n=4, random_state=seed), obj.sample(n=4, random_state=seed)
)

tm.assert_equal(
    obj.sample(frac=0.7, random_state=seed),
    obj.sample(frac=0.7, random_state=seed),
)

tm.assert_equal(
    obj.sample(n=4, random_state=np.random.RandomState(test)),
    obj.sample(n=4, random_state=np.random.RandomState(test)),
)

tm.assert_equal(
    obj.sample(frac=0.7, random_state=np.random.RandomState(test)),
    obj.sample(frac=0.7, random_state=np.random.RandomState(test)),
)

tm.assert_equal(
    obj.sample(frac=2, replace=True, random_state=np.random.RandomState(test)),
    obj.sample(frac=2, replace=True, random_state=np.random.RandomState(test)),
)

os1, os2 = [], []
for _ in range(2):
    np.random.seed(test)
    os1.append(obj.sample(n=4))
    os2.append(obj.sample(frac=0.7))
tm.assert_equal(*os1)
tm.assert_equal(*os2)
