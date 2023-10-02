# Создаем пустую сетку 3x3
grid = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]


# Функция для отображения сетки
def display_grid():
    for row in grid:
        print(' | '.join(row))
        print('-' * 9)


# Функция для проверки выигрышной комбинации
def check_winner(player):
    # Проверка горизонтальных линий
    for row in grid:
        if row.count(player) == 3:
            return True

    # Проверка вертикальных линий
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] == player:
            return True

    # Проверка диагоналей
    if grid[0][0] == grid[1][1] == grid[2][2] == player or grid[0][2] == grid[1][1] == grid[2][0] == player:
        return True

    return False


# Функция для осуществления хода игрока
def make_move(player):
    while True:
        row = int(input("Введите номер строки [1-3]: ")) - 1
        col = int(input("Введите номер столбца [1-3]: ")) - 1
        if row in range(3) and col in range(3) and grid[row][col] == '-':
            grid[row][col] = player
            break
        else:
            print("Неверный ход. Попробуйте еще раз.")


# Основной игровой цикл
def play_game():
    player = 'X'
    while True:
        display_grid()
        make_move(player)

        if check_winner(player):
            display_grid()
            print("Игрок", player, "победил!")
            break

        if all(grid[i][j] != '-' for i in range(3) for j in range(3)):
            display_grid()
            print("Ничья!")
            break

        # Смена игрока
        player = 'O' if player == 'X' else 'X'


# Запуск игры
play_game()
