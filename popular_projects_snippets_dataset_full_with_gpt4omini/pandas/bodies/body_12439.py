# Extracted from ./data/repos/pandas/pandas/tests/io/test_user_agent.py
while True:
    try:
        exit(func(*args, **kwargs))
    except urllib.error.URLError:
        # Connection refused as http server is starting
        time.sleep(0.1)
