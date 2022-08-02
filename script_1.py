def translate_number(number):
    message = ""
    if number % 3 == 0:
        message += "xepe"
    if number % 5 == 0:
        message += "lin"

    return message.capitalize()


if __name__ == "__main__":
    result = translate_number(2)
    print(result)
