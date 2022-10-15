from datetime import datetime as dt

def universal_logger(data, data_description = "процесс"):
    """Функция логинит любые данные

    при вызове функциив в data_description подставляется строковое описание
    процесса(например, 'ввод значения а', 'ввод зщначения в'), которыый 
    сопровождает появление переменной data 
    """  
    time = dt.now().strftime('%d-%m-%Y %H:%M:%S')
    with open('log.csv', 'a') as file:
        file.write('{};{};{}\n'
                    .format(time, data_description, data))

