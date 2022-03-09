def movies():
    count = 0
    print("""
            There are 5 questions in this round.

            QUESTION ONE:

            What's the name of the skyscraper in Die Hard?
            a) Nakatomi Plaza c) Eifel Tower
            b) Trump Tower    d) World Trade Center

            Enter a choice Choice ['a', 'b', 'c', 'd']:
            """)
    movie_question1_input = input()
    if movie_question1_input == "a":
        print("Correct")
        count_1 = count + 10
        print(f'Your score is {count_1}/10!')
    else:
        print("Sorry.The correct answer was a) Nakatomi Plaza")
        count_1 = count
    print("""
            QUESTION TWO:

            
            What flavor of Pop Tarts does Buddy the Elf use in his spaghetti in 'Elf'?
            a) Brown Sugar c) Chocolate
            b) Cherry      d) Blueberry
            Choice ['a', 'b', 'c', 'd']: 

            """)
    movie_question2_input = input()
    if movie_question2_input == "c":
        print("Correct")
        count_2 = count_1 + 10
        print(f'Your score is {count_2}/20!')
    else:
        print("Sorry.The correct answer was c) Chocolate")
        print(f'Your score is {count_1}/20!')
        count_2 = count_1
    
    print("""
            QUESTION THREE:

            
            For what movie did Steven Spielberg win his first Oscar for best director?
            a) The Post     c) E.T
            b) Lincoln      d) Schindler's List

            Choice ['a', 'b', 'c', 'd']:
           """)
    movie_question3_input = input()
    if movie_question3_input == "d":
        print("Correct")
        count_3 = count_2 + 10
        print(f'Your score is {count_3}/30!')
    else:
        print("Sorry.The correct answer was d) Schindler's List")
        print(f'Your score is {count_2}/30!')
        count_3 = count_2
    
    print("""
            QUESTION FOUR:

            
            What was Quentin Tarantino's first film as writer and director?
            a) Pulp Fiction     c) Jackie Brown
            b) Reservoir Dogs   d) From Dusk Til Dawn

            Choice ['a', 'b', 'c', 'd']:
           """)
    movie_question4_input = input()
    if movie_question4_input == "b":
        print("Correct")
        count_4 = count_3 + 10
        print(f'Your score is {count_4}/40!')
    else:
        print("Sorry.The correct answer was b) Reservoir Dogs")
        print(f'Your score is {count_3}/40!')
        count_4 = count_3

    print("""
            QUESTION FIVE:

            
            Where is Jurassic park located in the film?
            a) Isla Nublar      c) Bora Bora
            b) Maui             d) Santorini

            Choice ['a', 'b', 'c', 'd']:
           """)
    movie_question5_input = input()
    if movie_question5_input == "a":
        print("Correct")
        count_5 = count_4 + 10
        print(f'Your score is {count_5}/50!')
    else:
        print("Sorry.The correct answer was b) Reservoir Dogs")
        print(f'Your score is {count_4}/50!')
        count_5 = count_4
    
    if count_5 >= 40:
        print("You are very sharp, GREAT JOB!")
    elif count_5 >= 20 and count_5 < 40:
        print("You should work hard next time!")
    elif count_5 < 20:
        print("Maybe try another section, next time. ")


if __name__ == "__main__":
    movies()