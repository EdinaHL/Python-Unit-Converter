from decimal import Decimal


class Capacity:

    cap_units_list = ["ml (millilitres)", "l (litres)", "fl oz (fluid ounces)",
                      "pt UK (pints)", "gal UK (UK gallons)", "gal US (US gallons)"]

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
            case "l (litres)":
                self.source_exchanged_to_ml = self.user_input * Decimal("1000")
            case "fl oz (fluid ounces)":
                self.source_exchanged_to_ml = self.user_input * Decimal("29.574")
            case "pt UK (pints)":
                self.source_exchanged_to_ml = self.user_input * Decimal("568.3")
            case "gal UK (UK gallons)":
                self.source_exchanged_to_ml = self.user_input * Decimal("4546.09")
            case "gal US (US gallons)":
                self.source_exchanged_to_ml = self.user_input * Decimal("3785.412")

    def from_ml_to_target_unit(self):
        match self.to_unit:
            case "ml (millilitres)":
                self.ml_exchanged_to_target = self.source_exchanged_to_ml
            case "l (litres)":
                self.ml_exchanged_to_target = self.source_exchanged_to_ml / Decimal("1000")
            case "fl oz (fluid ounces)":
                self.ml_exchanged_to_target = self.source_exchanged_to_ml / Decimal("29.574")
            case "pt UK (pints)":
                self.ml_exchanged_to_target = self.source_exchanged_to_ml / Decimal("568.3")
            case "gal UK (UK gallons)":
                self.ml_exchanged_to_target = self.source_exchanged_to_ml / Decimal("4546.09")
            case "gal US (US gallons)":
                self.ml_exchanged_to_target = self.source_exchanged_to_ml / Decimal("3785.412")

    def calculation(self, value):
        self.user_input_value(value)
        self.from_source_to_ml()
        self.from_ml_to_target_unit()
        self.return_result()
