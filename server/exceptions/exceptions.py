class EndpointNotFountError(ValueError):
    """Исключение. Используется, когда не найден обработчик запроса для ручки."""
    def __init__(self, endpoint_name):
        self.message = "There is no endpoint with name {}!".format(endpoint_name)
        super().__init__(self.message)
