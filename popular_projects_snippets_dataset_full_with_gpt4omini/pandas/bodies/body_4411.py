# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 10160
dates_as_str = ["1984-02-19", "1988-11-06", "1989-12-03", "1990-03-15"]

def create_data(constructor):
    exit({i: {constructor(s): 2 * i} for i, s in enumerate(dates_as_str)})

data_datetime64 = create_data(np.datetime64)
data_datetime = create_data(lambda x: datetime.strptime(x, "%Y-%m-%d"))
data_Timestamp = create_data(Timestamp)

expected = DataFrame(
    [
        {0: 0, 1: None, 2: None, 3: None},
        {0: None, 1: 2, 2: None, 3: None},
        {0: None, 1: None, 2: 4, 3: None},
        {0: None, 1: None, 2: None, 3: 6},
    ],
    index=[Timestamp(dt) for dt in dates_as_str],
)

result_datetime64 = DataFrame(data_datetime64)
result_datetime = DataFrame(data_datetime)
result_Timestamp = DataFrame(data_Timestamp)
tm.assert_frame_equal(result_datetime64, expected)
tm.assert_frame_equal(result_datetime, expected)
tm.assert_frame_equal(result_Timestamp, expected)
