import json
import random
from termcolor import colored

color = ["blue", "grey", "yellow", "cyan", "magenta"]

def main():
    with open("data.json", "r") as question_data:
        questions = json.load(question_data)

    tmp = list(questions.keys())
    random.shuffle(tmp)
    for question in tmp:
        print(question)
        choices = questions[question]
        random.shuffle(choices)
        for idx, choice in enumerate(choices):
            print(colored(f"{idx}. {choice[0]}", color[idx]))
        pick = -1
        while(pick == -1):
            print(f"Pick an answer ({0} - {len(choices) - 1})")
            try:
                pick = int(input())
            except ValueError:
                pick = -1
        if(choices[pick][1]):
            print(colored("OK", "green"))
        else:
            print()
            print(colored(f"wrong, answer is: ", "red"))
            for idx, choice in enumerate(choices):
                if(choice[1]):
                    print(colored(f"{idx}. {choice[0]}", color[idx]))
        input()
        print("\n\n")


if __name__ == '__main__':
    main()