from tkinter import *
import tkinter.messagebox as msgbox
from capacity_converter import Capacity as CapCon
from mass_converter import Mass as MassCon
from length_converter import Length as LengthCon
from speed_converter import Speed as SpeedCon
from area_converter import Area as AreaCon
from kitchen_units_converter import KitchenUnits as KUCon


def about_the_unit_converter():
    msgbox.showinfo(title="About the Converter",
                    message="This Unit Converter was designed and created by "
                    "Edina Horvath-Lazar as a Python practice project."
                    "\nIt is not meant for commercial use."
                    "\nFor more info visit edinahorvathlazar.ch")


main_window = Tk()
main_window.title("EHL Unit Converter")

# Menu
menu_bar = Menu(main_window)
main_window.config(menu=menu_bar, padx=10, pady=10, bg="darkslategray2")
about_menu = Menu(menu_bar, tearoff=0)
about_menu.add_command(label="About the Unit Converter", command=about_the_unit_converter)
about_menu.add_command(label="Exit", command=main_window.quit)
menu_bar.add_cascade(label="About", menu=about_menu)


def category_selection_change(cat):

    if cat == "Capacity":
        selected_category.set("Capacity")
        output_entry.delete(0, 100)
        display_capacity()

    if cat == "Mass":
        selected_category.set("Mass")
        output_entry.delete(0, 100)
        display_mass()

    if cat == "Length":
        selected_category.set("Length")
        output_entry.delete(0, 100)
        display_length()

    if cat == "Speed":
        selected_category.set("Speed")
        output_entry.delete(0, 100)
        display_speed()

    if cat == "Area":
        selected_category.set("Area")
        output_entry.delete(0, 100)
        display_area()

    if cat == "Kitchen Units":
        selected_category.set("Kitchen Units")
        output_entry.delete(0, 100)
        display_kitchen_units()

# Categories
category_frame = Frame(main_window, bg="darkslategray2", pady=10,
                       highlightbackground="darkslategray3", highlightthickness=1)
selected_category = StringVar(value="Capacity")

capacity_rb = Radiobutton(category_frame, text="Capacity",
                          variable=selected_category, value="Capacity",
                          bg="darkslategray2",
                          command=lambda: category_selection_change("Capacity"))
mass_rb = Radiobutton(category_frame, text="Mass",
                      variable=selected_category, value="Mass",
                      bg="darkslategray2",
                      command=lambda: category_selection_change("Mass"))
length_rb = Radiobutton(category_frame, text="Length",
                        variable=selected_category, value="Length",
                        bg="darkslategray2",
                        command=lambda: category_selection_change("Length"))
area_rb = Radiobutton(category_frame, text="Area",
                      variable=selected_category, value="Area",
                      bg="darkslategray2",
                      command=lambda: category_selection_change("Area"))
speed_rb = Radiobutton(category_frame, text="Speed",
                       variable=selected_category, value="Speed",
                       bg="darkslategray2",
                       command=lambda: category_selection_change("Speed"))
kitchen_unit_rb = Radiobutton(category_frame, text="Kitchen Units",
                              variable=selected_category, value="Kitchen Units",
                              bg="darkslategray2",
                              command=lambda: category_selection_change("Kitchen Units"))

category_frame.pack()
capacity_rb.grid(row=0, column=0)
mass_rb.grid(row=0, column=1)
length_rb.grid(row=0, column=2)
area_rb.grid(row=1, column=0)
speed_rb.grid(row=1, column=1)
kitchen_unit_rb.grid(row=1, column=2)

# User input & Result
input_output_frame = Frame(main_window, bg="darkslategray2", pady=10)
input_label = Label(input_output_frame, text="Enter value to convert: ", bg="darkslategray2")
output_label = Label(input_output_frame, text="Converted value: ", bg="darkslategray2")
input_entry = Entry(input_output_frame, bg="ghostwhite")
output_entry = Entry(input_output_frame, bg="ghostwhite")
input_output_frame.pack()
input_label.grid(row=0, column=0)
input_entry.grid(row=0, column=1)
output_label.grid(row=1, column=0)
output_entry.grid(row=1, column=1)

# Conversion
conversion_units = Frame(main_window, bg="darkslategray2", pady=10)
conversion_units.pack()

from_frame = Frame(conversion_units, bg="darkslategray2",
                   highlightbackground="darkslategray3", highlightthickness=1)
from_frame.pack(expand=True, fill=BOTH, side=LEFT)

to_frame = Frame(conversion_units, bg="darkslategray2",
                 highlightbackground="darkslategray3", highlightthickness=1)
to_frame.pack(expand=True, fill=BOTH, side=RIGHT)


