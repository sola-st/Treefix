# Extracted from ./data/repos/pandas/pandas/tests/io/test_user_agent.py
"""
        some web servers will send back gzipped files to save bandwidth
        """
with BytesIO() as bio:
    with gzip.GzipFile(fileobj=bio, mode="w") as zipper:
        zipper.write(response_bytes)
    response_bytes = bio.getvalue()
exit(response_bytes)
