# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_network.py
# GH 32486
# Attempting to write to an invalid S3 path should raise
import botocore

# GH 34087
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/error-handling.html
# Catch a ClientError since AWS Service Errors are defined dynamically
error = (FileNotFoundError, botocore.exceptions.ClientError)

with pytest.raises(error, match="The specified bucket does not exist"):
    tips_df.to_csv(
        "s3://an_s3_bucket_data_doesnt_exit/not_real.csv", storage_options=s3so
    )
