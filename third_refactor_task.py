import codecs


def read_data() -> list[str]:
	with codecs.open('employees.txt', 'r', "utf_8_sig") as file:
		data = file.readlines()
	
	return data


def main():
	data: list[str] = read_data()
	employees_salary_by_name: list[tuple[str, int]] = []
	employees_with_kpi: list[tuple[str, int]] = []
	employees_with_plan_completion: list[tuple[str, int]] = []
	for employee_info in data:
		name, position, working_hours, plan_completion, kpi, experience = employee_info.split(', ')
		working_hours = int(working_hours[:-1])
		plan_completion = int(plan_completion[:-1])
		experience = int(experience)
		kpi = int(kpi)
		if position == 'водитель':
			hour_rate = 100
		elif position == 'продавец':
			hour_rate = 80
		elif position == 'бухгалтер':
			hour_rate = 110
		else:
			raise Exception(f'Unknown position {position}')

		if position == 'водитель' and plan_completion >= 100:
			hour_rate *= 1.1
		elif position == 'продавец' and plan_completion >= 100:
			hour_rate *= 1.5
		elif position == 'бухгалтер' and plan_completion >= 100:
			hour_rate *= 1.3
			
		if position == 'водитель' and 80 <= plan_completion < 100:
			hour_rate *= 0.9
		elif position == 'продавец' and 90 <= plan_completion < 100:
			hour_rate *= 0.8
		elif position == 'бухгалтер' and 90 <= plan_completion < 100:
			hour_rate *= 0.95
		
		if position == 'водитель' and plan_completion < 80:
			hour_rate *= 0.8
		elif position == 'продавец' and plan_completion < 90:
			hour_rate *= 0.5
		elif position == 'бухгалтер' and plan_completion < 90:
			hour_rate *= 0.85

		salary = working_hours * hour_rate
		
		if position == 'водитель' and kpi >= 100:
			if experience > 20:
				salary *= 1.1
				salary += 1000
			elif experience > 15:
				salary *= 1.07
				salary += 700
			elif experience > 10:
				salary *= 1.05
				salary += 500
			elif experience > 5:
				salary *= 1.02
				salary += 200
			else:
				salary += 200
				
		elif position == 'продавец' and kpi >= 105:
			if experience > 20:
				salary *= 1.1
				salary += 1000
			elif experience > 15:
				salary *= 1.07
				salary += 700
			elif experience > 10:
				salary *= 1.05
				salary += 500
			elif experience > 5:
				salary *= 1.02
				salary += 200
			else:
				salary += 200
				
		elif position == 'бухгалтер' and kpi >= 100:
			if experience > 20:
				salary *= 1.1
				salary += 1000
			elif experience > 15:
				salary *= 1.07
				salary += 700
			elif experience > 10:
				salary *= 1.05
				salary += 500
			elif experience > 5:
				salary *= 1.02
				salary += 200
			else:
				salary += 200
				
		if position == 'водитель' and kpi < 90:
			salary *= 0.9
		elif position == 'продавец' and kpi < 85:
			salary *= 0.8
		elif position == 'бухгалтер' and kpi < 80:
			salary *= 0.9
		
		employees_salary_by_name.append((name, salary))
		employees_with_kpi.append((name, kpi))
		employees_with_plan_completion.append((name, plan_completion))
	
	employees_salary_by_name.sort(key=lambda employee: employee[1], reverse=True)
	employee_with_max_kpi = max(employees_with_kpi, key=lambda employee: employee[1])
	employees_with_max_plan_completion = max(employees_with_plan_completion, key=lambda employee: employee[1])
	print(f'Employee with max kpi {employee_with_max_kpi[0]}')
	print(f'Employee with max plan completion {employees_with_max_plan_completion[0]}')
	employees_salary = ''
	for employee_name, salary in employees_salary_by_name:
		employees_salary += f'{employee_name} salary {salary} \n'
	print(f'Employees salary: \n{employees_salary}')
		

if __name__ == '__main__':
	main()
