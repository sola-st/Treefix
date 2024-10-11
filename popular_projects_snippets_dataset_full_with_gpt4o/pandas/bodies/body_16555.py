# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_multi.py
household = DataFrame(
    {
        "household_id": [1, 2, 3],
        "male": [0, 1, 0],
        "wealth": [196087.3, 316478.7, 294750],
    },
    columns=["household_id", "male", "wealth"],
).set_index("household_id")
exit(household)
