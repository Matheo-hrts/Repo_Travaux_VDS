import csv
import os

""" Ce code a été écrit avec l'aide de ChatGPT """


def write_csv(file, name, quantity, price, category):

    try:
        with open(f'CSV/{file}', 'a', encoding='utf-8') as CSV_file:
            CSV_file.write(f'{name},{quantity},{price},{category}\n')

    except IOError:
        print('ErreurIO')


def print_csv(path):

    with open(path, 'r') as CSV_file:
        reader = csv.reader(CSV_file)
        i = 0

        for line in reader:
            i += 1

            if i != 1:
                print(f'line {i} : name = {line[0]}, quantity = {line[1]},' +
                      'price = {line[2]}, category = {line[3]}.')


def merge_csv(directory, file_output):

    # Vérifie si le dossier existe
    if not os.path.exists(directory):
        raise FileNotFoundError('Le dossier n\'exitste pas')

    # Liste pour stocker les fichiers CSV
    file_csv = [f for f in os.listdir(directory) if f.endswith('.csv')]

    # Vérifie s'il y a des fichiers CSV à fusionner
    if not file_csv:
        raise FileNotFoundError('Aucun CSV dans le dossier')

    else:
        with open(file_output, 'w', newline='', encoding='utf-8') as output:
            output.write('name,quantity,price,category\n')
            for file in file_csv:
                file_path = os.path.join(directory, file)
                with open(file_path, 'r', encoding='utf-8') as entree:
                    reader = csv.reader(entree)
                    writer = csv.writer(output)
                    writer.writerow(next(reader))

                    # Écrire les lignes du fichier courant
                    for line in reader:
                        writer.writerow(line)

        print(f"Fusion terminée. Fichier créé : {file_output}")


def write_option():

    write_input = input('what do you want to write ? : ')

    if write_input == 'exit':
        exit()

    list_input = write_input.split(',')
    if len(list_input) < 5:
        print('Please enter enough argument (5)\n')
        write_option()

    else:
        write_csv(list_input[0], list_input[1],
                  list_input[2], list_input[3], list_input[4])


def what_to_do():

    first_input = input('read [r] write [w] merge [m] sort [s] quit [exit]' +
                        '\nWhat do you want to do ? : ')

    if first_input == 'w':
        write_option()

    elif first_input == 'm':
        merge_csv('CSV', 'merged_csv/merge.csv')

    elif first_input == 'r':
        read = input('Which file do you want to read ? : ')

        try:
            print_csv(read)

        except FileNotFoundError:
            what_to_do()

    elif first_input == 's':
        sort_csv('merged_csv/merge.csv')

    elif first_input == 'exit':
        exit()

    else:
        print("Plase enter a valid option")
        what_to_do()


def sort_csv(file_input):

    sort_column = input('name quantity price category\n' +
                        'On what do you want to sort ? : ')

    if sort_column == 'exit':
        exit()

    elif (sort_column != 'name' and sort_column != 'quantity' and
            sort_column != 'price' and sort_column != 'category'):
        print('Please enter an existinge column : ' +
              'name quantity price category\n')
        sort_csv('merged_csv/merge.csv')

    else:
        with open(file_input, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)  # Lecture en tant que dictionnaire
            lignes = list(reader)  # Charger toutes les lignes
            # Trier les lignes en fonction de la colonne
            if sort_column == 'price' or sort_column == 'quantity':
                sorted_lines = sorted(lignes, key=lambda x:
                                      float(x[sort_column]))
            else:
                sorted_lines = sorted(lignes, key=lambda x: x[sort_column])
            for i in sorted_lines:
                print(f'name = {i['name']}, quantity = {i['quantity']},' +
                      f' price = {i['price']}, category = {i['category']}.')

            save = input('Do you want to save that sorted list ? : ')
            if (save == '' or save == 'y' or save == 'Y' or
                    save == 'yes' or save == 'Yes' or save == 'YES'):

                file_output = input('What will be the name of the file ? : ')
                directory = 'sorted_csv'
                with open(f'{directory}/{file_output}.csv', 'w', newline='',
                          encoding='utf-8') as file:
                    writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
                    writer.writeheader()  # Écrire l'en-tête
                    writer.writerows(sorted_lines)  # Écrire les lignes triées


if __name__ == '__main__':

    what_to_do()
