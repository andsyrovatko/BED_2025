# BED_2025
Test task for BED_2025

# Відновлення Пошкодженого Тексту

## Опис Задачі

Ця програма призначена для відновлення англомовного тексту,
який був пошкоджений внаслідок невідомого "шифрування".
Cпотворення полягає в:
* Заміні деяких літер символом `*` (1 зірочка = 1 літера).
* Випадкове перемішування букв у деяких словах.
* Видалення всіх пробілів та знаків пунктуації.

Приклад: `H*ll*Wrodl` -> `Hello World`

## Використаний Підхід

### 1. Словниковий Пошук
Основою рішення є використання великого англомовного словника (`words_alpha.txt`).
Всі слова зі словника завантажуються та використовуються для перевірки потенційних кандидатів на відновлення.

### 2. Частотний Аналіз Літер
Для підстановки літер на місце символів `*` використовується частотний аналіз літер з завантаженого словника.
Більш часті літери мають пріоритет.

### 3. Жадібний Алгоритм Розбиття
Оскільки пробіли видалені, програма використовує "жадібний" підхід для розбиття вхідного пошкодженого рядка на потенційні слова.
Вона намагається знайти найдовше можливе слово, що відповідає словнику, починаючи з поточної позиції в тексті.

### 4. Обробка Символів `*`
Функція `_find_possible_words` перевіряє, чи відповідає потенційне слово зі словника сегменту пошкодженого тексту, враховуючи символи `*` як "будь-яку літеру".

### 5. Обробка Перестановок (Майбутні Покращення)
На поточному етапі обробка перестановок літер у словах є спрощеною.
Для повноцінного вирішення цієї частини завдання необхідна інтеграція більш складних евристик, таких як:
* Використання відстані Левенштейна (Levenshtein distance) для пошуку "найближчих" слів.
* Обмеження кількості перестановок за довжиною слова або кількістю зіпсованих літер.
* Генерація перестановок тільки для тієї частини слова, яка, ймовірно, була перемішана.

### 6. N-грамний Аналіз (Майбутні Покращення)
Для підвищення якості відновлення тексту, особливо при розбитті на слова та виборі між кількома кандидатами, планується інтеграція N-грамних моделей (наприклад, біграм або триграм). Це дозволить оцінювати ймовірність послідовності слів та вибирати найбільш осмислені комбінації.

## Вимоги та Залежності

* **Python 3**: Програма написана на Python 3.
* **Словник**: Потрібен файл зі списком англійських слів, наприклад `words_alpha.txt`.
Його можна знайти за посиланням: [https://github.com/dwyl/english-words/blob/master/words_alpha.txt](https://github.com/dwyl/english-words/blob/master/words_alpha.txt). Розмістіть його в тій же директорії, що й файли Python.
* Програма працює локально, без доступу до інтернету.

## Як Запустити

1.  Завантажте всі файли (`main.py`, `text_restorer.py`, `dictionary_manager.py`, `README.md`).
2.  Завантажте файл словника `words_alpha.txt` і розмістіть його в тій же директорії, де й програма.
3.  "Поламаний" текст потрібно вставити у файл `input_corrupted_text.txt` в тій же директорії, де й програма.
4.  Відкрийте термінал або командний рядок у директорії з файлами.
5.  Запустіть програму командою:
    ```bash
    python main.py
    ```
OR
    ```bash
    python3 main.py
    ```
5.  Відновлений текст буде виведений у консоль та збережений у файл `recovered_text.txt`.

## Подальший Розвиток

* Вдосконалення алгоритму розбиття тексту на слова.
* Покращення логіки обробки перестановок літер.
* Реалізація N-грамного аналізу для оцінки вірогідності послідовностей слів.
* Інтеграція більш складних лінгвістичних моделей (наприклад, Parts-of-Speech tagging).
