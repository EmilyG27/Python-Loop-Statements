# Task 1
import random
genres = ["Jazz", "Rock", "Hip-hop", "Classical"]
track = ["Track 1", "Track 2", "Track 3", "Track 4"]
while genres:
    if "Jazz":
        print(f"You are listening to {random.choice(track)} jazz music")
    if "Rock":
        print(f"You are listening to {random.choice(track)} rock music")
    if "Hip-hop":
        print(f"you are listening to {random.choice(track)} hip-hop music")
        break 
else:
    print(f"you are listening to {random.choice(track)} classical music")

for genre in range(1,4):
    if "Jazz":
        print(f"{random.choice(track)}: The light show is ready.")
    if "Rock":
        print(f"{random.choice(track)}: The light show is ready.")
    if "Hip-hop":
        print(f"{random.choice(track)}: The light show is ready.")
    else:
        continue