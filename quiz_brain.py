import html
from data import question_data

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        self.true_false= None
        self.next_question()

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        qui = f"Q.{self.question_number}: {html.unescape(self.current_question.text)}"
        return qui
        # user_answer = input(f"Q.{self.question_number}: {html.unescape(self.current_question.text)} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self, is_yes: str):
        correct_answer = self.current_question.answer
        print(correct_answer)
        if is_yes == correct_answer :
            self.score += 1
            self.true_false = True
        else:
            self.true_false = False
