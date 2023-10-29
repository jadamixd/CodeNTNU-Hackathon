import sqlite3

# Koble til databasen
def connect_to_database(database_name):
    conn = sqlite3.connect(database_name)
    return conn

# Lukk databaseforbindelsen
def close_database_connection(conn):
    conn.close()

# Legg til en kunde i Customers-tabellen
def add_customer(conn, username=0, password=0):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Customers (username, password) VALUES (?, ?)", (username, password))
    conn.commit()

# Legg til en kvittering i Reciept-tabellen
def add_receipt(conn, shopName=0, customerID=0):
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(recieptID) FROM Reciept")
    max_reciept_id = cursor.fetchone()[0]

    # Increment the highest recieptID or set to 1 if no records exist
    if max_reciept_id is not None:
        recieptID = max_reciept_id + 1
    else:
        recieptID = 1
        
    cursor.execute("INSERT INTO Reciept (recieptID, shopName, customerID) VALUES (?, ?)", (recieptID, shopName, customerID))
    conn.commit()

# Legg til et element i ItemInRecipt-tabellen
def add_item_in_receipt(conn, recieptID=0, itemID=0):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ItemInRecipt (recieptID, itemID) VALUES (?, ?)", (recieptID, itemID))
    conn.commit()
    return recieptID

# Legg til et element i Item-tabellen
def add_item(conn, name, weight=0, amount=0, cost=0):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Item (name, weight, amount, cost) VALUES (?, ?, ?, ?)", (name, weight, amount, cost))
    conn.commit()

# Hent alle kvitteringer for en bestemt kunde
def get_receipts_for_customer(conn, customerID=0):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Reciept WHERE customerID = ?", (customerID,))
    return cursor.fetchall()

# Hent alle elementer i en bestemt kvittering
def get_items_in_receipt(conn, recieptID=0):
    cursor = conn.cursor()
    cursor.execute("SELECT i.name, i.weight, i.amount, i.cost FROM Item i JOIN ItemInRecipt ir ON i.itemID = ir.itemID WHERE ir.recieptID = ?", (recieptID,))
    return cursor.fetchall()







"""
# Eksempel på bruk:
if __name__ == "__main__":
    conn = connect_to_database("persistence\data.db")

    # Legg til en kunde
    add_customer(conn, "mister_man", "cbt")

    # Legg til en kvittering
    add_receipt(conn, "Shop X", 1)  # Her antar vi at kundeID er 1

    # Legg til et element i kvitteringen
    add_item_in_receipt(conn, 2, 1)  # Her antar vi at recieptID og itemID er 1

    # Legg til et element
    add_item(conn, "Item A", 100, 5, 10)

    # Hent alle kvitteringer for en kunde
    receipts = get_receipts_for_customer(conn, 1)  # Her antar vi at kundeID er 1
    print("Kvitteringer for kunde 1:", receipts)

    # Hent alle elementer i en kvittering
    items = get_items_in_receipt(conn, 1)  # Her antar vi at recieptID er 1
    print("Elementer i kvittering 1:", items)

    close_database_connection(conn)

"""