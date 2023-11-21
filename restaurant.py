import random

fast_food = [
    "Arbys",
    "Burger King",
    "Kentucky Fried Chicken",
    "Taco Bell",
    "McDonalds"
]

sit_down = [
    "Texas Roadhouse",
    "Olive Garden",
    "Apple Bees",
    "Friendly's",
    "Buca di Beppo"
]

while True:
    restaurant = random.randrange(0, 5)
    with open("/Users/paulmancini/Users/paulmancini/Desktop/CS361/CS361Microservice/venv/microservice.txt") as infile:
        rest_type = infile.read()
        if rest_type == "fast food":
            with open("/Users/paulmancini/Users/paulmancini/Desktop/CS361/"
                      "CS361Microservice/venv/Restuarant.txt", 'w') as outfile:
                outfile.write(fast_food[restaurant])
        if rest_type == "sit down":
            with open("/Users/paulmancini/Users/paulmancini/"
                      "Desktop/CS361/CS361Microservice/venv/Restuarant.txt", 'w') as outfile:
                outfile.write(sit_down[restaurant])
