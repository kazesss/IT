class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f"Имя: {self.name}, идентификационный номер: {self.id}"


class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department

    def get_info(self):
        return f"Имя: {self.name}, идентификационный номер: {self.id}, "

    def manage_project(self):
        return f"Менеджер {self.name} работает над проектами в отделе: {self.department}"


class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"Техник {self.name} выполняет техническое обслуживание в области: {self.specialization}"


class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.team = []

    def add_employee(self):
        self.team.append(input("Введите имя и id сотрудника: "))

    def get_team_info(self):
        return f"Сотрудники в подчинении: {self.team}"


Employer1 = Employee("Пеунков Лев", "656d")
Manager1 = Manager("Курчиев Аскер", "8ey3", "продажи")
Technician1 = Technician("Дербоян Эрик", "938fk", "электрик")
TechManager1 = TechManager("Лохмай Варвара", "93hk7", "аналитика", "системщик")

print(Employer1.get_info())
print(Manager1.get_info(), Manager1.manage_project())
print(Technician1.get_info(), Technician1.perform_maintenance())
print(TechManager1.get_info())
TechManager1.add_employee()
print(TechManager1.get_team_info())