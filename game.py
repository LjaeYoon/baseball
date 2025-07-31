from game_result import GameResult


class Game:

    def __init__(self):
        self._question = ""
        self.__ans = [0] * 10

    @property
    def question(self):
        raise AttributeError("읽을 수 없는 송성")

    @question.setter
    def question(self, question):
        self._question = question
        self.update_map(self.__ans, question)

    def guess(self, guess_number):
        self.assert_illegal_value(guess_number)

        guess_list = [0] * 10
        strike = 0
        ball = 0

        self.update_map(guess_list, guess_number)

        ball, strike = self.calculate_result(ball, guess_list, strike)

        solve = True if strike == 3 else False

        return GameResult(solve, strike, ball)

    def update_map(self, guess_list, guess_number):
        for idx in range(len(guess_number)):
            guess_list[int(guess_number[idx])] = int(idx) + 1

    def calculate_result(self, ball, guess_list, strike):
        for i in range(10):
            if self.__ans[i] == 0 or guess_list[i] == 0:
                continue

            if self.__ans[i] == guess_list[i]:
                strike += 1
            else:
                ball += 1
        return ball, strike

    def assert_illegal_value(self, guess_number):
        if guess_number is None:
            raise TypeError("입력이 None 임")

        if len(guess_number) != 3:
            raise TypeError("입력 문자열 길이가 3 이 아님")

        if not guess_number.isdigit():
            raise TypeError("숫자만 넣어야함")

        if self.is_duplicated_number(guess_number):
            raise TypeError("중복된 숫자 들어옴")

    def is_duplicated_number(self, guess_number):
        return guess_number[0] == guess_number[1] or \
            guess_number[0] == guess_number[2] or \
            guess_number[2] == guess_number[1]

