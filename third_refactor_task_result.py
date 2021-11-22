import codecs


# Вводим абстрактный класс сотрудника, чтобы вынести туда общую логику и сделать
# абстрактными методы, которые определяются для каждой должности отдельно
class Employee:
	def __init__(self, name: str, kpi: int, experience: int, working_hours: int, plan_completion: int):
		self.name: str = name
		self.kpi: int = kpi
		self.experience: int = experience
		self.working_hours: int = working_hours
		self.plan_completion: int = plan_completion
		self.hour_rate: int = 0
		self.salary: float = 0

	def _change_hour_rate_by_plan_completion(self) -> None:
		raise NotImplementedError
	
	def _calculate_base_salary(self) -> None:
		self.salary = self.hour_rate * self.working_hours
	
	def _change_salary_by_kpi(self) -> None:
		raise NotImplementedError
	
	def _apply_experience_bonus(self) -> None:
		if self.experience > 20:
			self.salary *= 1.1
			self.salary += 1000
		elif self.experience > 15:
			self.salary *= 1.07
			self.salary += 700
		elif self.experience > 10:
			self.salary *= 1.05
			self.salary += 500
		elif self.experience > 5:
			self.salary *= 1.02
			self.salary += 200
		else:
			self.salary += 200
	
	def calculate_salary(self):
		self._change_hour_rate_by_plan_completion()
		self._calculate_base_salary()
		self._change_salary_by_kpi()
	
	def __repr__(self):
		return f'{self.name} salary {self.salary}'


class Driver(Employee):
	def __init__(self, name: str, kpi: int, experience: int, working_hours: int, plan_completion: int):
		super().__init__(name, kpi, experience, working_hours, plan_completion)
		self.hour_rate = 100
		
	def _change_hour_rate_by_plan_completion(self) -> None:
		if self.plan_completion >= 100:
			self.hour_rate *= 1.1
		elif 80 < self.plan_completion < 100:
			self.hour_rate *= 0.9
		else:
			self.hour_rate *= 0.8
	
	def _change_salary_by_kpi(self) -> None:
		if self.kpi >= 100:
			self._apply_experience_bonus()
		elif self.kpi < 90:
			self.salary *= 0.9


class Seller(Employee):
	def __init__(self, name: str, kpi: int, experience: int, working_hours: int, plan_completion: int):
		super().__init__(name, kpi, experience, working_hours, plan_completion)
		self.hour_rate = 80
		
	def _change_hour_rate_by_plan_completion(self) -> None:
		if self.plan_completion >= 100:
			self.hour_rate *= 1.5
		elif 80 < self.plan_completion < 100:
			self.hour_rate *= 0.8
		else:
			self.hour_rate *= 0.5
	
	def _change_salary_by_kpi(self) -> None:
		if self.kpi >= 100:
			self._apply_experience_bonus()
		elif self.kpi < 90:
			self.salary *= 0.8


class Accountant(Employee):
	def __init__(self, name: str, kpi: int, experience: int, working_hours: int, plan_completion: int):
		super().__init__(name, kpi, experience, working_hours, plan_completion)
		self.hour_rate = 110
		
	def _change_hour_rate_by_plan_completion(self) -> None:
		if self.plan_completion >= 100:
			self.hour_rate *= 1.3
		elif 80 < self.plan_completion < 100:
			self.hour_rate *= 0.95
		else:
			self.hour_rate *= 0.85
	
	def _change_salary_by_kpi(self) -> None:
		if self.kpi >= 100:
			self._apply_experience_bonus()
		elif self.kpi < 90:
			self.salary *= 0.9


# Создаем фабрику, которая возвращает работника по его должности и показателям
def employee_factory(
	position: str,
	name: str,
	kpi: int,
	experience: int,
	working_hours: int,
	plan_completion: int
	) -> Employee:
	if position == 'водитель':
		return Driver(
			name=name,
			kpi=kpi,
			experience=experience,
			working_hours=working_hours,
			plan_completion=plan_completion
		)
	elif position == 'продавец':
		return Seller(
			name=name,
			kpi=kpi,
			experience=experience,
			working_hours=working_hours,
			plan_completion=plan_completion
		)
	elif position == 'бухгалтер':
		return Accountant(
			name=name,
			kpi=kpi,
			experience=experience,
			working_hours=working_hours,
			plan_completion=plan_completion
		)
	else:
		raise Exception(f'Unknown position {position}')


def read_data() -> list[str]:
	with codecs.open('employees.txt', 'r', "utf_8_sig") as file:
		data = file.readlines()
	
	return data


def main():
	data = read_data()
	employees_list: list[Employee] = []
	for employee_info in data:
		name, position, working_hours, plan_completion, kpi, experience = employee_info.split(', ')
		working_hours = int(working_hours[:-1])
		plan_completion = int(plan_completion[:-1])
		experience = int(experience)
		kpi = int(kpi)
		employee: Employee = employee_factory(
			position=position,
			working_hours=working_hours,
			plan_completion=plan_completion,
			experience=experience,
			kpi=kpi,
			name=name
		)
		employee.calculate_salary()
		employees_list.append(employee)
	
	employees_list.sort(key=lambda employee_: employee_.salary, reverse=True)
	print(f'Employee with max kpi {max(employees_list, key=lambda employee_: employee_.kpi)}')
	print(f'Employee with max plan {max(employees_list, key=lambda employee_: employee_.plan_completion)}')
	employees_salary_info = '\n'.join(map(str, employees_list))
	print(f"Employees salary: \n{employees_salary_info}")
	

if __name__ == '__main__':
	main()
