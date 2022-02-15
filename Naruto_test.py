def check_guess(guess, answer):
    global score
    if guess != answer:
        print('Ответ не верный')
    else:
        print('Ответ верный')
        score = score + 1
score = 0
print('Тест "Наруто"')
guessl = input('Как зовут отца Наруто? а)Намикадзе б)Минато в)Дейдара : ')
check_guess(guessl, 'б')
guess2 = input('кто такой Какаши? а)друг Наруто б)двоюродный дядя Наруто в)учитель Наруто : ')
check_guess(guess2, 'в')
guess3 = input('Кто такой Саске? а)друг Наруто б)брат Наруто в)отец Наруто : ')
check_guess(guess3, 'а')
guess4 = input('Кто такая Кушина ? а)мама Наруто б)сестра Наруто в)такого персонажа нет : ')
check_guess(guess4, 'а')
guess5 = input('Как зовут брата Саске? а)Хидан б)Джирая в)Итачи : ')
check_guess(guess5, 'в')
guess6 = input('Кто такой Аматерасу? а)Человек б)это не человек, это техника в)это питомец Саске : ')
check_guess(guess6, 'б')
guess7 = input('Сакура, кто это ? а)дерево б)подруга Наруто и Саске в)хокаге : ')
check_guess(guess7, 'б')
guess8 = input('Чидори это техника ? а)Наруто б)Саске в)Минато : ')
check_guess(guess8, 'б')
guess9 = input('У Наруто есть брат или сестра ? а)да б)нет : ')
check_guess(guess9, 'б')
print('Поздравляю! Вы набрали очков:'+ str(score))