import mysql.connector

# Establish a connection to the MySQL database
cnx = mysql.connector.connect(
    user='gsingh',
    password='root',
    host='localhost',
    database='car_rental'
)
cursor = cnx.cursor()

# Create the 'cars' table if it doesn't exist
create_table_query = '''
CREATE TABLE IF NOT EXISTS cars (
    id INT AUTO_INCREMENT PRIMARY KEY,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    available BOOLEAN NOT NULL
)
'''
cursor.execute(create_table_query)
cnx.commit()


def add_car(make, model, year):
    # Add a new car to the 'cars' table
    add_car_query = '''
    INSERT INTO cars (make, model, year, available)
    VALUES (%s, %s, %s, TRUE)
    '''
    car_data = (make, model, year)
    cursor.execute(add_car_query, car_data)
    cnx.commit()


def rent_car(car_id):
    # Rent a car by updating its 'available' status to False
    rent_car_query = '''
    UPDATE cars
    SET available = FALSE
    WHERE id = %s
    '''
    cursor.execute(rent_car_query, (car_id,))
    cnx.commit()


def return_car(car_id):
    # Return a rented car by updating its 'available' status to True
    return_car_query = '''
    UPDATE cars
    SET available = TRUE
    WHERE id = %s
    '''
    cursor.execute(return_car_query, (car_id,))
    cnx.commit()


def list_available_cars():
    # Retrieve and display all available cars
    available_cars_query = '''
    SELECT id, make, model, year
    FROM cars
    WHERE available = TRUE
    '''
    cursor.execute(available_cars_query)
    cars = cursor.fetchall()
    print("Available Cars:")
    for car in cars:
        car_id, make, model, year = car
        print(f"ID: {car_id}, Make: {make}, Model: {model}, Year: {year}")


# Example usage (will create menu later)
add_car("Toyota", "Camry", 2022)
add_car("Honda", "Civic", 2021)
list_available_cars()
rent_car(1)
list_available_cars()
return_car(1)
list_available_cars()

# Close the database connection
cursor.close()
cnx.close()
