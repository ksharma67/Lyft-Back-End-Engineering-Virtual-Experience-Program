from tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_sensor_data):
        super().__init__(tire_sensor_data)
        self.tire_sensor_data = tire_sensor_data

    def tire_needs_service(self):
        # lambda function to find sum of all values in tire_sensor_data
        # and check if it is greater than 3.0
        return sum(self.tire_sensor_data) >= 3.0
