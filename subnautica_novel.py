









print("SUBNAUTICA: ПОСЛЕДНИЙ СИГНАЛ")
print("После крушения «Авроры» ты оказался на планете 4546B.")
print("Пройди четыре этапа и выбери, чем закончится твоя история.")
name = input("Имя героя: ").strip()
while name == "":
    name = input("Имя не должно быть пустым: ").strip()
health = 100
stage = 1
ending = ""
inventory = []
tasks = set()
descriptions = {
    "титан": "металл для ремонтного инструмента",
    "медь": "проводник для ремонтного инструмента",
    "аптечка": "восстанавливает 30 единиц здоровья",
    "инструмент": "позволяет починить капсулу",
    "металл": "отвлекает сталкера своим блеском",
    "антенна": "позволяет передать сигнал спасателям",
    "фиолетовый ключ": "первая часть замка шлюза",
    "синий ключ": "вторая часть замка шлюза",
    "двигатель": "нужен для запуска спасательной ракеты",
    "водоросль": "первый компонент фермента",
    "гриб": "второй компонент фермента",
    "фермент": "помогает вылечить бактерию Хараа",
}
print("Добро пожаловать,", name)
print("Команда «рюкзак» показывает предметы и их назначение.")
print("Команда «аптечка» лечит героя, если аптечка найдена.")


story = (
    "Ты просыпаешься в спасательной капсуле № 5.",
    "За окном плещется океан, а на горизонте горит «Аврора».",
    "Панель шлюза искрит. Выйти через неё пока невозможно.",
    "На полу лежат титан, медь и аптечка.",
    "На схеме нарисовано: титан + медь = ремонтный инструмент.",
    "Ты пытаешься вспомнить, что произошло перед падением.",
    "Сирена, вспышка за иллюминатором, удар о воду.",
    "Компьютер сообщает: связь с экипажем потеряна.",
    "На экране висит последний приказ капитана: выжить.",
    "Ты осторожно поднимаешься, держась за край сиденья.",
    "В стене потрескивает повреждённый кабель.",
    "Если восстановить панель, капсула станет безопасным убежищем.",
    "Сначала нужно разобраться с предметами вокруг.",
)
for line in story:
    print(line)
resources = ("титан", "медь", "аптечка")
commands = ["осмотреть", "рюкзак", "аптечка", "собрать", "ремонт"]
for item in resources:
    commands.append("взять " + item)
while stage == 1 and health > 0:
    print("Действия:", ", ".join(commands))
    command = input("Капсула > ").strip().lower()
    while command not in commands:
        command = input("Нет такой команды. Выбери действие из списка: ").strip().lower()
    while command == "осмотреть":
        print("Собери титан и медь, создай инструмент и выполни ремонт.")
        print("На полу осталось:")
        for item in resources:
            while "взять " + item in commands:
                print("-", item)
                break
        break
    while command == "рюкзак":
        print("Предметов:", len(inventory))
        for item in inventory:
            print(item, "—", descriptions[item])
        break
    while command == "аптечка":
        print("Для лечения нужна аптечка в рюкзаке.")
        while "аптечка" in inventory:
            health = min(100, health + 30)
            inventory.remove("аптечка")
            print("Ты перевязал раны. Здоровье:", health)
            break
        break
    for item in resources:
        while command == "взять " + item:
            inventory.append(item)
            commands.remove(command)
            print("В рюкзак добавлен предмет:", item)
            break
    while command == "собрать":
        print("Для сборки нужны титан и медь.")
        while "титан" in inventory and "медь" in inventory:
            inventory.remove("титан")
            inventory.remove("медь")
            inventory.append("инструмент")
            print("Ремонтный инструмент готов!")
            break
        break
    while command == "ремонт":
        print("Проверка: нужен ремонтный инструмент.")
        while "инструмент" in inventory:
            tasks.add("капсула починена")
            stage = 2
            print("Шлюз открывается. Ты выплываешь в океан.")
            break
        break


story = (
    "В лесу водорослей ты находишь инопланетный шлюз.",
    "На двери два гнезда: фиолетовое и синее.",
    "Ключи лежат за сталкером, охраняющим проход.",
    "Рядом на песке видны кусок металла и старая антенна.",
    "Сталкеры любят блестящие предметы. Это может помочь.",
    "Над головой качаются длинные зелёные стебли.",
    "Вода здесь темнее, чем возле спасательной капсулы.",
    "Сталкер следит за тобой из тени каменной арки.",
    "Он сжимает в зубах обломок корабельной обшивки.",
    "Ты замечаешь, как хищник реагирует на блеск металла.",
    "На шлюзе вырезаны два одинаковых по форме углубления.",
    "Одного ключа явно недостаточно: нужны оба цвета.",
    "Ты решаешь, потратить время на хитрость или рискнуть здоровьем.",
)
for line in story:
    print(line)
