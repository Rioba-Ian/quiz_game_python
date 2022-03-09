from categories.history import history
from categories.movies import movies
from categories.history import history
def main():
    user_input = input("""
    WELCOME TO THE GAME TRIVIA!

    Please enter one of the following selections:

    'Movies':  1 
    'History': 2 
    'Art'    : 3 
    'Quit'   : 0

    Enter Your choice here ['1','2','3','0']:    
    """)

    while 1:

        if user_input == "1":
            print("""
                    You have chosen the movies category.
                    """)
            movies()
            main()
        elif user_input == "2":
            print("""
                    You have chosen the History category.
                    """)
            history()
            main()
        elif user_input == "3":
            print("""
                    You have chosen the Art category.
                    """)
            history()
            main()
        elif user_input == "0":
            print("""
                    Exiting the program.
                    """)
            break
        else:
            print("""
                    You haven't entered a valid choice.
                    Let us give you another chance.
                    """)
            main()

            
if __name__ == "__main__":
    main()
        