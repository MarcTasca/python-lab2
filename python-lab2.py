from sys import argv

#aggiungi elememto alla lista
def add_item(list):
    list.append(input('add item: '))

#fill the list with the task_list.txt
def create_list():
    file = open(argv[1],'r')
    list=file.read().split('\n')
    file.close()
    recursive_remove_items(list,'')
    return list

#elimina ricorsivamente tutte le task uguali
def recursive_remove_items(list,item):
    if list.count(item) > 0:
        list.remove(item)
        recursive_remove_items(list,item)

#elimina le task uguali dalla lista con funzione sopra
def remove_item(list):
    item = input('remove item: ')
    if list.count(item) > 0:
        recursive_remove_items(list,item)
    else:
        print("la task non è nella lista")

#rimuovo gli elementi con la ricorsione con sottostringhe
def recursive_remove_item_substring(list,substring):
    for item in list:
        if substring in item:
            list.remove(item)
            recursive_remove_item_substring(list,substring)

def remove_item_substring(list):
    substring = input('remove item by substring: ')
    recursive_remove_item_substring(list,substring)

#stampa a schermo tutte le task in lista
def show_items(list):
    list.sort()
    print('print items:')
    for item in list:
        print(item)

def save_tasks(list):
    file=open(argv[1],'w')
    for item in list:
        file.write(item+'\n')
    file.close()

#main del programma
if __name__=='__main__':
    list=create_list()
    while True:
        n=int(input("1. insert a new task."
                    "\n2. remove a task."
                    "\n3. show all the tasks."
                    "\n4. close the program."
                    "\n--> "))
        if n==1:
            add_item(list)
        elif n==2:
            #remove_item(list)
            remove_item_substring(list)
        elif n==3:
            show_items(list)
        elif n==4:
            save_tasks(list)
            del list
            break
        else:
            print("non ho capito")
        print("--------------------")