--Создание таблицы
CREATE TABLE models (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    ml_model_type VARCHAR(255),
    ml_model_version VARCHAR(255),
    author VARCHAR(255),
    created_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Вставка начальных данных
INSERT INTO models (name, description, ml_model_type, ml_model_version, author, created_date) VALUES
    ('Модель классификации', 'Классификатор изображений', 'Classification', '1.0', 'Иван Иванов', '2021-11-23 10:00:00+03:00'),
    ('Модель регрессии', 'Модель для прогнозирования цен', 'Regression', '2.1', 'Анна Петрова', '2022-11-23 10:00:00+03:00'),
    ('Модель кластеризации', 'Модель для группировки данных', 'Clustering', '0.1', 'Вася Сидоров', '2023-10-03 10:00:00+03:00');

