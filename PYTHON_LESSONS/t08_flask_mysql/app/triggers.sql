USE iot_db;
DELIMITER //
CREATE TRIGGER check_value_before_insert
BEFORE INSERT ON iot_db.user
FOR EACH ROW 
BEGIN 
  IF NEW.name LIKE '%00' THEN
  SIGNAL SQLSTATE '45000'
  SET MESSAGE_TEXT = 'A column value cannot end with two zeros';
  END IF;
END;

CREATE TRIGGER preventDataModification
BEFORE INSERT ON iot_db.city
FOR EACH ROW 
BEGIN
  SIGNAL SQLSTATE '45000'
  SET MESSAGE_TEXT = 'this table cannot be changed';
END;

CREATE TRIGGER preventDataModificationUpdate
BEFORE UPDATE ON iot_db.city 
FOR EACH ROW
BEGIN
   SIGNAL SQLSTATE '45000'
   SET MESSAGE_TEXT = 'this table cannot be changed';
END;

CREATE TRIGGER preventDataModificationDelete
BEFORE DELETE ON iot_db.city
FOR EACH ROW
BEGIN
  SIGNAL SQLSTATE '45000'
 SET MESSAGE_TEXT = 'this table cannot be changed';
END;

CREATE TRIGGER restrictNames
BEFORE INSERT ON iot_db.user
FOR EACH ROW 
BEGIN
  IF NEW.COLUMN_NAME NOT IN ('Svitlana', 'Petro', 'Olha', 'Taras') THEN
  SIGNAL SQLSTATE '45000'
  SET MESSAGE_TEXT = 'Допустимі імена для стовпця: Svitlana, Petro, Olha, Taras.';
  END IF;
END;

CREATE TRIGGER restrictNamesUpdate
BEFORE UPDATE ON iot_db.user
FOR EACH ROW
BEGIN
  IF NEW.COlumn_name NOT IN ('Svitlana', 'Petro', 'Olha', 'Taras') THEN
  SIGNAL SQLSTATE '45000'
  SET MESSAGE_TEXT = 'Допустимі імена для стовпця: Svitlana, Petro, Olha, Taras.';
  END IF;
END;

DELIMITER ;