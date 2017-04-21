#!bin/bash

python /home/edward237/Desktop/AutoQuiz/QuizCreator.py
mutt -e 'set content_type=text/html' -s 'Daily Generated Quiz' edwardseley@gmail.com < /home/edward237/Desktop/AutoQuiz/Quiz.html