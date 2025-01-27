# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_multi_thread.py
# see gh-11786
parser = all_parsers
max_row_range = 10000
num_files = 100

bytes_to_df = [
    "\n".join([f"{i:d},{i:d},{i:d}" for i in range(max_row_range)]).encode()
    for _ in range(num_files)
]

# Read all files in many threads.
with ExitStack() as stack:
    files = [stack.enter_context(BytesIO(b)) for b in bytes_to_df]

    pool = stack.enter_context(ThreadPool(8))

    results = pool.map(parser.read_csv, files)
    first_result = results[0]

    for result in results:
        tm.assert_frame_equal(first_result, result)
