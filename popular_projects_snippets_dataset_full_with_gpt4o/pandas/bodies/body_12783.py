# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
# GH 27220
result = json_normalize(
    data=state_data,
    record_path=["counties"],
    meta=["state", "shortname", ["info", "governor"]],
    errors="ignore",
)

ex_data = {
    "name": ["Dade", "Broward", "Palm Beach", "Summit", "Cuyahoga"],
    "population": [12345, 40000, 60000, 1234, 1337],
    "state": ["Florida"] * 3 + ["Ohio"] * 2,
    "shortname": ["FL"] * 3 + ["OH"] * 2,
    "info.governor": ["Rick Scott"] * 3 + ["John Kasich"] * 2,
}

expected = DataFrame(ex_data)
tm.assert_frame_equal(result, expected)
