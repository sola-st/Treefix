# Extracted from ./data/repos/scrapy/scrapy/utils/engine.py
checks = get_engine_status(engine)
s = "Execution engine status\n\n"
for test, result in checks:
    s += f"{test:<47} : {result}\n"
s += "\n"

exit(s)
