from random import randint
"""
This class is responsible for sorting through a list of problems and making a dictionary of the questions and answers.
"""
class QuestionMaker:

    def sort(self, path, delineater):
        """
        The DataSorter class takes a file path, which tells it where to open the file containing a list of
        problems/questions as well as a delineater to tell it where the line between questions and answers should be drawn.
        """
        questionDict = {}
        file = open(path, "r")
        for line in file:
            tempList = line.split(delineater, 1)
            if ("\n" in tempList[1]):
                tempList[1] = tempList[1].replace("\n", '', 1)
            questionDict[tempList[0]] = tempList[1]
        return questionDict

    def createQuestions(self, questionDict):
        """
        This method takes a dictionary of questions and answers and turns it into a multiple choice quiz
        """
        questList = [""] * 5
        for x in range(0, 5):
            quizNumb = randint(0, len(questionDict))
            vocabWord = str(list(quiz_questions.items())[quizNumb][0])
            formattedVocabWord = self.formatString(vocabWord)
            question = str(x + 1) + ". What does the Latin word " \
                   + formattedVocabWord + " mean?" + '\n'
            answerNum = randint(0, 3)
            for y in range(0, 4):
                if y is answerNum:
                    answer = str(y + 1) + ". " \
                    + self.formatString(str(quiz_questions.get(vocabWord)).replace(" ", '', 2)) + '\n'
                else:
                    randomAnswer = list(quiz_questions.values())[randint(0, len(questionDict))]
                    answer = str(y + 1) + ". " + self.formatString(str(randomAnswer)) + '\n'

                question += answer

            questList[x] = question
        return questList

    def formatString(self, string):
        formatedString = string.replace('\n', "")
        length = len(formatedString) - 1
        while formatedString[0] == " ":
            formatedString = formatedString[1:length]
            length -= 1
        length = len(formatedString) - 1
        while formatedString[length] == " ":
            formatedString = formatedString[0:length]
            length =- 1
        return formatedString

path = "LatinWords.txt"
quiz = QuestionMaker()
quiz_questions = quiz.sort(path, ":")
latinQuestions = quiz.createQuestions(quiz_questions)
for string in latinQuestions:
    print(string)