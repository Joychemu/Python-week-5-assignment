# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self._battery = battery  # protected attribute
        self.__is_on = False     # private attribute (encapsulated)

    def power_on(self):
        if not self.__is_on:
            self.__is_on = True
            return f"{self.brand} {self.model} is now ON."
        return f"{self.brand} {self.model} is already ON."

    def power_off(self):
        if self.__is_on:
            self.__is_on = False
            return f"{self.brand} {self.model} is now OFF."
        return f"{self.brand} {self.model} is already OFF."

    def check_status(self):
        return "ON" if self.__is_on else "OFF"

    def battery_status(self):
        return f"Battery: {self._battery}%"

# Subclass
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system, refresh_rate):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system
        self.refresh_rate = refresh_rate  # in Hz

    def launch_game_mode(self):
        if self.check_status() == "ON":
            return f"{self.brand} {self.model} is boosting performance with {self.cooling_system} and {self.refresh_rate}Hz refresh rate!"
        return "Turn on the phone first to launch game mode."

    # Polymorphism - override method
    def battery_status(self):
        return f"Gaming battery level: {self._battery}% (High-Performance Mode)"

# Instantiate both classes
basic_phone = Smartphone("Samsung", "S24", 128, 80)
gaming_phone = GamingPhone("Asus", "ROG Phone 7", 256, 95, "Vapor Chamber", 165)

# Demonstrate behavior
print(basic_phone.power_on())
print(basic_phone.battery_status())
print(basic_phone.power_off())

print("\n---\n")

print(gaming_phone.power_on())
print(gaming_phone.battery_status())  # uses overridden method
print(gaming_phone.launch_game_mode())
