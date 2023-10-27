CREATE TABLE Customers (
    customerID  integer,
    username    varchar(30),
    password    varchar(255),

    CONSTRAINT Customers_pk PRIMARY KEY (customerID)
);

CREATE TABLE Reciept (
    recieptID   integer,
    shopName    varchar(50),
    customerID  integer, -- Added a comma here

    CONSTRAINT Reciept_pk PRIMARY KEY (recieptID),
    CONSTRAINT Reciept_fk FOREIGN KEY (customerID) REFERENCES Customers(customerID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE ItemInRecipt (
    recieptID   integer,
    itemID      integer,

    CONSTRAINT ItemInRecipt_pk PRIMARY KEY (recieptID, itemID),
    CONSTRAINT ItemInRecipt_fk1 FOREIGN KEY (recieptID) REFERENCES Reciept(recieptID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT ItemInRecipt_fk2 FOREIGN KEY (itemID) REFERENCES Item(itemID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE Item (
    itemID  integer,
    name    varchar(50),
    weight  integer,
    amount  integer,
    cost    integer,

    CONSTRAINT Item_pk PRIMARY KEY (itemID)
);