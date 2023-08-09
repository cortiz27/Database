import pymysql
import methods

"""
If you type in your password down below after running the SQL Files in the MySQL WorkBench, it should work.
"""

def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="",
        database="ToteDB",
    )

    cur = conn.cursor()

    """
    TEST FOR get_table_name_selection(cursor) - works good, just uncomment to run
    """
    # table_name = methods.get_table_name_selection(cur)
    # cur.execute("SELECT * FROM " + table_name + ";")
    # output = cur.fetchall()
    # for i in output:
    #     print(i)

    """
    TEST FOR get_selected_table_preview(table_name_string, cursor) - works good, just uncomment to run
    """
    # table_name = methods.get_table_name_selection(cur)
    # methods.get_selected_table_preview(table_name, cur)

    """
    TEST FOR enter_data(table_name_string, cursor) - works good, just uncomment to run
    """
    # table_name = methods.get_table_name_selection(cur)
    # methods.print_column_data_format(table_name, cur)
    # methods.enter_data(table_name, cur)

    """
    TEST FOR delete_entry(table_name_string, cursor) - works good, just uncomment to run
    """
    # table_name = methods.get_table_name_selection(cur)
    # methods.delete_entry(table_name, cur)

    """
    TEST FOR update_table(table_name_string, cursor) - works good, just uncomment to run
    """
    # table_name = methods.get_table_name_selection(cur)
    # methods.update_table(table_name, cur)


    """
    TEST FOR view_table(table_name_string, cursor) - works good, just uncomment to run
    """
    # table_name = methods.get_table_name_selection(cur)
    # methods.view_table(table_name, cur)



    """
    BELOW WAS WHAT WAS ORIGINALLY IN THE main.py FILE AT THE BEGINNING
    """
    # cur.execute("SELECT * FROM Users")
    # output = cur.fetchall()
    # print(output)
    # for i in output:
    #     print(i)



    # To close the connection
    conn.close()


# Driver Code
if __name__ == "__main__":
    mysqlconnect()
