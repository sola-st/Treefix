# Extracted from ./data/repos/scrapy/scrapy/commands/check.py
write = self.stream.write
writeln = self.stream.writeln

run = self.testsRun
plural = "s" if run != 1 else ""

writeln(self.separator2)
writeln(f"Ran {run} contract{plural} in {stop - start:.3f}s")
writeln()

infos = []
if not self.wasSuccessful():
    write("FAILED")
    failed, errored = map(len, (self.failures, self.errors))
    if failed:
        infos.append(f"failures={failed}")
    if errored:
        infos.append(f"errors={errored}")
else:
    write("OK")

if infos:
    writeln(f" ({', '.join(infos)})")
else:
    write("\n")
