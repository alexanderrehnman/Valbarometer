

class Party:

    def __init__(self, name, answers) :
        self.name = name
        self.answers = answers


    def get_name(self):
        return self.name
    
    def get_answers(self):
        return self.answers
            
points = [0,0]


#Få den här klassen att funka 
class Question:
    def __init__(self, question : str, answer : str, choices : list()):
        self.choices = choices
        self.question = question
        self.answer = answer
    
    def get_name(self):
        return self.question

    def get_answer(self):
        return self.answer

    def get_choices(self):
        return self.choices
    
    
    #Hur det skrivs ut:
    def play_question(self, number: int):
        global points

        #Skapar de olika partierna
        global lst
        p1 = ("mod", ["a", "b", "c", "c", "b"])
        p2 = ("soc", ["b", "c", "c", "a", "b"])
        p3 = ("mp" , ["a", "c"])
        lst = [p1, p2, p3]

       
        print("Frågan:")
        print(self.question)
        print()
        print("Svarsalternativ:")
        for i in self.choices:
            print(i)
        print()
        answer = input("Svara här: ")
        i = 0
        for partie in lst :
            if answer == partie.get_answer[number]:
                points[i] = points[i] + 1
            i +1
                
                       
#Ta in frågorna och splitta upp dem i fråga, svar, alternativ
def load_question():
    questions = []

    #försök att få split att fungera!!!
    with open("", "r", encoding="utf8") as f:
        for line in f.readlines():
            selection = line.split("/")
            quiz = Question(selection[0],
                            selection[1],
                            selection[2].split(","))
            
            questions.append(quiz)
    return questions



#mainfunktionen som pratar med användaren.
def main():
    round = 1    


    while True:
            start = input(f" är antalet frågor som du har valt.\nTryck Enter för att starta: ")
            print()
            print()
            
            if "" in start:
                pass

            question = load_question()
            for round in range(5):
                question[round].play_question(round)
            
            #går igenom points för att hitta platsen för vinnaren
            n = 0
            for i in range(len.points) :
                if points[i+1] > points[i]:
                    n = i +1
            global winningPartie 
            #tar ut namnet till vinnande parti
            winningPartie= lst[n].get_name()



if __name__ == "__main__":
    print("Hej och välkomen till Alex quiz!")
    main()
    


    print("-------------------")
    print(f"Tack för att du spelade du fick {winningPartie} poäng")

