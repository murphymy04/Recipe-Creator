import tkinter as tk

DIET_OPTIONS = [
    "balanced",
    "high-fiber",
    "high-protein",
    "low-carb",
    "low-fat",
    "low-sodium"
]

HEALTH_OPTIONS = [
    "alcohol-free",
    "celery-free",
    "crustacean-free",
    "dairy-free",
    "DASH",
    "egg-free",
    "fish-free",
    "gluten-free",
    "immuno-supportive",
    "keto-friendly",
    "kidney-friendly",
    "kosher",
    "low-potassium",
    "low-sugar",
    "Mediterranean",
    "mustard-free",
    "no-oil-added",
    "paleo",
    "peanut-free",
    "pescatarian",
    "pork-free",
    "red-meat-free",
    "sesame-free",
    "shellfish-free",
    "soy-free",
    "tree-nut-free",
    "vegan",
    "vegetarian",
    "wheat-free"
]


class GUI:
    

    def __init__(self, diet_click, health_click):
        # creating window
        self.window = tk.Tk()
        self.window.title("Recipy")
        self.width= self.window.winfo_screenwidth()
        self.height= self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (self.width, self.height))
        
        # Entry bar
        self.query = tk.Entry()
        self.query.grid(row=1, column=0, columnspan=4)

        # diet dropdown menu
        self.diet_choice = tk.StringVar(self.window)
        self.diet_menu = tk.OptionMenu(self.window, self.diet_choice, *DIET_OPTIONS, command=diet_click)
        self.diet_menu.grid(row=2, column=0)

        # health menu
        self.health_choice = tk.StringVar(self.window)
        self.health_menu = tk.OptionMenu(self.window, self.health_choice, *HEALTH_OPTIONS, command=health_click)
        self.health_menu.grid(row=2, column=1)

        
        self.window.mainloop()

