import random 

masiv = random.randint(0, 4)
masiv_1 = random.randint(0, 4)
masiv_2 = random.randint(0, 4)
masiv_3 = random.randint(0, 4)
masiv_4 = random.randint(0, 4)

glav_masiv = [masiv, masiv_1, masiv_2, masiv_3, masiv_4]

while_0 = 1

While_1 = 0
While_2 = 0
While_3 = 0
While_4 = 0

while while_0 == 1:
    i = 0
    score = i + 1
    yes_no = input("Начать игру? yes/no: ").strip().lower()

    if yes_no == "no":
        print("Завершаем.....")
        print("20/100%") 
        print("40/100%") 
        print("60/100%") 
        print("80/100%") 
        print("100/100%")
        print("Завершено ...")
        break
    
    if yes_no == "yes":
        print("Начинаем ....")
        print("Твой массив выглядит так:", glav_masiv)
        print("Ты стоишь на цифре:", masiv)
        print("Пронумеровать цифры массива в ступени?")
        yes_no = input("yes/no: ").strip().lower()
        
        if yes_no == "yes":
            print("Окей")
            print("Первая ступень -", masiv_1, "вторая -", masiv_2, "третья -", masiv_3, "четвертая -", masiv_4)
            print("Ты стоишь на нулевой ступени, она равна:", masiv, "цифра на которой ты стоишь, обозначает силу твоего прыжка")
            print("То есть цифра твоего прыжка =", masiv)
            print("Впереди тебя осталось 4 ступени!")
            print("Удачи!")
            jump = int(input("Укажи номер ступени, на которую хочешь прыгнуть: "))
            
            if masiv == 0:
                print("Ты проиграл, твой прыжок был равен:", masiv)
                break
            
            if jump == 1 and masiv >= masiv_1:
                print("Ты на первой ступени! Она равна", masiv_1)
                While_1 = 1
            elif jump == 2 and masiv >= masiv_2:
                print("Ты на второй ступени! Она равна", masiv_2)
                While_2 = 2
            elif jump == 3 and masiv >= masiv_3:
                print("Ты на третьей ступени! Она равна", masiv_3)
                While_3 = 3
            elif jump == 4 and masiv >= masiv_4:
                print("Ты на четвертой ступени! Она равна", masiv_4)
                While_4 = 4

            # Пример для первого цикла
            while While_1 == 1:
                print("Цикл 1 - первая ступень")
                jump_1 = int(input("Укажи номер следующей ступени: "))
                if jump_1 == 2 and masiv_1 >= masiv_2:
                    print("Ты на второй ступени! Она равна", masiv_2)
                    While_2 = 2
                    While_1 = 0  # Закрываем цикл While_1
                    
            while While_2 == 2:
                print("Цикл 2 - вторая ступень")
                jump_2 = int(input("Укажи номер следующей ступени: "))
                if jump_2 == 3 and masiv_2 >= masiv_3:
                    print("Ты на третьей ступени! Она равна", masiv_3)
                    While_3 = 3
                    While_2 = 0  # Закрываем цикл While_2
                
            while While_3 == 3:
                print("Цикл 3 - третья ступень")
                jump_3 = int(input("Укажи номер следующей ступени: "))
                if jump_3 == 4 and masiv_3 >= masiv_4:
                    print("Ты на четвертой ступени! Она равна", masiv_4)
                    While_4 = 4
                    While_3 = 0  # Закрываем цикл While_3
                
            while While_4 == 4:
                print("Победа!")
                break