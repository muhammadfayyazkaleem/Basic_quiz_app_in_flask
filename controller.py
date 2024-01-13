from flask import Flask, render_template, request

app = Flask(__name__)

class Question:

    def __init__(self, q_id, question, option_1, option_2, option_3, correct_option):
        self.q_id = q_id
        self.question = question
        self.option_1 = option_1
        self.option_2 = option_2
        self.option_3 = option_3
        self.correct_option = correct_option

    def get_correct_option(self):

        if self.correct_option == 1:
            return self.option_1
        elif self.correct_option == 2:
            return self.option_2
        else:
            return self.option_3
        

q1 = Question(1,"Which is a largest city of Pakistan?","Karachi","lahore","Multan",1)
q2 = Question(2,"Which is a largest river of pakistan?", "Indus River", "Sutleh River", "chaneb River",1)
q3 = Question(3, "The Capital of pakistan is :" , "Karachi", "Lahore", "Islamabad",3)
q4 = Question(4 , "The President of Pakistan is :", "Arif Alavi" , "Imran Khan " , "Junaid Kaleem", 1)
q5 = Question(5,"Which is a largest city of Pakistan?","Karachi","lahore","Multan",1)
q6 = Question(6,"Which is a largest river of pakistan?", "Indus River", "Sutleh River", "chaneb River",1)
q7 = Question(7, "The Capital of pakistan is :" , "Karachi", "Lahore", "Islamabad",3)
q8 = Question(8 , "The President of Pakistan is :", "Arif Alavi" , "Imran Khan " , "Junaid Kaleem", 1)
q9 = Question(9,"Which is a largest city of Pakistan?","Karachi","lahore","Multan",1)
q10 = Question(10,"Which is a largest river of pakistan?", "Indus River", "Sutleh River", "chaneb River",1)
q11 = Question(11, "The Capital of pakistan is :" , "Karachi", "Lahore", "Islamabad",3)
q12 = Question(12 , "The President of Pakistan is :", "Arif Alavi" , "Imran Khan " , "Junaid Kaleem", 1)


question_list = [ q1, q2, q3 , q4, q5, q6, q7, q8, q9, q10, q11, q12]

    

@app.route('/')
def quiz_home():
    return render_template('index.html', question_list = question_list)


@app.route('/quizsubmit', methods=['POST'])
def quiz_submit():

    count_correct_option = 0
    for question in question_list:
        question_id = str(question.q_id)
        selected_option = request.form[question_id]
        correct_option = question.get_correct_option()
        if selected_option == correct_option:
            count_correct_option = count_correct_option + 1

    return render_template("submitted.html", result = str(count_correct_option)+ '/' +str(len(question_list)))


if __name__ == '__main__':
    app.run(debug=True)