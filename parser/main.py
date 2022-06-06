import glob
from bs4 import BeautifulSoup
import json
question_storage = dict()

WORKING_PATH = "data"
def main():
    datas = glob.glob(f"{WORKING_PATH}/*.html")
    for data in datas:
        print(f"Opening {data}")
        with open(data, "r") as html_doc:
            soup = BeautifulSoup(html_doc.read(), "html.parser")
            # print(soup.prettify())
            question_ol = soup.select(".question")[0]
            questions_li = question_ol.findChildren("li", recursive=False)
            for question in questions_li:
                # print(question.contents[4])
                question_contents = question.contents[4].strip()
                question_answers = question.contents[5].findChildren("li", recursive=True)
                ans_list = []
                for question_answer in question_answers:
                    answer_label = question_answer.contents[3]
                    is_correct = (question_answer.contents[2]['title'] == "correct")
                    ans_list.append((answer_label.strip(), is_correct))
                # print(ans_list)
                question_storage[question_contents] = ans_list
                # print(question_answers[0].contents[3])
            #     break
            # break
    print(f"Got {len(question_storage)} questions")
    with open("data.json", "w") as write_file:
        json.dump(question_storage, write_file, indent=4)

if __name__ == '__main__':
    main()