def clear_from_to_units_frame():
    for widgets in from_frame.winfo_children():
        widgets.destroy()
    for widgets in to_frame.winfo_children():
        widgets.destroy()


new_capacity = CapCon()
new_mass = MassCon()
new_length = LengthCon()
new_speed = SpeedCon()
new_area = AreaCon()
new_k_u = KUCon()


def display_capacity():

    clear_from_to_units_frame()

    from_capacity = StringVar(value="ml (millilitres)")
    CapCon.from_this_unit(new_capacity, from_capacity.get())
    convert_from_label = Label(from_frame, text="Convert from unit:", bg="darkslategray2")
    convert_from_label.pack()
    for unit in CapCon.cap_units_list:
        units_rb = Radiobutton(from_frame, text=unit, variable=from_capacity,
                               value=unit, bg="darkslategray2",
                               command=lambda: CapCon.from_this_unit(new_capacity, from_capacity.get()))
        units_rb.pack()

    to_capacity = StringVar(value="ml (millilitres)")
    CapCon.to_this_unit(new_capacity, to_capacity.get())
    convert_to_label = Label(to_frame, text="Convert to unit:", bg="darkslategray2")
    convert_to_label.pack()
    for unit in CapCon.cap_units_list:
        units_rb = Radiobutton(to_frame, text=unit, variable=to_capacity,
                               value=unit, bg="darkslategray2",
                               command=lambda: CapCon.to_this_unit(new_capacity, to_capacity.get()))
        units_rb.pack()


def startup_with_capacity():
    selected_category.set("Capacity")
    display_capacity()

startup_with_capacity()


def display_mass():

    clear_from_to_units_frame()

    from_mass = StringVar(value="mg (milligrams)")
    MassCon.from_this_unit(new_mass, from_mass.get())
    convert_from_label = Label(from_frame, text="Convert from unit:", bg="darkslategray2")
    convert_from_label.pack()
    for unit in MassCon.mass_units_list:
        units_rb = Radiobutton(from_frame, text=unit, variable=from_mass,
                               value=unit, bg="darkslategray2",
                               command=lambda: MassCon.from_this_unit(new_mass, from_mass.get()))
        units_rb.pack()

    to_mass = StringVar(value="mg (milligrams)")
    MassCon.to_this_unit(new_mass, to_mass.get())
    convert_to_label = Label(to_frame, text="Convert to unit:", bg="darkslategray2")
    convert_to_label.pack()
    for unit in MassCon.mass_units_list:
        units_rb = Radiobutton(to_frame, text=unit, variable=to_mass,
                               value=unit, bg="darkslategray2",
                               command=lambda: MassCon.to_this_unit(new_mass, to_mass.get()))
        units_rb.pack()


def display_length():

    clear_from_to_units_frame()

    from_length = StringVar(value="mm (millimeters)")
    LengthCon.from_this_unit(new_length, from_length.get())
    convert_from_label = Label(from_frame, text="Convert from unit:", bg="darkslategray2")
    convert_from_label.pack()
    for unit in LengthCon.length_units_list:
        units_rb = Radiobutton(from_frame, text=unit, variable=from_length,
                               value=unit, bg="darkslategray2",
                               command=lambda: LengthCon.from_this_unit(new_length, from_length.get()))
        units_rb.pack()

    to_length = StringVar(value="mm (millimeters)")
    LengthCon.to_this_unit(new_length, to_length.get())
    convert_to_label = Label(to_frame, text="Convert to unit:", bg="darkslategray2")
    convert_to_label.pack()
    for unit in LengthCon.length_units_list:
        units_rb = Radiobutton(to_frame, text=unit, variable=to_length,
                               value=unit, bg="darkslategray2",
                               command=lambda: LengthCon.to_this_unit(new_length, to_length.get()))
        units_rb.pack()


def display_speed():

    clear_from_to_units_frame()

    from_speed = StringVar(value="m/s (meter per seconds)")
    SpeedCon.from_this_unit(new_speed, from_speed.get())
    convert_from_label = Label(from_frame, text="Convert from unit:", bg="darkslategray2")
    convert_from_label.pack()
    for unit in SpeedCon.speed_units_list:
        units_rb = Radiobutton(from_frame, text=unit, variable=from_speed,
                               value=unit, bg="darkslategray2",
                               command=lambda: SpeedCon.from_this_unit(new_speed, from_speed.get()))
        units_rb.pack()

    to_speed = StringVar(value="m/s (meter per seconds)")
    SpeedCon.to_this_unit(new_speed, to_speed.get())
    convert_to_label = Label(to_frame, text="Convert to unit:", bg="darkslategray2")
    convert_to_label.pack()
    for unit in SpeedCon.speed_units_list:
        units_rb = Radiobutton(to_frame, text=unit, variable=to_speed,
                               value=unit, bg="darkslategray2",
                               command=lambda: SpeedCon.to_this_unit(new_speed, to_speed.get()))
        units_rb.pack()


