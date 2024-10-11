# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 10160
td_as_int = [1, 2, 3, 4]

data = {i: {klass(s): 2 * i} for i, s in enumerate(td_as_int)}

expected = DataFrame(
    [
        {0: 0, 1: None, 2: None, 3: None},
        {0: None, 1: 2, 2: None, 3: None},
        {0: None, 1: None, 2: 4, 3: None},
        {0: None, 1: None, 2: None, 3: 6},
    ],
    index=[Timedelta(td, "D") for td in td_as_int],
)

result = DataFrame(data)

tm.assert_frame_equal(result, expected)
