# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py

result = json_normalize(
    deep_nested, ["states", "cities"], meta=["country", ["states", "name"]]
)
ex_data = {
    "country": ["USA"] * 4 + ["Germany"] * 3,
    "states.name": [
        "California",
        "California",
        "Ohio",
        "Ohio",
        "Bayern",
        "Nordrhein-Westfalen",
        "Nordrhein-Westfalen",
    ],
    "name": [
        "San Francisco",
        "Los Angeles",
        "Columbus",
        "Cleveland",
        "Munich",
        "Duesseldorf",
        "Koeln",
    ],
    "pop": [12345, 12346, 1234, 1236, 12347, 1238, 1239],
}

expected = DataFrame(ex_data, columns=result.columns)
tm.assert_frame_equal(result, expected)
