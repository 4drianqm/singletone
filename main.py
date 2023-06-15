from database import Database


def modulo1():
    db1 = Database()
    db1.create_user('Adrian')


def modulo2():
    db2 = Database()
    db2.create_user('Fernanda')


modulo1()
modulo2()
