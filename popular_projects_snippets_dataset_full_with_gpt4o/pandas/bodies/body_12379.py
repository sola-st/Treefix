# Extracted from ./data/repos/pandas/pandas/tests/io/test_s3.py
# Ensure we can read from a public bucket with credentials
# GH 34626
# Use Amazon Open Data Registry - https://registry.opendata.aws/gdelt

with tm.ensure_safe_environment_variables():
    # temporary workaround as moto fails for botocore >= 1.11 otherwise,
    # see https://github.com/spulec/moto/issues/1924 & 1952
    os.environ.setdefault("AWS_ACCESS_KEY_ID", "foobar_key")
    os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "foobar_secret")
    df = read_csv(
        "s3://gdelt-open-data/events/1981.csv", nrows=5, sep="\t", header=None
    )
    assert len(df) == 5
