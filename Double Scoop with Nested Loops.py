# Task 1
import random

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
times = ["morning", "afternoon", "evening"]
moods = ["happy", "sad", "energetic", "calm"]

for i in days:
    for x in times:
        print(f"On {i} {x} you were {random.choice(moods)}")
