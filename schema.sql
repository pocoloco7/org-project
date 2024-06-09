-- Drop the table if it already exists
DROP TABLE IF EXISTS product;

-- Create the employees table
CREATE TABLE product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    quantity integer NOT NULL,
    purpose TEXT NOT NULL UNIQUE
);
