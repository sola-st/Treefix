# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# this used to core dump the parser
s = r"""{
        "status": "success",
        "data": {
        "posts": [
            {
            "id": 1,
            "title": "A blog post",
            "body": "Some useful content"
            },
            {
            "id": 2,
            "title": "Another blog post",
            "body": "More content"
            }
           ]
          }
        }"""

read_json(s)
