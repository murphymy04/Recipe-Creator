import tkinter as tk
from functools import partial
from PIL import ImageTk, Image

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
        self.master.config(bg="white")
        
        # background image
        self.image = Image.open("background4.jpg")
        self.resize = self.image.resize((500, 350))
        self.bg = ImageTk.PhotoImage(self.resize)
        self.bg_label = tk.Label(self.master, image=self.bg, border=0)
        self.bg_label.image = self.bg
        self.bg_label.grid(column=0, row=0, padx=(150))

        # main frame
        self.main_frame = tk.Frame(self.master, bg="white")
        self.main_frame.grid(column=1, row=0, padx=(50, 100), pady=350)

        # side frame
        self.side_frame = tk.Frame(self.master, highlightthickness=2, highlightbackground="green", bg="white")
        self.side_frame.grid(column=2, row=0, padx=(100, 0))

        # title
        self.title = tk.Label(self.main_frame, font=("Nexa", 30, "bold"), text="Pantry Pal", bg="white")
        self.title.grid(column=0, row=0, pady=(0, 15))

        # attribution
        self.image = Image.open("transparent.png")
        self.attribute = ImageTk.PhotoImage(self.image)
        self.attribute_label = tk.Label(self.main_frame, image=self.attribute, bg="white")
        self.attribute_label.grid(column=0, row=2, pady=8)
        
        # Entry bar
        self.query = tk.Entry(self.main_frame, width=50)
        self.query.insert(0, 'Enter Ingredients; Separate each with "and"')
        self.query.grid(column=0, row=1)

        # side title
        self.side_title = tk.Label(self.side_frame, font=("Nexa", 25, "underline", "bold"), text="Filters", bg="white")
        self.side_title.grid(column=0, row=0, pady=(0, 18))

        # diet dropdown menu
        self.diet_label = tk.Label(self.side_frame, text="Diet Options", bg="white")
        self.diet_label.grid(column=0, row=1)
        self.diet_choice = tk.StringVar(self.master)
        self.diet_menu = tk.OptionMenu(self.side_frame, self.diet_choice, *DIET_OPTIONS, command=diet_click)
        self.diet_menu.config(width=18)
        self.diet_menu.grid(column=0, row=2, padx=12, pady=(0, 12))

        # health dropdown menu
        self.health_label = tk.Label(self.side_frame, text="Health/Allergy Options", bg="white")
        self.health_label.grid(column=0, row=3)
        self.health_choice = tk.StringVar(self.master)
        self.health_menu = tk.OptionMenu(self.side_frame, self.health_choice, *HEALTH_OPTIONS, command=health_click)
        self.health_menu.config(width=18)
        self.health_menu.grid(column=0, row=4, padx=12, pady=(0, 12))

        # cuisine dropdown menu
        self.cuisine_label = tk.Label(self.side_frame, text="Cuisine Type", bg="white")
        self.cuisine_label.grid(column=0, row=5)
        self.cuisine_choice = tk.StringVar(self.master)
        self.cuisine_menu = tk.OptionMenu(self.side_frame, self.cuisine_choice, *CUISINE_OPTIONS, command=cuisine_click)
        self.cuisine_menu.config(width=18)
        self.cuisine_menu.grid(column=0, row=6, padx=12, pady=(0, 12))

        # meal dropdown menu
        self.meal_label = tk.Label(self.side_frame, text="Meal Type", bg="white")
        self.meal_label.grid(column=0, row=7)
        self.meal_choice = tk.StringVar(self.master)
        self.meal_menu = tk.OptionMenu(self.side_frame, self.meal_choice, *MEAL_OPTIONS, command=meal_click)
        self.meal_menu.config(width=18)
        self.meal_menu.grid(column=0, row=8, padx=12, pady=(0, 12))

        # randomize button
        self.rand_label = tk.Label(self.side_frame, text="Spice it Up!", bg="white")
        self.rand_label.grid(column=0, row=9)
        self.rand_button = tk.Button(self.side_frame, text="Randomize Results", bg="green", command=partial(self.Randomize, recipe_search))
        self.rand_button.grid(column=0, row=10, padx=12, pady=(0, 12))

        # search button
        self.search_button = tk.Button(self.main_frame, text="Go!", command=partial(self.Return_Query, recipe_search))
        self.search_button.grid(column=1, row=1, padx=(7, 0))
    

    def Return_Query(self, recipe_search):        
        recipe_search.query(input=self.query.get())
        recipe_search.search()
        # destroy window 1
        self.master.destroy()
        # create window 2
        self.new_window = tk.Tk()
        self.window2 = Window2(self.new_window)
    

    def Randomize(self, recipe_search):
        if recipe_search.is_random() == True:
            self.rand_button.config(bg="red")
            recipe_search.change_random(False)

        elif recipe_search.is_random() == False:
            self.rand_button.config(bg="green")
            recipe_search.change_random(True)

    

class Window2:

     def __init__(self, master):
        self.master = master
        self.master.title("Pantry Pal")
        self.width= self.master.winfo_screenwidth()
        self.height= self.master.winfo_screenheight()
        self.master.geometry("%dx%d" % (self.width, self.height))
        self.master.config(bg="white")
