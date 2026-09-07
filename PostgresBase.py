class PostgresBase:
    """
    Класс для сохранения данных сервиса
    """

    def __init__(self, dbname, user, password, host="127.0.0.1", port="5432"):
        """
        Конструктор класса PostgresBase

        Args:
            dbname: Название базы данных
            user: Наименование пользователя обращающегося к БД
            password: Пароль от БД
            host: Адрес БД
            port: Порт БД
        """
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    