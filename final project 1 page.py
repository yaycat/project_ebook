from tkinter import *
from PIL import ImageTk, Image
from io import BytesIO
import webbrowser




def AuthPage():
    global startPage
    
    def ClickBtn():
        
        if login.get()==user and secret.get()==key:
            MainPageOpen()
            
    startPage = Tk()
    startPage.title("Authorization")
    startPage.geometry("300x400")
    startPage.resizable(0, 0)
    
            
            
    user = "admin"
    key = "admin"
    
    login = Entry()
    login.place(x=80, y=140)
    
    secret = Entry()
    secret.place(x=80, y=170)
    
    btn = Button(text="Accept", command = ClickBtn)
    btn.place(x=120, y=200)

    try:
        MainPage.destroy()
    except:
        pass
    
    startPage.mainloop()
    


def MainPageOpen():
    global MainPage
    MainPage = Tk()
    MainPage.title("Introduction")
    MainPage.geometry("1280x720")
    MainPage.resizable(0, 0)
    mainmenu = Menu(MainPage)
    try:
        startPage.destroy()
    except:
        pass

    def BackToAuth():
        AuthPage()

    def ToPageBok():
        PageBook1()
    
    def ToPageBook():
        PageBook2()
    
    def ToPageBoook():
        PageBook3()
    
    def ToPageBokTest():
        PageBookTest1()
        
    def ToPageBookTest():
        PageBookTest2()
        
    def ToPageBoookTest():
        PageBookTest3()
        
    def Exit():
        MainPage.destroy()


    
    MainPage.config(menu= mainmenu)

    filemenu = Menu(mainmenu, tearoff=0)
    filemenu.add_command(label="Exit", command=Exit)

    
    paronemenu = Menu(mainmenu, tearoff=0)
    paronemenu.add_command(label="Abstract in Russian", command=ToPageBok)
    paronemenu.add_command(label="Test in Russian", command=ToPageBokTest)
    
    partwomenu = Menu(mainmenu, tearoff=0)
    partwomenu.add_command(label="Abstract in Russian", command=ToPageBook)
    partwomenu.add_command(label="Test in Russian", command=ToPageBookTest)
    
    partwhreemenu = Menu(mainmenu, tearoff=0)
    partwhreemenu.add_command(label="Abstract in Russian", command=ToPageBoook)
    partwhreemenu.add_command(label="Test in Russian", command=ToPageBoookTest)
    

    mainmenu.add_cascade(label="File", menu=filemenu)
    mainmenu.add_cascade(label="§1", menu=paronemenu)
    mainmenu.add_cascade(label="§2", menu=partwomenu)
    mainmenu.add_cascade(label="§3", menu=partwhreemenu)

    
    


    Label(MainPage, text = "Content").place(x=500, y=10)
    
    Button(MainPage, text="Exit", command=Exit).place(x=10, y=10)
    
    
    MainPage.mainloop()




