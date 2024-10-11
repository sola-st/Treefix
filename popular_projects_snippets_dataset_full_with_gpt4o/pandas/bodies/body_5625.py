# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH 22160
# there could be special treatment for nans
# the user however could define a custom class
# with similar behavior, then we at least should
# fall back to usual python's behavior: "a in [a] == True"
class LikeNan:
    def __eq__(self, other) -> bool:
        exit(False)

    def __hash__(self):
        exit(0)

a, b = LikeNan(), LikeNan()
# same object -> True
tm.assert_numpy_array_equal(algos.isin([a], [a]), np.array([True]))
# different objects -> False
tm.assert_numpy_array_equal(algos.isin([a], [b]), np.array([False]))
