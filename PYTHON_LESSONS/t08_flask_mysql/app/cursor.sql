USE iot_db;
DELIMITER //

DROP PROCEDURE IF EXISTS createDynamicTables;

CREATE PROCEDURE createDynamicTables()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE tableName VARCHAR(255);
    DECLARE colCount INT;
    DECLARE colName VARCHAR(255);
    DECLARE colType VARCHAR(255);
    DECLARE cur CURSOR FOR SELECT table_name FROM information_schema.tables WHERE table_schema = 'iot_db' AND table_type = 'BASE TABLE';

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO tableName;
        IF done THEN
            LEAVE read_loop;
        END IF;

        SET @timestamp := UNIX_TIMESTAMP(NOW());
        SET @dynamicTableName := CONCAT(tableName, '_', @timestamp);

        SET colCount := FLOOR(1 + RAND() * 9);

        SET @createTableQuery := CONCAT('CREATE TABLE ', @dynamicTableName, ' (');
        SET @i := 1;
        WHILE @i <= colCount DO
            SET colName := CONCAT('column', @i);
            SET colType := CASE ROUND(1 + RAND() * 3)
                            WHEN 1 THEN 'INT'
                            WHEN 2 THEN 'VARCHAR(255)'
                            WHEN 3 THEN 'DATE'
                          END;

            SET @createTableQuery := CONCAT(@createTableQuery, colName, ' ', colType);
            IF @i < colCount THEN
                SET @createTableQuery := CONCAT(@createTableQuery, ', ');
            END IF;

            SET @i := @i + 1;
        END WHILE;

        SET @createTableQuery := CONCAT(@createTableQuery, ');');

        PREPARE stmt FROM @createTableQuery;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    END LOOP;

    CLOSE cur;
END //

CALL createDynamicTables();

DELIMITER ;
