# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema_ext_dtype.py
# GH#40255
data_json = """{
            "schema":{
                "fields":[
                    {
                        "name":"a",
                        "type":"integer",
                        "extDtype":"Int64"
                    }
                ],
            },
            "data":[
                {
                    "a":2
                },
                {
                    "a":null
                }
            ]
        }"""
result = read_json(data_json, orient="table")
expected = DataFrame({"a": Series([2, NA], dtype="Int64")})
tm.assert_frame_equal(result, expected)
