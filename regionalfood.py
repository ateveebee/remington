import webbrowser
import random


# Name of region, recipe, playlist, grocery list
# To do: fill out details of other regions, add more recipes for each region, add function to randomly select 3 regions for user to choose from, scrape web for recipes/playlists/grocery lists, graphic interface?


region = {

    'New Orleans': {'recipe': 'https://copykat.com/new-orleans-style-shrimp-and-grits/',
                    'grocery list': ['grits', 'whole milk', 'romano cheesee', 'butter', '1lb of large shrimp', 'garlic', 'worcestershire sauce', 'light-tasting beer',
                                    'cajun seasoning', 'crab/shrimp boil seasoning', 'thyme leaves', 'oregano', 'rosemary leaves'],
                    'playlist': 'https://www.youtube.com/watch?v=0wAMr3V5lN4&list=PL58D1905639B26DB8'},
    'Cajun': {'recipe': 'www.recipe.com', 'grocery list': ['chicken', 'onion', 'sausage'], 'playlist': 'www.playlist.com'},
    'Italian':{'recipe': 'www.recipe.com', 'grocery list': ['chicken', 'onion', 'sausage'], 'playlist': 'www.playlist.com'},
    'Mexican': {'recipe': 'www.recipe.com', 'grocery list': ['chicken', 'onion', 'sausage'], 'playlist': 'www.playlist.com'},
    'Greek': {'recipe': 'www.recipe.com', 'grocery list': ['chicken', 'onion', 'sausage'], 'playlist': 'www.playlist.com'},
    'Thai': {'recipe': 'www.recipe.com', 'grocery list': ['chicken', 'onion', 'sausage'], 'playlist': 'www.playlist.com'},
    'Chinese': {'recipe': 'www.recipe.com', 'grocery list': ['chicken', 'onion', 'sausage'], 'playlist': 'www.playlist.com'},
    'French': {'recipe': 'www.recipe.com', 'grocery list': ['chicken', 'onion', 'sausage'], 'playlist': 'www.playlist.com'},
    'Indian': {'recipe': 'www.recipe.com', 'grocery list': ['chicken', 'onion', 'sausage'], 'playlist': 'www.playlist.com'},
    'Japanese': {'recipe': 'www.recipe.com', 'grocery list': ['chicken', 'onion', 'sausage'], 'playlist': 'www.playlist.com'},

    }

#**** Open Brower and save shopping list *****

#shopping_list = region['New Orleans']['grocery list']
#open_nola_recipe = webbrowser.open(region['New Orleans']['recipe'])
#open_nola_playlist = webbrowser.open_new(region['New Orleans']['playlist'])

#with open('Shopping_List.txt', 'w') as f:
    #f.write('Here is your shopping list:\n\n')
    #for items in shopping_list:
        #f.write("O -- %s\n" % items)


random_region = random.sample(list(region), 3)
random_region_string = ' \n'.join(random_region)

#print(random_region)
print('Here are your choices:\n')
print(f'{random_region_string}\n')
print('Which would you like to choose?\n')

answer = input()

print(f'you chose {answer}, here is your recipe!')
