user_list = []
file = open('list.txt', 'r')
for i in file.readlines():
    user_list.append(i.strip())
while True:
    print("Input values: 1. Add Task \n2. Edit Task \n3. Delete Task \n4. Exit")
    action = int(input('Action: '))
    if action == 4:
        file = open('list.txt', 'w')

        for i in user_list:
            file.write('%s\n' % i)
        break
    elif action == 1:
        task = input('input task: ')
        user_list.append(task)
    elif action == 5:
        i = 0
        for item in user_list:
            print(i, '>', item)
            i += 1
    elif action == 3:
        delete_index = int(input('del'))
        user_list.remove(delete_index)
    elif action == 2:
        edit_index = int(input('edit'))
        user_list.index(edit_index)
