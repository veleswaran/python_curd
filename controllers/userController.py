import mysql.connector

class UserController:
    def __init__(self):

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin123",
            database="python_crud",
            auth_plugin="mysql_native_password"
        )
        self.db_cursor = self.db.cursor(dictionary=True)

        self.db_cursor = self.db.cursor(dictionary = True)

    # get all users from database
    def get_users(self):
        sql = "select * from users"
        self.db_cursor.execute(sql) 
        return self.db_cursor.fetchall()

    # get all users from database
    def get_user(self,id):
        sql = "select * from users where id = %s"
        self.db_cursor.execute(sql,(id,)) 
        return self.db_cursor.fetchall()

    # add user 
    def add_user(self,name,phone,email,age):
        sql = "insert into users(name,phone,email,age) values (%s,%s,%s,%s)"
        self.db_cursor.execute(sql,(name,phone,email,age))
        self.db.commit()

     # delete user 
    def delete_user(self,id):
        sql = "delete from users where id = %s"
        self.db_cursor.execute(sql,(id,))
        self.db.commit()
 
        # add user 
    def update_user(self,name,phone,email,age,id):
        sql = "update users set name = %s , phone = %s ,email = %s,age = %s where id = %s"
        self.db_cursor.execute(sql,(name,phone,email,age,id))
        self.db.commit()