required_keys = {"фиолетовый ключ", "синий ключ"}
found_keys = set()
resources = ("металл", "антенна")
commands = ["осмотреть", "рюкзак", "аптечка", "отвлечь", "проплыть", "открыть"]
for item in resources:
    commands.append("взять " + item)
for item in ("фиолетовый ключ", "синий ключ"):
    commands.append("взять " + item)
while stage == 2 and health > 0:
    print("Действия:", ", ".join(commands))
    command = input("Лес водорослей > ").strip().lower()
    while command not in commands:
        command = input("Нет такой команды. Выбери действие из списка: ").strip().lower()
    while command == "осмотреть":
        print("Отвлеки сталкера металлом или рискни проплыть мимо.")
        print("Для шлюза нужны оба ключа:", required_keys)
        print("Уже собраны:", found_keys)
        break
    while command == "рюкзак":
        for item in inventory:
            print(item, "—", descriptions[item])
        break
    while command == "аптечка":
        print("Для лечения нужна аптечка в рюкзаке.")
        while "аптечка" in inventory:
            health = min(100, health + 30)
            inventory.remove("аптечка")
            print("Здоровье:", health)
            break
        break
    for item in resources:
        while command == "взять " + item and item not in inventory:
            inventory.append(item)
            commands.remove(command)
            print("Ты подобрал:", item)
            break
    while command == "отвлечь":
        print("Чтобы отвлечь сталкера, нужен металл.")
        while "металл" in inventory and "сталкер пройден" not in tasks:
            inventory.remove("металл")
            tasks.add("сталкер пройден")
            print("Сталкер уносит металл. Путь к ключам свободен.")
            break
        break
    while command == "проплыть" and "сталкер пройден" not in tasks:
        health -= 25
        tasks.add("сталкер пройден")
        print("Ты проскользнул мимо, но получил укус. Здоровье:", health)
        break
    for item in ("фиолетовый ключ", "синий ключ"):
        while command == "взять " + item:
            print("Ключ можно взять, когда сталкер пройден.")
            while "сталкер пройден" in tasks and item not in inventory:
                inventory.append(item)
                found_keys.add(item)
                commands.remove(command)
                print("Ты забрал:", item)
                break
            break
    while command == "открыть":
        print("Проверка замка: нужны два разных ключа.")
        while found_keys == required_keys:
            tasks.add("шлюз открыт")
            stage = 3
            print("Оба ключа подходят. Шлюз открывает путь к «Авроре».")
            break
        break


story = (
    "Через подводный тоннель ты добираешься до трюма «Авроры».",
    "Внутри гремит аварийный сигнал: реактор перегревается.",
    "За защитным экраном виден двигатель спасательной ракеты.",
    "Панель управления предлагает три действия.",
    "Ошибка вызовет выброс пара и отнимет 20 единиц здоровья.",
    "Аварийное освещение превращает коридор в красный тоннель.",
    "Ты находишь на стене инструкцию технической службы.",
    "Большая часть букв стёрта, но сканирование восстановит запись.",
    "Клапан нельзя трогать, пока система не остыла.",
    "Отключать питание тоже нужно в нужный момент.",
    "Двигатель за экраном выглядит почти неповреждённым.",
    "Без него о возвращении домой останется только мечтать.",
    "Ты кладёшь руку на панель и стараешься не торопиться.",
)
for line in story:
    print(line)
sequence = ("охлаждение", "клапан", "питание")
step = 0
commands = ["сканировать", "рюкзак", "аптечка", "охлаждение", "клапан", "питание", "взять двигатель", "уйти"]
while stage == 3 and health > 0:
    print("Действия:", ", ".join(commands))
    command = input("Реактор > ").strip().lower()
    while command not in commands:
        command = input("Нет такой команды. Выбери действие из списка: ").strip().lower()
    while command == "сканировать":
        print("Инструкция: сначала охлаждение, затем клапан, затем питание.")
        print("Порядок действий:", sequence)
        print("Выполнено шагов:", step, "из", len(sequence))
        break
    while command == "рюкзак":
        for item in inventory:
            print(item, "—", descriptions[item])
        break
    while command == "аптечка":
        print("Для лечения нужна аптечка в рюкзаке.")
        while "аптечка" in inventory:
            health = min(100, health + 30)
            inventory.remove("аптечка")
            print("Здоровье:", health)
            break
        break
    while command in sequence and step < len(sequence):
        is_correct = command == sequence[step]
        while is_correct:
            step += 1
            print("Действие выполнено. Завершено шагов:", step)
            break
        while not is_correct:
            health -= 20
            print("Неверный порядок! Пар обжигает тебя. Здоровье:", health)
            print("Посмотри инструкцию командой «сканировать».")
            break
        break
    while step == len(sequence) and "реактор выключен" not in tasks:
        tasks.add("реактор выключен")
        print("Реактор выключен. Защитный экран двигателя поднят.")
        break
    while command == "взять двигатель":
        print("Двигатель доступен только после выключения реактора.")
        while "реактор выключен" in tasks and "двигатель" not in inventory:
            inventory.append("двигатель")
            commands.remove(command)
            print("Ты забираешь двигатель спасательной ракеты.")
            break
        break
    while command == "уйти":
        print("Перед уходом нужно забрать двигатель.")
        while "двигатель" in inventory:
            stage = 4
            print("На карте появляется сигнал Морского императора.")
            break
        break


