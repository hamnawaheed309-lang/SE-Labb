def login(username, password):
    if username == "admin" and password == "1234":
        return "Login Successful"
    else:
        return "Invalid Credentials"


def main():
    user = input("Enter username: ")
    pwd = input("Enter password: ")

    result = login(user, pwd)
    print(result)


if __name__ == "__main__":
    main()