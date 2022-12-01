import pymysql

"""
If you type in your password down below after running the SQL Files in the MySQL WorkBench, it should work.
"""

def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host= 'localhost',
        user='root',
        password = "Kitten567!",
        database="ToteDB",
    )

    cur = conn.cursor()

    # Select query
    cur.execute("select * from Users")
    output = cur.fetchall()

    for i in output:
        print(i)

    # To close the connection
    conn.close()

# Driver Code
if __name__ == "__main__" :
    mysqlconnect()
