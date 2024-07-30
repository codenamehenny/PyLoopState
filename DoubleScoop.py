#Task 1: Your Mood Tracker Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. 
# Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. For each time, randomly select a mood from a predefined list and print it. 
# Use the random module again to randomly select the mood.
import random

# lists for days of week, times of day and moods
DayOfWeek  = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
TimeOfDay = ["morning", "afternoon", "evening"]
moods = ["happy", "sad", "tired", "energetic"]

for day in range(7): # outer loop for each week day
    for time in range(3): # inner loop for each time of day
        mood = random.choice(moods) # random mood selected
        print(f"On {DayOfWeek[day]} {TimeOfDay[time]} you were feeling {mood}") # output for the mood at that day and time