def PageBook1():
    global PageBook1
    #характеристика окна
    PageBook1 = Tk()
    PageBook1.title("§1. ПРОТИВОРЕЧИЯ МЕЖДУ ВЕДУЩИМИ КАПИТАЛИСТИЧЕСКИМИ СТРАНАМИ В НАЧАЛЕ XX ВЕКА. ПРИЧИНЫ ПЕРВОЙ МИРОВОЙ ВОЙНЫ")
    PageBook1.resizable(0, 0)
    PageBook1.geometry("1920x1080")
    
    def BackMainPage():
        PageBook1.destroy()
    
    def callback(event):
        webbrowser.open_new(r"https://www.youtube.com/watch?v=sMzulae79gE&ab_channel=%D0%9C%D1%83%D0%B4%D1%80%D0%B5%D0%BD%D1%8B%D1%87")
    
    def callback2(event):
        webbrowser.open_new(r"https://www.youtube.com/watch?v=CYA_smtRlHQ&ab_channel=%D0%9C%D1%83%D0%B4%D1%80%D0%B5%D0%BD%D1%8B%D1%87")    
    
    
    
    #текст в окне
    s = "В конце XIX - начале ХХ в. Германия, чувствовавшая себя обделенной при колоннальном разделе мира, пыталась создать союз с Великобританией против Франции и в то же время договориться с другими странами о континентальной блокаде Великобритании Планам Германии не удалось осуществиться. так как у Англии сложились хорошие дипломатические отношения с французским руководством, а в сферу французских интересов оказалась втянута Россия. В итоге запертой в центре Европы Германии не осталось иного выбора, как заключить союз с более слабыми странами - Австро-Венгрией и Италией. Так сформировался Тройственный cols. Позже он переименуется в Четверной союз. который будут называть Центральными державами военно-политический блок государств. противостоявших державам 'дружественного соглашения' (Антанте в Первой мировой войне 1914-1918 гг. Название 'Центральные державы связано с тем, что страны-основатели этого блока Германская и Австро-Венгерская империи- располагались в центре Европы. В ходе войны к этому блоку присоединились Османская империя (октябрь 1914г.) и Болгария (октябрь 1915 г.). Таким образом, в начале ХХ в. сформировалась взрывоопасная система международных отношений. На мировой политической арене появились новые силы в лице объединенной Германии и Италии. Их столкновение с Англией, Францией. Россией. Австро-Венгрией и другими империалистическими государствами было неизбежным .В Азии на доминирующую роль претендовала Япония, что противоречило интересам России, Англии, Германии, Франции и США. В центре конфликтов Османская империя. оказалась которая обладала огромными территориями в Северной Африке, на Ближнем Востоке, в Юго-Восточной Европе, ставшими объектом империалистического дележа. В конце XIX начале ХХ в. - произошли первые межимпериалистические конфликты пред- - вестники будущих мировых войн Победа США над Испанией в результате Испано-американской войны 1898 г. открыла пути дальнейшей экспансии на юг Латинской Америки, в районы Дальнего Востока и Юго-Восточной Азии. Американские волонтеры на Кубе во время Испано-американской войны. 1898 г. Другая война, связанная с колониальным переделом мира, была развязана Англией против двух бурских республик на юге Африканского континента бурская война 1899-1902 гг. Трансвааля и Оранжевой. Англо- завершилась поражением буров. Их республики вошли в состав британских колоний. Компромисс между англичанами и белыми бурами, которые в отношении аборигенов были такими же колонизаторами, завершился созданием Южно-Африканского Союза, получившего в 1910 г. статус самоуправляющегося Доминиона. На Дальнем Востоке за сферу влияний шла Русско-японская Война 1904 1905 гr. В ходе этой войны Япония укрепила свои позиции в Южной Маньчжурии и создала предпосылки для последующей в 1910 г. аннексии Кореи и дальнейшей экспансии В Китае и Юго- Восточной Азии, тем самым став агрессивным соперником США. Во время Англо-бурской войны германские правящие круги приняли новые планы реализации лозунга Вильгельма II 'Наше будущее на воде!'. В июне 1900 г.. в разгар войны, рейхстаг утвердил новую программу гонки морских вооружений. Это вызвало в Англии ответные планы строительства новых военных кораблей. Обострение англо-германского соперничества привело к изменениям во внешней политике Англии в Европе. В 1904 г. Великобритания и Франция подписали соглашение, которое получило название 'Антанта' (от франц. entente 'согласие'). В секретных протоколах к соглашению Великобритания н Франция поделили между собой сферы влияния. Согласно этому договору Франция отказалась от своих притязаний на Судан и Египет, Англия же обязалась под- держать претензии французов на Марокко. Следует отметить, что в договоре не было сказано ни о каком со юзе против Германии, но именно то, что ее не пригласили к разделу. фактически и означало, что договор направлен против этой страны. Так в Европе появился политический блок, противопоставивший себя Тройственному союзу. В сложившейся ситуации Германия стала искать союз с Россией, которая нуждалась в финансовых средствах для войны с Японией. В начале 1906г. секретные памятные записи Англии и Франции определяли условия их военного сотрудничества и возможность передислокация во Францию английских дивизий на случай войны с Германией. В это время укрепились и франко-русские отношения. в том числе и в области военного сотрудничества. Основными целями Германии были недопущение создания союза между Россией и Англией и ослабление русско-французской коалиции. На Дальнем Востоке продолжалась Русско-японская война. Российская армия оказалась побежденной. Так один из противников Германии утратил статус опасного врага. Поражение России в Русско-японской войне в начале ХХ в. облегчило группировку государств вокруг основных противников Англии и Германии. После заключения англо-французского соглашения"
    t = Text(PageBook1, width=130, height=53)
    t.insert(1.0, s)
    t.place(x=0, y=40)


    #Картинка справа от текста
    img2 = Image.open("map1.jpg") #map1.jpg
    img2 = img2.resize((400, 350))
    img2 = ImageTk.PhotoImage(img2)
    label2 = Label(PageBook1,image=img2)
    label2.image = img2
    label2.place(x = 1060, y=40)

        
    img3 = Image.open("rusyap.jpg")
    img3 = img3.resize((200, 200))
    img3 = ImageTk.PhotoImage(img3)
    label3 = Label(PageBook1, image=img3)
    label3.image = img3
    label3.place(x = 1060, y=400)
    
    img4 = Image.open("francdead.png")
    img4 = img4.resize((350, 250))
    img4 = ImageTk.PhotoImage(img4)
    label4 = Label(PageBook1, image=img4)
    label4.image = img4
    label4.place(x = 1060, y=600)
    
    
    #ссылки для видосов
    label5 = Label(PageBook1, text="ПРИЧИНЫ ПЕРВОЙ МИРОВОЙ ВОЙНЫ-1", fg="blue", cursor="hand2")
    label5.place(x= 1290, y= 400)
    label5.bind("<Button-1>", callback)
    
    label6 = Label(PageBook1, text="ПРИЧИНЫ ПЕРВОЙ МИРОВОЙ ВОЙНЫ-2", fg="blue", cursor="hand2")
    label6.place(x= 1290, y= 430)
    label6.bind("<Button-1>", callback2)

    
    Label(PageBook1, text= "ПРОТИВОРЕЧИЯ МЕЖДУ ВЕДУЩИМИ КАПИТАЛИСТИЧЕСКИМИ СТРАНАМИ В НАЧАЛЕ XX ВЕКА. ПРИЧИНЫ ПЕРВОЙ МИРОВОЙ ВОЙНЫ").place(x=100, y=10)
    Button(PageBook1, text="Back", command=BackMainPage).place(x=10,y=10)

    PageBook1.mainloop()
    

