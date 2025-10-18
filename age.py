from abc import ABC, abstractmethod
from datetime import date, datetime
import inquirer
import anthropic
import os
from dotenv import load_dotenv
load_dotenv()

class Person(ABC):
    def __init__(self, name):
        self.name = name
class Guest(Person):
    pass
class Member(Person):
    def __init__(self, name, birth, yarigai, hobby):
        super().__init__(name)
        self.birth = birth
        self.yarigai = yarigai
        self.hobby = hobby

    def get_age(self):
        today = date.today()
        age = today.year - self.birth.year
        if(today.month, today.day) < (self.birth.month, self.birth.day):
            age -= 1
        return age
    def get_yarigai(self):
        if self.yarigai == "ある":
            hyouka_yarigai = 0
        elif self.yarigai == "わからない":
            hyouka_yarigai = 25
        else:
            hyouka_yarigai = 50
        return hyouka_yarigai
    def get_hobby(self):
        if self.hobby == "大麻":
            hyouka_hobby = 50
        elif self.hobby == "酒" or self.hobby == "たばこ":
            hyouka_hobby = 30
        elif self.hobby == "読書" or self.hobby == "楽曲制作":
            hyouka_hobby = 20
        return hyouka_hobby
    
def get_stress_score(hyouka_yarigai, hyouka_hobby):
    return hyouka_hobby + hyouka_yarigai

print("こんにちは！\n\nあなたのストレス度を計測します！\n\n")

questions_hobby = [
  inquirer.List("hobby",
                message="あなたの趣味は？",
                choices=["酒", "たばこ", "読書", "楽曲制作", "大麻"],
            ),
]
answer_hobby = inquirer.prompt(questions_hobby)

questions_yarigai = [
  inquirer.List("yarigai",
                message="仕事にやりがいはある？",
                choices=["ある", "わからない", "ない"],
            ),
]
answer_yarigai = inquirer.prompt(questions_yarigai)


name = str(input("あなたの名前："))
birth = input("あなたの誕生日：")


print("======================\n\n")
user = Member(name, datetime.strptime(birth,"%Y%m%d"), answer_yarigai["yarigai"], answer_hobby["hobby"])
print(user.name + "さん、こんにちは。" ,int(user.get_age()), "歳ですね！\n")
print("あなたへのリフレッシュ方法を提案します。少々お待ちください！\n")


# print("あなたのストレス度は、", get_stress_score(user.get_yarigai(), user.get_hobby()), "/ 100です！\n\n")
client = anthropic.Anthropic(api_key=os.environ.get("API"))

userprompt = "患者の名前："+ user.name +"患者の仕事のやりがい：" + str(answer_yarigai["yarigai"]) + "患者の趣味：" + str(answer_hobby["hobby"] + "患者の年齢：" + str(user.get_age()))
message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=1024,
    system="あなたは、メンタルヘルス専門家です。患者の趣味と仕事へのやりがいをもとに、明日の一日のリフレッシュ方法を考えて端的なスケジュールにしてください。追加の確認は不要です。5行程度で提案してください。",
    messages=[
        {"role": "user", "content": userprompt}
    ]
)

print(message.content[0].text)