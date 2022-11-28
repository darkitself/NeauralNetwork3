from class_neural import neuralNetwork  # импортирование класса нейронной сети

from Drawer import Paint
import numpy as np  # импортируем библиотек для работы с массивами
import matplotlib.pyplot  # импортируем библиотеку для построения графиков
# количество входных, скрытых и выходных узлов
# задано 784 узла на входном слое т.к. размер картинок с цирфами 23 пикселя на 23 пикселя
input_nodes = 784
# переход от большого числа узлов к меньшему
hidden_nodes = [500]
# задано 10 узлов на выходе, чтобы в итоге получать число от 0 до 9
output_nodes = 10
# коэффициент обучения равен 0,2
learning_rate = 0.2
# создание экземпляр нейронной сети
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
# задание именни файла с тренировочными данными
file_name_train = "data_set/mnist_train.csv"
# конструкция для чтения данных из файла по линиям и закрыти файла
with open(file_name_train, 'r') as f_o:
    data_list = f_o.readlines()
# перемешевиние дата сета с числами
np.random.shuffle(data_list)
i = 0
for elem in data_list:
    # разаделение считанной строки запятыми
    all_values = elem.split(',')
    # asfarray() преобразует тип входного массива к вещественному типу float64. так же идет форматирование входных
    # данных для подачи их в нейронную сеть
    scaled_input = ((np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01)
    # создание корректных выходных данных. np.zeros создает массив 0 размером output_nodes. все занчения становятся 0.01
    targets = np.zeros(output_nodes) + 0.01
    # задание значения 0.99 у того элемента, цира которого на картинке
    targets[int(all_values[0])] = 0.99
    # подача входных и выходных данных для тренировки нейронки
    n.train(scaled_input, targets)
    i = i + 1
    print(f'Trained for {i * 100 / len(data_list)}%')
Paint(n, np)
