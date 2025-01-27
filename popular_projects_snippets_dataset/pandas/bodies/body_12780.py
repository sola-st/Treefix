# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
# GH 22706
data = {
    "state": "Florida",
    "info": {
        "governor": "Rick Scott",
        "counties": [
            {"name": "Dade", "population": 12345},
            {"name": "Broward", "population": 40000},
            {"name": "Palm Beach", "population": 60000},
        ],
    },
}
result = json_normalize(data, record_path=["info", "counties"])
expected = DataFrame(
    [["Dade", 12345], ["Broward", 40000], ["Palm Beach", 60000]],
    columns=["name", "population"],
)
tm.assert_frame_equal(result, expected)
