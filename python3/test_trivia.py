from trivia import main, Game


class Printer:
    def __init__(self):
        self.messages = []
        self.track = False

    def print(self, message):
        if self.track:
            self.messages.append(message)

    def do_track(self):
        self.track = True


class TestTrivia:
    def test_wrong_answer(self):
        printer = Printer()
        game = Game(printer.print)
        game.add('Chet')
        game.add('Pat')
        printer.do_track()

        game.wrong_answer()
        game.wrong_answer()

        assert printer.messages == ['Question was incorrectly answered',
                                    'Chet was sent to the penalty box',
                                    'Question was incorrectly answered',
                                    'Pat was sent to the penalty box'
                                    ]
        assert game.in_penalty_box == [True, True, 0, 0, 0, 0]
        assert game.current_player == 0
