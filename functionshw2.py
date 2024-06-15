def a():
    print('a() starts')
    b()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    d()
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()