def PageBookTest1():
    global PageBookTest1
    PageBookTest1 = Tk()
    PageBookTest1.title("Проверь свои знания к §1")
    PageBookTest1.geometry("1920x1080")
    PageBookTest1.resizable(0, 0)
    
    
    
    
    var = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var.set(0)
    
    

    def BackMainPage():
        PageBookTest1.destroy()
    
    
    Button(PageBookTest1, text="Back", command=BackMainPage).place(x=10,y=10)
    
   
    def change():
        varr = var.get()
        print (varr)
        if varr == 0:
            Label(PageBookTest1, text="Correct").place(x=75, y=175)
        else:
            Label(PageBookTest1, text="Incorrect").place(x=75, y=175)
            
    def change2():
        if var2.get() == 0:
            lb2 = Label(PageBookTest1, text="Correct").place(x=75, y=330)
        else:
            lb2 =  Label(PageBookTest1, text="Incorrect").place(x=75, y=330)

    
    def change3():
        if var3.get() == 0:
            lb3 = Label(PageBookTest1, text="Correct").place(x=75, y=485)
        else:
            lb3 =  Label(PageBookTest1, text="Incorrect").place(x=75, y=485)
            
    def change4():
        if var4.get() == 0:
            lb4 = Label(PageBookTest1, text="Correct").place(x=75, y=650)
            Label(PageBookTest1, text="Вы Завершили Тест!").place(x=100, y=700)
        else:
            lb4 =  Label(PageBookTest1, text="Incorrect").place(x=75, y=650)
            Label(PageBookTest1, text="Вы Завершили Тест!").place(x=100, y=700)
        
    
    
    
    
    Label(PageBookTest1, text="Тест на знание 1 Параграфа").place(x=500, y=10)
    
    
    
    #1 vopros
    Label(PageBookTest1, text="Кто такой Гаврило Принцип?:").place(x=20, y=40)
    
    r1 = Radiobutton(PageBookTest1, text="Полицейский",   variable=var, value=1 ,command=change).place(x=40, y=70, anchor=W)
    r2 = Radiobutton(PageBookTest1, text="Студент",       variable=var, value=0 ,command=change).place(x=40, y=95, anchor=W)
    r3 = Radiobutton(PageBookTest1, text="Медбрат",       variable=var, value=2 ,command=change).place(x=40, y=120, anchor=W)
    r4 = Radiobutton(PageBookTest1, text="Водитель",      variable=var, value=3 ,command=change).place(x=40, y=145, anchor=W)
    
    
    
    
    #2 vopros
    Label(PageBookTest1, text="Выберите страны Антанты:").place(x=20, y=200)
    
    r12 = Radiobutton(PageBookTest1, text="Англия, Франция, Россия",                               variable=var2, value=0 ,command=change2).place(x=40, y=230, anchor=W)
    r22 = Radiobutton(PageBookTest1, text="Германская империя, Османская империя, Австро-Венгрия", variable=var2, value=1 ,command=change2).place(x=40, y=255, anchor=W)
    r32 = Radiobutton(PageBookTest1, text="Англия, Франция, Сербия",                               variable=var2, value=2 ,command=change2).place(x=40, y=280, anchor=W)
    r42 = Radiobutton(PageBookTest1, text="Англия, Испания, Италия",                               variable=var2, value=3 ,command=change2).place(x=40, y=305, anchor=W)
    
    
    # mu btn last i new lab = 35/ mu lab i radio = 30 / mu radiobutoon = 25/ radiobutton i btn = 25
    
    
    
    
    #3 vorpos
    Label(PageBookTest1, text="Когда Австро-Венгрия объявила войну Сербии?:").place(x=20, y=355)
    
    r1s = Radiobutton(PageBookTest1, text="28 июня 1914",      variable=var3, value=2 ,command=change3).place(x=40, y=385, anchor=W)
    r2 = Radiobutton(PageBookTest1, text="1 августа 1914",    variable=var3, value=1 ,command=change3).place(x=40, y=410, anchor=W)
    r3 = Radiobutton(PageBookTest1, text="28 июля 1914",      variable=var3, value=0 ,command=change3).place(x=40, y=435, anchor=W)
    r4 = Radiobutton(PageBookTest1, text="1 января 1914",     variable=var3, value=3 ,command=change3).place(x=40, y=460, anchor=W)
    
    
    
    
    
    
    #4 vorpos
    Label(PageBookTest1, text="Члены Тройственного союза:").place(x=20, y=520)
    
    r1 = Radiobutton(PageBookTest1, text="Италия, Австро-Венгрия, Франция",    variable=var4, value=2 ,command=change4).place(x=40, y=550, anchor=W)
    r2 = Radiobutton(PageBookTest1, text="Италия, Австро-Венгрия, Германия",   variable=var4, value=0 ,command=change4).place(x=40, y=575, anchor=W)
    r3 = Radiobutton(PageBookTest1, text="Италия, Франция, Англия",            variable=var4, value=1 ,command=change4).place(x=40, y=600, anchor=W)
    r4 = Radiobutton(PageBookTest1, text="Россия, Османская империя, Италия",  variable=var4, value=3 ,command=change4).place(x=40, y=625, anchor=W)
    

    


