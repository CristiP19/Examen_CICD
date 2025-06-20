from flask import Flask, render_template
import mysql.connector  # Adăugați această linie de import
import os

app = Flask(__name__)

# Configurare baza de date
db_config = {
    'host': os.getenv('DB_HOST', 'db'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'example'),
    'database': os.getenv('DB_NAME', 'myapp_base')
}

def init_db():
    try:
        conn = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database']
        )
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS shoes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description TEXT,
            price DECIMAL(10, 2) NOT NULL,
            image VARCHAR(100) NOT NULL
        )
        """)

        # Verificăm dacă tabela este goală și inserăm date demo
        cursor.execute("SELECT COUNT(*) FROM shoes")
        count = cursor.fetchone()[0]
        if count == 0:
            cursor.execute("""
            INSERT INTO shoes (name, description, price, image) VALUES
            ('Nike Air Max', 'Pantofi sport de calitate superioară', 599.99, 'nike_air_max.jpg'),
            ('Adidas Superstar', 'Clasici Adidas cu vârf shell toe', 449.99, 'adidas_superstar.jpg'),
            ('Timberland', 'Ghete rezistente la apă', 799.99, 'timberland.jpg');
            """)

        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error initializing database: {e}")

# Inițializare bază de date la pornire
init_db()

@app.route('/')
def index():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM shoes")
        shoes = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('index.html', shoes=shoes)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)