class InvalidNFEKeyLenght(BaseException):
    code = 0

    def __init__(self, lenght: int | str) -> None:
        self.msg = f'Invalid Length({lenght}) of NF-e Number.'

    def __str__(self) -> str:
        return self.msg
