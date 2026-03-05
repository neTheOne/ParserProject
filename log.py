import logging

def log_init():
    '''
    функция объявления обработчика логов
    :param name:
    :return: обработчик логов
    '''
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] => %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    logger = logging.getLogger()
    py_handler = logging.FileHandler("logs\logs.log", mode='w')
    logger.addHandler(py_handler)

    return logger

