def send_email(message, recipient, sender="university.help@gmail.com"):
    domain = ["ru", "com", "net"]
    doge = '@'

    rec_split = recipient.rsplit('@')
    rec_split = rec_split[1].split('.')
    rec_split = rec_split[1]

    send_split = sender.rsplit('@')
    send_split = send_split[1].split('.')
    send_split = send_split[1]

    if (not (doge in recipient and rec_split in domain)) or (not (doge in sender and send_split in domain)):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print(f"Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')