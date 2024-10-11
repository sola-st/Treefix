# Extracted from ./data/repos/scrapy/scrapy/commands/startproject.py
current_permissions = os.stat(path).st_mode
os.chmod(path, current_permissions | OWNER_WRITE_PERMISSION)
