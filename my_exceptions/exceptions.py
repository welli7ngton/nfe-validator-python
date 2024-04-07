class InvalidNFEKeyLength(BaseException):
    code = 0

    def __init__(self, length: int | str) -> None:
        self.msg = f'Invalid Length({length}) of NF-e Number.'

    def __str__(self) -> str:
        return self.msg
