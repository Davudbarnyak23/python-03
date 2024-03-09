import os
os.system("clear")


print("=============================")
print("===========start=============")
print("=============================", end='\n'*3)

p = "123"
passw = input("paswork: ")

if passw == p:
    print("************")
    print("  молодець")
    print("============")
    allow = input("дати доступ до даних y/n")
    if allow =="y":
        print("ядерка запущена")
        print("\n","\U0001f44d \U0001F923")
    else:
        print("самознищеня через 5 сек.")


elif passw == "user":
    print("************")
    print("увийшли як гість")
    print("============")

elif passw == "uer":
    print("************")
    print("увийшли як гість 1")
    print("============")
else:
    print("не получилось \" ' взламати :(")