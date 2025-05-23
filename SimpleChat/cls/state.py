import datetime


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Данная реализация не учитывает возможное изменение передаваемых
        аргументов в `__init__`.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class State(metaclass=SingletonMeta):
    times = []

    def add_to_times(self):
        self.times.append(datetime.datetime.now())

    def get_times(self):
        return [datetime.datetime.strftime(the_time, "%d-%b-%Y-%H:%M:%S") for the_time in self.times]