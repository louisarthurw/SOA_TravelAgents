import json
from nameko.rpc import RpcProxy
from nameko.web.handlers import http
import eventlet

eventlet.monkey_patch()

class GatewayService:
    name = 'gateway'
    
    header = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "*",
        "Access-Control-Allow-Headers": "*",     
    }

    travel_agent_rpc = RpcProxy('travel_agent_1')

    @http('GET', '/travel-agent')
    def get_travel_agent(self, request):
        travel_agent = self.travel_agent_rpc.get_travel_agent()
        return (200, self.header, json.dumps(travel_agent))

    @http('GET', '/travel-agent/packages')
    def get_packages(self, request):
        packages = self.travel_agent_rpc.get_packages()
        return (200, self.header, json.dumps(packages))

    @http('GET', '/travel-agent/package_details')
    def get_all_package_details(self, request):
        package_details = self.travel_agent_rpc.get_all_package_details()
        return (200, self.header, json.dumps(package_details))
    
    @http('GET', '/travel-agent/package/<int:id>')
    def get_package_by_id(self, request, id):
        package = self.travel_agent_rpc.get_package_by_id(id)
        return (200, self.header, json.dumps(package))
    
    @http('GET', '/travel-agent/package_details/<int:package_id>')
    def get_package_details(self, request, package_id):
        package_details = self.travel_agent_rpc.get_package_details(package_id)
        return (200, self.header, json.dumps(package_details))
    
    @http('GET', '/travel-agent/package/<int:package_id>/day/<int:day>')
    def get_package_detail_by_day(self, request, package_id, day):
        package_detail_by_day = self.travel_agent_rpc.get_package_detail_by_day(package_id, day)
        return (200, self.header, json.dumps(package_detail_by_day))
    
    @http('GET', '/travel-agent/bookings/<int:user_id>')
    def get_my_booking(self,request, user_id):
        my_booking = self.travel_agent_rpc.get_my_booking(user_id)
        return (200, self.header, json.dumps(my_booking))
    
    @http('POST', '/travel-agent/book')
    def add_booking(self, request):
        data = json.loads(request.get_data(as_text=True))
        user_id = data['user_id']
        package_id = data['package_id']
        booking = self.travel_agent_rpc.add_booking(user_id, package_id)
        return (200, self.header, json.dumps(booking))
    
    @http('GET', '/travel-agent/filter')
    def filter_packages(self, request):
        origin_city = request.args.get('origin_city')
        destination_city = request.args.get('destination_city')
        number_of_people = request.args.get('number_of_people')
        departure_date = request.args.get('departure_date')
        return_date = request.args.get('return_date')
        filtered_packages = self.travel_agent_rpc.filter(origin_city, destination_city, number_of_people, departure_date, return_date)
        return (200, self.header, json.dumps(filtered_packages))