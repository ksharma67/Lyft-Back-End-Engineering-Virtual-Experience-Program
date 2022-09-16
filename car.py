from engine import Engine
from battery import Battery
from tire import Tire

class Car(Engine, Battery):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def battery_needs_service(self):
        return self.battery.battery_needs_service()

    def engine_needs_service(self):
        return self.engine.engine_needs_service()

    def tire_needs_service(self):
        return self.tire.tire_needs_service()

    def needs_service(self):
        return self.engine_needs_service() or self.battery_needs_service() or self.tire_needs_service()
