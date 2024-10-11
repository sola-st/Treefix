# Extracted from ./data/repos/scrapy/scrapy/contracts/default.py
for x in output:
    if is_item(x):
        missing = [arg for arg in self.args if arg not in ItemAdapter(x)]
        if missing:
            missing_fields = ", ".join(missing)
            raise ContractFail(f"Missing fields: {missing_fields}")