story = (
    "В глубине океана тебя встречает Морской император.",
    "Его голос звучит прямо в голове: «Ты заражён Хараа».",
    "Из-за инфекции защитная пушка не выпускает корабли с планеты.",
    "Император показывает рецепт: водоросль + гриб = фермент.",
    "После лечения можно отключить пушку и выбрать путь домой.",
    "Вокруг медленно проплывают детёныши древнего существа.",
    "Император говорит, что болезнь пришла задолго до людей.",
    "Ты смотришь на зелёные пятна на собственной ладони.",
    "Теперь становится понятно, почему чужая техника отвергала тебя.",
    "На столе лежат два растения для приготовления лекарства.",
    "Рядом работает терминал управления защитной пушкой.",
    "На поверхности можно собрать ракету или построить новый дом.",
    "Все дороги открыты, но последствия решения будут разными.",
)
while health > 0:
    for line in story:
        print(line)
    break
resources = ("водоросль", "гриб")
commands = ["осмотреть", "рюкзак", "аптечка", "приготовить", "вылечиться", "отключить пушку", "улететь", "остаться", "позвать помощь"]
for item in resources:
    commands.append("взять " + item)
while stage == 4 and health > 0 and ending == "":
    print("Действия:", ", ".join(commands))
    command = input("Комплекс императора > ").strip().lower()
    while command not in commands:
        command = input("Нет такой команды. Выбери действие из списка: ").strip().lower()
    while command == "осмотреть":
        print("Собери водоросль и гриб, приготовь фермент и вылечись.")
        print("Затем отключи пушку. Для вызова спасателей нужна антенна.")
        print("Можно также остаться или попытаться улететь без лечения.")
        break
    while command == "рюкзак":
        for item in inventory:
            print(item, "—", descriptions[item])
        break
    while command == "аптечка":
        print("Для лечения нужна аптечка в рюкзаке.")
        while "аптечка" in inventory:
            health = min(100, health + 30)
            inventory.remove("аптечка")
            print("Здоровье:", health)
            break
        break
    for item in resources:
        while command == "взять " + item and item not in inventory:
            inventory.append(item)
            commands.remove(command)
            print("Ты находишь:", item)
            break
    while command == "приготовить":
        print("Рецепт фермента: водоросль и гриб.")
        while "водоросль" in inventory and "гриб" in inventory:
            inventory.remove("водоросль")
            inventory.remove("гриб")
            inventory.append("фермент")
            tasks.add("фермент приготовлен")
            print("Фермент готов. Теперь можно вылечиться.")
            break
        break
    while command == "вылечиться":
        print("Для лечения Хараа нужен фермент, аптечка не поможет.")
        while "фермент" in inventory:
            inventory.remove("фермент")
            tasks.add("герой здоров")
            print("Зелёные пятна исчезают. Ты победил инфекцию!")
            break
        break
    while command == "отключить пушку":
        print("Пушка подчинится только здоровому человеку.")
        while "герой здоров" in tasks:
            tasks.add("пушка отключена")
            print("Карантин снят. Небо над планетой теперь безопасно.")
            break
        break
    while command == "улететь":
        ending = "5. Небо закрыто"
        while "пушка отключена" in tasks and "двигатель" in inventory:
            ending = "2. Дорога домой"
            break
        break
    while command == "остаться":
        ending = "4. Борьба продолжается"
        while "герой здоров" in tasks:
            ending = "3. Дом среди волн"
            break
        break
    while command == "позвать помощь":
        print("Для спасения нужны антенна и отключённая пушка.")
        while "антенна" in inventory and "пушка отключена" in tasks:
            ending = "6. Ты больше не один"
            break
        break













while health <= 0:
    ending = "1. Океан забирает своё"
    break
endings = {
    "1. Океан забирает своё": "Твои силы иссякли. Последний сигнал теряется в океане.",
    "2. Дорога домой": "Ракета покидает планету. Впереди звёзды и путь к Земле.",
    "3. Дом среди волн": "Ты здоров и строишь подводную базу. Океан стал твоим домом.",
    "4. Борьба продолжается": "Ты остаёшься на планете. Теперь твоя цель — победить Хараа.",
    "5. Небо закрыто": "Пушка ещё активна. Ты отменяешь запуск и остаёшься искать решение.",
    "6. Ты больше не один": "На сигнал отвечает корабль. Над океаном появляется свет спасателей.",
}
print()
print("КОНЦОВКА:", ending)
print(endings[ending])
print("Герой:", name)
print("Здоровье:", max(0, health))
print("Выполненные задачи:")
for task in sorted(tasks):
    print("-", task)
print("Спасибо за игру!")
