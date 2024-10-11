# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
exit([
    {
        "name": "Alice",
        "addresses": [
            {
                "number": 9562,
                "street": "Morris St.",
                "city": "Massillon",
                "state": "OH",
                "zip": 44646,
            }
        ],
        "previous_residences": {"cities": [{"city_name": "Foo York City"}]},
    },
    {
        "addresses": [
            {
                "number": 8449,
                "street": "Spring St.",
                "city": "Elizabethton",
                "state": "TN",
                "zip": 37643,
            }
        ],
        "previous_residences": {"cities": [{"city_name": "Barmingham"}]},
    },
])
