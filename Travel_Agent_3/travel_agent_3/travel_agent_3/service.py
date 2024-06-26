import json
from nameko.rpc import rpc
from travel_agent_3 import dependencies

class TravelAgent3:
    name = 'travel_agent_3'

    database = dependencies.Database()

    @rpc
    def get_travel_agent(self):
        travel_agent = self.database.get_travel_agent()
        return travel_agent
    
    @rpc
    def get_packages(self):
        packages = self.database.get_packages()
        return packages
    
    @rpc
    def get_all_package_details(self):
        package_details = self.database.get_all_package_details()
        return package_details
    
    @rpc
    def get_package_by_id(self, id):
        package = self.database.get_package_by_id(id)
        return package
    
    @rpc
    def get_package_details(self, package_id):
        package_details = self.database.get_package_details(package_id)
        return package_details
    
    @rpc
    def get_package_detail_by_day(self, package_id, day):
        package_detail_by_day = self.database.get_package_detail_by_day(package_id,day)
        return package_detail_by_day
    
    @rpc
    def add_booking(self, user_id, package_id):
        booking = self.database.add_booking(user_id, package_id)
        return booking
    @rpc
    def get_my_booking(self, user_id):
        booking = self.database.get_my_booking(user_id)
        return booking
    @rpc
    def filter(self, origin_city, destination_city, number_of_people, departure_date, return_date):
        filter = self.database.filter(origin_city, destination_city, number_of_people, departure_date, return_date)
        return filter