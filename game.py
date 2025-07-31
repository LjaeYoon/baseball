class Game:
    def guess(self, guess_number):
        self.assert_illegal_value(guess_number)

    def assert_illegal_value(self, guess_number):
        if guess_number is None:
            raise TypeError("입력이 None 임")

        if len(guess_number) != 3:
            raise TypeError("입력 문자열 길이가 3 이 아님")

        if not self.is_duplicated_number(guess_number):
            raise TypeError("숫자만 넣어야함")

        if self.is_duplicated_number(guess_number):
            raise TypeError("중복된 숫자 들어옴")

    def is_duplicated_number(self, guess_number):
        return guess_number[0] == guess_number[1] or \
            guess_number[0] == guess_number[2] or \
            guess_number[2] == guess_number[1]
