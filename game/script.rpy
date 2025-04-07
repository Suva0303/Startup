# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define u = Character('Админ УО', color="#c8ffc8", image = 'admin_uo')

define k = Character('Куратор', color="#c8ffc8", image = 'kurator')

define g = Character('Админ Компа', color="#c8ffc8", image = 'admin_k')

define f = Character('Физрук', color="#c8ffc8", image = 'fizruk')

define oskorbit = False
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

init: 
    $ left2 = Position(xalign=0.2, yalign=0.99) # Выравнивание по центру по оси X и Y
    $ right2 = Position(xalign=0.7, yalign=1.1) # Выравнивание по центру по оси X и Y

# Игра начинается здесь:
label start:

    scene bg mirea
    with dissolve

    show kurator at right2

    with dissolve

    # {w} - позволяет дописывать текст при нажатии
    k '''
    Добрый день! Ты, наверное, мой новый студент? 
    
    Я Арион и твой куратор на сегодня

    Сегодня я проведу тебе экскурсию по нашему прекрасному вузу

    Позади меня наш главный корпус, именно туда мы сегодня направимся

    Чтож давай начнем и зайдем внутрь 
    '''
    hide kurator
    with dissolve

    scene bg hall
    with dissolve

    show kurator at right2
    with dissolve

    k '''
    Это наш главный холл, и чтобы попасть внутрь тебе нужно пройти через турникеты.

    Для этого тебе в будущем нужен будет студенческий билет, он твой пропуск в вуз

    Хочешь подробнее узнать об активностях вуза?

    '''
    
    k "Тебе нравится наш вуз?"

    menu:
        "Какой ответ выберешь?"

        "Да все супер":
            "Куратор счастлив"
        
        "Нет ты мне не нравишься":
            "Куратор обиделся"
            $ oskorbit = True

    menu: 
        "Выбрать дальнейшее действие"

        "Узнать про активности":
            jump active # jump - команда для перехода к другому label 

        "Прогулятся по вузу":
            jump koridor

    hide kurator
    with dissolve

    return

# Ветка про рассказ активностей 
label active: 
    scene bg koridor 
    with dissolve

    show kurator at right2
    with dissolve
    #Проверка на оскорбление куратора
    if oskorbit: 
        k "Я обижен на тебя и не буду ничего показывать!"
        hide kurator
        with dissolve

        menu:
            "Ты обидел куратора, что будешь делать дальше?"

            "Прогуляюсь по вузу": 
                jump koridor
            "Выйду на улицу":
                show bg game over 
                with dissolve
    else:
        k '''
        Я поддробно расскажу тебе про активности в нашем вузе
        '''
        "Рассказывает про активности"

        k"Хочешь проведу краткий экскурс по вузу?"

        menu:
            "Что ты хочешь сделать?"

            "Согласиться на экскурс":
                jump ekskurs
            "Пойти гулять самому":
                jump koridor

    return

# Ветка если выбрал погулять по вузу
label koridor:

    scene bg koridor
    with dissolve

    '''
    Ты находишься в коридоре вуза 
    '''

    menu: 
        "Куда хочешь пойти?"

        "Спуститься вниз по лестнице": 
            jump game

        "Пойти прямо":
            jump UO

        "Пойти на лево":
            jump Sport

        "Догнать куратора ":
            if oskorbit:
                jump sorry
            else:
                jump ekskurs

    return

# Ветка про компьютерный клуб
label game: 

    scene bg game
    with dissolve

    show admin_k at right2
    with dissolve

    g '''
    О новичок? 

    Это компьтерный клуб вуза, а я тут всем заправляю. 
    '''
    menu: 
        "Отказаться и выйти в коридор": 
            jump koridor
        "Послушать":
            "Рассказывает про компютеры итп"
            jump koridor

    return

# Ветка учебный отдел
label UO:

    scene bg office
    with dissolve

    show admin_uo
    with dissolve

    u '''
    Привет новичок

    Я админ УО 

    Хочешь подробнее узнать про сессию итп?
    '''

    menu: 
        "Отказаться и выйти в коридор": 
            jump koridor
        "Послушать":
            "Рассказывает про сессию итп"
            jump koridor

    return

# Ветка физрука
label Sport: 

    scene bg kachalka
    with dissolve

    show fizruk
    with dissolve

    f '''
    Здарово новобранец!

    Я преподаватель физкультуры и скорее всего ты попадешь ко мне

    Я очень требователен и буду вас жеско гонять
    '''

    menu: 
        "Что ты сдеалешь после встречи с физруком?"

        "Сбежать со всех ног":
            jump koridor

        "Послушать физрука":
            jump koridor
    return

# Ветка экскурсии по вузу
label ekskurs:

    scene bg koridor
    with dissolve

    show kurator at right2
    with dissolve

    k'''
    Чтож я проведу тебе краткий экскурс по нашему вузу

    Начнем по порядку
    '''

    scene bg stolovka
    with dissolve

    show kurator at right2
    with dissolve

    k'''
    Это самое главное место столовая 

    Здесь самые вкусные бургеры

    И также есть Добрый кола С САХАРОМ!
    '''

    scene bg lectory
    with dissolve

    show kurator at right2
    with dissolve

    k'''
    А это наш лектории, здесь ты будешь слущать лекции 
    '''
    scene bg class
    with dissolve

    show kurator at right2
    with dissolve

    k'''
    А это наши аудитории здесь будут проходить семинары 
    '''

    scene bg comp_class
    with dissolve

    show kurator at right2
    with dissolve

    k '''
    А это аудитории оборудованные компьютерами, здесь будут проходить практические занятия

    В целом это пока все, {w} Подожди меня в корридоре я пока отлучусь в уборную.
    '''
    jump koridor

    return

# Ветка с извинениями у куратора
label sorry:

    scene bg koridor
    with dissolve

    show kurator
    with dissolve

    k'''
    Пришел еще меня оскорблять?

    Или извинишься
    '''

    menu:
        "Куратор весьма зол на тебя"
        "Что ты будешь делать дальше?"

        "Ивзинюсь":
            k"Хорошо я тогда проведу тебе экскурсию!"
            jump ekskurs
        "Пошлю его и вернусь домой":
            hide kurator
            show bg game over 
            with dissolve

    return