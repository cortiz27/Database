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
    main_menu_items = methods.get_table_names(cursor)
    #main_menu_items.append("Quit")
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

    method_menu_title = "Modify Menu Selected.\n Would you like to update, enter or delete?" \
                        "\n  Press Q or Esc to back to main menu. \n\n"
    method_menu_items = ["Enter Data", "Update Data", "Delete Data", "Back"]
    method_back = False
    methods_menu = TerminalMenu(
        menu_entries=method_menu_items,
        title=method_menu_title,
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
                if selection == 0:
                    print("Markets Table View Selected. \n\n")
                    print("Here is a preview of this tables data and format below: \n")
                    methods.get_selected_table_preview("Markets", cursor)
                    print("\n\n")
                    methods.view_table("Markets", cursor)
                    time.sleep(10)
                elif selection == 1:
                    while not method_back:
                        methodselect = methods_menu.show()
                        if methodselect == 0:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("Markets", cursor)
                            print("\n\n")
                            methods.enter_data("Markets", cursor)
                            time.sleep(10)
                        elif methodselect == 1:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("Markets", cursor)
                            print("\n\n")
                            methods.update_table("Markets", cursor)
                            time.sleep(10)
                        elif methodselect == 2:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("Markets", cursor)
                            print("\n\n")
                            methods.delete_entry("Markets", cursor)
                            time.sleep(10)
                        elif methodselect == 3 or methodselect is None:
                            method_back = True
                            print("back selected")
                elif selection == 2 or selection is None:
                    back = True
                    print("Back Selected")
            back = False
        elif main_sel == 1:
            while not back:
                selection = table_view_menu.show()
                if selection == 0:
                    print("MarketStores Table View Selected. \n\n")
                    print("Here is a preview of this tables data and format below: \n")
                    methods.get_selected_table_preview("MarketStores", cursor)
                    print("\n\n")
                    methods.view_table("MarketStores", cursor)
                    time.sleep(10)
                elif selection == 1:
                    while not method_back:
                        methodselect = methods_menu.show()
                        if methodselect == 0:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("MarketStores", cursor)
                            print("\n\n")
                            methods.enter_data("MarketStores", cursor)
                            time.sleep(10)
                        elif methodselect == 1:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("MarketStores", cursor)
                            print("\n\n")
                            methods.update_table("MarketStores", cursor)
                            time.sleep(10)
                        elif methodselect == 2:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("MarketStores", cursor)
                            print("\n\n")
                            methods.delete_entry("MarketStores", cursor)
                            time.sleep(10)
                        elif methodselect == 3 or methodselect is None:
                            method_back = True
                            print("back selected")
                elif selection == 2 or selection is None:
                    back = True
                    print("Back Selected")
            back = False
        elif main_sel == 2:
            while not back:
                selection = table_view_menu.show()
                if selection == 0:
                    print("Products Table View Selected. \n\n")
                    print("Here is a preview of this tables data and format below: \n")
                    methods.get_selected_table_preview("Products", cursor)
                    print("\n\n")
                    methods.view_table("Products", cursor)
                    time.sleep(10)
                elif selection == 1:
                    while not method_back:
                        methodselect = methods_menu.show()
                        if methodselect == 0:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("Products", cursor)
                            print("\n\n")
                            methods.enter_data("Products", cursor)
                            time.sleep(10)
                        elif methodselect == 1:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("Products", cursor)
                            print("\n\n")
                            methods.update_table("Products", cursor)
                            time.sleep(10)
                        elif methodselect == 2:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("Products", cursor)
                            print("\n\n")
                            methods.delete_entry("Products", cursor)
                            time.sleep(10)
                        elif methodselect == 3 or methodselect is None:
                            method_back = True
                            print("back selected")
                elif selection == 2 or selection is None:
                    back = True
                    print("Back Selected")
            back = False
        elif main_sel == 3:
            while not back:
                selection = table_view_menu.show()
                if selection == 0:
                    print("ProductsTransactions Table View Selected. \n\n")
                    print("Here is a preview of this tables data and format below: \n")
                    methods.get_selected_table_preview("ProductsTransactions", cursor)
                    print("\n\n")
                    methods.view_table("ProductsTransactions", cursor)
                    time.sleep(10)
                elif selection == 1:
                    while not method_back:
                        methodselect = methods_menu.show()
                        if methodselect == 0:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("ProductsTransactions", cursor)
                            print("\n\n")
                            methods.enter_data("ProductsTransactions", cursor)
                            time.sleep(10)
                        elif methodselect == 1:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("ProductsTransactions", cursor)
                            print("\n\n")
                            methods.update_table("ProductsTransactions", cursor)
                            time.sleep(10)
                        elif methodselect == 2:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("ProductsTransactions", cursor)
                            print("\n\n")
                            methods.delete_entry("ProductsTransactions", cursor)
                            time.sleep(10)
                        elif methodselect == 3 or methodselect is None:
                            method_back = True
                            print("back selected")
                elif selection == 2 or selection is None:
                    back = True
                    print("Back Selected")
            back = False
        elif main_sel == 4:
            while not back:
                selection = table_view_menu.show()
                if selection == 0:
                    print("Properties Table View Selected. \n\n")
                    print("Here is a preview of this tables data and format below: \n")
                    methods.get_selected_table_preview("Properties", cursor)
                    print("\n\n")
                    methods.view_table("Properties", cursor)
                    time.sleep(10)
                elif selection == 1:
                    while not method_back:
                        methodselect = methods_menu.show()
                        if methodselect == 0:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("Properties", cursor)
                            print("\n\n")
                            methods.enter_data("Properties", cursor)
                            time.sleep(10)
                        elif methodselect == 1:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("Properties", cursor)
                            print("\n\n")
                            methods.update_table("Properties", cursor)
                            time.sleep(10)
                        elif methodselect == 2:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("Properties", cursor)
                            print("\n\n")
                            methods.delete_entry("Properties", cursor)
                            time.sleep(10)
                        elif methodselect == 3 or methodselect is None:
                            method_back = True
                            print("back selected")
                elif selection == 2 or selection is None:
                    back = True
                    print("Back Selected")
            back = False
        elif main_sel == 5:
            while not back:
                selection = table_view_menu.show()
                if selection == 0:
                    print("Stores Table View Selected. \n\n")
                    print("Here is a preview of this tables data and format below: \n")
                    methods.get_selected_table_preview("Stores", cursor)
                    print("\n\n")
                    methods.view_table("Stores", cursor)
                    time.sleep(10)
                elif selection == 1:
                    while not method_back:
                        methodselect = methods_menu.show()
                        if methodselect == 0:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("Stores", cursor)
                            print("\n\n")
                            methods.enter_data("Stores", cursor)
                            time.sleep(10)
                        elif methodselect == 1:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("Stores", cursor)
                            print("\n\n")
                            methods.update_table("Stores", cursor)
                            time.sleep(10)
                        elif methodselect == 2:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("Stores", cursor)
                            print("\n\n")
                            methods.delete_entry("Stores", cursor)
                            time.sleep(10)
                        elif methodselect == 3 or methodselect is None:
                            method_back = True
                            print("back selected")
                elif selection == 2 or selection is None:
                    back = True
                    print("Back Selected")
            back = False
        elif main_sel == 6:
            while not back:
                selection = table_view_menu.show()
                if selection == 0:
                    print("Transactions Table View Selected. \n\n")
                    print("Here is a preview of this tables data and format below: \n")
                    methods.get_selected_table_preview("Transactions", cursor)
                    print("\n\n")
                    methods.view_table("Transactions", cursor)
                    time.sleep(10)
                elif selection == 1:
                    while not method_back:
                        methodselect = methods_menu.show()
                        if methodselect == 0:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("Transactions", cursor)
                            print("\n\n")
                            methods.enter_data("Transactions", cursor)
                            time.sleep(10)
                        elif methodselect == 1:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("Transactions", cursor)
                            print("\n\n")
                            methods.update_table("Transactions", cursor)
                            time.sleep(10)
                        elif methodselect == 2:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("Transactions", cursor)
                            print("\n\n")
                            methods.delete_entry("Transactions", cursor)
                            time.sleep(10)
                        elif methodselect == 3 or methodselect is None:
                            method_back = True
                            print("back selected")
                elif selection == 2 or selection is None:
                    back = True
                    print("Back Selected")
            back = False
        elif main_sel == 7:
            while not back:
                selection = table_view_menu.show()
                if selection == 0:
                    print("UserProperties Table View Selected. \n\n")
                    print("Here is a preview of this tables data and format below: \n")
                    methods.get_selected_table_preview("UserProperties", cursor)
                    print("\n\n")
                    methods.view_table("UserProperties", cursor)
                    time.sleep(10)
                elif selection == 1:
                    while not method_back:
                        methodselect = methods_menu.show()
                        if methodselect == 0:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("UserProperties", cursor)
                            print("\n\n")
                            methods.enter_data("UserProperties", cursor)
                            time.sleep(10)
                        elif methodselect == 1:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("UserProperties", cursor)
                            print("\n\n")
                            methods.update_table("UserProperties", cursor)
                            time.sleep(10)
                        elif methodselect == 2:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("UserProperties", cursor)
                            print("\n\n")
                            methods.delete_entry("UserProperties", cursor)
                            time.sleep(10)
                        elif methodselect == 3 or methodselect is None:
                            method_back = True
                            print("back selected")
                elif selection == 2 or selection is None:
                    back = True
                    print("Back Selected")
            back = False
        elif main_sel == 8:
            while not back:
                selection = table_view_menu.show()
                if selection == 0:
                    print("Users Table View Selected. \n\n")
                    print("Here is a preview of this tables data and format below: \n")
                    methods.get_selected_table_preview("Users", cursor)
                    print("\n\n")
                    methods.view_table("Users", cursor)
                    time.sleep(10)
                elif selection == 1:
                    while not method_back:
                        methodselect = methods_menu.show()
                        if methodselect == 0:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("Users", cursor)
                            print("\n\n")
                            methods.enter_data("Users", cursor)
                            time.sleep(10)
                        elif methodselect == 1:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("Users", cursor)
                            print("\n\n")
                            methods.update_table("Users", cursor)
                            time.sleep(10)
                        elif methodselect == 2:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("Users", cursor)
                            print("\n\n")
                            methods.delete_entry("Users", cursor)
                            time.sleep(10)
                        elif methodselect == 3 or methodselect is None:
                            method_back = True
                            print("back selected")
                elif selection == 2 or selection is None:
                    back = True
                    print("Back Selected")
            back = False
        elif main_sel == 9:
            while not back:
                selection = table_view_menu.show()
                if selection == 0:
                    print("UserStores Table View Selected. \n\n")
                    print("Here is a preview of this tables data and format below: \n")
                    methods.get_selected_table_preview("UserStores", cursor)
                    print("\n\n")
                    methods.view_table("UserStores", cursor)
                    time.sleep(10)
                elif selection == 1:
                    while not method_back:
                        methodselect = methods_menu.show()
                        if methodselect == 0:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("UserStores", cursor)
                            print("\n\n")
                            methods.enter_data("UserStores", cursor)
                            time.sleep(10)
                        elif methodselect == 1:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("UserStores", cursor)
                            print("\n\n")
                            methods.update_table("UserStores", cursor)
                            time.sleep(10)
                        elif methodselect == 2:
                            print("Here is a preview of this tables data and format below: \n")
                            methods.get_selected_table_preview("UserStores", cursor)
                            print("\n\n")
                            methods.delete_entry("UserStores", cursor)
                            time.sleep(10)
                        elif methodselect == 3 or methodselect is None:
                            method_back = True
                            print("back selected")
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
    output = methods.get_table_names(cursor)
    for i in output:
        print(i)