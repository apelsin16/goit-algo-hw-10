import pulp

# Створення моделі задачі
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні для кількості вироблених одиниць Лимонаду та Фруктового соку
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

# Обмеження ресурсів
water_limit = 100
sugar_limit = 50
lemon_juice_limit = 30
fruit_puree_limit = 40

# Обмеження на використання ресурсів
model += (2 * lemonade + 1 * fruit_juice <= water_limit, "Water_Constraint")
model += (1 * lemonade <= sugar_limit, "Sugar_Constraint")
model += (1 * lemonade <= lemon_juice_limit, "Lemon_Juice_Constraint")
model += (2 * fruit_juice <= fruit_puree_limit, "Fruit_Puree_Constraint")

# Цільова функція: максимізація загальної кількості вироблених продуктів
model += lemonade + fruit_juice, "Total_Production"

# Розв'язання задачі
model.solve()

# Виведення результатів
print(f"Статус: {pulp.LpStatus[model.status]}")
print(f"Максимальна кількість виробленого Лимонаду: {lemonade.varValue}")
print(f"Максимальна кількість виробленого Фруктового соку: {fruit_juice.varValue}")
print(f"Загальна кількість вироблених продуктів: {lemonade.varValue + fruit_juice.varValue}")