def display_area():

    clear_from_to_units_frame()

    from_area = StringVar(value="sq cm (square centimeters)")
    AreaCon.from_this_unit(new_area, from_area.get())
    convert_from_label = Label(from_frame, text="Convert from unit:", bg="darkslategray2")
    convert_from_label.pack()
    for unit in AreaCon.area_units_list:
        units_rb = Radiobutton(from_frame, text=unit, variable=from_area,
                               value=unit, bg="darkslategray2",
                               command=lambda: AreaCon.from_this_unit(new_area, from_area.get()))
        units_rb.pack()

    to_area = StringVar(value="sq cm (square centimeters)")
    AreaCon.to_this_unit(new_area, to_area.get())
    convert_to_label = Label(to_frame, text="Convert to unit:", bg="darkslategray2")
    convert_to_label.pack()
    for unit in AreaCon.area_units_list:
        units_rb = Radiobutton(to_frame, text=unit, variable=to_area,
                               value=unit, bg="darkslategray2",
                               command=lambda: AreaCon.to_this_unit(new_area, to_area.get()))
        units_rb.pack()


def display_kitchen_units():

    clear_from_to_units_frame()

    from_kitchen_units = StringVar(value="ml (millilitres)")
    KUCon.from_this_unit(new_k_u, from_kitchen_units.get())
    convert_from_label = Label(from_frame, text="Convert from unit:", bg="darkslategray2")
    convert_from_label.pack()
    for unit in KUCon.kitchen_units_list:
        units_rb = Radiobutton(from_frame, text=unit, variable=from_kitchen_units,
                               value=unit, bg="darkslategray2",
                               command=lambda: KUCon.from_this_unit(new_k_u, from_kitchen_units.get()))
        units_rb.pack()

    to_kunits = StringVar(value="ml (millilitres)")
    KUCon.to_this_unit(new_k_u, to_kunits.get())
    convert_to_label = Label(to_frame, text="Convert to unit:", bg="darkslategray2")
    convert_to_label.pack()
    for unit in KUCon.kitchen_units_list:
        units_rb = Radiobutton(to_frame, text=unit, variable=to_kunits,
                               value=unit, bg="darkslategray2",
                               command=lambda: KUCon.to_this_unit(new_k_u, to_kunits.get()))
        units_rb.pack()


def calculate_result():

    if (CapCon.user_input_value(new_capacity, input_entry.get()) == "Invalid Number"
            or MassCon.user_input_value(new_mass, input_entry.get()) == "Invalid Number"
            or LengthCon.user_input_value(new_length, input_entry.get()) == "Invalid Number"
            or SpeedCon.user_input_value(new_speed, input_entry.get()) == "Invalid Number"
            or AreaCon.user_input_value(new_area, input_entry.get()) == "Invalid Number"
            or KUCon.user_input_value(new_k_u, input_entry.get()) == "Invalid Number"):
        msgbox.showerror("Invalid Number", "Please enter a valid number.")

    if selected_category.get() == "Capacity":
        output_entry.delete(0, 100)
        CapCon.calculation(new_capacity, input_entry.get())
        result = CapCon.return_result(new_capacity)
        output_entry.insert(0, result)

    if selected_category.get() == "Mass":
        output_entry.delete(0, 100)
        MassCon.calculation(new_mass, input_entry.get())
        result = MassCon.return_result(new_mass)
        output_entry.insert(0, result)

    if selected_category.get() == "Length":
        output_entry.delete(0, 100)
        LengthCon.calculation(new_length, input_entry.get())
        result = LengthCon.return_result(new_length)
        output_entry.insert(0, result)

    if selected_category.get() == "Speed":
        output_entry.delete(0, 100)
        SpeedCon.calculation(new_speed, input_entry.get())
        result = SpeedCon.return_result(new_speed)
        output_entry.insert(0, result)

    if selected_category.get() == "Area":
        output_entry.delete(0, 100)
        AreaCon.calculation(new_area, input_entry.get())
        result = AreaCon.return_result(new_area)
        output_entry.insert(0, result)

    if selected_category.get() == "Kitchen Units":
        output_entry.delete(0, 100)
        KUCon.calculation(new_k_u, input_entry.get())
        result = KUCon.return_result(new_k_u)
        output_entry.insert(0, result)


calculate_button = Button(main_window, text="Calculate", bg="ghostwhite",
                          pady=10,
                          command=calculate_result)

calculate_button.pack()


main_window.mainloop()
