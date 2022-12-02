def get_table_names(cursor):
    output = []
    cursor.execute("SHOW TABLES;")

    tables = cursor.fetchall()

    for i in tables:
        output.append(str(i[0]))

    return output

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

    operators_dict = {1: "=", 2: ">", 3: "<", 4: ">=", 5: "<=", 6: "!=", 7: " BETWEEN ", 8: " LIKE "}

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

    num_of_conditions = input("How many conditions would you like to filter the " + table_name_string + " table on?: ")
    num_of_conditions = int(num_of_conditions)

    if num_of_conditions == 0:
        where_string = ""

    print("The following output includes the columns and data format for the " + table_name_string + " table, \nplease refer to these numbered options when selecting the column(s) you'd like to filter on: ")

    column_options_dictionary = print_column_data_format(table_name_string, cursor)

    for i in range(num_of_conditions):
        column_choice = input("please enter the column you'd like to filter condition " + str(i+1) + " on: ")
        column_choice = int(column_choice)

        metadata_of_column = column_options_dictionary[column_choice]

        where_string += metadata_of_column[0] + " "# this is the name of the column

        operator = select_operator()

        where_string += operator + " "

        if operator == " BETWEEN ":

            condition1 = input("Please enter lower limit condition: ")
            if "date" in metadata_of_column[1]:
                condition1 = "'" + condition1 + "'"
            where_string += " " + condition1 + " AND "
            condition2 = input("Please enter upper limit condition: ")
            if "date" in metadata_of_column[1]:
                condition2 = "'" + condition2 + "'"
            where_string += " " + condition2 + " "

        elif operator == " LIKE ":

            print("When using LIKE operator to search for a similar string:\
            \n- The percent sign (%) represents zero, one, or multiple characters\
            \n- The underscore sign (_) represents one, single character\
            \n- i.e: _r% - Finds any values that have "r" in the second position")

            string_to_match = input("Please enter the string you'd like to search this condition for: ")
            where_string += " '" + string_to_match + "' "

        else:
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
                where_string += " AND "
            elif conjunction_choice == 2:
                where_string += " OR "
        else:
            where_string += " "

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
    # Update the Table Query
    update_query = "UPDATE " + table_name_string + " "

    # so maybe here we first query the where values
    where_part_of_query = get_where_conditions(table_name_string, cursor)
    where_part_of_query += ";"


    # here are all the rows that match the query before they're updated
    show_filtered_query = "SELECT * FROM " + table_name_string + " " + where_part_of_query
    cursor.execute(show_filtered_query)
    preupdate_output = cursor.fetchall()
    print("\n The following are the rows that match your filters [BEFORE] being updated: ")
    for row in preupdate_output:
        print(row)

    # this is the set portion of the query
    set_part_of_query = "SET "
    print("The following are the columns available in the " + table_name_string + " table: ")
    columns_dict = print_column_data_format(table_name_string, cursor)
    num_of_updates = input("How many columns would you like to update?: ")
    num_of_updates = int(num_of_updates)

    math_operations_dict = {1: "+", 2: "-", 3: "*", 4: "/"}


    for i in range(num_of_updates):
        column_to_update = input("Please select which column you'd like to update for update " + str(i+1) + ": ")
        column_to_update = int(column_to_update)

        column_tuple = columns_dict[column_to_update]
        column_name = column_tuple[0]
        column_data_type = column_tuple[1]
        set_part_of_query += column_name
        set_part_of_query += " = "

        if "int" in column_data_type:
            # because the value is an int, no quotes needed
            scaling_numeric_column_choice = input("Would you like to scale the " + column_name + " column? (Y/N): ")
            scaling_numeric_column_choice = scaling_numeric_column_choice.upper()
            if scaling_numeric_column_choice == "Y":

                set_part_of_query += column_name + " "

                print("These are the following math operations you can use to scale the column: ")
                for key, val in math_operations_dict.items():
                    print(str(key) + ") " + val)
                math_operation_choice = input("Please select which math operation you'd like to use on the " + column_name + " column: ")
                math_operation_choice = int(math_operation_choice)

                set_part_of_query += math_operations_dict[math_operation_choice] + " "

                set_part_of_query += input("Please enter the number you'd like to scale the numeric values in the " + column_name + " column by: ")

            elif scaling_numeric_column_choice == "N":

                set_part_of_query += input("Please enter the number you'd like to change the numeric values in the " + column_name + " column to: " )

        else:
            #in this case, column_value is a string type
            set_part_of_query += "'"
            set_part_of_query += input("Please enter the string you'd like to change the string values in the " + column_name + " column to: " )
            set_part_of_query += "'"

        if i != num_of_updates-1:
            set_part_of_query += ", "
        else:
            set_part_of_query += " "

    update_query += set_part_of_query + where_part_of_query

    cursor.execute(update_query)

    # here are all the rows that match the query after updating
    cursor.execute(show_filtered_query)
    updated_output = cursor.fetchall()
    print("\n The following are the rows that match your filters [AFTER] being updated: ")
    for row in updated_output:
        print(row)

    continue_updating_choice = input("Would you like to continue updating entries for the " + table_name_string + " table?:")
    continue_updating_choice = continue_updating_choice.upper()
    if continue_updating_choice == "Y":
        update_table(table_name_string, cursor)
    elif continue_updating_choice == "N":
        print(table_name_string + " update complete. Thank you.")


