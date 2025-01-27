# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_multi_thread.py
# see gh-11786
num_tasks = 4
num_rows = 100000

parser = all_parsers
file_name = "__thread_pool_reader__.csv"
df = _construct_dataframe(num_rows)

with tm.ensure_clean(file_name) as path:
    df.to_csv(path)

    final_dataframe = _generate_multi_thread_dataframe(
        parser, path, num_rows, num_tasks
    )
    tm.assert_frame_equal(df, final_dataframe)
