import random

def load_questions(filepath):
    questions = []
    with open(filepath, 'r') as file:
        for line in file.readlines():
            question, answer_type, *choices = line.strip().split(',')
            if answer_type == 'multiple-choice':
                answer = choices.pop()
            else:
                answer = None
            questions.append({'question': question,
                             'answer_type': answer_type,
                             'choices': choices,
                             'answer': answer})
    return questions

def ask_question(question, answer_type, choices=None):
    print(question)
    if answer_type == 'multiple-choice':
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        answer = input("Enter your answer (number): ")
        try:
            answer = int(answer) - 1
        except ValueError:
            print("Invalid input. Please enter a number.")
            return ask_question(question, answer_type, choices)
        if answer < 0 or answer >= len(choices):
            print("Invalid choice. Please try again.")
            return ask_question(question, answer_type, choices)
        return choices[answer]
    else:
        return input("Enter your answer: ")

def evaluate_answer(question, answer_type, user_answer, correct_answer):
    is_correct = user_answer.lower() == correct_answer.lower()
    print("-" * 40)
    if is_correct:
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The correct answer is: {correct_answer}")
    return is_correct

def calculate_score(questions, is_correct_list):
    score = 0
    for i, question in enumerate(questions):
        if is_correct_list[i]:
            score += 1
    return score

def display_results(score, total_questions):
    print("-" * 40)
    print(f"Final score: {score} out of {total_questions}")

def play_again():
    answer = input("Do you want to play again? (yes/no): ").lower()
    return answer.startswith('y')

if __name__ == "__main__":
    quiz_name = "Quiz"
    topic = "Random"
    question_file = "quiz_questions.csv"  # Replace with your CSV file
