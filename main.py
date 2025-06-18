

movie:str = "Spider man"
rating_of_movie:int = 3
score:float = 72.65

if rating_of_movie >= 4 and score > 80:
    print("Highly recomnded")
elif  rating_of_movie >= 3 and score > 70:
    print("It is good")
elif rating_of_movie <= 2 and score > 60:
    print("You should check it out!")
else:
    print("Don't watch it. It is a waste of time")