class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    #new_password = (input("Введите старый пароль: "))
    def set_password(self, new_password):
        #self.new_password = new_password
        if len(new_password) < 4:
            print("ошибка")
            return False
        self.__password = new_password
        print("пароль изменен")
        return True
    def check_password(self, password):
        return password == self.__password


userAccount = UserAccount("sss", "sss@gmail.com", "sss2280")


print(f"проверка пароля 'qwerty123': {userAccount.check_password('qwerty123')}")
print(f"проверка пароля 'неверный': {userAccount.check_password('неверный')}")
print(f"пробуем поставить короткий пароль '123':")
userAccount.set_password('123')
print(f"пробуем поставить хороший пароль 'sss2280':")
userAccount.set_password('sss2280')
print(f"проверка новго пароля 'sss2280': {userAccount.check_password('sss2280')}")

#print(userAccount.check_password())
#userAccount.set_password("sss2280")
#print(userAccount.check_password())