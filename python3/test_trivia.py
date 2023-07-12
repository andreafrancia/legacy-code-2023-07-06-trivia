from trivia import main, Game


class TestTrivia:
    def test_wrong_answer(self):
        messages = []

        def my_print(message):
            messages.append(message)

        game = Game(my_print)
        game.add('Chet')
        game.wrong_answer()

        assert messages == ['Chet was added',
                            'They are player number 1',
                            'Question was incorrectly answered',
                            'Chet was sent to the penalty box']
