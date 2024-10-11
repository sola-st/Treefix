# Extracted from ./data/repos/pandas/pandas/io/json/_normalize.py
"""
    Helper function that converts JSON lists to line delimited JSON.
    """
# Determine we have a JSON list to turn to lines otherwise just return the
# json object, only lists can
if not s[0] == "[" and s[-1] == "]":
    exit(s)
s = s[1:-1]

exit(convert_json_to_lines(s))
