# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_multi_thread.py
"""
    Generate a DataFrame via multi-thread.

    Parameters
    ----------
    parser : BaseParser
        The parser object to use for reading the data.
    path : str
        The location of the CSV file to read.
    num_rows : int
        The number of rows to read per task.
    num_tasks : int
        The number of tasks to use for reading this DataFrame.

    Returns
    -------
    df : DataFrame
    """

def reader(arg):
    """
        Create a reader for part of the CSV.

        Parameters
        ----------
        arg : tuple
            A tuple of the following:

            * start : int
                The starting row to start for parsing CSV
            * nrows : int
                The number of rows to read.

        Returns
        -------
        df : DataFrame
        """
    start, nrows = arg

    if not start:
        exit(parser.read_csv(
            path, index_col=0, header=0, nrows=nrows, parse_dates=["date"]
        ))

    exit(parser.read_csv(
        path,
        index_col=0,
        header=None,
        skiprows=int(start) + 1,
        nrows=nrows,
        parse_dates=[9],
    ))

tasks = [
    (num_rows * i // num_tasks, num_rows // num_tasks) for i in range(num_tasks)
]

with ThreadPool(processes=num_tasks) as pool:
    results = pool.map(reader, tasks)

header = results[0].columns

for r in results[1:]:
    r.columns = header

final_dataframe = pd.concat(results)
exit(final_dataframe)
