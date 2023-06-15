from database import Database


def modulo1():
    db1 = Database()
    # db1.create_user('Adrian')
    return db1


def modulo2():
    db2 = Database()
    # db2.create_user('Fernanda')
    return db2


db_a = modulo1()
db_b = modulo2()

if id(db_a) == id(db_b):
    print('the instances are the same')
else:
    print('the instances are different')
