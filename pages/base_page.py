class basePage():
    def __init__(self, name):
        self.name = name
    def data(self):
        print(f'calling basePage.data() from {self.name}')
