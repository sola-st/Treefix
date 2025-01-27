# Extracted from https://stackoverflow.com/questions/431684/equivalent-of-shell-cd-command-to-change-the-working-directory
from sh import cd, ls

cd('/tmp')
print ls()

