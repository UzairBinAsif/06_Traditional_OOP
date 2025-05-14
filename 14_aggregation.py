''' Create a class Department and a class Employee. Use aggregation by having a Department object store a
    reference to an Employee object that exists independently of it.'''

class Employee:
    def __init__(self, name: str, salary: int, tel: int) -> None:
        self.name: str = name
        self.salary: int = salary
        self.tel: int = tel

    def fetch_details(self) -> tuple:
        return self.name, '\n', self.salary, '\n', self.tel

class Department:
    def __init__(self, dept_name: str, employee: Employee) -> None:
        self.dept_name: str = dept_name
        self.employee: Employee = employee       # Aggregation: Department is referring to an existing Employee
    
    def show_details(self) -> None:
        initial_list = list(self.employee.fetch_details())  # while plain' with the code, I added little bit of 
        final_list = [str(i) for i in initial_list]         # spice here just to show what amazing things could
        print(f'{''.join(final_list)} \n{self.dept_name} Department.')  # be done using python :)🐍

emp1 = Employee('Usman', 800, 111345786)
department1 = Department('Civil Engineering', emp1)
department1.show_details()