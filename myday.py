import random
import queue


class MyDay:
    def __init__(self):
        self.state = "Sleep"
        self.energy = 100
        self.hunger = 0
        self.event_queue = queue.Queue()

    def add_event(self, event):
        self.event_queue.put(event)

    def states(self):
        for hour in range(24):
            if self.state == "Sleep":
                if random.random() > 0.5 and hour == 7:
                    print("Ah.., a new day")
                elif hour == 8:
                    print("Oh my god, I didn't wake up in time again.")
                    self.state = "Eat"
                else:
                    print("zzz...")

            elif self.state == "Eat":
                if hour == 9:
                    print("Good breakfast, full and satisfied.")
                    self.state = "Work"
                elif self.hunger >= 70:
                    print("Wow, I'm really hungry, I need to eat something.")
                    self.state = "Eat"
                else:
                    self.hunger += random.randint(5, 15)
                    print("Hmm, something tasty was...")

            elif self.state == "Work":
                if hour == 17:
                    print("Finally, the working day is over.")
                    self.state = "Rest"
                else:
                    print("I work hard...")

            elif self.state == "Rest":
                if random.random() > 0.7:
                    print("Received a phone call.")
                    self.state = "Phone Call"
                elif hour == 20:
                    print("Fun time! I start playing favorite game.")
                    self.state = "Entertainment"
                else:
                    print("Resting...")

            elif self.state == "Phone Call":
                print("Talking on the phone...")
                if random.random() > 0.5:
                    print("The conversation ended. I continue to rest.")
                    self.state = "Rest"
                else:
                    print("Important news has arrived. I switch to work")
                    self.state = "Work"

            elif self.state == "Entertainment":
                if random.random() > 0.8:
                    print("I have lot of energy, I continue to play.")
                elif random.random() > 0.6:
                    print("Finished playing. I start watching the movie.")
                    self.state = "TV"
                else:
                    print("I'm bored, I need to do something interesting")
                    self.state = "Unexpected guests"

            elif self.state == "TV":
                print("Oops! I accidentally broke the TV!")
                print("I need to fix it or buy a new one.")
                self.state = "Rest"

            elif self.state == "Unexpected guests":
                print("Someone knocked on my door.")
                if random.random() > 0.5:
                    print("My friends came to my house and we spend time together.")
                    self.state = "Entertainment"
                else:
                    print("My friends left my house. Back to entertainment.")
                    self.state = "Entertainment"

            self.energy -= random.randint(1, 6)
            if self.energy <= 10:
                print("I am very tired. It's time to sleep.")
                self.state = "Sleep"

            print(f"Hour: {hour}, State: {self.state}\n")


my_day = MyDay()

# Simulate events
my_day.add_event("Phone Call")
my_day.add_event("Unexpected guests")


# Simulate the day
my_day.states()

