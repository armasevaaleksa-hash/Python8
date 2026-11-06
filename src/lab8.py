import mysql.connector
from mysql.connector import Error

try:
    #підключення до сервера MySQL
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        port=1234,
        password='0993337631Aleksa-'
    )

    if connection.is_connected():
        cursor = connection.cursor()

        #бази даних «Магазин»
        cursor.execute("CREATE DATABASE IF NOT EXISTS Магазин;")
        cursor.execute("USE Магазин;")
        print("Базу даних «Магазин» успішно створено та обрано.")

        #таблиця «Товари»
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Товари (
                id INT AUTO_INCREMENT PRIMARY KEY,
                назва VARCHAR(255) NOT NULL,
                ціна DECIMAL(10, 2) NOT NULL,
                кількість INT NOT NULL
            );
        """)
        print("Таблицю «Товари» створено.")


        insert_query = """
            INSERT INTO Товари (назва, ціна, кількість) 
            VALUES (%s, %s, %s);
        """
        records = [
            ("Смартфон", 12500.50, 15),
            ("Ноутбук", 28000.00, 7),
            ("Навушники", 1800.25, 30),
            ("Мишка", 750.00, 50),
            ("Клавіатура", 1400.00, 25)

        ]
        cursor.executemany(insert_query, records)
        connection.commit()
        print(f"Успішно додано рядків: {cursor.rowcount}")


        #оновлення даних
        update_query = "UPDATE Товари SET ціна = 800.00 WHERE назва = 'Мишка';"
        cursor.execute(update_query)
        connection.commit()
        print("Дані успішно оновлено.")

        #видалення даних
        delete_query = "DELETE FROM Товари ORDER BY кількість ASC LIMIT 1;"
        cursor.execute(delete_query)
        connection.commit()
        print("Запис із найменшою кількістю видалено.")

        #вибірка даних з умовою та сортуванням
        print("\n--- Виведення всіх товарів, відсортованих за ціною (від найдорожчих) ---")
        cursor.execute("SELECT * FROM Товари ORDER BY ціна DESC;")
        for row in cursor.fetchall():
            print(row)

        print("\n--- Виведення товарів, ціна яких більша за 2000 грн ---")
        cursor.execute("SELECT назва, ціна FROM Товари WHERE ціна > 2000;")
        for row in cursor.fetchall():
            print(row)

except Error as e:
    print("Помилка під час роботи з MySQL:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("\nЗ'єднання з базою даних закрито.")

        #USE магазин;
        #TRUNCATE TABLE товари;
