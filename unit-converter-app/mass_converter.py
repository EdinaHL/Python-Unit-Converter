from decimal import Decimal


class Mass:

    mass_units_list = ["mg (milligrams)", "g (grams)", "dkg (dekagrams)"
        , "kg (kilograms)", "oz (ounces)", "lb (pounds)", "st (stones)"
        , "t (metric tons)"]

    # Base of conversion: mg

    def __init__(self):
        self.source_exchanged_to_mg = Decimal()
        self.to_unit = ""
        self.from_unit = ""
        self.user_input = Decimal()
        self.mg_exchanged_to_target = Decimal()

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
        return round(self.mg_exchanged_to_target, 4)

    def from_source_to_mg(self):
        match self.from_unit:
            case "mg (milligrams)": self.source_exchanged_to_mg = self.user_input
            case "g (grams)": self.source_exchanged_to_mg = self.user_input * Decimal("1000")
            case "dkg (dekagrams)": self.source_exchanged_to_mg = self.user_input * Decimal("10000")
            case "kg (kilograms)": self.source_exchanged_to_mg = self.user_input * Decimal("1000000")
            case "oz (ounces)": self.source_exchanged_to_mg = self.user_input * Decimal("28350")
            case "lb (pounds)": self.source_exchanged_to_mg = self.user_input * Decimal("453600")
            case "st (stones)": self.source_exchanged_to_mg = self.user_input * Decimal("6350293")
            case "t (metric tons)": self.source_exchanged_to_mg = self.user_input * Decimal("1000000000")

    def from_mg_to_target_unit(self):
        match self.to_unit:
            case "mg (milligrams)": self.mg_exchanged_to_target = self.source_exchanged_to_mg
            case "g (grams)": self.mg_exchanged_to_target = self.source_exchanged_to_mg / Decimal("1000")
            case "dkg (dekagrams)": self.mg_exchanged_to_target = self.source_exchanged_to_mg / Decimal("10000")
            case "kg (kilograms)": self.mg_exchanged_to_target = self.source_exchanged_to_mg / Decimal("1000000")
            case "oz (ounces)": self.mg_exchanged_to_target = self.source_exchanged_to_mg / Decimal("28350")
            case "lb (pounds)": self.mg_exchanged_to_target = self.source_exchanged_to_mg / Decimal("453600")
            case "st (stones)": self.mg_exchanged_to_target = self.source_exchanged_to_mg / Decimal("6350293")
            case "t (metric tons)": self.mg_exchanged_to_target = self.source_exchanged_to_mg / Decimal("1000000000")

    def calculation(self, value):
        self.user_input_value(value)
        self.from_source_to_mg()
        self.from_mg_to_target_unit()
        self.return_result()