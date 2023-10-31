from tkinter import *
from tkinter import font
import tkinter.messagebox as msgbox
from capacity_converter import Capacity as CapCon


def about_the_unit_converter():
    msgbox.showinfo(title="About the Converter"
                    , message="This Unit Converter was designed and created by Edina Horvath-Lazar as a Python practice project."
                              "\nIt is not meant for commercial use."
                              "\nFor more info visit edinahorvathlazar.ch")



main_window = Tk()
main_window.geometry("400x400")

# ---------------------- Menu ----------------------
menu_bar = Menu(main_window)
about_menu = Menu(menu_bar, tearoff=0)
about_menu.add_command(label="About the Unit Converter", command=about_the_unit_converter)
about_menu.add_command(label="Exit", command=main_window.quit)
menu_bar.add_cascade(label="About", menu=about_menu)

# ---------------------- Window design ----------------------
main_window.config(menu=menu_bar, padx=10, pady=10, bg="seashell2")
main_window.title("EHL Unit Converter")

# ---------------------- Category section ----------------------
category_frame = Frame(main_window, bg="seashell2", pady=10)
selected_category = StringVar(value="Capacity")

capacity_rb = Radiobutton(category_frame, text="Capacity"
                          , variable=selected_category, value="Capacity"
                          , bg="seashell2", command=lambda: selected_category.set("Capacity"))
mass_rb = Radiobutton(category_frame, text="Mass"
                      , variable=selected_category, value="Mass"
                      , bg="seashell2")
length_rb = Radiobutton(category_frame, text="Length"
                        , variable=selected_category, value="Length"
                        , bg="seashell2")
area_rb = Radiobutton(category_frame, text="Area"
                      , variable=selected_category, value="Area"
                      , bg="seashell2")
speed_rb = Radiobutton(category_frame, text="Speed"
                       , variable=selected_category, value="Speed"
                       , bg="seashell2")
temperature_rb = Radiobutton(category_frame, text="Temperature"
                             , variable=selected_category, value="Temperature"
                             , bg="seashell2")
kitchen_unit_rb = Radiobutton(category_frame, text="Kitchen Units"
                              , variable=selected_category, value="Kitchen Units"
                              , bg="seashell2")

category_frame.pack()
capacity_rb.grid(row=0, column=0)
mass_rb.grid(row=0, column=1)
length_rb.grid(row=0, column=2)
area_rb.grid(row=1, column=0)
speed_rb.grid(row=1, column=1)
temperature_rb.grid(row=1, column=2)
kitchen_unit_rb.grid(row=2, column=1)

# ---------------------- User input and Result section ----------------------
input_output_frame = Frame(main_window, bg="seashell2", pady=10)
input_label = Label(input_output_frame, text="Enter value to convert: ", bg="seashell2")
output_label = Label(input_output_frame, text="Converted value: ", bg="seashell2")
input_entry = Entry(input_output_frame, bg="seashell1")
output_entry = Entry(input_output_frame, bg="seashell1")
input_output_frame.pack()
input_label.grid(row=0, column=0)
input_entry.grid(row=0, column=1)
output_label.grid(row=1, column=0)
output_entry.grid(row=1, column=1)

# ---------------------- Conversion section frames ----------------------
conversion_units = Frame(main_window, bg="seashell2", pady=10)
conversion_units.pack()
from_frame = Frame(conversion_units, bg="seashell2")
from_frame.pack(expand=True, fill=BOTH, side=LEFT)
to_frame = Frame(conversion_units, bg="seashell2")
to_frame.pack(expand=True, fill=BOTH, side=RIGHT)

# ---------------------- "Convert from" section ----------------------
from_label = Label(from_frame, text="Convert from:", bg="seashell2")
from_label.place(anchor=W)
from_label.pack()

# ---------------------- "Convert to" section ----------------------
to_label = Label(to_frame, text="Convert to:", bg="seashell2")
to_label.place(anchor=W)
to_label.pack()

# ---------------------- Category object creation ----------------------
new_capacity = CapCon()

# ---------------------- Display Capacity units in "From" section ----------------------
if selected_category.get() == "Capacity":
    from_capacity = StringVar(value="ml (millilitres)")
    CapCon.from_this_unit(new_capacity, from_capacity.get())
    for unit in CapCon.cap_units_long:
        units_rb = Radiobutton(from_frame, text=unit, variable=from_capacity
                               , value=unit, bg="seashell2"
                               , command=lambda: CapCon.from_this_unit(new_capacity, from_capacity.get()))
        units_rb.pack()


# ---------------------- Display Capacity units in "To" section ----------------------
if selected_category.get() == "Capacity":
    to_capacity = StringVar(value=CapCon.cap_units_long[0])
    CapCon.to_this_unit(new_capacity, to_capacity.get())
    for unit in CapCon.cap_units_long:
        units_rb = Radiobutton(to_frame, text=unit, variable=to_capacity
                               , value=unit, bg="seashell2"
                               , command=lambda: CapCon.to_this_unit(new_capacity, to_capacity.get()))
        units_rb.pack()


# ---------------------- Send user input, calculate and display result ----------------------
def calculate_result():
    # ---------------------- Handle invalid number ----------------------
    if CapCon.user_input_value(new_capacity, input_entry.get()) == "Invalid Number":
        msgbox.showerror("Invalid Number", "Please enter a valid number.")
    if selected_category.get() == "Capacity":
        output_entry.delete(0,100)
        CapCon.calculation(new_capacity, input_entry.get())
        result = CapCon.return_result(new_capacity)
        output_entry.insert(0, result)

# ---------------------- Calculate button ----------------------
calculate_button = Button(main_window, text="Calculate", bg="seashell1"
                          , pady=10, command=calculate_result)
calculate_button.pack()


main_window.mainloop()