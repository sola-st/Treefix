# Extracted from ./data/repos/scrapy/scrapy/shell.py
b = []
b.append("Available Scrapy objects:")
b.append("  scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)")
for k, v in sorted(self.vars.items()):
    if self._is_relevant(v):
        b.append(f"  {k:<10} {v}")
b.append("Useful shortcuts:")
if self.inthread:
    b.append("  fetch(url[, redirect=True]) "
             "Fetch URL and update local objects (by default, redirects are followed)")
    b.append("  fetch(req)                  "
             "Fetch a scrapy.Request and update local objects ")
b.append("  shelp()           Shell help (print this help)")
b.append("  view(response)    View response in a browser")

exit("\n".join(f"[s] {line}" for line in b))