def PageBook2():
    global PageBook2
    PageBook2 = Tk()
    PageBook2.title("§2. ОСНОВНЫЕ ВОЕННЫЕ ДЕЙСТВИЯ В 1914-1918 годы и ПОСЛЕДСТВИЯ ВОЙНЫ")
    PageBook2.geometry("1920x1080")
    PageBook2.resizable(0, 0)

    def BackMainPage():
        PageBook2.destroy()
        
    def callback(event):
        webbrowser.open_new(r"https://www.youtube.com/watch?v=VjpRZkbttSk&ab_channel=%D0%93%D0%B5%D0%BE-%D0%98%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F")
        
    
    
    Button(PageBook2, text="Back", command=BackMainPage).place(x=10,y=10)

    s = "Военная кампания 1914 г. С первых дней войны в Европе образовалось два фронта: Западный (в Бельгии и Франции) и Восточный (против России). В начале августа 1914 г. в соответствие с 'планом Шлиффена' германское командование бросило групи- ровку войск на слабозащищенные границы Люксембурга и Бельгии. В короткие сроки бельгийская была отброшена к Антверпену. путь на север Франции был открыт Не выдержав стремительного удара германских армий, союзники откатил и на запад. Немецкие части были в 40 км от Парижа. В городе началась паника. Французское правительство оставило столицу и переехало в г. Бордо. Правительство Франции обратилось к российскому правительству с просьбой о помощи. Русские войска были брошены в наступление. Две российские армии заняли значительную часть территории Восточной Пруссии. На Западном фронте развернулись упорные сражения на р. Марне. Битва на Марне — одна из самых крупных операций. в которой участвовало более 2 млн. человек. и стала поворотным моментом войны на французском театре военных действий. Для французов это сражение стало первой победой над германцами, преодолением позора поражения во Франко-прусской войне. Тяжелые потери заставили немцев отступить. План молниеносного разгрома Франшн окончательно рухнул. С учетом затяжного характера войны обе воюющие группировки активно привлекают новых союзников. В конце августа войну Германии объявила Япония. Она захватила принадлежащие Германии острова в Тихом океане и ее колонии в Китае. Под давлением немцев Османская империя была втянута в войну против Антанты Война на море свелась к блокаде германского побережья английским флотом, к активным действиям подводных лодок и крейсеров. В первые же месяцы войны обозначилось преимущество военноморских сил блока Антанты. Главным итогом военной кампании 1914 г. стал срыв странами Антанты германского плана молниеносной войны. Война приняла затяжной характер. Германия была вынуждена вести активные военные действия как на Западе, так и на Востоке. Кампания 1915 г. Подведя итоги 1914 г. германское командование разработало на 1915 г. новый военный план. Он предусматривал переход к стратегической обороне на Западном фронте при концентрации сил и средств на Восточном фронте с целью скорейшего разгрома русской армии и вывода России из войны. Руководители Германии и Австро-Венгрии решили в 1915 г. нанести поражение России и заставить ее просить мира. Против России было брошено более половины всех вооруженных сил этих держав a ciora войска Османской империи. В феврале-марте немецким войскам удалось вытеснять российские армии из Восточной Пруссии В мае австро-германские войска прорвали слабо укрепленный русский фронт и начали наступление севернее Варшавы. К осени вооруженные силы Австро-Венгрии и Германии захватили всю Польшу. Галицию' "
    t = Text(PageBook2, width=130, height=53)
    t.insert(1.0, s)
    t.place(x=0, y=40)
    
    label5 = Label(PageBook2, text="ПЕРВАЯ МИРОВАЯ ВОЙНА", fg="blue", cursor="hand2")
    label5.place(x= 1290, y= 400)
    label5.bind("<Button-1>", callback)
    
    
    
    

