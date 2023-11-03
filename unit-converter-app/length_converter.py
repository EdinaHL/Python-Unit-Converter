from decimal import Decimal


class Length:

    length_units_list = ["mm (millimeters)", "cm (centimeters)", "m (meters)",
                         "km (kilometers)", "in (inches)", "ft (feet)", "yd (yards)",
                         "mi (miles)", "nm (nautical miles)"]

    # Base of conversion: mm

    def __init__(self):
        self.source_exchanged_to_mm = Decimal()
        self.to_unit = ""
        self.from_unit = ""
        self.user_input = Decimal()
        self.mm_exchanged_to_target = Decimal()

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
        return round(self.mm_exchanged_to_target, 4)

    def from_source_to_mm(self):
        match self.from_unit:
            case "mm (millimeters)":
                self.source_exchanged_to_mm = self.user_input
            case "cm (centimeters)":
                self.source_exchanged_to_mm = self.user_input * Decimal("10")
            case "m (meters)":
                self.source_exchanged_to_mm = self.user_input * Decimal("1000")
            case "km (kilometers)":
                self.source_exchanged_to_mm = self.user_input * Decimal("1000000")
            case "in (inches)":
                self.source_exchanged_to_mm = self.user_input * Decimal("25.4")
            case "ft (feet)":
                self.source_exchanged_to_mm = self.user_input * Decimal("304.8")
            case "yd (yards)":
                self.source_exchanged_to_mm = self.user_input * Decimal("914.4")
            case "mi (miles)":
                self.source_exchanged_to_mm = self.user_input * Decimal("1479804")
            case "nm (nautical miles)":
                self.source_exchanged_to_mm = self.user_input * Decimal("1852000")

    def from_mm_to_target_unit(self):
        match self.to_unit:
            case "mm (millimeters)":
                self.mm_exchanged_to_target = self.source_exchanged_to_mm
            case "cm (centimeters)":
                self.mm_exchanged_to_target = self.source_exchanged_to_mm / Decimal("10")
            case "m (meters)":
                self.mm_exchanged_to_target = self.source_exchanged_to_mm / Decimal("1000")
            case "km (kilometers)":
                self.mm_exchanged_to_target = self.source_exchanged_to_mm / Decimal("1000000")
            case "in (inches)":
                self.mm_exchanged_to_target = self.source_exchanged_to_mm / Decimal("25.4")
            case "ft (feet)":
                self.mm_exchanged_to_target = self.source_exchanged_to_mm / Decimal("304.8")
            case "yd (yards)":
                self.mm_exchanged_to_target = self.source_exchanged_to_mm / Decimal("914.4")
            case "mi (miles)":
                self.mm_exchanged_to_target = self.source_exchanged_to_mm / Decimal("1479804")
            case "nm (nautical miles)":
                self.mm_exchanged_to_target = self.source_exchanged_to_mm / Decimal("1852000")

    def calculation(self, value):
        self.user_input_value(value)
        self.from_source_to_mm()
        self.from_mm_to_target_unit()
        self.return_result()
