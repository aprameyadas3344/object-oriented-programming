pasta = ("pasta arrbiata", "Italian", 20, "medium" )
biriyani = ("chicken biriyani", "Indian", 45, "hard")
print("recipe 1:", pasta)
print("name", pasta[0])
print("cuisine", pasta[1])
print("difficulty", pasta[-1])


all_recipes = (pasta, biriyani)
print("\nFirst recipe name:", all_recipes[0][0])
print("Second recipe time:", all_recipes[1][2], "mins")
print("pasta details (sliced):", pasta[1:3])


print("\nPasta recipe details:")
for details in pasta:
    print(" -", details)


pasta_ingredients = {"tomato", "garlic", "olive oil", "chilli", "pasta", "garlic"}
biriyani_ingredients = {"rice", "chicken", "garlic", "onion", "tomato", "spices"}
print("\nPasta ingredients:", pasta_ingredients)
print("biriyani ingredients:", biriyani_ingredients)
print("Total pasta ingredients:", len(pasta_ingredients))