def PageBookTest2():
    global PageBookTest2
    PageBookTest2 = Tk()
    PageBookTest2.title("Проверь свои знания к §1")
    PageBookTest2.geometry("1920x1080")
    PageBookTest2.resizable(0, 0)
    
    
    
    
    var = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var.set(0)
    
    

    def BackMainPage():
        PageBookTest2.destroy()
    
    
    Button(PageBookTest2, text="Back", command=BackMainPage).place(x=10,y=10)


    
    def change():
        varr = var.get()
        print (varr)
        if varr == 0:
            Label(PageBookTest2, text="Correct").place(x=75, y=175)
        else:
            Label(PageBookTest2, text="Incorrect").place(x=75, y=175)
            
    def change2():
        if var2.get() == 0:
            lb2 = Label(PageBookTest2, text="Correct").place(x=75, y=330)
        else:
            lb2 =  Label(PageBookTest2, text="Incorrect").place(x=75, y=330)

    
    def change3():
        if var3.get() == 0:
            lb3 = Label(PageBookTest2, text="Correct").place(x=75, y=485)
        else:
            lb3 =  Label(PageBookTest2, text="Incorrect").place(x=75, y=485)
            
    def change4():
        if var4.get() == 0:
            lb4 = Label(PageBookTest2, text="Correct").place(x=75, y=650)
            Label(PageBookTest2, text="Вы Завершили Тест!").place(x=100, y=700)
        else:
            lb4 =  Label(PageBookTest2, text="Incorrect").place(x=75, y=650)
            Label(PageBookTest2, text="Вы Завершили Тест!").place(x=100, y=700)
        
    
    
    
    
    Label(PageBookTest2, text="Тест на знание 2 Параграфа").place(x=500, y=10)
    
    
    
    #1 vopros
    Label(PageBookTest2, text="Кто такой Гаврило Принцип?:").place(x=20, y=40)
    
    r1 = Radiobutton(PageBookTest2, text="Полицейский",   variable=var, value=1 ,command=change).place(x=40, y=70)
    r2 = Radiobutton(PageBookTest2, text="Студент",       variable=var, value=0 ,command=change).place(x=40, y=95)
    r3 = Radiobutton(PageBookTest2, text="Медбрат",       variable=var, value=2 ,command=change).place(x=40, y=120)
    r4 = Radiobutton(PageBookTest2, text="Водитель",      variable=var, value=3 ,command=change).place(x=40, y=145)
    
    
    
    
    #2 vopros
    Label(PageBookTest2, text="Выберите страны Антанты:").place(x=20, y=200)
    
    r12 = Radiobutton(PageBookTest2, text="Англия, Франция, Россия",                               variable=var2, value=0 ,command=change2).place(x=40, y=230, anchor=W)
    r22 = Radiobutton(PageBookTest2, text="Германская империя, Османская империя, Австро-Венгрия", variable=var2, value=1 ,command=change2).place(x=40, y=255, anchor=W)
    r32 = Radiobutton(PageBookTest2, text="Англия, Франция, Сербия",                               variable=var2, value=2 ,command=change2).place(x=40, y=280, anchor=W)
    r42 = Radiobutton(PageBookTest2, text="Англия, Испания, Италия",                               variable=var2, value=3 ,command=change2).place(x=40, y=305, anchor=W)
    
    
    # mu btn last i new lab = 35/ mu lab i radio = 30 / mu radiobutoon = 25/ radiobutton i btn = 25
    
    
    
    
    #3 vorpos
    Label(PageBookTest2, text="Когда Австро-Венгрия объявила войну Сербии?:").place(x=20, y=355)
    
    r1s = Radiobutton(PageBookTest2, text="28 июня 1914",      variable=var3, value=2 ,command=change3).place(x=40, y=385, anchor=W)
    r2 = Radiobutton(PageBookTest2, text="1 августа 1914",    variable=var3, value=1 ,command=change3).place(x=40, y=410, anchor=W)
    r3 = Radiobutton(PageBookTest2, text="28 июля 1914",      variable=var3, value=0 ,command=change3).place(x=40, y=435, anchor=W)
    r4 = Radiobutton(PageBookTest2, text="1 января 1914",     variable=var3, value=3 ,command=change3).place(x=40, y=460, anchor=W)
    
    
    
    
    
    
    #4 vorpos
    Label(PageBookTest2, text="Члены Тройственного союза:").place(x=20, y=520)
    
    r1 = Radiobutton(PageBookTest2, text="Италия, Австро-Венгрия, Франция",    variable=var4, value=2 ,command=change4).place(x=40, y=550, anchor=W)
    r2 = Radiobutton(PageBookTest2, text="Италия, Австро-Венгрия, Германия",   variable=var4, value=0 ,command=change4).place(x=40, y=575, anchor=W)
    r3 = Radiobutton(PageBookTest2, text="Италия, Франция, Англия",            variable=var4, value=1 ,command=change4).place(x=40, y=600, anchor=W)
    r4 = Radiobutton(PageBookTest2, text="Россия, Османская империя, Италия",  variable=var4, value=3 ,command=change4).place(x=40, y=625, anchor=W)




