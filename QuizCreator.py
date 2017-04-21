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

    def formatString(self, string):
        """
        Removes any end characters, starting spaces, or end spaces
        """
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

    def createQuestions(self, questionDict):
        """
        This method takes a dictionary of questions and answers and turns it into a multiple choice quiz
        It returns a tuple of both a list of five questions and a list of four options for each question
        """
        questList = [None] * 5
        tempAnswerList = [None] * 4
        correctAnswerList = [None] * 5
        multipleChoiceList = [None] * 5
        for x in range(0, 5):
            quizNumb = randint(0, len(questionDict))
            vocabWord = str(list(questionDict.items())[quizNumb][0])
            formattedVocabWord = self.formatString(vocabWord)
            question = "What does the Latin word " + formattedVocabWord + " mean?"
            answerNum = randint(0, 3)
            correctAnswerList[x] = answerNum
            for y in range(0, 4):
                if y is answerNum:
                    answer = self.formatString(str(questionDict.get(vocabWord)))
                else:
                    randomAnswer = list(questionDict.values())[randint(0, len(questionDict))]
                    answer = self.formatString(str(randomAnswer))

                tempAnswerList[y] = answer

            multipleChoiceList[x] = list(tempAnswerList)
            questList[x] = formattedVocabWord

        return (questList, multipleChoiceList, correctAnswerList)

    def createLayout(self, questions, multipleChoice):
        with open("Quiz.html", 'w') as file:
            file.write("<!DOCTYPE html> \n")
            file.write("<html> \n")
            file.write("\t<head>\n")
            file.write("\t\t<title> Automated Quiz </title> \n")
            file.write("\t\t <style type = \"text/css\"> \n")
            file.write("\t\t\t body { \n")
            file.write("\t\t\t\t font-family: sans-serif; \n")
            file.write("\t\t\t\t color: darkcyan;}\n")
            file.write("\t\t\t .latin-word { \n")
            file.write("\t\t\t\t color: rgb(0, 62, 62); \n")
            file.write("\t\t\t\t font-weight: bold;} \n")
            file.write("\t\t\t h2 { \n")
            file.write("\t\t\t\t color: rgb(0, 62, 62); \n")
            file.write("\t\t\t\t font-weight: bold;} \n")
            file.write("\t\t </style> \n")
            file.write("\t</head> \n")
            file.write("\t<body> \n")
            file.write("\t\t<h2> Greetings! Here is Your Daily Latin Quiz: </h2>\n")
            file.write("\t\t <ol> \n")
            for x in range(0, 5):
                file.write("\t\t\t <li> What does the Latin word <span class = \"latin-word\"> "
                           + questions[x] + " </span> mean? </li> \n")
                file.write("\t\t\t <ol> \n")
                for y in range(0, 4):
                    file.write("\t\t\t\t <li>" + str(multipleChoice[x][y]) + "</li> \n")
                file.write("\t\t\t </ol> \n")
                file.write("\t\t\t <br> \n")
            file.write("\t\t </ol> \n")
            file.write("\t</body>\n")
            file.write("</html>\n")
            file.close()

    def main(self):
        quizQuestions = self.sort("LatinWords.txt", ":")
        latinQuestions, latinChoices, answers = self.createQuestions(quizQuestions)
        self.createLayout(latinQuestions, latinChoices)

if __name__ == "__main__":
    quiz = QuestionMaker()
    quiz.main()

