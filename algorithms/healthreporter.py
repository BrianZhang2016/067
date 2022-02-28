def healthy(list):
    list[sleep, exercise, calories, screentime]
    if int(sleep) < 8:
        print("get some more sleep!")
    else:
        print("you are getting enough sleep :)")
    if int(exercise) < 30:
        print("stand up and go for a walk!")
    else:
        print("you are very active :)")
    if int(calories) < 2000:
        print("consume some more fats, carbs, protein!")
    else:
        print("you have good eating habits :)")
    if int(screentime) > 12:
        print("rest your eyes!")
    else:
        print("you are keeping your eyes healthy :)")

sleep = input('enter your hours of sleep: ')
exercise = input('enter your minutes of exercise: ')
calories = input('enter your amount of calories: ')
screentime = input('enter your hours of screentime: ')

healthy(list)