def PageBook3():
    global PageBook3
    PageBook3 = Tk()
    PageBook3.title("§3. МИР ПОСЛЕ ПЕРВОЙ МИРОВОЙ ВОЙНЫ")
    PageBook3.geometry("1920x1080")
    PageBook3.resizable(0, 0)
    
    def BackMainPage():
        PageBook3.destroy()
        
    def callback(event):
        webbrowser.open_new(r"https://www.youtube.com/watch?v=zaWi8F0jOvE&ab_channel=DW%D0%BD%D0%B0%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%BC")
        
    w = "Парижская мирная конференция. 18 января 1919 г. в Париже открылась мирная конференция. В ее работе приняли участие Делегации 35 государств. но практически все основные дела решались так называемой 'Большой тройкой': премьер-министр Англии Дэвид Ллойд Джордж, премьер-министр Франшин Жорж Клемансо и президент США Вудро Вильсон. Главной целью Парижской конференции было подведение итогов Первой мировой войны, раздел территорий в Европе в пользу победивших государств, а также ограничение вооруженных сил стран, которые оказались побежденными в войне. Кроме того, нужно было заставить эти страны выплачивать репарации, т. е. возместить нанесенный ущерб. Парижская мир ная конференция обозначила начало нового этапа в развитии дипломатин и международных отношений. С каждой побежденной страной были подготовлены отдельные мирные договоры: Версальский - с Германией (28 июня 1919). Сен-Жерменский с Австрией (1919) Нейнский с Болгарией (1919), Трианонский  с Венгрией (1920) Севрский с Турцией (1920). Версальский мирный договор является главным документом послевоенного мирного урегулирования, завершившим Первую мировую войну 1914-1918 г. Это соглашение предусматривало следующие положения: Германия признавала себя виновной в разжигании Первой мировой войны и обязалась возместить победившим ее странам все убытки, причиненные им в результате ведения боев. Также Германия признала независимость Австрии, Чехословакии, Польши: вернула Франции Эльзас, Лотарингию и на 15 лет угольные шахты Саара; Бельгии округа Эйпен, Мальмеди и Морено: Польше Познань, часть Верхней Силезии, Померанин и Восточной Пруссии; Данин - северную часть Шлезвига: Литве Мемель (Клайпеда). - По Версальскому договору Германия полностью лишалась своих колониальных владений на Африканском континенте и в Азии. Ей запрещалось держать в армии более 100 тыс. человек, иметь военно-воздушный и подводный флот, отменялась всеобщая воинская повинность. Версальская система создавала новый баланс сил на континенте. сложившийся в результате победы стран Антанты над германским блоком. Изменение политической карты мира. На Парижской мирной конференции было подписано несколько мирных договоров и с союзниками Германии. Они касались в основном послевоенного раз- дела территорий, изменивших карту мира. Сен-Жерменский договор касался Австрии. Он утвердил распад Австро-Венгрии, запретил аншлюс Австрии, узаконил ограничение вооружений Австрии и выплату ею репараций. Южный Тироль передавался Италии. Трианонский договор был посвящен Венгрии. По договору Словакия и украинское Закарпатье становились частью Чехословакии: Трансильвания отходила к Румынии: к Югославии отошла Хорватия. Кроме того, договор узаконил ограничения оружений Венгрии и уплату ею репараций. Согласно Нейнскому договору с Болгарией Южная Добруджа передавалась Румынии. Западная Фракия - Греции. Севрский договор касался Турции, раздела земель Османской империи и даже собственно турецких. Был введен международный контроль над проливами, была сокращена турецкая армия. Таким образом, в результате Первой мировой войны изменилась карта мира. Создание и деятельность Лиги Наций. Важной составной частью Версальского договора стал Устав Лиги Наций - новой международной организации. Устав Лиги Наций был подписан в 1919 г. 44 государствами. Принятие устава Лиги означало создание межправительственной организации. Учредителями стали страны Антанты и новые государства- Польша, Чехословакия. Хиджаз. Целью Лиги Наций провозглашались развитие сотрудничества между народами и гарантия безопасности послевоенного мира. Ее основными задачами было развитие сотрудничества между странами и поддержание мира, введение санкций против стран-агрессоров. Главным органом этой международной организации были ежегодная ассамблея, в которую входили все члены организации. и Совет Лиги, где были представлены Великобритания. Франция. Япония, Италия, а также пять непостоянных членов. Решения по всем вопросам должны были выноситься единогласно. Побежденные в войне государства, а также советская Россия не входили в Лигу Наций. Распад империй. Одним из результатов Первой мировой войны стало крушение и распад огромных империй - Германской, Австро- Венгерской, Российской. Османской. Война обострила социальные и политические конфликты во всех странах. Поражения на фронтах и экономическая разруха ускорили протестные настроения в Германии. 9 ноября в ходе Ноябрьской революции монархия во главе с кайзером Вильгельмом была свергнута. затем Германия капитулировала, подписав в Компьенском лесу перемирие. В Германии образовалась Веймарская республика. Судьба Германии была решена на Парижской конференции. В октябре 1918 г. произошло вооруженное восстание в Будапеште, а Чехословакия объявила o независимости это ознаменовало распад Австро-Венгерской империи. В Австрии была провозглашена республика. На территории бывшей Австро-Венгрии возникли Австрия, Венгрия. Чехословакия, пестрое по национальному составу Югославское государство Российская монархия была свергнута в ходе революции 1917 г На территории бывшей империи образовалось несколько независимых государств: Финляндия, Эстония, Латвия, Литва, Польша, Белорусская Народная Республика и Украинская Народная Республика- две последние вскоре присоединились к СССР. В со- - став Польши вошел ряд польских земель, ранее принадлежавших Германии и Австро-Венгрии. Османская империя. вступившая в Первую мировую войну в качестве союзника Германии, также потерпела к концу 1918 г. поражение. После оккупации Стамбула английскими и французскими войсками в ноябре 1918 г. правительство Османской империи окончательно рухнуло, на ее обломках появилась Турецкая Республика, а арабские регионы перешли под протекторат стран Антанты. Затем они были переданы в управление отдельным странам согласно мандатной системе. Мандатная система. Для того чтобы определить судьбу бывших германских колоний и арабских провинций бывшей Османской империи, была введена мандатная система. Это была идея передать опеку или управление этими территориями передовым державам от имени Лиги Наций Великобритания получила мандаты на управление Палестиной, Транспорданией, Ираком. а также Танганьку, части Того и Камеруна. Франция - на Сирию, Ливан и части территории Того и Камеруна. Бельгия - на Руанду-Урунди. Япония - на Маршалловы Каролинские и Марианские острова. Южно-Африканский на бывшую германскую Юго-Западную Африку. Союз Вашингтонская конференция. После урегулирования спорных вопросов в Европе возникла необходимость разрешения противоречий между державами на Дальнем Востоке, поэтому в 1921-1922 г прошла Вашингтонская мирная конференция. После Первой мировой войны международная обстановка на Дальнем Востоке и в районе Тихого океана во многом изменилась. Япония, которая фактически не принимала участия в войне, воспользовавшись тем, что главные ее соперники были заняты на европейском театре военных действий, укрепила свои позиции на Тихом океане и Дальнем Востоке. Японская Экспансия в этом районе вызывала противодействие великих держав. Целью Вашингтонской конференции было рассмотрение вопросов о послевоенном соотношении сил в государствах, расположенных в Тихом океане. и сокращении морских вооружений. Участниками конференции. которая открылась в 1921 г., были заинтересованные в решении спорных вопросов государства: США, Великобритания, Япония, Франция. Италия, Бельгия, Голландия, Португалия и Китай. Во время конференции было заключено три договора. Представители США, Великобритании. Франции и Японии подписали 'Трактат четырех держав'. Он гарантировал островные владения его участников в бассейне Тихого океана, оказывал стабилизирующее воздействие на позиции держав в Тихом океане. Договор укрепил позиции США: с его заключением союз 1902-1921 гг. утрачивал силу англо-японский 'Трактат пяти держав' был подписан США, Великобританией, Японией, Францией, Италией и касался ограничения морских вооружений. Между ними устанавливалось соотношение размеров линейного флота: 5 (США): 5 (Англия): 3 (Япония): 1,75 (Франция): 1,75 (Италия). Для остальных классов кораблей, в том числе под- водных лодок, ограничений не было. Договор запрещал создавать новые военно-морские базы на Тихом океане восточнее 110-го меридиана В. Д. и усиливать береговую охрану, за исключением островов, непосредственно прилегающих к побережью США, Канады. Аляски, Австралии, Новой Зеландии, Гавайских островов. США и Англия не могли иметь военно-морские базы на расстоянии менее 5 тыс. км от Японии. Это решение явилось крупным стратегическим Выигрышем для этой страны. В целом договор пяти держав устанавливал глобальное военно-морское равновесие. Особое внимание на Вашингтонской конференции было уделе- но проблеме Китая. 'Трактат девяти держав был подписан всеми участниками конференции. Он провозглашал принцип суверенитета и территориальной целостности Кита я. Договор содержал обязательства придерживаться принципов 'открытых дверей' и 'равных возможностей' для торговли и промышленности 'всех наций на всей территории Китая'. В целом договор создавал угрозу ограбления и закабаления Китая наиболее сильными государствами. Решения Вашингтонской конференции дополняли Версальский мирный договор 1919г. и явились попыткой держав, главным об- разом США, создать новое равновесие сил на Дальнем Востоке и в Тихом океане. Противоречивость и слабость Версальско-Вашингтонской системы. Совокупность договоров и соглашений, заключенных в Версале и Вашингтоне, стала называться Версальско-Вашингтонской cucmeмой. В целом Версальско-Вашингтонская система завершила процесс послевоенного мирного урегулирования и подготовила условия для временной отношений. относительной стабилизации международных системы. Тем не менее эта система была внутренне противоречивой, она не смогла устранить все спорные вопросы и противоречия в международных отношениях. Границы новых европейских государств опрделялись без учета мнения народов, населявших эти территории. В Германии, Венгрии, Болгарии вопрос о возвращении утерянных территории стал одним из главных во внутренней и внешней политике. Италия, во время войны перешедшая в лагерь Антанты, относилась к странам-победительницам, но ее интересы не были учтены на Парижской конференции. Усилилась роль США на международной арене, заметно возросло влияние Японии на Дальнем Востоке. Так были заложены основы новых разногласий и конфликтов."
    
    Label(PageBook3, text=" ").pack()
    
    label5 = Label(PageBook3, text="ПОСЛЕДСТВИЯ ПЕРВОЙ МИРОВОЙ ВОЙНЫ", fg="blue", cursor="hand2")
    label5.place(x= 1290, y= 400)
    label5.bind("<Button-1>", callback)
    
    t = Text(PageBook3, width=130, height=53)
    t.insert(1.0, w)
    t.place(x=0, y=40)
    
    Button(PageBook3, text="Back", command=BackMainPage).place(x=10, y=10)
    

