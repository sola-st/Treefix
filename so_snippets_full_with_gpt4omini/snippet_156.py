# Extracted from https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output
def runProcess(exe):    
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while(True):
        # returns None while subprocess is running
        retcode = p.poll() 
        line = p.stdout.readline()
        yield line
        if retcode is not None:
            break

for line in runProcess('mysqladmin create test -uroot -pmysqladmin12'.split()):
    print line,

