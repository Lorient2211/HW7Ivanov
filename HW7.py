def cook_book():
    cook_book = {}
    with open('recipes.txt', 'r', encoding='utf8') as f:
        for line in f:
            dish = line.strip()
            cook_book[dish] = []
            ingredient_count = f.readline()
            for count in range(int(ingredient_count)):
                ing = f.readline()
                ingredient_name, quantity, measure = ing.split(' | ')
                ingredient_dict = {'ingredient_name':ingredient_name, 'quantity':quantity, 'measure':measure.strip()}
                cook_book[dish].append(ingredient_dict)
            f.readline()
    return cook_book

def get_shop_dishes_list(dishes, person_count):
    cook_book_dict = cook_book()
    cook_book_filtred = {}
    for dish_name, ingredients in cook_book_dict.items():
        if dish_name in dishes:
            for ingredient_name1 in cook_book_dict[dish_name]:
                if ingredient_name1['ingredient_name'] in cook_book_filtred.keys():
                    cook_book_filtred[ingredient_name1['ingredient_name']]['quantity'] += int(ingredient_name1['quantity'])*person_count
                else:
                    cook_book_filtred[ingredient_name1['ingredient_name']]={'measure':ingredient_name1['measure'],'quantity':int(ingredient_name1['quantity'])*person_count}
    return cook_book_filtred
print(get_shop_dishes_list(['Омлет','Утка по-пекински'],2))


def text_change():
    import os
    current_directory = os.getcwd()

    folder = 'text_content'
    file_name1 = 'text_file1.txt'
    file_name2 = 'text_file2.txt'
    full_path1 = os.path.join(current_directory, folder, file_name1)
    full_path2 = os.path.join(current_directory, folder, file_name2)

    with open(full_path1, 'r') as file1:
        content_length1 = len(file1.readlines())
    with open(full_path1, 'r') as file1:
        content1 = file1.read()

    with open(full_path2, 'r') as file2:
        content_length2 = len(file2.readlines())
    with open(full_path2, 'r') as file2:
        content2 = file2.read()

    if content_length1 > content_length2:
        with open('text_file3.txt', 'w') as file3:
            file3.write(file_name1)
            file3.write('\n')
        with open('text_file3.txt', 'a') as file3:
            file3.write(str(content_length1))
            file3.write('\n')
            file3.write(content1)
            file3.write('\n')
            file3.write(file_name2)
            file3.write('\n')
            file3.write(str(content_length2))
            file3.write('\n')
            file3.write(content2)
    else:
        with open('text_file3.txt', 'w') as file3:
            file3.write(file_name2)
            file3.write('\n')
        with open('text_file3.txt', 'a') as file3:
            file3.write(str(content_length2))
            file3.write('\n')
            file3.write(content2)
            file3.write('\n')
            file3.write(file_name1)
            file3.write('\n')
            file3.write(str(content_length1))
            file3.write('\n')
            file3.write(content1)

text_change()


