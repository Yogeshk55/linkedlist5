import random

def run_quiz(questions):
    score = 0
    random.shuffle(questions)

    for i, question in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {question['question']}")
        for j, option in enumerate(question['options'], start=1):
            print(f"{j}. {option}")

        user_answer = input("Your answer: ")

        if user_answer.lower() == question['answer'].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['answer']}")

    print(f"\nYou scored {score} out of {len(questions)} questions.")

if __name__ == "__main__":
    quiz_questions = [
        {
            'question': 'What is the capital of Italy?',
            'options': ['Berlin', 'Madrid', 'Paris', 'Rome'],
            'answer': 'Rome'
        },
        {
            'question': 'Solve the equation: 2 + 3 * 4',
            'options': ['14', '20', '32', '10'],
            'answer': '14'
        },
        {
            'question': 'Who developed the theory of relativity?',
            'options': ['Isaac Newton', 'Albert Einstein', 'Galileo Galilei', 'Stephen Hawking'],
            'answer': 'Albert Einstein'
        },
        {
            'question': 'Simplify: 5 * (2 + 3) - 4',
            'options': ['5', '20', '25', '15'],
            'answer': '25'
        },
        {
            'question':'solve the equation : 50**50(20+40)*98',
            'options':['14700000','13700000','14500000','1400000'],
            'answer':'14700000'
            },
    ]

    run_quiz(quiz_questions)
