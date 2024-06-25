from nameko.extensions import DependencyProvider

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling
from datetime import date
import requests

class DatabaseWrapper:
    connection = None

    def __init__(self, connection):
        self.connection = connection

    def get_travel_agent(self):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM travel_agent"
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return self.convert_dates_to_strings(result)
    
    def get_packages(self):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM package WHERE quota > 0"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return [self.convert_dates_to_strings(row) for row in result]
    
    def get_all_package_details(self):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM package_details"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return [self.convert_dates_to_strings(row) for row in result]
    
    def get_my_booking(self):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM booking b LEFT JOIN package p ON b.package_id = p.id WHERE p.id = b.package_id"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return [self.convert_dates_to_strings(row) for row in result]
    
    def get_package_by_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM package WHERE id = %s" 
        cursor.execute(sql, (id,))
        package = cursor.fetchone()
        self.connection.commit()
        cursor.close()
        return self.convert_dates_to_strings(package)
    
    def get_package_details(self, package_id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM package_details pd LEFT JOIN hotel_details hd ON pd.id = hd.package_details_id LEFT JOIN flight_details fd ON pd.id = fd.package_details_id LEFT JOIN attraction_details ad ON pd.id = ad.package_details_id WHERE package_id = %s"
        cursor.execute(sql, (package_id,))
        package_details = cursor.fetchall()
        self.connection.commit()
        cursor.close()
        return [self.convert_dates_to_strings(row) for row in package_details]
    
    def get_package_detail_by_day(self, package_id, day):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM package_details pd LEFT JOIN hotel_details hd ON pd.id = hd.package_details_id LEFT JOIN flight_details fd ON pd.id = fd.package_details_id  LEFT JOIN attraction_details ad ON pd.id = ad.package_details_id WHERE package_id = %s AND day = %s"
        cursor.execute(sql, (package_id, day,))
        package_details = cursor.fetchone()
        self.connection.commit()
        cursor.close()
        return self.convert_dates_to_strings(package_details)
        
    def add_booking(self, user_id, package_id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "INSERT INTO booking (user_id, package_id) VALUES (%s, %s)"
        sql2 = "UPDATE package SET quota = quota - 1 WHERE id = %s"
        cursor.execute(sql, (user_id, package_id,))
        cursor.execute(sql2, (package_id,))
        self.connection.commit()
        cursor.close()
        return {"Message": "Booking success"}
    
    def filter(self, origin_city, destination_city, number_of_people, departure_date, return_date):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT p.id, p.name, p.description, p.departure_date, p.return_date, p.number_of_people, p.quota, p.price, p.image, pd.id AS idd, pd.package_id, pd.day, pd.description, pd.origin_city, pd.destination_city FROM package p LEFT JOIN package_details pd ON p.id = pd.package_id WHERE day = 1 AND origin_city = %s AND destination_city = %s AND number_of_people >= %s AND departure_date = %s AND return_date = %s"
        cursor.execute(sql, (origin_city, destination_city, number_of_people, departure_date, return_date,))
        packages = cursor.fetchall()
        self.connection.commit()
        cursor.close()
        return [self.convert_dates_to_strings(package) for package in packages]
    
    def convert_dates_to_strings(self, data):
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, date):
                    data[key] = value.isoformat()
        return data
    
class Database(DependencyProvider):
    connection_pool = None

    def __init__(self):
        try:
            self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name="database_pool",
                pool_size=10,
                pool_reset_session=True,
                host='localhost',
                database='travel_agent_2',
                user='root',
                password=''
            )
        except Error as e :
            print ("Error while connecting to MySQL using Connection pool ", e)

    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())