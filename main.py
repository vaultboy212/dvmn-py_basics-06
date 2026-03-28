def main():
    score = 0
    password = input('Введите пароль:')

    def is_very_long(password):
        return len(password) >= 12

    def has_digit(password):
        return any(letter.isdigit() for letter in password)

    def has_lower_letters(password):
        return any(letter.islower() for letter in password)

    def has_upper_letters(password):
        return any(letter.isupper() for letter in password)

    def has_symbols(password):
        return any(not letter.isdigit() and not letter.isalpha()
                   for letter in password)

    checks = [
        is_very_long,
        has_digit,
        has_lower_letters,
        has_upper_letters,
        has_symbols
    ]

    for check in checks:
        if check(password):
            score += 2

    print('Рейтинг пароля', score)


if __name__ == "__main__":
    main()
