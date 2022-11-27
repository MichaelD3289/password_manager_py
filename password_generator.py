# Password Generator Project
from random import choice, randint, shuffle

all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
all_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
all_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def create_password():
    letters = [choice(all_letters) for _ in range(randint(8, 10))]
    symbols = [choice(all_symbols) for _ in range(randint(2, 4))]
    numbers = [choice(all_numbers) for _ in range(randint(2, 4))]

    password_list = letters + symbols + numbers

    shuffle(password_list)

    return ''.join(password_list)
