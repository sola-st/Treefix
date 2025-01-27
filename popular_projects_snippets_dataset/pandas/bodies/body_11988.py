# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
# see gh-3071
parser = all_parsers
data = (
    "posix_timestamp,elapsed,sys,user,queries,query_time,rows,"
    "accountid,userid,contactid,level,silo,method\n"
    "1343103150,0.062353,0,4,6,0.01690,3,"
    "12345,1,-1,3,invoice_InvoiceResource,search\n"
)

result = parser.read_csv(
    StringIO(data),
    index_col=0,
    parse_dates=[0],
    date_parser=lambda x: datetime.utcfromtimestamp(int(x)),
)
expected = DataFrame(
    [
        [
            0.062353,
            0,
            4,
            6,
            0.01690,
            3,
            12345,
            1,
            -1,
            3,
            "invoice_InvoiceResource",
            "search",
        ]
    ],
    columns=[
        "elapsed",
        "sys",
        "user",
        "queries",
        "query_time",
        "rows",
        "accountid",
        "userid",
        "contactid",
        "level",
        "silo",
        "method",
    ],
    index=Index([Timestamp("2012-07-24 04:12:30")], name="posix_timestamp"),
)
tm.assert_frame_equal(result, expected)
