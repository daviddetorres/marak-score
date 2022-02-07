
class Context():

    def __init__(self, logger):
        self.logger = logger

    def __str__(self):
        return "Context: {0}".format(self.logger)
    