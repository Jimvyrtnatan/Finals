import random

def quiz():
  questions = [
    "What is the capital of France?",
    "What is the square root of 16?",
    "Who wrote 'Romeo and Juliet'?",
    "What is the boiling point of water in Celsius?",
    "What is the derivative of (x^2)?",
    "What is the sum of the interior angles of a triangle?",
    "What is the chemical symbol for Iron?",
    "What is the speed of light in a vacuum?",
    "What is the name of the process by which plants make food?",
    "What is the smallest prime number?"
  ]
  answers = [  # Use a separate list for answers
    "Paris",
    "4",
    "William Shakespeare",
    "100°C",
    "2x",
    "180°",
    "Fe",
    "299,792,458 m/s",
    "Photosynthesis",
    "2"
  ]

  random_questions = random.sample(questions, 10)
  score = 0

  for question_index, question in enumerate(random_questions):
    print(question)
    user_answer = input("Your answer: ")
    if user_answer == answers[question_index]:
      print("Correct!")
      score += 1
    else:
      print("Incorrect. The correct answer is:", answers[question_index])

  print("Congratulations! You finished the quiz with", score, "out of 10 points.")

quiz()
