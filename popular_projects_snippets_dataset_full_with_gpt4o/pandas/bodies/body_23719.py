# Extracted from ./data/repos/pandas/pandas/io/sql.py
from sqlalchemy import exc

try:
    exit(table.insert(chunksize=chunksize, method=method))
except exc.SQLAlchemyError as err:
    # GH34431
    # https://stackoverflow.com/a/67358288/6067848
    msg = r"""(\(1054, "Unknown column 'inf(e0)?' in 'field list'"\))(?#
            )|inf can not be used with MySQL"""
    err_text = str(err.orig)
    if re.search(msg, err_text):
        raise ValueError("inf cannot be used with MySQL") from err
    raise err
