# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
ctx = df.style.set_table_styles(
    [
        {"selector": "th,td", "props": "color:red;"},
        {"selector": "tr", "props": "color:green;"},
    ]
)._translate(True, True)["table_styles"]
assert ctx == [
    {"selector": "th", "props": [("color", "red")]},
    {"selector": "td", "props": [("color", "red")]},
    {"selector": "tr", "props": [("color", "green")]},
]
