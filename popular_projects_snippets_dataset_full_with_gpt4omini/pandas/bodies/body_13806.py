# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# GH 44011
result = df.style.set_table_styles(
    {
        "B": [
            {"selector": "th,td", "props": [("border-left", "2px solid black")]}
        ]
    }
)._translate(True, True)["table_styles"]

expected = [
    {"selector": "th.col1", "props": [("border-left", "2px solid black")]},
    {"selector": "td.col1", "props": [("border-left", "2px solid black")]},
]

assert result == expected
