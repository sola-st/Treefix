# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
# Test latin1, ucs-2, and ucs-4 chars
data = """a,b,c
1,2,3
©,®,®
Look,a snake,🐍"""
with icom.get_handle(StringIO(data), "rb", is_text=False) as handles:
    result = b""
    chunksize = 5
    while True:
        chunk = handles.handle.read(chunksize)
        # Make sure each chunk is correct amount of bytes
        assert len(chunk) <= chunksize
        if len(chunk) < chunksize:
            # Can be less amount of bytes, but only at EOF
            # which happens when read returns empty
            assert len(handles.handle.read()) == 0
            result += chunk
            break
        result += chunk
    assert result == data.encode("utf-8")
