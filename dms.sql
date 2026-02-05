CREATE DATABASE dispute_management;
USE dispute_management;


CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    role VARCHAR(50)
);


CREATE TABLE disputes (
    dispute_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200),
    description TEXT,
    status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    assigned_to INT,
    FOREIGN KEY (assigned_to) REFERENCES users(user_id)
);


ALTER TABLE users
ADD COLUMN username VARCHAR(50) UNIQUE,
ADD COLUMN password VARCHAR(255);


INSERT INTO users (name, role, username, password)
VALUES (
  'System Admin',
  'Admin',
  'admin',
  SHA2('admin123', 256)
);



