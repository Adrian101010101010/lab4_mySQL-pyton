USE iot_db;
DELIMITER //

CREATE FUNCTION get_aggregate_value(
    table_name VARCHAR(255),
    column_name VARCHAR(255),
    aggregate_type VARCHAR(255)
) RETURNS DECIMAL(10,2)
BEGIN
    DECLARE result DECIMAL(10,2);
    SET @sql_query := CONCAT('SELECT ', aggregate_type, '(', column_name, ') FROM ', table_name);
    PREPARE stmt FROM @sql_query;
    EXECUTE stmt;
    FETCH stmt INTO result;
    DEALLOCATE PREPARE stmt;
    RETURN result;
END  //

CREATE PROCEDURE get_aggregate_result(
    table_name VARCHAR(255),
    column_name VARCHAR(255),
    aggregate_type VARCHAR(255)
)
BEGIN
    DECLARE result DECIMAL(10,2);
    SET result := get_aggregate_value(table_name, column_name, aggregate_type);
    SELECT CONCAT('Aggregate result for ', table_name, ' in ', aggregate_type, ' is: ', result) AS notice;
END //

DELIMITER ;
