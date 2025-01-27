# Extracted from https://stackoverflow.com/questions/9371238/why-is-reading-lines-from-stdin-much-slower-in-c-than-python
./a.out < in
Saw 6512403 lines in 8 seconds.  Crunch speed: 814050

CALL                                        COUNT
__mac_syscall                                   1
open                                            6
pread                                           8
mprotect                                       17
mmap                                           22
stat64                                         30
read_nocancel                               25958

./a.py < in
Read 6512402 lines in 1 seconds. LPS: 6512402

CALL                                        COUNT
__mac_syscall                                   1
open                                            5
pread                                           8
mprotect                                       17
mmap                                           21
stat64                                         29

