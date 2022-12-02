#!/usr/bin/env python3
import time
import methods
import pymysql
from simple_term_menu import TerminalMenu


def main():
    # start connection to database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="Kitten567!",
        database="ToteDB",
    )
    cursor = conn.cursor()

    main_menu_title = "Hello and welcome to Tote!\n  You may press the escape key or select 'Quit' at any time to " \
                      "quit. \n \n Here are the tables we have created: \n "
    # Getting the current names of tables from the sql database
    main_menu_items = methods.get_table_name_selection(cursor)
    main_menu_items.append("Quit")
    main_menu_cursor = "> "
    main_menu_cursor_style = ("fg_red", "bold")
    main_menu_style = ("fg_green", "fg_black", "bold")
    main_menu_exit = False

    main_menu = TerminalMenu(
        menu_entries=main_menu_items,
        title=main_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    table_view_title = "  Table selected.\n  Press Q or Esc to back to main menu. \n\nHere is a preview of this " \
                       "table's data below:  \n\n"
    table_view_items = ["View Table", "Modify Table", "Back to Main Menu"]
    back = False
    table_view_menu = TerminalMenu(
        menu_entries=table_view_items,
        title=table_view_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    while not main_menu_exit:
        main_sel = main_menu.show()

        if main_sel == 0:
            while not back:
                selection = table_view_menu.show()
                # preview = methods.get_selected_table_preview("Users", cursor)
                if selection == 0:
                    print(main_menu_items[0] + " Table View Selected. \n Here is the table's data: \n\n")
                    methods.show_selected_table(main_menu_items[0], cursor)
                    time.sleep(10)
                elif selection == 1:
                    print("Modify Table Selected.\n Would you like to enter, update, or delete data from this table?\n")
                    time.sleep(10)
                elif selection == 2 or selection is None:
                    back = True
                    print("Back Selected")
            back = False
        elif main_sel == 1:
            while not back:
                selection = table_view_menu.show()
                # preview = methods.get_selected_table_preview("Users", cursor)
                if selection == 0:
                    print(main_menu_items[1] + " Table View Selected. \n Here is the table's data: \n\n")
                    methods.show_selected_table(main_menu_items[1], cursor)
                    time.sleep(10)
                elif selection == 1:
                    print("Modify Table Selected.\n Would you like to enter, update, or delete data from this table?\n")
                    time.sleep(10)
                elif selection == 2 or selection is None:
                    back = True
                    print("Back Selected")
            back = False
        elif main_sel == 2:
            while not back:
                selection = table_view_menu.show()
                # preview = methods.get_selected_table_preview("Users", cursor)
                if selection == 0:
                    print(main_menu_items[2] + " Table View Selected. \n Here is the table's data: \n\n")
                    methods.show_selected_table(main_menu_items[2], cursor)
                    time.sleep(10)
                elif selection == 1:
                    print("Modify Table Selected.\n Would you like to enter, update, or delete data from this table?\n")
                    time.sleep(10)
                elif selection == 2 or selection is None:
                    back = True
                    print("Back Selected")
            back = False
        elif main_sel == 3:
            while not back:
                selection = table_view_menu.show()
                # preview = methods.get_selected_table_preview("Users", cursor)
                if selection == 0:
                    print(main_menu_items[3] + " Table View Selected. \n Here is the table's data: \n\n")
                    methods.show_selected_table(main_menu_items[3], cursor)
                    time.sleep(10)
                elif selection == 1:
                    print("Modify Table Selected.\n Would you like to enter, update, or delete data from this table?\n")
                    time.sleep(10)
                elif selection == 2 or selection is None:
                    back = True
                    print("Back Selected")
            back = False
        elif main_sel == 4:
            while not back:
                selection = table_view_menu.show()
                # preview = methods.get_selected_table_preview("Users", cursor)
                if selection == 0:
                    print(main_menu_items[4] + " Table View Selected. \n Here is the table's data: \n\n")
                    methods.show_selected_table(main_menu_items[4], cursor)
                    time.sleep(10)
                elif selection == 1:
                    print("Modify Table Selected.\n Would you like to enter, update, or delete data from this table?\n")
                    time.sleep(10)
                elif selection == 2 or selection is None:
                    back = True
                    print("Back Selected")
            back = False
        elif main_sel == 5:
            while not back:
                selection = table_view_menu.show()
                # preview = methods.get_selected_table_preview("Users", cursor)
                if selection == 0:
                    print(main_menu_items[5] + " Table View Selected. \n Here is the table's data: \n\n")
                    methods.show_selected_table(main_menu_items[5], cursor)
                    time.sleep(10)
                elif selection == 1:
                    print("Modify Table Selected.\n Would you like to enter, update, or delete data from this table?\n")
                    time.sleep(10)
                elif selection == 2 or selection is None:
                    back = True
                    print("Back Selected")
            back = False
        elif main_sel == 6:
            while not back:
                selection = table_view_menu.show()
                # preview = methods.get_selected_table_preview("Users", cursor)
                if selection == 0:
                    print(main_menu_items[6] + " Table View Selected. \n Here is the table's data: \n\n")
                    methods.show_selected_table(main_menu_items[6], cursor)
                    time.sleep(10)
                elif selection == 1:
                    print("Modify Table Selected.\n Would you like to enter, update, or delete data from this table?\n")
                    time.sleep(10)
                elif selection == 2 or selection is None:
                    back = True
                    print("Back Selected")
            back = False
        elif main_sel == 7:
            while not back:
                selection = table_view_menu.show()
                # preview = methods.get_selected_table_preview("Users", cursor)
                if selection == 0:
                    print(main_menu_items[7] + " Table View Selected. \n Here is the table's data: \n\n")
                    methods.show_selected_table(main_menu_items[7], cursor)
                    time.sleep(10)
                elif selection == 1:
                    print("Modify Table Selected.\n Would you like to enter, update, or delete data from this table?\n")
                    time.sleep(10)
                elif selection == 2 or selection is None:
                    back = True
                    print("Back Selected")
            back = False
        elif main_sel == 8:
            while not back:
                selection = table_view_menu.show()
                # preview = methods.get_selected_table_preview("Users", cursor)
                if selection == 0:
                    print(main_menu_items[8] + " Table View Selected. \n Here is the table's data: \n\n")
                    methods.show_selected_table(main_menu_items[8], cursor)
                    time.sleep(10)
                elif selection == 1:
                    print("Modify Table Selected.\n Would you like to enter, update, or delete data from this table?\n")
                    time.sleep(10)
                elif selection == 2 or selection is None:
                    back = True
                    print("Back Selected")
            back = False
        elif main_sel == 9:
            while not back:
                selection = table_view_menu.show()
                # preview = methods.get_selected_table_preview("Users", cursor)
                if selection == 0:
                    print(main_menu_items[9] + " Table View Selected. \n Here is the table's data: \n\n")
                    methods.show_selected_table(main_menu_items[9], cursor)
                    time.sleep(10)
                elif selection == 1:
                    print("Modify Table Selected.\n Would you like to enter, update, or delete data from this table?\n")
                    time.sleep(10)
                elif selection == 2 or selection is None:
                    back = True
                    print("Back Selected")
            back = False
        # if the user selects the last item in the menu set exit to true
        elif main_sel == len(main_menu_items) or main_sel is None:
            main_menu_exit = True
            print("Quit Selected")


# pasted this in here, I think these need to be in the same file...
# ignore my super secure and safe system password :)
def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="Kitten567!",
        database="ToteDB",
    )

    cur = conn.cursor()
    output = gettables(conn)

    # Select query
    # cur.execute("select * from Users")
    # output = cur.fetchall()

    for i in output:
        print(i)

    # To close the connection
    conn.close()


def gettables(conn):
    cur = conn.cursor()
    cur.execute("SHOW TABLES;")
    return cur.fetchall()


if __name__ == "__main__":
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="Kitten567!",
        database="ToteDB",
    )
    cursor = conn.cursor()
    main()
