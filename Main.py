import time
import textwrap
import random

class InterviewCoach:
    def __init__(self):
        self.name = ""
        self.interview_history = []
        self.current_question = 0
        self.questions = [
            "Tell me about yourself",
            "What are your greatest strengths?",
            "What is your biggest weakness?",
            "Why do you want this position?",
            "Where do you see yourself in 5 years?",
            "Tell me about a challenge you overcame",
            "Why should we hire you?",
            "Do you have any questions for us?"
        ]
        self.feedback = [
            "Good start! Try to be more specific with your examples.",
            "Nice answer! Consider connecting this to the job requirements.",
            "Good self-awareness. Now suggest how you're improving in this area.",
            "Great enthusiasm! Add what specifically excites you about this role.",
            "Good vision. Relate this back to how the company can help you grow.",
            "Well explained. Quantify the results if possible.",
            "Strong closing! Emphasize your unique value one more time.",
            "Excellent questions! Shows you've done your research."
        ]

    def display_welcome(self):
        print("\033[1;36m" + r"""
  __  __            _        __  __       _        _   
 |  \/  |          | |      |  \/  |     | |      | |  
 | \  / | ___   ___| | _____| \  / | ___ | |_ __ _| |_ 
 | |\/| |/ _ \ / __| |/ / __| |\/| |/ _ \| __/ _` | __|
 | |  | | (_) | (__|   <\__ \ |  | | (_) | || (_| | |_ 
 |_|  |_|\___/ \___|_|\_\___/_|  |_|\___/ \__\__,_|\__|
        """ + "\033[0m")
        print("Welcome to your interview preparation session!")
        print("I'll ask common interview questions and give you feedback after each answer.\n")
        self.name = input("First, what's your name? ").strip()
        print(f"\nNice to meet you, {self.name}! Let's begin when you're ready.\n")
        input("Press Enter to start your interview...")
        print("-" * 60)

    def ask_question(self, index):
        q = self.questions[index]
        print(f"\n\033[1;34mQuestion {index+1}/{len(self.questions)}:\033[0m")
        print(f"\033[1;32m{q}\033[0m\n")
        return input("Your answer: ")

    def give_feedback(self, index, answer):
        print("\n\033[1;35mFeedback:\033[0m")
        print(f"\033[3m{self.feedback[index]}\033[0m")
        
        # Show sample answer 50% of the time
        if random.random() > 0.5:
            print("\n\033[1;33mExample approach:\033[0m")
            samples = {
                0: f"I'm {self.name}, a [Your Major] student at [University]. I've developed [Skill 1] and [Skill 2] through my experience at [Project/Job]. I'm particularly proud of [Specific Achievement] which demonstrates my [Relevant Quality].",
                1: "My key strengths include [Strength 1], [Strength 2], and [Strength 3]. For example, when I [Specific Example], I was able to [Positive Outcome] which resulted in [Quantifiable Result].",
                6: f"You should hire me because my combination of [Skill 1] and [Skill 2] aligns perfectly with your needs. My experience with [Relevant Experience] has prepared me to contribute immediately to [Specific Company Goal]."
            }
            if index in samples:
                print(textwrap.fill(samples[index], width=70))
        
        print("\n" + "-" * 60)

    def show_menu(self):
        print("\nChoose next action:")
        print("1. Next question")
        print("2. Re-answer this question")
        print("3. Review history")
        print("4. End interview")
        
        while True:
            choice = input("Enter choice (1-4): ")
            if choice in ['1', '2', '3', '4']:
                return int(choice)
            print("Invalid choice. Please enter 1-4")

    def run_interview(self):
        self.display_welcome()
        
        while self.current_question < len(self.questions):
            # Ask question and get answer
            answer = self.ask_question(self.current_question)
            self.interview_history.append((self.questions[self.current_question], answer))
            
            # Give feedback
            self.give_feedback(self.current_question, answer)
            
            # Show navigation options
            choice = self.show_menu()
            
            if choice == 1:  # Next question
                self.current_question += 1
            elif choice == 2:  # Re-answer
                continue
            elif choice == 3:  # Review history
                self.review_history()
            elif choice == 4:  # End interview
                print("\nInterview ended. Good luck with your real interview!")
                return
                
        print("\n\033[1;32mCongratulations! You've completed the practice interview!\033[0m")
        print("Here's your final history review:")
        self.review_history()

    def review_history(self):
        print("\n\033[1;35m" + "=" * 60)
        print(" INTERVIEW HISTORY REVIEW ".center(60))
        print("=" * 60 + "\033[0m")
        
        for i, (question, answer) in enumerate(self.interview_history):
            print(f"\n\033[1;34mQuestion {i+1}: {question}\033[0m")
            print(f"\033[1;32mYour Answer:\033[0m {answer}")
            print("-" * 60)
        
        input("\nPress Enter to return to your interview...")

if __name__ == "__main__":
    coach = InterviewCoach()
    coach.run_interview()