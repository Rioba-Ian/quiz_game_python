def history():
    count = 0
    print("""
            There are 5 questions in this round.

            QUESTION ONE:

            Which of these nations was neutral in World War I?
            a) Germany   c) Italy
            b) Norway    d) England

            Enter a choice Choice ['a', 'b', 'c', 'd']:
            """)
    history_question1_input = input()
    if history_question1_input == "b":
        print("Correct")
        count_1 = count + 10
        print(f'Your score is {count_1}/10!')
    else:
        print("Sorry.The correct answer was b) Norway")
        count_1 = count
    print("""
            QUESTION TWO:

            
            How many republics made up the former Soviet Union?
            a) 15          c) 20
            b) 12          d) 10
            Choice ['a', 'b', 'c', 'd']: 

            """)
    history_question2_input = input()
    if history_question2_input == "a":
        print("Correct")
        count_2 = count_1 + 10
        print(f'Your score is {count_2}/20!')
    else:
        print("Sorry.The correct answer was a) 15")
        print(f'Your score is {count_1}/20!')
        count_2 = count_1
    
    print("""
            QUESTION THREE:

            
            Which Indian president was involved in the struggle for Irish independence?
            a) V.V. Giri                c) Gulzarilal Nanda
            b) Neelam Sanjiva Reddy      d) S. Radhakrishnan

            Choice ['a', 'b', 'c', 'd']:
           """)
    history_question3_input = input()
    if history_question3_input == "a":
        print("Correct")
        count_3 = count_2 + 10
        print(f'Your score is {count_3}/30!')
    else:
        print("Sorry.The correct answer was a) V.V. Giri")
        print(f'Your score is {count_2}/30!')
        count_3 = count_2
    
    print("""
            QUESTION FOUR:

            
            Who was the first U.S. president to appear on television?
            a) Richard Nixon     c) Abraham Lincoln
            b) Ronald Reagan    d) Franklin Delano Rossevelt

            Choice ['a', 'b', 'c', 'd']:
           """)
    history_question4_input = input()
    if history_question4_input == "d":
        print("Correct")
        count_4 = count_3 + 10
        print(f'Your score is {count_4}/40!')
    else:
        print("Sorry.The correct answer was d) Franklin Delano Rossevelt")
        print(f'Your score is {count_3}/40!')
        count_4 = count_3

    print("""
            QUESTION FIVE: A BONUS QUESTION 

            
            How old is the Earth?
            a) 4.5 billion yrs  c) 6000 years old
            b) 2000 years       d) 1 million years old

            Choice ['a', 'b', 'c', 'd']:
           """)
    history_question5_input = input()
    if history_question5_input == "a":
        print("Correct")
        count_5 = count_4 + 10
        print(f'Your score is {count_5}/50!')
    else:
        print("Sorry.The correct answer was a) 4.5 billion yrs")
        print(f'Your score is {count_4}/50!')
        count_5 = count_4
    
    if count_5 >= 40:
        print("You are very sharp, GREAT JOB!")
    elif count_5 >= 20 and count_5 < 40:
        print("You should work hard next time!")
    elif count_5 < 20:
        print("Maybe try another section, next time. ")


if __name__ == "__main__":
    history()