def get_select(table_name_string, cursor):

    select_query = "SELECT "

    print("The following output includes the columns and data format for the " + table_name_string + " table, \nplease refer to these numbered options when selecting the column(s) you'd like to view in this query: ")
    columns_metadata = print_column_data_format(table_name_string, cursor)


    aggregating_choice = input("Would you like to calculate any aggregates for this query? (Y/N): ")
    aggregating_choice = aggregating_choice.upper()
    aggregate_functions_dict = {1: "SUM( )", 2: "COUNT( )", 3: "AVG( )", 4: "MIN( )", 5: "MAX( )"}

    if aggregating_choice == "Y":

        aggregate_num_of_cols = input("Over how many columns would you like to group your aggregates by?: ")
        aggregate_num_of_cols = int(aggregate_num_of_cols)
        print("Please enter the numbered column options you'd like group these aggregates by: ")
        for i in range(aggregate_num_of_cols):
            column_agg_choice = input("Group by Column: ")
            col_tup = columns_metadata[int(column_agg_choice)]
            column_name = col_tup[0]
            select_query += column_name
            select_query += ", "

        num_of_aggregated_cols = input("How many columns would you like to perform aggregations on?: ")
        num_of_aggregated_cols = int(num_of_aggregated_cols)

        for i in range(num_of_aggregated_cols):
            col_choice_to_agg = input("Please enter a numbered column option: ")
            col_choice_to_agg = int(col_choice_to_agg)
            col_tup = columns_metadata[col_choice_to_agg]
            column_name = col_tup[0]
            for key, val in aggregate_functions_dict.items():
                print(str(key) + ") " + val)
            agg_func_choice = input("Please enter the numbered choice for the aggregate function you'd like to use on the " + column_name + " column: ")
            agg_func_choice = int(agg_func_choice)
            agg_func = aggregate_functions_dict[agg_func_choice]
            agg_func = agg_func.split()
            select_query += agg_func[0]
            select_query += column_name
            select_query += agg_func[1]
            if i != num_of_aggregated_cols-1:
                select_query += ", "
            else:
                select_query += " "


    elif aggregating_choice == "N":
        num_of_cols = input("How many columns would you like to include in this query?: ")
        num_of_cols = int(num_of_cols)
        print("Please enter the numbered column options you'd like include in this query: ")
        for i in range(num_of_cols):
            col_choice = input("Column to include: ")
            col_tup = columns_metadata[int(col_choice)]
            column_name = col_tup[0]
            select_query += column_name
            if i != num_of_cols-1:
                select_query += ", "
            else:
                select_query += " "

    return select_query, columns_metadata

def get_having(table_name_string, cursor, column_options_dictionary, agg_dict):

    having_query = "HAVING "
    num_of_conditions = input("How many conditions would you like to filter the aggregates on?: ")
    num_of_conditions = int(num_of_conditions)

    for i in range(num_of_conditions):
        column_choice = input("please enter the column you'd like to filter the " + str(i+1) + " aggregate on: ")
        column_choice = int(column_choice)

        metadata_of_column = column_options_dictionary[column_choice]

        column_name= metadata_of_column[0] + " "# this is the name of the column

        for key, val in agg_dict.items():
            print(str(key) + ") " + val)

        agg_func_choice = input("Please enter the numbered choice for the aggregate function you'd like to use on the " + column_name + " column: ")
        agg_func_choice = int(agg_func_choice)
        agg_func = agg_dict[agg_func_choice]
        agg_func = agg_func.split()
        having_query += agg_func[0]
        having_query += column_name
        having_query += agg_func[1]



        operator = select_operator()

        having_query += " " + operator + " "

        condition = input("Please enter the condition to filter aggregate on: ")

        having_query += condition

        if i != num_of_conditions-1:
            print("Conjuction Options:")
            print("1) AND")
            print("2) OR")
            conjunction_choice= input("Please enter your conjunction choice: ")
            conjunction_choice = int(conjunction_choice)
            if conjunction_choice == 1:
                having_query += " AND "
            elif conjunction_choice == 2:
                having_query += " OR "
        else:
            having_query += " "

    return having_query




def view_table(table_name_string, cursor):

    query, columns_metadata = get_select(table_name_string, cursor)

    query += "FROM " + table_name_string + " "

    # you would probably have some sort of join option here

    # get where
    query += get_where_conditions(table_name_string, cursor)

    group_by_num = input("How many columns did you group by?: ")
    group_by_num = int(group_by_num)

    aggregate_functions_dict = {1: "SUM( )", 2: "COUNT( )", 3: "AVG( )", 4: "MIN( )", 5: "MAX( )"}

    if group_by_num > 0:
        query += "GROUP BY "
        for i in range(group_by_num):
            col_to_group_by = input("Please enter the column you'd like to group by: ")
            col_to_group_by = int(col_to_group_by)
            col_tup = columns_metadata[col_to_group_by]
            column_name = col_tup[0]
            query += column_name
            if i != group_by_num-1:
                query += ", "
            else:
                query += " "
        # Having Option Here
        having_choice = input("Would you like to filter any aggregates? (Y/N): ")
        if having_choice == "Y":
            query += get_having(table_name_string, cursor, columns_metadata, aggregate_functions_dict)

    order_by_num = input("How many columns would you like to order your query by?: ")
    order_by_num = int(order_by_num)

    if order_by_num > 0:
        query += "ORDER BY "
        print("Please enter the numbered column options you'd like to order this query by: ")
        for i in range(order_by_num):
            col_choice = input("Column to include: ")
            col_tup = columns_metadata[int(col_choice)]
            column_name = col_tup[0]
            query += column_name + " "
            desc_choice = input("Would you like to order the " + column_name + " column in a descending order? (Y/N): " )
            desc_choice = desc_choice.upper()
            if desc_choice == "Y":
                query += "DESC "
            if i != order_by_num-1:
                query += ", "
            else:
                query += " "

    query += ";"

    print(query)

    cursor.execute(query)
    view = cursor.fetchall()
    if len(view) == 0:
        print("No matching result for this query.")
    for i in view:
        print(i)




























    





