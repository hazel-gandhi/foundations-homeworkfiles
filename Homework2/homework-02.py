## Hazel Gandhi
## 10/28/2024
## Homework 2

year = int(input("What is your year of birth?"))
if year <= 2024:
    print("You were born in", year)

    # Calculate the person's age to make the next queries easier
    user_age = 2024 - year
    print("Your age is", user_age)

    # Calculate how many times the user's heart has beaten
    heartbeat = user_age * 35000000
    print("Since", year, "your heart has beaten", heartbeat, "times")

    # How many times a blue whale's heart has beaten
    blue_whale = user_age * 13140000
    print("Since you were born, a blue whale's heart has beaten", blue_whale, "times")

    # How many times a rabbit's heart has beaten since then
    rabbit = user_age * 170 * 60 * 24 * 365
    print("Since you were born, a rabbit's heart has beaten", rabbit, "times")

    my_age = 24
    if user_age > my_age:
        print("You are", (user_age - my_age), "years older than me")
    else:
        print("You are", (my_age - user_age), "years younger than me")
    
    if year % 2 == 0:
        print("You were born in an even year")
    else:
        print("You were born in an odd year")

    # Presidents from the Democratic party since 1980
    presidents = [
        {"name": "Jimmy Carter", "start_year": 1977, "end_year": 1981},
        {"name": "Bill Clinton", "start_year": 1993, "end_year": 2001},
        {"name": "Barack Obama", "start_year": 2009, "end_year": 2017},
        {"name": "Joe Biden", "start_year": 2021, "end_year": 2024}
    ]
    
    # Determine which Democratic president was in office during birth year
    president_found = False
    for president in presidents:
        if president["start_year"] <= year <= president["end_year"]:
            print(f"When you were born, President {president['name']} was in office.")
            president_found = True
            break

    if not president_found:
        print("No Democratic president was in office when you were born.")
else:
    print("Year of birth cannot be in the future.")