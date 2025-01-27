# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
# GH23843: Enhanced JSON normalize
max_level = 100
input_data = [
    {
        "CreatedBy": {
            "user": {
                "name": {"firstname": "Leo", "LastName": "Thomson"},
                "family_tree": {
                    "father": {
                        "name": "Father001",
                        "father": {
                            "Name": "Father002",
                            "father": {
                                "name": "Father003",
                                "father": {"Name": "Father004"},
                            },
                        },
                    }
                },
            }
        }
    }
]
expected = [
    {
        "CreatedBy.user.name.firstname": "Leo",
        "CreatedBy.user.name.LastName": "Thomson",
        "CreatedBy.user.family_tree.father.name": "Father001",
        "CreatedBy.user.family_tree.father.father.Name": "Father002",
        "CreatedBy.user.family_tree.father.father.father.name": "Father003",
        "CreatedBy.user.family_tree.father.father.father.father.Name": "Father004",  # noqa: E501
    }
]
output = nested_to_record(input_data, max_level=max_level)
assert output == expected
