import random 

masiv = random.randint(0,4)
masiv_1 = random.randint(0,4)
masiv_2 = random.randint(0,4)
masiv_3 = random.randint(0,4)
masiv_4 = random.randint(0,4)

masiv_syupen = 0 
masiv_syupen_1 = 1 
masiv_stupen_2 = 2 
masiv_syupen_3 = 3 
masiv_syupen_4 = 4 

glav_masiv = [masiv,masiv_1,masiv_2,masiv_3,masiv_4]

jump = 0 
jump_1 = 0 
jump_2 = 0 
jump_3 = 0 
jump_4 = 0 




while_0 = 1 



while while_0 == 1 : 
    i = 0 
    score = i + 0 
    print("Привет! Твоя задача попасть в конец масива")
    print("Ты на 0 й ступени , она равна ",masiv)
    print("чтобы выбрать ступень укажи ее номер")
    print("Так же следущие ступени равны : ступень 1:",masiv_1,"ступень 2 :",masiv_2,"ступень 3 :",masiv_3,"cnegtym 4 ",masiv_4) 
    print("Твоя сила прыжка = ",masiv)
    
    if masiv == 0  : 
        print("False")
        break
    if masiv == 1 :
        print("Доступная ступень:",masiv_syupen_1)
        jaump = int(input("Сюда номер ступени: "))
    if masiv_syupen == jump : 
        print("Ты на ",masiv_syupen_1,"Ступени ")
        print(" ступени впереди :",masiv_stupen_2,masiv_syupen_3,masiv_syupen_4)
        print("Твоя сила прыжка: ",masiv_syupen_1)
        jump_1 = int(input("Номер ступени сюда:"))
    if jump_1 == masiv_stupen_2 :
             
    
        
        
