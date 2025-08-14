def greet_user():
    name = input("Таны нэрийг хэн гэдэг вэ?: ")
    print(f"Сайн байна уу, {name}! Mini Quiz тоглоомд тавтай морил!")
    return name

def ask_question(question, answer):
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print("Зөв!")
        return 1
    else:
        print("Буруу!")
        return 0

def run():
    score = 0
    print("Тоглоом эхэлж байна...")
    
    score += ask_question("Монгол улсын нийслэл аль хот вэ?", "Улаанбаатар")
    score += ask_question("2 + 2 хэд вэ?", "4")
    score += ask_question("Python гэдэг нь ямар төрлийн хэл вэ? (programming / human / animal)", "programming")
    
    score(score)

def score(score):
    print(f"Таны авсан оноо: {score} / 3")
    if score == 3:
        print("Маш сайн!")
    elif score == 2:
        print("Сайн байна!")
    else:
        print("Дараагийн удаа илүү сайн хийнэ гэж найдая!")

# Програмыг ажиллуулах хэсэг
if __name__ == "__main__":
    greet_user()
    run()
