from decimal import Decimal


class Kitchen_Units:

    kitchen_units_list = ["ml (millilitres)", "cup UK", "cup US", "tsp (teaspoon)", "tbsp (tablespoon)"]

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
        except:
            return "Invalid Number"

    def return_result(self):
        return round(self.ml_exchanged_to_target, 4)

    def from_source_to_ml(self):
        match self.from_unit:
            case "g (grams)": self.source_exchanged_to_ml = self.user_input
            case "cup UK": self.source_exchanged_to_ml = self.user_input * Decimal("284")
            case "cup US": self.source_exchanged_to_ml = self.user_input * Decimal("237")
            case "tsp (teaspoon)": self.source_exchanged_to_ml = self.user_input * Decimal("5")
            case "tbsp (tablespoon)": self.source_exchanged_to_ml = self.user_input * Decimal("15")

    def from_ml_to_target_unit(self):
        match self.to_unit:
            case "g (grams)": self.ml_exchanged_to_target = self.source_exchanged_to_ml
            case "cup UK": self.ml_exchanged_to_target = self.source_exchanged_to_ml / Decimal("284")
            case "cup US": self.ml_exchanged_to_target = self.source_exchanged_to_ml / Decimal("237")
            case "tsp (teaspoon)": self.ml_exchanged_to_target = self.source_exchanged_to_ml / Decimal("5")
            case "tbsp (tablespoon)": self.ml_exchanged_to_target = self.source_exchanged_to_ml / Decimal("15")

    def calculation(self, value):
        self.user_input_value(value)
        self.from_source_to_ml()
        self.from_ml_to_target_unit()
        self.return_result()