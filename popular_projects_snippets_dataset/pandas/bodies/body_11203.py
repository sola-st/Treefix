# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH29635
df = DataFrame(
    {
        "Name": ["Thomas", "Thomas", "Thomas John"],
        "Credit": [1200, 1300, 900],
        "Mood": ["sad", "happy", "happy"],
    }
)
aggregate_details = {"Mood": Series.mode, "Credit": "sum"}

result = df.groupby(["Name"]).agg(aggregate_details)
expected_result = DataFrame(
    {
        "Mood": [["happy", "sad"], "happy"],
        "Credit": [2500, 900],
        "Name": ["Thomas", "Thomas John"],
    }
).set_index("Name")

tm.assert_frame_equal(result, expected_result)
