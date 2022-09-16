from tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_sensor_data):
        super().__init__(tire_sensor_data)
        self.tire_sensor_data = tire_sensor_data

    def tire_needs_service(self):
        # lambda function to find if a tire has any value greater than 0.9
        return any(map(lambda current_tire: current_tire >= 0.9, self.tire_sensor_data))
