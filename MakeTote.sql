CREATE DATABASE ToteDB;
USE ToteDB;

CREATE TABLE Users (
userID INT NOT NULL,
firstName CHAR(15) NOT NULL,
lastName CHAR(15) NOT NULL,
dob DATE NOT NULL,
email CHAR(35) NOT NULL,
phone INT NOT NULL,
city CHAR(25) NOT NULL,
biography TEXT,
vendor BOOLEAN NOT NULL,
hostStatus BOOLEAN NOT NULL,
PRIMARY KEY (userID)
);

CREATE TABLE Stores (
storeID INT NOT NULL,
storeName CHAR(35) NOT NULL,
description TEXT NOT NULL,
location CHAR(25) NOT NULL,
activeStatus BOOLEAN NOT NULL,
PRIMARY KEY (storeID)
);

CREATE TABLE UserStores (
userID INT NOT NULL,
storeID INT NOT NULL,
FOREIGN KEY (userID) REFERENCES Users (userID),
FOREIGN KEY (storeID) REFERENCES Stores (storeID),
PRIMARY KEY (userID, storeID)
);

CREATE TABLE Products (
productID 	INT NOT NULL, 
storeID 	INT NOT NULL, 
productName 	CHAR(25) NOT NULL, 
productCategory CHAR(20) NOT NULL,
productDescription TEXT NOT NULL,
price INT NOT NULL,
availability BOOLEAN NOT NULL,
FOREIGN KEY (storeID) REFERENCES Stores (storeID),
PRIMARY KEY (productID)
);



CREATE TABLE Properties (
propertyID INT NOT NULL,
address MEDIUMTEXT NOT NULL,
activeStatus BOOLEAN NOT NULL,
PRIMARY KEY (propertyID)
);

CREATE TABLE UserProperties (
propertyID INT NOT NULL,
userID INT NOT NULL,
FOREIGN KEY  (propertyID) REFERENCES Properties (propertyID),
FOREIGN KEY (userID) REFERENCES Users (userID),
PRIMARY KEY (propertyID, userID)
);

CREATE TABLE Markets (
marketID INT NOT NULL,
propertyID INT NOT NULL,
marketName CHAR(30) NOT NULL,
marketDescription mediumtext NOT NULL,
startDateTime datetime NOT NULL,
endDateTime datetime NOT NULL,
FOREIGN KEY (propertyID) REFERENCES Properties (propertyID),
PRIMARY KEY (marketID)
);

CREATE TABLE MarketStores (
marketID INT NOT NULL,
storeID INT NOT NULL,
FOREIGN KEY (marketID) REFERENCES Markets (marketID),
FOREIGN KEY (storeID) REFERENCES Stores (storeID),
PRIMARY KEY (marketID, storeID)
);

CREATE TABLE Transactions (
transactionID INT NOT NULL,
storeID INT NOT NULL,
userID INT NOT NULL,
marketID INT,
transactionTime DATETIME NOT NULL,
transactionTotal FLOAT(5,2) NOT NULL,
FOREIGN KEY (storeID) REFERENCES Stores (storeID),
FOREIGN KEY (userID) REFERENCES Users (userID),
FOREIGN KEY (marketID) REFERENCES Markets (marketID),
PRIMARY KEY (transactionID)
);

CREATE TABLE ProductsTransactions (
transactionID INT NOT NULL,
productID 	INT NOT NULL, 
quantity INT NOT NULL,
FOREIGN KEY (transactionID) REFERENCES Transactions (transactionID),
FOREIGN KEY (productID) REFERENCES Products (productID),
PRIMARY KEY (transactionID, productID)
);
