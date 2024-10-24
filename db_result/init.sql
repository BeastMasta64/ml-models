--Создание таблицы
CREATE TABLE results (
    delivery_tag INT PRIMARY KEY,
    result NUMERIC(10, 5) ,
    created_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
