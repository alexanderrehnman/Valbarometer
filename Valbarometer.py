# imports

# globals
points = [0,0]


class Party:

    def __init__(self, name, answers) :
        self.name = name
        self.answers = answers


    def get_name(self):
        return self.name
    
    def get_answers(self):
        return self.answers
        
class Question:
    def __init__(self, question : str, choices : str, answer : list()):
        self.choices = choices
        self.question = question
        self.answer = answer
    
    def get_name(self):
        return self.question

    def get_answer(self):
        return self.answer

    def get_choices(self):
        

        return self.choices

        

    def play_question(self, number: int):
        """What the user sees when the code is executed, 
            and how the points get added to every party. 

        Args:
            number (int): Saving the points in number(list) if answer = party.get_answers.
        """
        print("Frågan:")
        print(self.question)
        print()
        print("Svarsalternativ:")
        for i in self.choices:
            print(i)
        print()
        answer = input("Svara här: ")

        # lägger till poäng i de partiet som matchar med svaret
        i = 0
    
        for party in lst :
            if answer == party.get_answers()[number]:
                points[i] = points[i] + 1
            i = i +1
                                  

def load_question():
    """file manager that takes information from a file and then splits it into question objects.

    Returns:
        questions(list): saves the questions in a list from the file that later gets splited into questions and answers.
            
    """
    questions = []
    with open("valfragor.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            selection = line.split("/")
            quiz = Question(selection[0],
                            selection[2].split(","),
                            selection[1])


            questions.append(quiz)
    return questions



# mainfunktionen som pratar med användaren.
def main(): 

    """_summary_
    """

    global points
    points = [0, 0, 0]

    # Skapar de olika partierna
    global lst 
    p1 = Party("djurpartiet", ["a", "c", "a", "c", "b"])
    p2 = Party("spelpartiet", ["b", "a", "b", "c", "c"])
    p3 = Party("vinterpartiet", ["c", "c", "c", "a", "b"])
    lst = [p1, p2, p3]

    round = 1    
    run = True

    while run:
        start = input(f"\nTryck Enter för att starta: ")
        print()
        print()
        
        if "" in start:
            pass

        question = load_question()
        for round in range(5):
            question[round].play_question(round)
        
        # går igenom points för att hitta platsen för vinnaren
        n = 0
        tie = False
        global winningParty 
        for i in range(len(points)-1) :
            if points[i+1] > points[i]:
                n = i +1
                tie == False
            if points[i+1] == points[i] and points[n] <= points[i]:
                tie = True


        # tar ut namnet till vinnande parti
        if tie == True:
            winningParty = lst[n].get_name() + " & " + lst[n+1].get_name()
        if tie == False:
            winningParty= lst[n].get_name()
        run = False

    

if __name__ == "__main__":
    print("Valbarometer!")
    main()
    


    print("-------------------")
    print(f"Tack för att du körde vårat program, ditt parti blev: {winningParty}")

