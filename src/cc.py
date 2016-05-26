import os

class cc(object):
    @staticmethod
    def persist(prompt):
        # Persistently ask for input from the user
        _input = raw_input(prompt)
        while not _input:
            _input = raw_input(prompt + " ")

        return _input

    @staticmethod
    def ask(prompt, default):
        # Ask for input from user with a default answer
        _input = raw_input(prompt + " (" + str(default) + "): ")

        return _input if _input else default

    @staticmethod
    def say(prompt):

        print(prompt)
