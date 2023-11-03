from decimal import Decimal


class KitchenUnits:

    kitchen_units_list = ["ml (millilitres)", "cup UK", "cup US",
                          "tsp UK (teaspoon)", "tbsp UK (tablespoon)",
                          "tsp US (teaspoon)", "tbsp US (tablespoon)"]

    # Base of conversion: ml

    def __init__(self):
        self.source_exchanged_to_ml = Decimal()
        self.to_unit = ""
        self.from_unit = ""
        self.user_input = Decimal()
        self.ml_exchanged_to_target = Decimal()

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
        return round(self.ml_exchanged_to_target, 4)

    def from_source_to_ml(self):
        match self.from_unit:
            case "ml (millilitres)":
                self.source_exchanged_to_ml = self.user_input
            case "cup UK":
                self.source_exchanged_to_ml = self.user_input * Decimal("284.1")
            case "cup US":
                self.source_exchanged_to_ml = self.user_input * Decimal("240")
            case "tsp UK (teaspoon)":
                self.source_exchanged_to_ml = self.user_input * Decimal("5.919")
            case "tbsp UK (tablespoon)":
                self.source_exchanged_to_ml = self.user_input * Decimal("17.758")
            case "tsp US (teaspoon)":
                self.source_exchanged_to_ml = self.user_input * Decimal("4.929")
            case "tbsp US (tablespoon)":
                self.source_exchanged_to_ml = self.user_input * Decimal("14.787")

    def from_ml_to_target_unit(self):
        match self.to_unit:
            case "ml (millilitres)":
                self.ml_exchanged_to_target = self.source_exchanged_to_ml
            case "cup UK":
                self.ml_exchanged_to_target = self.source_exchanged_to_ml / Decimal("284.1")
            case "cup US":
                self.ml_exchanged_to_target = self.source_exchanged_to_ml / Decimal("240")
            case "tsp UK (teaspoon)":
                self.ml_exchanged_to_target = self.source_exchanged_to_ml / Decimal("5.919")
            case "tbsp UK (tablespoon)":
                self.ml_exchanged_to_target = self.source_exchanged_to_ml / Decimal("17.758")
            case "tsp US (teaspoon)":
                self.ml_exchanged_to_target = self.source_exchanged_to_ml / Decimal("4.929")
            case "tbsp US (tablespoon)":
                self.ml_exchanged_to_target = self.source_exchanged_to_ml / Decimal("14.787")

    def calculation(self, value):
        self.user_input_value(value)
        self.from_source_to_ml()
        self.from_ml_to_target_unit()
        self.return_result()
