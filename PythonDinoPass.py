import requests


number_of_passwords = 100
min_password_length = 8
max_password_length = 10

password_array = []
URL = 'http://www.dinopass.com/password/simple'

# increment variable for while loop
i = 0
while True:
    r = requests.get(url=URL)

    # only add passwords to array that are above min and below max
    if len(r.text) < min_password_length or len(r.text) > max_password_length:
        continue
    password_array.append(r.text)

    # Quit while loop when num passwords reached
    if len(password_array) == number_of_passwords:
        break

    # Show progress
    if i % 10 == 0:
        print(str(len(password_array)) + ' passwords generated.')

    # increment the counter
    i += 1

# print them to the screen
for i in password_array:
    print(i)