def PageBookTest3():
    global PageBookTest3
    PageBookTest3 = Tk()
    PageBookTest3.title("Проверь свои знания к §1")
    PageBookTest3.geometry("1920x1080")
    PageBookTest3.resizable(0, 0)
    
    
    
    
    var = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var.set(0)
    
    

    def BackMainPage():
        PageBookTest3.destroy()
    
    
    Button(PageBookTest3, text="Back", command=BackMainPage).place(x=10,y=10)


    
    def change():
        varr = var.get()
        print (varr)
        if varr == 0:
            Label(PageBookTest3, text="Correct").place(x=75, y=175)
        else:
            Label(PageBookTest3, text="Incorrect").place(x=75, y=175)
            
    def change2():
        if var2.get() == 0:
            lb2 = Label(PageBookTest3, text="Correct").place(x=75, y=330)
        else:
            lb2 =  Label(PageBookTest3, text="Incorrect").place(x=75, y=330)

    
    def change3():
        if var3.get() == 0:
            lb3 = Label(PageBookTest3, text="Correct").place(x=75, y=485)
        else:
            lb3 =  Label(PageBookTest3, text="Incorrect").place(x=75, y=485)
            
    def change4():
        if var4.get() == 0:
            lb4 = Label(PageBookTest3, text="Correct").place(x=75, y=650)
            Label(PageBookTest3, text="Вы Завершили Тест!").place(x=100, y=700)
        else:
            lb4 =  Label(PageBookTest3, text="Incorrect").place(x=75, y=650)
            Label(PageBookTest3, text="Вы Завершили Тест!").place(x=100, y=700)
        
    
    
    
    
    Label(PageBookTest3, text="Тест на знание 3 Параграфа").place(x=500, y=10)
    
    
    
    #1 vopros
    Label(PageBookTest3, text="Кто такой Гаврило Принцип?:").place(x=20, y=40)
    
    r1 = Radiobutton(PageBookTest3, text="Полицейский",   variable=var, value=1 ,command=change).place(x=40, y=70)
    r2 = Radiobutton(PageBookTest3, text="Студент",       variable=var, value=0 ,command=change).place(x=40, y=95)
    r3 = Radiobutton(PageBookTest3, text="Медбрат",       variable=var, value=2 ,command=change).place(x=40, y=120)
    r4 = Radiobutton(PageBookTest3, text="Водитель",      variable=var, value=3 ,command=change).place(x=40, y=145)
    
    
    
    
    #2 vopros
    Label(PageBookTest3, text="Выберите страны Антанты:").place(x=20, y=200)
    
    r12 = Radiobutton(PageBookTest3, text="Англия, Франция, Россия",                               variable=var2, value=0 ,command=change2).place(x=40, y=230, anchor=W)
    r22 = Radiobutton(PageBookTest3, text="Германская империя, Османская империя, Австро-Венгрия", variable=var2, value=1 ,command=change2).place(x=40, y=255, anchor=W)
    r32 = Radiobutton(PageBookTest3, text="Англия, Франция, Сербия",                               variable=var2, value=2 ,command=change2).place(x=40, y=280, anchor=W)
    r42 = Radiobutton(PageBookTest3, text="Англия, Испания, Италия",                               variable=var2, value=3 ,command=change2).place(x=40, y=305, anchor=W)
    
    
    # mu btn last i new lab = 35/ mu lab i radio = 30 / mu radiobutoon = 25/ radiobutton i btn = 25
    
    
    
    
    #3 vorpos
    Label(PageBookTest3, text="Когда Австро-Венгрия объявила войну Сербии?:").place(x=20, y=355)
    
    r1s = Radiobutton(PageBookTest3, text="28 июня 1914",      variable=var3, value=2 ,command=change3).place(x=40, y=385, anchor=W)
    r2 = Radiobutton(PageBookTest3, text="1 августа 1914",    variable=var3, value=1 ,command=change3).place(x=40, y=410, anchor=W)
    r3 = Radiobutton(PageBookTest3, text="28 июля 1914",      variable=var3, value=0 ,command=change3).place(x=40, y=435, anchor=W)
    r4 = Radiobutton(PageBookTest3, text="1 января 1914",     variable=var3, value=3 ,command=change3).place(x=40, y=460, anchor=W)
    
    
    
    
    
    
    #4 vorpos
    Label(PageBookTest3, text="Члены Тройственного союза:").place(x=20, y=520)
    
    r1 = Radiobutton(PageBookTest3, text="Италия, Австро-Венгрия, Франция",    variable=var4, value=2 ,command=change4).place(x=40, y=550, anchor=W)
    r2 = Radiobutton(PageBookTest3, text="Италия, Австро-Венгрия, Германия",   variable=var4, value=0 ,command=change4).place(x=40, y=575, anchor=W)
    r3 = Radiobutton(PageBookTest3, text="Италия, Франция, Англия",            variable=var4, value=1 ,command=change4).place(x=40, y=600, anchor=W)
    r4 = Radiobutton(PageBookTest3, text="Россия, Османская империя, Италия",  variable=var4, value=3 ,command=change4).place(x=40, y=625, anchor=W)



AuthPage()
Tk().mainloop
