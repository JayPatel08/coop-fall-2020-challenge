class EventSourcer():
    # Do not change the operatorature of any functions
    def __init__(self):
        self.value = 0
        # list of tuples(<num,operation>) to keep track of undo actions
        self.undoActions = []
        # list of tuples(<num,operation>) to keep track of redo actions
        self.redoActions = []

    def add(self, num: int):
        self.value += num
        self.undoActions.append((num, '+'))

    def subtract(self, num: int):
        self.value -= num
        self.undoActions.append((num, '-'))

    def undo(self):
        if len(self.undoActions) == 0:
            return
        num, operator = self.undoActions[-1]
        del self.undoActions[-1]
        if operator == '+':
            self.value -= num
        else:
            self.value += num
        self.redoActions.append((num, operator))

    def redo(self):
        if len(self.redoActions) == 0:
            return
        num, operator = self.redoActions[-1]
        del self.redoActions[-1]
        if operator == '+':
            self.value += num
        else:
            self.value -= num

        self.undoActions.append((num, operator))

    def bulk_undo(self, steps: int):
        if steps > len(self.undoActions):
            steps = len(self.undoActions)
        for i in range(steps):
            self.undo()

    def bulk_redo(self, steps: int):
        if steps > len(self.redoActions):
            steps = len(self.redoActions)
        for i in range(steps):
            self.redo() 
