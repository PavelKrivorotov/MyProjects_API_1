

import psycopg2


def db_connect(func):
    def wrapper(params):
        con = psycopg2.connect(dbname='project_api', user='postgres', password='postgresql')
        cursor = con.cursor()
        ans = func(cursor, params)
        con.commit()
        con.close()
        return ans
    return wrapper


class OAuth():
    @db_connect
    def registration(cursor, params):
        sql = "SELECT * FROM START_REGISTRATION('{}', '{}', '{}', '{}', '{}')".format(*params)
        cursor.execute(sql)
        status = list(cursor)[0][0]
        return status

    @db_connect
    def authentication(cursor, params):
        sql = "SELECT * FROM END_REGISTRATION('{}', '{}', '{}')".format(*params)
        cursor.execute(sql)
        status = list(cursor)[0][0]
        return status

    @db_connect
    def authorisation(cursor, params):
        sql = "SELECT * FROM AUTHORISATION('{}', '{}')".format(*params)
        cursor.execute(sql)
        status = list(cursor)[0][0]
        return status

    @db_connect
    def delete_user(cursor, params):
        sql = "SELECT * FROM DELETE_USER('{}')".format(params)
        cursor.execute(sql)
        status = list(cursor)[0][0]
        return status
    
    @db_connect
    def check_password(cursor, params):
        sql = "SELECT * FROM CHECK_PASSWORD('{}')".format(params)
        cursor.execute(sql)
        hash_pass = list(cursor)[0]
        return hash_pass

    @db_connect
    def session(cursor):
        pass


class User():
    @db_connect
    def create_group(cursor, params):
        sql = "SELECT * FROM CREATE_USERS_GROUP('{}', '{}', '{}')".format(*params)
        cursor.execute(sql)
        status = list(cursor)[0][0]
        return status

    @db_connect
    def delete_group(cursor, params):
        sql = "SELECT * FROM DELETE_USERS_GROUP('{}', '{}')".format(*params)
        cursor.execute(sql)
        status = list(cursor)[0][0]
        return status

    @db_connect
    def add_user(cursor, params):
        sql = "SELECT * FROM ADD_USERS_IN_GROUP('{}', '{}', '{}')".format(*params)
        cursor.execute(sql)
        status = list(cursor)[0][0]
        return status

    @db_connect
    def delete_user(cursor, params):
        sql = "SELECT * FROM DELETE_USERS_IN_GROUP('{}', '{}', '{}')".format(*params)
        cursor.execute(sql)
        status = list(cursor)[0][0]
        return status

    @db_connect
    def add_item(cursor, params):
        sql = "SELECT * FROM ADD_ITEMS_IN_GROUP('{}', '{}', '{}')".format(*params)
        cursor.execute(sql)
        status = list(cursor)[0][0]
        return status

    @db_connect
    def delete_item(cursor, params):
        sql = "SELECT * FROM DELETE_ITEMS_IN_GROUP('{}', '{}', '{}')".format(*params)
        cursor.execute(sql)
        status = list(cursor)[0][0]
        return status

    @db_connect
    def update_data(cursor, params):
        sql = "SELECT * FROM UPDATE_DATA_IN_GROUP('{}', '{}', '{}', {}, {})".format(*params)
        cursor.execute(sql)
        status = list(cursor)[0][0]
        return status

    @db_connect
    def select_items(cursor, params):
        sql = "SELECT * FROM SELECT_ITEMS_IN_GROUP('{}', '{}')".format(*params)
        cursor.execute(sql)
        data = list(cursor)
        return data

    @db_connect
    def select_data(cursor, params):
        sql = "SELECT * FROM SELECT_DATA_IN_GROUP('{}', '{}', '{}')".format(*params)
        cursor.execute(sql)
        data = list(cursor)
        return data