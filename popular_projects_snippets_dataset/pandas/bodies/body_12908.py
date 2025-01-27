# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
df_json = """
        {
            "schema":{
                "fields":[
                    {"name":"index","type":"integer"},
                    {"name":"a","type":"string"}
                ],
                "primaryKey":["index"],
                "pandas_version":"0.20.0"
            },
            "data":[
                {"index":0,"a":1},
                {"index":1,"a":2.0},
                {"index":2,"a":"s"}
            ]
        }
        """
expected = DataFrame({"a": [1, 2.0, "s"]})
result = pd.read_json(df_json, orient="table")
tm.assert_frame_equal(expected, result)
