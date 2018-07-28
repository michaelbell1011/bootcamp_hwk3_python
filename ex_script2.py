# * Create a dictionary to store the following:

#   * Your name
#   * Your age
#   * A list of a few of your hobbies
#   * A dictionary of a few times you wake up during the week

# * Print out your name, how many hobbies you have and a time you get up during the week

personal_info = {
    "name": "Michael Bell",
    "age": 28,
    "hobbies": ["data", "Rocket League", "Cooking", "Walking Maggie"],
    "wake_up_times" : {
        "M": 5,
        "T": 6,
        "W": 7
    }
}

print(personal_info)
print(personal_info ["name"])
print(str(len(personal_info ["hobbies"])) + " hobbies")
print(str(personal_info ["wake_up_times"]["M"]) + " AM")