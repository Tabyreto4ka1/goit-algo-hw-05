from collections import Counter
import sys

def load_logs(file_path: str) -> list:         
    log_list=[]
    with open(file_path,"r", encoding="utf-8") as file: 
        while True:            #  Читаємо кожен рядок і якщо рядка немає - функція зупиняється 
            line = file.readline()     
            if not line:
                break
            log_list.append(parse_log_line(line))    # кожен рядок обробляємо і додаємо в список

    
    logs=log_list
  
    
    return logs

def parse_log_line(line: str) -> dict: 
    values=line.split(maxsplit=3)      #  Обробка рядків. Беремо рядок та робимо словник 
    return {"date":values[0], "time":values[1], "levels":values[2],"message":values[3].strip()}

   
def filter_logs_by_level(log_list: list, level_chosen: str) -> list:
    filtered_logs =  list(filter(lambda log_list :level_chosen.upper() ==log_list["levels"], log_list)) #фільтруємо за допомогою лямбда -функції. Якщо у списку-словнику рівень == обраному користувачем - вносимо у список. 
    print(f"Деталі логів для рівня {level_chosen} :")
    for logs_dict in filtered_logs:
        print(logs_dict["date"], logs_dict["time"], logs_dict["message"])

def count_logs_by_level(log_list: list) -> dict:
    counted_levels=Counter(item["levels"]  for item in log_list)     #Рахуємо кількість рівнів кожного логування
    return counted_levels


def display_log_counts(counted_levels: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counted_levels.items():     #Виводимо з словника рівень та кількість 
        print(level, count)
    

try:
    file_path=sys.argv[1]
    if len(sys.argv)>2:
        level_chosen=sys.argv[2]
    logs = load_logs(file_path)
    counted_levels = count_logs_by_level(logs)
    display_log_counts(counted_levels)
    try:                                                                #Якщо користувач ввів рівень логування - перевіряємо чи такий існує, якщо так - відправляємо фільтрувати
            if level_chosen.upper() in ["INFO","DEBUG","ERROR","WARNING"]:
                filter_logs_by_level(logs, level_chosen)
            else: 
                print("Невідомий рівень логування")
    except NameError:     #Якщо рівень не був введений - функція буде працювати без нього
        pass

except (ValueError, IndexError):
    print("Користувач нічого не ввів")
except FileNotFoundError:
    print("Файл не знайдено")


