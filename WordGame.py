import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Создаём объект переводчика
translator = Translator()


# Функция для получения и перевода информации
def get_english_words():
    url = "https://randomword.com/"
    try:
        # Получаем данные с сайта
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Получаем слово и описание
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        # Переводим слово и его описание на русский
        translated_word = translator.translate(english_word, src="en", dest="ru").text
        translated_definition = translator.translate(word_definition, src="en", dest="ru").text

        # Возвращаем переведённые данные
        return {
            "english_word": english_word,
            "word_definition": word_definition,
            "translated_word": translated_word,
            "translated_definition": translated_definition
        }
    except Exception as e:
        print("Произошла ошибка:", e)
        return None


# Функция для игры
def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_data = get_english_words()
        if not word_data:
            print("Не удалось получить данные. Попробуйте снова.")
            continue

        # Получаем данные
        word = word_data["translated_word"]
        word_definition = word_data["translated_definition"]

        # Начинаем игру
        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ").strip()

        if user.lower() == word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный. Было загадано слово - {word}")

        # Возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n ").strip().lower()
        if play_again != "y":
            print("Спасибо за игру!")
            break


# Запускаем игру
word_game()
