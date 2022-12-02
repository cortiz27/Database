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

def print_table_size(table_name_string, cursor):
    table_query = "SELECT * FROM " + table_name_string + ";"
    cursor.execute(table_query)
    table_output = cursor.fetchall()
    table_size = str(int(len(table_output)))
    print("Table '" + table_name_string + "' has " + table_size + " rows.")


def enter_data(table_name_string, cursor):
    # This shows the user the size of the table before their data entry
    print_table_size(table_name_string, cursor)

    # The following is the query to get column names and column data type

    table_column_info_query = \
    "SELECT `COLUMN_NAME`, `DATA_TYPE`\
    FROM `INFORMATION_SCHEMA`.`COLUMNS` \
    WHERE `TABLE_SCHEMA`='ToteDB' AND `TABLE_NAME`='" + table_name_string + "';"

    cursor.execute(table_column_info_query)
    table_column_info = cursor.fetchall()

    print("Please enter the following information for a new data entry in " + table_name_string + "\n")

    new_data_entry_query = "INSERT INTO " + table_name_string + " VALUES ("

    cursor.execute("SELECT * FROM " + table_name_string + " LIMIT 1")
    first_row = cursor.fetchall()
    first_row = first_row[0]

    for i, tup in enumerate(table_column_info):
        column_name = tup[0]
        column_data_type = tup[1]
        column_data_format = first_row[i]

        column_value = input(column_name + "(example: " + str(column_data_format) + ") : ")

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

    # This now prints the updated table size
    print_table_size(table_name_string, cursor)

    add_more_condition = input("Would you like to add another entry? (Y/N): ")
    add_more_condition = add_more_condition.strip()
    add_more_condition = add_more_condition.upper()

    if add_more_condition == "Y":
        enter_data(table_name_string, cursor)

def print_column_data_format(table_name_string, cursor):

    table_column_info_query = \
        "SELECT `COLUMN_NAME`, `DATA_TYPE`\
        FROM `INFORMATION_SCHEMA`.`COLUMNS` \
        WHERE `TABLE_SCHEMA`='ToteDB' AND `TABLE_NAME`='" + table_name_string + "';"

    cursor.execute(table_column_info_query)
    table_column_info = cursor.fetchall()

    cursor.execute("SELECT * FROM " + table_name_string + " LIMIT 1")
    first_row = cursor.fetchall()
    first_row = first_row[0]

    out = ""
    column_options_dict = {}
    for i, tup in enumerate(table_column_info):
        # tup = (column_name, data_type_of_column)
        # so column_options_dict = { 1: (column_name1, data_type_of_column1), 2: (column_name2, data_type_of_column2)...}
        column_options_dict[(i+1)] = tup
        column_name = tup[0]
        out += str(i+1) + ") " + column_name + " (i.e: " + str(first_row[i]) + " ) \n"
    print(out)

    return column_options_dict

def select_operator():

    operators_dict = {1: "=", 2: ">", 3: "<", 4: ">=", 5: "<=", 6: "!="}

    print("Operator Options Available: ")

    for key, val in operators_dict.items():
        print(str(key) + ") " + val)

    operator_selection = input("Please select the operator you would like to use from the options listed above: ")


    return  operators_dict[int(operator_selection)]


def get_where_conditions(table_name_string, cursor):
    """
    So WHERE can:
    - have multiple conditions
    - multiple conditions (except last one) are seperated by AND or OR
    - Operators to Handle Include: = , >, <, >=, <=, !=, LIKE (probably the hardest one to handle), BETWEEN, IN
    - Conditions can have several formats, but largely between numeric and string types
    """
    where_string = "WHERE "

    num_of_conditions = input("How many conditions would you like to filter the " + table_name_string + " on?: ")
    num_of_conditions = int(num_of_conditions)

    print("The following output includes the columns and data format for the " + table_name_string + " table, \nplease refer to these numbered options when selecting the column(s) you'd like to filter on: ")

    column_options_dictionary = print_column_data_format(table_name_string, cursor)

    for i in range(num_of_conditions):
        column_choice = input("please enter the column you'd like to set condition " + str(i+1) + " table on: ")
        column_choice = int(column_choice)

        metadata_of_column = column_options_dictionary[column_choice]

        where_string += metadata_of_column[0] + " "# this is the name of the column

        operator = select_operator()

        where_string += operator + " "

        condition = input("Please enter the condition: ")

        if "int" in metadata_of_column[1]:
            # because the value is an int, no quotes needed
            where_string += condition
        else:
            #in this case, column_value is a string type
            quoted_condition = "'"
            quoted_condition += condition
            quoted_condition += "'"
            where_string += quoted_condition + " "



        if i != num_of_conditions-1:
            print("Conjuction Options:")
            print("1) AND")
            print("2) OR")
            conjunction_choice= input("Please enter your conjunction choice: ")
            conjunction_choice = int(conjunction_choice)
            if conjunction_choice == 1:
                where_string += "AND "
            elif conjunction_choice == 2:
                where_string += "OR "

    return where_string



def delete_entry(table_name_string, cursor):

    # So we want to print table size to know that this is working
    print_table_size(table_name_string, cursor)

    # Set up SQL Delete String Query
    delete_data_entry_query = "DELETE FROM " + table_name_string + " "
    delete_data_entry_query += get_where_conditions(table_name_string, cursor)

    cursor.execute(delete_data_entry_query)

    print_table_size(table_name_string, cursor)

def update_table(table_name_string, cursor):
    # so maybe here we first query the where values










    





