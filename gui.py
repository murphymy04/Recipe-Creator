import tkinter as tk
from functools import partial

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

CUISINE_OPTIONS = [
    "American",
    "Asian",
    "British",
    "Caribbean",
    "Central Europe",
    "Chinese",
    "Eastern Europe",
    "French",
    "Indian",
    "Italian",
    "Japanese",
    "Mexican",
    "Middle Eastern",
    "Nordic",
    "South American",
    "South East Asian"
]

MEAL_OPTIONS = [
    "Breakfast",
    "Lunch",
    "Dinner",
    "Snack"
]


class Window1:
    

    def __init__(self, master, diet_click, health_click, cuisine_click, meal_click, recipe_search):
        # creating window
        self.master = master
        self.master.title("Pantry Pal")
        self.width= self.master.winfo_screenwidth()
        self.height= self.master.winfo_screenheight()
        self.master.geometry("%dx%d" % (self.width, self.height))

        # main frame
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(side=tk.TOP, pady=(self.height/4, 0))

        # side frame
        self.side_frame = tk.Frame(self.master)
        self.side_frame.pack(side=tk.RIGHT, padx=(0, 50))

        # title
        self.title = tk.Label(self.main_frame, font=("Nexa", 30, "bold"), text="Pantry Pal")
        self.title.pack(anchor="center", pady=(0, 25))
        
        # Entry bar
        self.query = tk.Entry(self.main_frame)
        self.query.pack(side=tk.LEFT)

        # diet dropdown menu
        self.diet_choice = tk.StringVar(self.master)
        self.diet_menu = tk.OptionMenu(self.side_frame, self.diet_choice, *DIET_OPTIONS, command=diet_click)
        #self.diet_menu.grid(row=2, column=0)
        self.diet_menu.pack()

        # health menu
        self.health_choice = tk.StringVar(self.master)
        self.health_menu = tk.OptionMenu(self.side_frame, self.health_choice, *HEALTH_OPTIONS, command=health_click)
        #self.health_menu.grid(row=2, column=1)
        self.health_menu.pack()

        # cuisine menu
        self.cuisine_choice = tk.StringVar(self.master)
        self.cuisine_menu = tk.OptionMenu(self.side_frame, self.cuisine_choice, *CUISINE_OPTIONS, command=cuisine_click)
        #self.cuisine_menu.grid(row=2, column=2)
        self.cuisine_menu.pack()

        # meal menu
        self.meal_choice = tk.StringVar(self.master)
        self.meal_menu = tk.OptionMenu(self.side_frame, self.meal_choice, *MEAL_OPTIONS, command=meal_click)
        #self.meal_menu.grid(row=2, column=3)
        self.meal_menu.pack()

        # search button
        self.search_button = tk.Button(self.main_frame, text="Go!", command=partial(self.Return_Query, recipe_search))
        #self.search_button.grid(row=1, column=5)
        self.search_button.pack(side=tk.LEFT)
    

    def Return_Query(self, recipe_search):
        recipe_search.query(input=self.query.get())
        recipe_search.search()
