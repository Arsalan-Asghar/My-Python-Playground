# Simple Terminal based DIARY

def newWrite():
    NoteToWrite = input("Please enter the text you want to store:\n ")
    with open('diary.txt', 'w') as f:
        f.write(NoteToWrite)
    print("Successfully done!")

def addAppend():
    NoteToAppend = input("Please enter the text you want to store:\n ")
    with open('diary.txt', 'a') as f:
        f.write("\n" + NoteToAppend)
    print("Successfully done!")

def readingFile():
    try:
        with open('diary.txt', 'r') as f:
            for lines in f:
                print("\nContent in Diary:\n" + lines.strip())
    except FileNotFoundError:
        print("No file to read.")


def main():
    while True:
        try:
            print('*'*30)
            print("Welcome to the Simple DIARY.")
            print('*'*30)
            print()

            choice = input("""What do you want to perform in the Diary?
1. Read the content available in the Diary:
2. Write a completely new content by overwriting the previous one:
3. Add new content to existing one:
4. Exit:

Choose (1,2,3,4): """)

            match choice:
                case '1':
                    readingFile()
                case '2':
                    newWrite()
                case '3':
                    addAppend()
                case'4':
                    print("Thanks for using")
                    break
                case _:
                    print("Please choose a correct option please.")

            ask = input("\n\nDo you want to perform any task again? (Y/n): ").lower()

            if ask == 'n':
                print("Thanks for using.")
                break

        except ValueError:
            print("Please enter a correct Values.")

if __name__ == "__main__":
    main()