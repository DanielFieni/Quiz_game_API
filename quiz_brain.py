import html

class QuizBrain:
    def __init__(self, q_question):
        self.number_question = 0
        self.question_list = q_question
        self.score = 0
    
    def finish_quiz(self):
        if(self.number_question < len(self.question_list)):
            return True
    
    def next_question(self):
        self.current_question = self.question_list[self.number_question]
        self.number_question += 1
        q_text = html.unescape(self.current_question.text)
        # to learn more about HTML entities: https://www.w3schools.com/html/html_entities.asp
        return f"Q{self.number_question}: {q_text}"
    
    def check_answer(self, answer_user):
        self.answer_correct = self.current_question.answer
        if answer_user.lower() == self.answer_correct.lower():
            self.score += 1
            return True
        else :
            return False