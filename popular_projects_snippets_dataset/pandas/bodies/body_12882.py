# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
# GH32383
df = DataFrame(
    {
        "_id": {"row_0": 0},
        "category": {"row_0": "Goods"},
        "recommender_id": {"row_0": 3},
        "recommender_name_jp": {"row_0": "浦田"},
        "recommender_name_en": {"row_0": "Urata"},
        "name_jp": {"row_0": "博多人形（松尾吉将まつお よしまさ）"},
        "name_en": {"row_0": "Hakata Dolls Matsuo"},
    }
)
result1 = pd.read_json(df.to_json())
result2 = DataFrame.from_dict(json.loads(df.to_json()))
tm.assert_frame_equal(result1, df)
tm.assert_frame_equal(result2, df)
