INSERT INTO patients (first_name, last_name, date_of_birth, gender, contact_number, email, address) 
VALUES
    ('Иван', 'Иванов', '1985-03-12', 'Мужской', '89991234567', 'ivanov@example.com', 'ул. Ленина, 10, кв. 5'),
    ('Мария', 'Петрова', '1990-07-25', 'Женский', '89996543210', 'petrova@example.com', 'ул. Победы, 15, кв. 2'),
    ('Алексей', 'Смирнов', '1978-11-01', 'Мужской', '89997654321', 'smirnov@example.com', 'ул. Карла Маркса, 20, кв. 7'),
    ('Екатерина', 'Попова', '2000-06-30', 'Женский', '89998765432', 'popova@example.com', 'ул. Гагарина, 8, кв. 3');

INSERT INTO doctors (first_name, last_name, specialty, contact_number, email, office_number) 
VALUES
    ('Анатолий', 'Кузнецов', 'Терапевт', '89995551234', 'kuznetsov@example.com', '101'),
    ('Ольга', 'Соколова', 'Кардиолог', '89992223344', 'sokolova@example.com', '102'),
    ('Игорь', 'Морозов', 'Хирург', '89993334455', 'morozov@example.com', '103'),
    ('Наталья', 'Романова', 'Гинеколог', '89996667788', 'romanova@example.com', '104');

INSERT INTO appointments (patient_id, doctor_id, appointment_date, status, notes)
VALUES
    (1, 1, '2025-04-01 10:00:00', 'Scheduled', 'Пациент пришел на плановый осмотр'),
    (2, 2, '2025-04-01 11:30:00', 'Scheduled', 'Записан на консультацию по кардиологии'),
    (3, 3, '2025-04-02 09:00:00', 'Scheduled', 'Записан на операцию по удалению аппендицита'),
    (4, 4, '2025-04-02 14:30:00', 'Scheduled', 'Консультация по вопросам женского здоровья');

