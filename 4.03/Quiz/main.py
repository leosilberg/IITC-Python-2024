from random import shuffle
from pathlib import Path

class Quiz:
    def __init__(self,question:str,options:dict,answer:str) -> None:
        self.question=question
        self.options=options
        self.answer=answer
    
    def __str__(self):
        return f"\n{self.question}\n{" ".join("{}) {} ".format(k,v.strip()) for k,v in self.options.items())}"

class User:
    def __init__(self) -> None:
        self.answers=[]
    
    def answer(self,answer:str):
        self.answers.append(answer)
        
class Game:
    def __init__(self) -> None:
        self.quiz_list=self.loadQuizes()
            
    def loadQuizes(self)->list:
        with  Path(__file__).with_name('quizes.txt').open("r") as file:
            lines=[line.strip() for line in file.readlines()]
            return [Quiz(quiz[0],dict(option.split(") ") for option in quiz[1:5]),quiz[5].split(": ")[1]) for quiz in [lines[i:i+6] for i in range(0,len(lines),6)]]
                
    def pickDifficulty(self):
        self.user=User()
        difficulty={"1","2","3"}
        while True:
            choice=input("Choose a difficulty\n1) Easy\n2) Medium\n3) Hard\n")
            if choice in difficulty:
                shuffle(self.quiz_list)
                self.difficulty_quiz_list= self.quiz_list[::4-int(choice)]
                break
        
    def start(self):
        for quiz in self.difficulty_quiz_list:
            print(quiz)
            while True:
                answer=input("Enter your answer or q to exit:\n").upper()
                if(answer.lower()=="q"):
                    return
                if answer in quiz.options.keys():
                    self.user.answer(answer)  
                    break   
                print(f"{answer} is not a valid option")
     
    def checkAnswers(self):
        return [ answer for index,answer in enumerate(self.user.answers) if answer==self.difficulty_quiz_list[index].answer]
    
    def displayResults(self):
        print(f"\nQuiz complete! You scored {len(self.checkAnswers())} out of {len(self.user.answers)}.\nThank you for playing!\n")
        
    def displaySummary(self):
        print("Quiz summary")
        print("\n".join([f"\n{self.difficulty_quiz_list[index].question}\nCorrect Answer: {self.difficulty_quiz_list[index].options[self.difficulty_quiz_list[index].answer]}\nYour Answer: {self.difficulty_quiz_list[index].options[answer]}" for index,answer in enumerate(self.user.answers)]))
    
if __name__=="__main__":   
    print("Welcome to the Python Quiz Game!\nYou will be presented with multiple-choice questions.\nEnter the letter corresponding to your answer.") 
    game=Game()
    while True:
        game.pickDifficulty()
        game.start()
        game.displaySummary()
        game.displayResults()
        menu=input(f"\nPlay another game? Y or N\n")
        if menu.lower()=="n":
            break
