from recipe_search import RecipeSearch
from gui import GUI

recipe_search = RecipeSearch()

def diet_clicked(diet_choice):
    recipe_search.diet(diet_choice)


def health_clicked(health_choice):
    recipe_search.health(health_input=health_choice)


def cuisine_clicked(cuisine_choice):
    recipe_search.cuisine_type(cuisine_input=cuisine_choice)


def meal_clicked(meal_choice):
    recipe_search.meal_type(meal_input=meal_choice)


gui = GUI(diet_click=diet_clicked, health_click=health_clicked)




