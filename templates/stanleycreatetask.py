def healthy(list):
    list[checkup, eyeDoctor, screens, diet, water, exercise, sleep, drugs, alcohol, smoke, depression,]

    if int(checkup) > 12:
        print("please schedule annual checkup with your doctor asap")
    else:
        print("continue keeping track of annual checkups")

    if int(eyeDoctor) > 24:
        print("please schedule eye doctor appointment asap")
    else:
        print("continue keeping track of eye exams")

    if int(screens) > 8:
        print("try to decrease screen time to 8 hours or less each day")
    else:
        print("your screen time is suitable")

    if diet == 'no':
        print("try to consume balanced levels of fruits, vegetables, and red meats")
    else:
        print("keep up your balanced diet")

    if int(water) < 3:
        print("try to drink at least 3 liters of water a day")
    else:
        print("keep drinking lots of water")

    if exercise == 'no':
        print("try exercising 30 minutes at least 3+ days each week")
    else:
        print("keep exercising 30 minutes at least 3+ days each week")

    if int(sleep) < 7.5:
        print("try to get at least 7.5 hours of sleep each night")
    else:
        print("continue getting 7.5+ hours")

    if int(drugs) > 1:
        print("please don't do drugs")
    else:
        print("stay drug free")

    if int(alcohol) > 3:
        print("drinking is okay, but try to cut back")
    else:
        print("keep up good drinking habits")

    if int(smoke) > 3:
        print("try to cut back on how much you smoke")
    else:
        print("try to quit smoking, and if you don't smoke already good job")

    if depression == 'yes':
        print("talk to friends/family or seek professional help")
    else:
        print("stay happy and keep making friends")




checkup = input('how many months since last annual checkup')
eyeDoctor = input('how many months since last eye checkup')
screens = input('on average, how many hours do you use screens')
diet = input('are you eating healthy portions of fruits, vegetables, and red meats')
water = input('how many liters of water do you drink each day')
exercise = input('do you exercise at least 30 minutes for 3+ days a week')
sleep = input('on average, how many hours of sleep do you get each night')
drugs = input('how many times a week do you use drugs')
alcohol = input('how many times a week do you consume alcohol')
smoke = input('how many times a week do you smoke')
depression = input('have you experienced signs of depression/anxiety recently')


healthy(list)