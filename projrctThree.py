import tkinter as tk
import random
from tkinter import messagebox

class TruthOrDare:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Truth or Dare")
        self.window.geometry("400x300")
        self.window.configure(background="lightblue")

        self.menu = tk.Menu(self.window)
        self.window.config(menu=self.menu)
        self.menu.add_command(label="Settings",command=self.settings_window)
        self.menu.add_command(label="Options",command=self.option_window)

        self.start_label = tk.Label(self.window,text="Truth or Dare", font=("Arial",24), fg="red", bg="blue")
        self.start_label.pack()
        self.start_button = tk.Button(self.window,text="Start", command=self.start_game, bg="black", fg="white")
        self.start_button.pack()
        self.settings_button = tk.Button(self.window, text="Settings", command=self.settings_window, bg="black", fg="white")
        self.settings_button.pack()
        self.option_button = tk.Button(self.window, text="Options", command=self.option_window, bg="black", fg="white")
        self.option_button.pack()

        self.label = tk.Label(self.window, text="Truth or Dare", font=("Arial", 24))
        self.label.pack()
        self.truth_button = tk.Button(self.window, text="Truth", command=self.truth_selected)
        self.truth_button.pack()
        self.dare_button = tk.Button(self.window, text="Dare", command=self.dare_selected)
        self.dare_button.pack()
        self.text_area = tk.Text(self.window, height=10, width=40)
        self.text_area.pack()
        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit_answer)
        self.submit_button.pack()
        self.animation_label = tk.Label(self.window, text="", font=("Arial", 24))
        self.animation_label.pack()
        self.window.mainloop()
    def settings_window(self):
        self.settings_window =tk.Toplevel(self.window)
        self.settings_window.title("Settings")
        self.settings_window.configure(background="#FF69BA")

        self.settings_label =tk.Label(self.settings_window, text="Name:",font=("Arial",12), fg="#FFFFFF",bg="#FF69B4")
        self.settings_label.pack()
        self.name_entry =tk.Entry(self.settings_window, font=("Arial",12))
        self.name_entry.pack()
    def option_window(self):
        self.option_window = tk.Toplevel(self.window)
        self.option_window.title("Options")
        self.option_window.configure(background="#FF69BA")

        self.option_label = tk.Label(self.option_window, text="Music", font=("Arial",12),fg="#FFFFFF", bg="#FF69B4")
        self.option_label.pack()
        self.music_option = tk.Checkbutton(self.option_window, text="Music", font=("Arial",12),fg="#FFFFFF", bg="#FF69B4")
        self.music_option.pack()
        self.sound_option = tk.Checkbutton(self.option_window, text="Sound", font=("Arial",12), fg="#FFFFFF", bg="#FF69B4")
        self.sound_option.pack()
    def start_game(self):
        pass

    def truth_selected(self):
        self.animation_label.config(text="You selected Truth!")
        self.animation_label.after(1000, self.generate_question)

    def dare_selected(self):
        self.animation_label.config(text="You selected Dare!")
        self.animation_label.after(1000, self.generate_task)

    def generate_question(self):
        questions = [ "What's the weirdest thing you've ever been asked on a dare?", "What's the worst habit a potential partner could have?",
                      "What is your favorite hobby?","Would you hook up with your high school crush today?","What's the most childish thing that you still do as an adult?",
                      "What's something you've never told anyone, not even your closest friend?","What's the last lie you told?","Who is the person you'll never date?",
                      "When last did you have sex?","What is your body count?","Have you ever cheated on your partner?","One ex you'd date again?","Who gave you the best sex?",
                      "Have you ever had a one night stand?","Who would you sleep with without protection","Something you don't like about you current partner?",
                      "What is Your D size?","The last person you hooked up with?","Have you ever dated a teacher?","Would you date someone TWICE YOUR AGE?",
                      "Have you ever been in a Threesome?","Someone you are secretly in love with?","How many sex toys do you have?","Do you enjoy dirty talk?","What is you favorite sex position?",
                      "What is your least favorite sex position?","Have you ever been caught masturbating?","What's the weirdest place you've had sex?",
                      "When was the last time you were in a friend-with-benefits situation?","What's the most attractive thing about the opposite sex that will forever keep you from batting for the same team?",
                      "have you ever looked up a celebrity Sextape?","What's your biggest fantasy in the bedroom?","Which sexual act do you really excel at?","Have you ever had angry sex... and liked it?"]
        question = random.choice(questions)
        self.text_area.insert(tk.END, question)

    def generate_task(self):
        tasks = ["Do 10 jumping jacks", "Sing a silly song", "Do a funny dance","jack off","Take of your top","Only answer yes for an hour","Exchange an item of clothing with the player on your right",
                 "Attempt the first TikTok dance that appears on your for you page.","Eat one teaspoon of the spiciest thing you can find","Drink a shot of vinegar.",
                 "Send a weird GIF to the 10th person on your contacts list","Use a voice changing filter and send a funny voice message to your ex","Get back with your ex",
                 "Let's Do a Sextape","Freestyle rap about our relationship.","Go live on any social media account and declare your love for me","Send nudes","Delete whatsapp"
                 "Twerk along to a boring song until the music stops","Let your partner give you a makeover","Give a Bj","Take Off your underware","Let's vidoe call topless"
                 "Put on a blindfold and eat whatever your partner gives you","Put two drops of the spiciest sauce on your tongue","Send your ex a message saying you miss them",
                 "Make eye contact with the person to your right and moan for 10 seconds","Ask a stranger for advice on a strange rash you’ve recently developed","Send a text to your partner saying it's over",
                 "Make your orgasm face the next stranger you see until they make eye contact with you","Seductively eat a banana whilst locking eyes with the person to your left","Strip and dance",
                 "Send one of your parents a sext and don’t reply for one hour","Pass your phone to the person on your left and let them post a sexual status to your Facebook","Drink the whole bottle",
                 "Perform a seductive dance in front of the group","Pick up the nearest object to you and demonstrate how to put on protection","Close your eyes, pick a random phone contact and leave them a dirty voicemail",
                 "Drop an ice cube in your pants","Google the dirtiest thing you can think of and show it to the person next to you","FaceTime your most recent contact, burp, then hang up","Show your Private part",
                 "Smell everyone’s armpits and rank them from best to worst","Tell us the one bedtime secret no one knows about you.","kiss the person next to you","fart","Phone sex","Text your crush","Finger me for 5 minutes",
                 "Make me cum","Bj then swallow","Put your hands in your Private part","Send your parents random nudes from the internet"]
        task = random.choice(tasks)
        self.text_area.insert(tk.END, task)

    def submit_answer(self):
        answer = self.text_area.get("1.0", "end-1c")
        if answer:
            self.animation_label.config(text="Great job! You answered: " + answer)
            self.animation_label.after(1000, self.clear_text_area)
        else:
            self.animation_label.config(text="Please enter an answer!")

    def clear_text_area(self):
        self.text_area.delete("1.0", "end")

if __name__ == "__main__":
    game = TruthOrDare()
    game.window.mainloop()