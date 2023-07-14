from recipe_search import RecipeSearch
from functools import partial
from gui import Window1
import tkinter as tk

recipe_search = RecipeSearch()

def diet_clicked(diet_choice):
    recipe_search.diet(diet_choice)


def health_clicked(health_choice):
    recipe_search.health(health_input=health_choice)


def cuisine_clicked(cuisine_choice):
    recipe_search.cuisine_type(cuisine_input=cuisine_choice)


def meal_clicked(meal_choice):
    recipe_search.meal_type(meal_input=meal_choice)


def main():
    root = tk.Tk()
    window1 = Window1(master=root, diet_click=diet_clicked, health_click=health_clicked, cuisine_click=cuisine_clicked, meal_click=meal_clicked, recipe_search=recipe_search)
    root.mainloop()

main()

