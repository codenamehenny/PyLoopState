#Task 1: Your Mood Today Write a program that prints off different moods for each day of the week. 
# Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through every day of the week and for each day, randomly select a mood from the list and print it. 
#Ensure that your program includes the use of the random module to select the mood.
import random

# lists for days of week and moods
DayOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
moods = ["happy", "sad", "energetic", "calm"]

for day in range(7): # goes through loop 7 times for each day of week
    mood = random.choice(moods)  # random mood selected for each loop
    print(f"On {DayOfWeek[day]}, you were feeling {mood}") #prints both the day in position and a random mood for that day