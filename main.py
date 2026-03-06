import random

questions = {
    "Who wrote Harry Potter?":"JK Rowling",
    "In Alice’s Adventures in Wonderland, what animal does Alice follow down the hole?":"White Rabbit",
    "Who is the author of The Diary of a Young Girl?":"Anne Frank",
    "In The Jungle Book, what is the name of the boy raised by wolves?":"Mowgli",
    "In Before the Coffee Gets Cold, what special ability does the café have?":"It allows people to travel through time.",
    "Who wrote Matilda?":"Roald Dahl",
    "In The Lion, the Witch and the Wardrobe, what magical object leads the children to Narnia?":"A Wardrobe",
    "Who wrote pride and prejudice?":"Jane Austen",
    "What is the name of the main character in Days at the Morisaki Bookshop?":"Takako",
    "In Treasure Island, what kind of treasure are the characters searching for?":"Pirate Treasure"
}

def trivia():
    questions_list =list(questions.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(questions_list,total_questions)
    for idx,question in enumerate(selected_questions):
        print(f"{idx + 1}.{question}")
        user_answer = input("Your Answer: ").title().strip()

        correct_answer = questions[question]
        if user_answer == correct_answer.title():
            print("Correct! \n")
            score += 1
        else:
            print(f"Oops! The correct answer is: {correct_answer}.\n")
    print(f"Game over.Your score is: {score}/{total_questions}")

trivia()


