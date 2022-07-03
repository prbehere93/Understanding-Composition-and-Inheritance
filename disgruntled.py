class DisgruntledEmployee:
    """This class does not inherit from Employee class however
    it  it exposes the same interface required by the PayrollSystem.
    So, it can be used by the PayrollSystem (duck-typing)
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def calculate_payroll(self):
        return 1000000