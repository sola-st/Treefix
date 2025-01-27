# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_compression.py
uncompressed_path = datapath("io", "json", "data", "tsframe_v012.json")
uncompressed_df = pd.read_json(uncompressed_path)

compressed_path = datapath("io", "json", "data", "tsframe_v012.json.zip")
compressed_df = pd.read_json(compressed_path, compression="zip")

tm.assert_frame_equal(uncompressed_df, compressed_df)
