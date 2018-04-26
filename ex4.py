def create_task(string):
    answer=input('Is it urgent? [y/n]: ')
    if  answer == 'y':
        temp='True'
    elif answer == 'n':
        temp='False'
    else:
        print("try again")
        return None
    return {'todo':string,'urgent':temp}

def create_dictionary():
    dictionary=[]

    while True:
        task=None
        string = input('scrivi la stringa: ')
        if string=='end':
            break
        while task == None:
            task=create_task(string)
        dictionary.append(task)

    return dictionary

def show_dictionary(dictionary):
    for task in dictionary:
        print(task)
    print('')

def delete_not_urgent(dictionary):
    for task in dictionary:
        if task['urgent']=='False':
            dictionary.remove(task)
            delete_not_urgent(dictionary)

if __name__=='__main__':
    tasks=create_dictionary()
    show_dictionary(tasks)
    delete_not_urgent(tasks)
    show_dictionary(tasks)