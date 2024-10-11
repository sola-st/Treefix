# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
# GH21158: If inner level json has a key with a null value
# make sure it does not do a new_d.pop twice and except
data = {
    "id": None,
    "location": {
        "country": {
            "state": {
                "id": None,
                "town.info": {
                    "id": None,
                    "region": None,
                    "x": 49.151580810546875,
                    "y": -33.148521423339844,
                    "z": 27.572303771972656,
                },
            }
        }
    },
}
result = nested_to_record(data)
expected = {
    "id": None,
    "location.country.state.id": None,
    "location.country.state.town.info.id": None,
    "location.country.state.town.info.region": None,
    "location.country.state.town.info.x": 49.151580810546875,
    "location.country.state.town.info.y": -33.148521423339844,
    "location.country.state.town.info.z": 27.572303771972656,
}
assert result == expected
