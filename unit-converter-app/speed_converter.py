from decimal import Decimal


class Speed:

    speed_units_list = ["m/s (meter per seconds)", "km/h (kilometers per hour)",
                        "mph (miles per hour)", "kn (knots)"]

    # Base of conversion: m/s

    def __init__(self):
        self.source_exchanged_to_mps = Decimal()
        self.to_unit = ""
        self.from_unit = ""
        self.user_input = Decimal()
        self.mps_exchanged_to_target = Decimal()

    def from_this_unit(self, unit):
        self.from_unit = unit

    def to_this_unit(self, unit):
        self.to_unit = unit

    def user_input_value(self, value):
        try:
            self.user_input = Decimal(value)
        except ArithmeticError:
            return "Invalid Number"

    def return_result(self):
        return round(self.mps_exchanged_to_target, 4)

    def from_source_to_mps(self):
        match self.from_unit:
            case "m/s (meter per seconds)":
                self.source_exchanged_to_mps = self.user_input
            case "km/h (kilometers per hour)":
                self.source_exchanged_to_mps = self.user_input / Decimal("3.6")
            case "mph (miles per hour)":
                self.source_exchanged_to_mps = self.user_input / Decimal("2.237")
            case "kn (knots)":
                self.source_exchanged_to_mps = self.user_input / Decimal("1.944")

    def from_mps_to_target_unit(self):
        match self.to_unit:
            case "m/s (meter per seconds)":
                self.mps_exchanged_to_target = self.source_exchanged_to_mps
            case "km/h (kilometers per hour)":
                self.mps_exchanged_to_target = self.source_exchanged_to_mps * Decimal("3.6")
            case "mph (miles per hour)":
                self.mps_exchanged_to_target = self.source_exchanged_to_mps * Decimal("2.237")
            case "kn (knots)":
                self.mps_exchanged_to_target = self.source_exchanged_to_mps * Decimal("1.944")

    def calculation(self, value):
        self.user_input_value(value)
        self.from_source_to_mps()
        self.from_mps_to_target_unit()
        self.return_result()
