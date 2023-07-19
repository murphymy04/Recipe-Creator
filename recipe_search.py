from dotenv import load_dotenv
import os
import requests


class RecipeSearch:
    
    
    def __init__(self):
        load_dotenv()
        self.RECIPE_ID = os.getenv("recipe_id")
        self.RECIPE_KEY = os.getenv("recipe_key")
        self.PARAMS = {
            "type": "public",
            "app_id": self.RECIPE_ID,
            "app_key": self.RECIPE_KEY,
            "random": True
        }


    def query(self, input):
        self.PARAMS["q"] = input

    
    def diet(self, diet_input):
        self.PARAMS["diet"] = diet_input

    
    def health(self, health_input):
        self.PARAMS["health"] = health_input


    def cuisine_type(self, cuisine_input):
        self.PARAMS["cuisineType"] = cuisine_input
    

    def meal_type(self, meal_input):
        self.PARAMS["mealType"] = meal_input

    
    def is_random(self):
        return self.PARAMS["random"]
    
    def change_random(self, boolean):
        self.PARAMS["random"] = boolean


    def search(self):
        #self.response = requests.get("https://api.edamam.com/api/recipes/v2", params=self.PARAMS)
        #self.response.raise_for_status()
        #self.data = self.response.json()
        #print(self.data["hits"][0]["recipe"]["ingredientLines"])
        pass
