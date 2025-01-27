# Extracted from https://stackoverflow.com/questions/625083/what-do-init-and-self-do-in-python
#! /usr/bin/python2

class Person:

    '''Doc - Inside Class '''

    def __init__(self, name):
        '''Doc - __init__ Constructor'''
        self.n_name = name        

    def show(self, n1, n2):
        '''Doc - Inside Show'''
        print self.n_name
        print 'Sum = ', (n1 + n2)

    def __del__(self):
        print 'Destructor Deleting object - ', self.n_name

p=Person('Jay')
p.show(2, 3)
print p.__doc__
print p.__init__.__doc__
print p.show.__doc__

