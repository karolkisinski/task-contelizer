from datetime import date
from .exceptions import InvalidPesel


class Pesel():

    @classmethod
    def validate(cls, pesel):
        weights = [9, 7, 3, 1, 9, 7, 3, 1, 9, 7]
        try:
            checksum = sum(int(pesel[i]) * weights[i] for i in range(10)) % 10
            if checksum != int(pesel[10]):
                return False
            return True
        except ValueError:
            return False

    @classmethod
    def get_birth_date(cls, pesel):
        year = int(pesel[0:2])
        month = int(pesel[2:4])
        day = int(pesel[4:6])
        year += {
            0: 1900,
            1: 2000,
            2: 2100,
            3: 2200,
            4: 1800,
        }[month // 20]
        month = month % 20
        try:
            return date(year, month, day)
        except ValueError:
            raise InvalidPesel("Pesel jest niepoprawny")

    @classmethod
    def get_gender(cls, pesel):
        gender = 'Meżczyzna' if int(pesel[9]) % 2 == 1 else 'Kobieta'
        return gender
