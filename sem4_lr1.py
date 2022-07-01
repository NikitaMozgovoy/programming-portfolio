"""
    TODO:   
    - реализовать параметризацию формулы для вычисления левого и правого ветвей дерева
    - реализовать параметризованный вариант решения с значениями корня и длины по своему варианту
    - переписать (рефакторить) тесты на UnitTest
    - предложить реализацию алгоритма построения дерева без использования рекурсии
    
    Позднее на ЛР: 
    - вернуть значение дерева в виде json-объекта
    - 
"""


def gen_bin_tree(height, root):

    tree = {str(root): []}  # {"5": []} рекурсия: {"8": []} {"10": []}

    # 1. рекурсивное решение
    if height == 1:
        return tree

    left_leaf = root + 3  # 8
    right_leaf = root * 2  # 10

    height -= 1  # 1
    tree.get(str(root)).append(gen_bin_tree(height, left_leaf))
    tree.get(str(root)).append(gen_bin_tree(height, right_leaf))
    print(tree)
    return tree


def main():
    # Функция main должна позволять вводить данные и
    #
    # вызывать искомую функцию (gen_bin_tree) и
    # возврщать ответ с помощью print

    h = int(input("height = "))
    r = int(input("root = "))

    result = gen_bin_tree(height=h, root=r)

    print(result)

    return result


# gen_bin_tree(2, 5)
print(gen_bin_tree(2, 5).get("5")[0].get("8"))

if __name__ == '__main__':
    # height = 1
    example1 = {"5": [{"8": []}, {"10": []}]}
    height = 2
    example2 = {
        "5": [{
            "8": [{
                "11": []
            }, {
                "16": []
            }]
        }, {
            "10": [{
                "13": []
            }, {
                "20": []
            }]
        }]
    }

    assert type(gen_bin_tree(
        1, 5).get("5")) is list, " Примитивный тест для height=1, root=5"
    assert type(gen_bin_tree(1, 5)) is dict, "Вернули ли мы словарь?"
    assert type(gen_bin_tree(2, 5).get("5")[0].get(
        "8")) is list, "Тест для левого поддерева, должен быть  лист"
    assert len(gen_bin_tree(2, 5).get("5")[0].get(
        "8")) == 0, "Тест для длины левого поддерева, должен быть пустой list"
