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
        

q1 = Question(1,"What does the len() function in Python do?","Returns the last element of a list","Returns the length of a sequence","Rounds a floating-point number",2)

q2 = Question(2,"What is the purpose of the __init__ method in a Python class?", "Initializes the class object", "Defines class variables", "Performs mathematical operations",1)

q3 = Question(3, "What does the import keyword do in Python?" , "Imports a module or a package", "Defines a new variable", "Creates a loop",1)

q4 = Question(4 , "What does the range() function in Python generate?", "A range object representing a sequence of numbers" , "A list of numbers" , "A random number", 1)

q5 = Question(5,"What is the purpose of the __str__ method in Python?","Converts an object to a string","Computes the square root of a number","Checks if two objects are equal",1)

q6 = Question(6,"What does the pop() method do in Python?", "Adds an element to the end of a list", "Removes and returns the last element from a list", "Reverses the order of elements in a list",2)



question_list = [ q1, q2, q3 , q4, q5, q6]

    

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