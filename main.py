import os
import time
import progressbar

list_name = os.listdir()                # obtendremos la lista de todos los archivos donde se encuentra nuestro script.
list_name_lenght = len(list_name)       # obtendremos la longitud de cada uno de los archivos donde se encuentra
                                        # nuestro script.
new_list = []                           # será un array vacío, donde almacenaremos la lista de los archivos
new_list_updated = []                   # será un array vacío, donde almacenaremos la lista de los archivos con los
                                        # nombres cambiados.


def normalize(s):
    s = s.lower()
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b)
    return s


def _create_list():

    global list_name_lenght, list_name, new_list
    list_name_norm = []
    print('Creando listas…')

    for i in range(list_name_lenght):
        old_name_norm = normalize(old_name)
        list_name_norm.append(normalize(list_name[i]))

        if old_name_norm in list_name_norm[i]:
            print(list_name_norm[i])
            print(list_name[i])
            new_list.append(list_name[i])

        # time.sleep(0.02)


def _create_list_updated():

    print('Creando nueva lista de cambio de nombre…')

    global new_list, new_list_updated

    new_list_updated = [name.replace(old_name, new_name) for name in new_list]


def _change_filename():

    print('Cambiando los nombres de los archivos…')

    global new_list, new_list_updated

    for i in range(len(new_list)):
        try:
            os.rename(new_list[i], new_list_updated[i])
        except FileExistsError:
            print()
            renamed_name = input('Ya existe un archivo con el nombre ' + new_list_updated[i] + '\n Introduzca un nuevo '
                                                                                            'nombre ')
            splited = (new_list_updated[i].split('.'))
            os.rename(new_list[i], renamed_name + '.' + splited[1])

        time.sleep(0.02)


if __name__ == '__main__':

    old_name = input('Valor a Buscar: ')

    new_name = input('Reemplazarlo por: ')

    _create_list()

    _create_list_updated()

    _change_filename()

    print('**PROCESO TERMINADO**')
