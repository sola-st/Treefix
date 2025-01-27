# Extracted from https://stackoverflow.com/questions/4256107/running-bash-commands-in-python
import subprocess

args = ['echo', 'Hello!']
subprocess.Popen(args) // same as running `echo Hello!` on cmd line

args2 = ['echo', '-v', '"Hello Again"']
subprocess.Popen(args2) // same as running 'echo -v "Hello Again!"` on cmd line

