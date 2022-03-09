def art():
    count = 0
    print("""
            There are 3 questions in this round.

            QUESTION ONE:

            Early photographers made their images on which of these materials?
            a) Glass     c) Paper
            b) Plastic    d) Stone

            Enter a choice Choice ['a', 'b', 'c', 'd']:
            """)
    art_question1_input = input()
    if art_question1_input == "a":
        print("Correct")
        count_1 = count + 10
        print(f'Your score is {count_1}/10!')
    else:
        print("Sorry.The correct answer was a) Glass")
        count_1 = count
    print("""
            QUESTION TWO:

            
            What did I.M. Pei design outside the Louvre, in Paris?
            a) Sarcophagus   c) Obelisk
            b) Ziggurat      d) Pyramid
            Choice ['a', 'b', 'c', 'd']: 

            """)
    art_question2_input = input()
    if art_question2_input == "d":
        print("Correct")
        count_2 = count_1 + 10
        print(f'Your score is {count_2}/20!')
    else:
        print("Sorry.The correct answer was d) Pyramid")
        print(f'Your score is {count_1}/20!')
        count_2 = count_1
    
    print("""
            QUESTION THREE:

            
            What animal often symbolizes peace in art?
            a) Dog     c) Dove
            b) Deer    d) Swan

            Choice ['a', 'b', 'c', 'd']:
           """)
    art_question3_input = input()
    if art_question3_input == "c":
        print("Correct")
        count_3 = count_2 + 10
        print(f'Your score is {count_3}/30!')
    else:
        print("Sorry.The correct answer was c) Dove")
        print(f'Your score is {count_2}/30!')
        count_3 = count_2
    
    
    if count_3 >= 20:
        print("You are very sharp, GREAT JOB!")
    elif count_3 >= 10 and count_3 < 20:
        print("You should work hard next time!")
    elif count_3 < 10:
        print("Maybe try another section, next time. ")


if __name__ == "__main__":
    art()