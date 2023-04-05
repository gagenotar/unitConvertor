# Gage Notargiacomo, Spring 2023
# This program utilizes the CustomKinter library that is a more modern version of the integrated Tkinter library
# The program generates a basic unit converter with a GUI that runs through CustomTkinter

import customtkinter
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class unitConvertor(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Sets screen size and title
        self.geometry("500x500")
        self.title("Unit Converter")
        
        # Presents a welcome message at top of page
        self.label = customtkinter.CTkLabel(master=self, text="Welcome to the Unit Converter", font=("Arial", 18, "underline"))
        self.label.pack(pady=10)

        # Creates an outer grid structure to hold inner frame and convert button
        self.outer_frame = customtkinter.CTkFrame(master=self,width=300, height=300)
        self.outer_frame.pack()

        # Creates multiple tabs to offer different unit types
        self.tabview = customtkinter.CTkTabview(master=self.outer_frame, height=100, width=350)
        self.tabview.pack(padx=5, pady=5)

        self.tabview.add("Distance")
        self.tabview.add("Mass") 
        self.tabview.add("Volume")
        self.tabview.set("Distance")  # set currently visible tab

        # Creates a set of instructions for the user
        self.instructions = customtkinter.CTkTextbox(master=self.outer_frame, height=230, width=350, font=("Arial", 13), wrap="word")
        self.instructions.pack(padx=5, pady=5)
        self.instructions.insert("0.0", "This is a classic unit converter that can be used to input " 
                                        "a certain value of one unit, and determine its equivalent value of a different unit.\n\n")
        self.instructions.insert("3.0", "In order to get started, insert a value in the left textbox.\n")
        self.instructions.insert("4.0", "Then, use the left drop down menu to determine the units you are converting from.\n")
        self.instructions.insert("7.0", "Next, select the unit you are converting to by using the right drop down menu.\n")
        self.instructions.insert("9.0", "To get your equivalent value simply click the convert button.\n")
        self.instructions.insert("11.0", "To change the type of measurement use the tabs at the top.\n\n")
        self.instructions.insert("12.0", "Enjoy! :)")
        self.instructions.configure(state="disabled")

        def convertDistanceUnits(self, og_units, new_units, value_in, right):
            # Centimeters will be the universal unit

            if (value_in == ""):
                value_in = 0
            value_in = float(value_in)
            
            match og_units:
                case "Inch":
                    value_in = value_in * 2.54
                case "Foot":
                    value_in = value_in * 30.48
                case "Yard":
                    value_in = value_in * 91.44
                case "Mile":
                    value_in = value_in * 160934.4            
                case "Meter":
                    value_in = value_in * 100.0
                case "Kilometer":
                    value_in = value_in * 100000.0       

            match new_units:
                case "Inch":
                    value_in = value_in / 2.54
                case "Foot":
                    value_in = value_in / 30.48
                case "Yard":
                    value_in = value_in / 91.44
                case "Mile":
                    value_in = value_in / 160934.4            
                case "Meter":
                    value_in = value_in / 100.0
                case "Kilometer":
                    value_in = value_in / 100000.0                        
            
            value_in = round(value_in, 3)

            right.delete(0, END)
            right.insert("insert", value_in)

        def convertMassUnits(self, og_units, new_units, value_in, right):
            # Grams will be the universal unit

            if (value_in == ""):
                value_in = 0
            value_in = float(value_in)
            
            match og_units:
                case "Pound":
                    value_in = value_in * 16.0
                case "Ton (US)":
                    value_in = value_in * 32000
                case "Microgram":
                    value_in = value_in * 0.000000035274
                case "Milligram":
                    value_in = value_in * 0.000035274            
                case "Gram":
                    value_in = value_in * 0.035274
                case "Kilogram":
                    value_in = value_in * 35.274       

            match new_units:
                case "Pound":
                    value_in = value_in / 16.0
                case "Ton (US)":
                    value_in = value_in / 32000
                case "Microgram":
                    value_in = value_in / 0.000000035274
                case "Milligram":
                    value_in = value_in / 0.000035274            
                case "Gram":
                    value_in = value_in / 0.035274
                case "Kilogram":
                    value_in = value_in / 35.274                          
            
            value_in = round(value_in, 3)

            right.delete(0, END)
            right.insert("insert", value_in)

        def convertVolumeUnits(self, og_units, new_units, value_in, right):
            # Milliliters will be the universal unit

            if (value_in == ""):
                value_in = 0
            value_in = float(value_in)
            
            match og_units:
                case "Teaspoon":
                    value_in = value_in * 4.929
                case "Tablespoon":
                    value_in = value_in * 14.787
                case "Ounce":
                    value_in = value_in * 29.574
                case "Cup":
                    value_in = value_in * 240.0            
                case "Quart":
                    value_in = value_in * 946.353
                case "Liter":
                    value_in = value_in * 1000.0       

            match new_units:
                case "Teaspoon":
                    value_in = value_in / 4.929
                case "Tablespoon":
                    value_in = value_in / 14.787
                case "Ounce":
                    value_in = value_in / 29.574
                case "Cup":
                    value_in = value_in / 240.0            
                case "Quart":
                    value_in = value_in / 946.353
                case "Liter":
                    value_in = value_in / 1000.0                        
            
            value_in = round(value_in, 3)

            right.configure("disabled")
            right.delete(0, END)
            right.insert("insert", value_in)

        def createTabInfo(self, menu_options, convert_func, tab_name, tempr):
            # Creates a grid structure to input widgets such as drop down menus
            frame = customtkinter.CTkFrame(master=self.tabview.tab(tab_name),width=10, height=10, fg_color="transparent")

            self.grid_rowconfigure((0, 1, 2), weight=1)
            self.grid_columnconfigure((0, 1, 2), weight=1)

            left = customtkinter.CTkEntry(master=frame, font=("Arial", 13, "bold"), placeholder_text="1.0")
            left.grid(row=0, column=0, sticky=NSEW, padx=10)
            equals = customtkinter.CTkLabel(master=frame, text="=", font=("Arial", 13, "bold"))
            equals.grid(row=0, column=1, sticky=NSEW, padx=10)
            right = customtkinter.CTkEntry(master=frame, font=("Arial", 13, "bold"), placeholder_text=tempr)
            right.grid(row=0, column=2, sticky=NSEW, padx=10) 

            drop_templ = customtkinter.StringVar(value=menu_options[1])
            drop_tempr = customtkinter.StringVar(value=menu_options[0])

            dropl = customtkinter.CTkOptionMenu(master=frame, font=("Arial", 13, "bold"), 
                                                dropdown_font=("Arial", 13, "bold"),
                                                values=menu_options,
                                                variable=drop_templ)
            dropl.grid(row=1, column=0, sticky=NSEW, padx=10)
            dropr = customtkinter.CTkOptionMenu(master=frame, font=("Arial", 13, "bold"), 
                                                dropdown_font=("Arial", 13, "bold"),
                                                values=menu_options,
                                                variable=drop_tempr)
            dropr.grid(row=1, column=2, sticky=NSEW, padx=10)

            frame.pack(pady=10)
            frame.pack()

            # Users push this button to convert their units
            convertor = customtkinter.CTkButton(master=frame, text="Convert", font=("Arial", 13, "bold"), 
                                        command=lambda: convert_func(self, dropl.get(), dropr.get(), left.get(), right))
            convertor.grid(row=2, column=0, sticky=NSEW, padx=10, columnspan=3)    

        distance_values = ["Inch", "Foot", "Yard", "Mile", "Centimeter", "Meter", "Kilometer"]
        mass_values=["Ounce", "Pound", "Ton (US)", "Microgram", "Milligram", "Gram", "Kilogram"]
        volume_values=["Teaspoon", "Tablespoon", "Ounce", "Cup", "Quart", "Milliliter", "Liter"]
        createTabInfo(self, distance_values, convertDistanceUnits, "Distance", "12.0")
        createTabInfo(self, mass_values, convertMassUnits, "Mass", "16.0")
        createTabInfo(self, volume_values, convertVolumeUnits, "Volume", "3.0")

app = unitConvertor()
app.mainloop()
