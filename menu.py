#!/usr/bin/env python3
import time

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

    main_menu_title = "Hello and welcome to Tote!\n  You may press the escape key or select 'Quit' at any time to " \
                      "quit. \n \n Here are the tables we have created: \n "
    main_menu_items = ["Markets", "Market Stores", "Products", "Products Transactions", "Properties", "Stores",
                       "Transactions", "User Properties", "Users", "User Stores", "Quit"]
    # main_menu_items = gettables(conn)
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

    edit_menu_title = "  Edit Menu.\n  Press Q or Esc to back to main menu. \n"
    edit_menu_items = ["Edit Config", "Save Settings", "Back to Main Menu"]
    edit_menu_back = False
    edit_menu = TerminalMenu(
        edit_menu_items,
        title=edit_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    while not main_menu_exit:
        main_sel = main_menu.show()

        if main_sel == 0:
            while not edit_menu_back:
                edit_sel = edit_menu.show()
                if edit_sel == 0:
                    print("Edit Config Selected")
                    time.sleep(5)
                elif edit_sel == 1:
                    print("Save Selected")
                    time.sleep(5)
                elif edit_sel == 2 or edit_sel is None:
                    edit_menu_back = True
                    print("Back Selected")
            edit_menu_back = False
        elif main_sel == 1:
            print("option 2 selected")
            time.sleep(5)
        elif main_sel == 2:
            print("option 3 selected")
            time.sleep(5)
        # if the user selects the last item in the menu set exit to true
        elif main_sel == main_menu_items.len() or main_sel is None:
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
    main()
