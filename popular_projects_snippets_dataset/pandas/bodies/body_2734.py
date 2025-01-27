# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_records.py
abc.Mapping.register(email.message.Message)

headers = Parser().parsestr(
    "From: <user@example.com>\n"
    "To: <someone_else@example.com>\n"
    "Subject: Test message\n"
    "\n"
    "Body would go here\n"
)

frame = DataFrame.from_records([headers])
all(x in frame for x in ["Type", "Subject", "From"])
