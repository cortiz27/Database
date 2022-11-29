def get_table_name_selection(cursor):
    """
    :param cursor: we pass in the cursor connected to the database
    :return: the string for the table name of the table selected is returned
    """

    tables_dictionary = {}

    cursor.execute("SHOW TABLES;")

    # tables seems to be a list of tuples with strings of table names i.e [('User'), ('Market), ...]
    tables = cursor.fetchall()

    for i, table in enumerate(tables):
        table_name = table[0]
        tables_dictionary[i] = table_name
        print(str(i+1) + ") " + table_name)

    user_table_selection = input("Enter Table Number: ")
    user_table_selection = int(user_table_selection.strip())
    user_table_selection = user_table_selection - 1

    return tables_dictionary[user_table_selection]


def get_selected_table_preview(table_name_string, cursor):

    preview_query = "SELECT * FROM " + table_name_string + " LIMIT 3;"

    cursor.execute(preview_query)

    # Rough Draft of Output format

    preview = cursor.fetchall()

    for i in preview:
        print(i)

def enter_data(table_name_string, cursor):

    table_query = "SELECT * FROM " + table_name_string + ";"

    # This shows the user the size of the table before their data entry
    cursor.execute(table_query)
    table_output = cursor.fetchall()
    table_size = str(int(len(table_output)))
    print("Table '" + table_name_string + "' has " + table_size + " rows.")

    # The following is the query to get column names and column data type

    table_column_info_query = \
    "SELECT `COLUMN_NAME`, `DATA_TYPE`\
    FROM `INFORMATION_SCHEMA`.`COLUMNS` \
    WHERE `TABLE_SCHEMA`='ToteDB' AND `TABLE_NAME`='" + table_name_string + "';"

    cursor.execute(table_column_info_query)
    table_column_info = cursor.fetchall()

    print("Please enter the following information for a new data entry in " + table_name_string + "\n")

    new_data_entry_query = "INSERT INTO " + table_name_string + " VALUES ("

    for i, tup in enumerate(table_column_info):
        column_name = tup[0]
        column_data_type = tup[1]

        column_value = input(column_name + "(type: " + column_data_type + ") : ")

        # The following is a very preliminary way to figure out how to create the data entry query based on column data type
        if "int" in column_data_type:
            # because the value is an int, no quotes needed
            new_data_entry_query += column_value
            if i != len(table_column_info)-1:
                new_data_entry_query += ", "
        else:
            #in this case, column_value is a string type
            new_data_entry_query += "'"
            new_data_entry_query += column_value
            new_data_entry_query += "'"
            if i != len(table_column_info)-1:
                new_data_entry_query += ", "

    new_data_entry_query += ");"

    cursor.execute(new_data_entry_query)
    cursor.execute(table_query)
    table_output = cursor.fetchall()
    table_size = str(int(len(table_output)))
    print("Table '" + table_name_string + "' NOW has " + table_size + " rows.")





    





