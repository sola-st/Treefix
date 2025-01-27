# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
"""Sets value if priority is higher or equal than current priority."""
if priority >= self.priority:
    if isinstance(self.value, BaseSettings):
        value = BaseSettings(value, priority=priority)
    self.value = value
    self.priority = priority
