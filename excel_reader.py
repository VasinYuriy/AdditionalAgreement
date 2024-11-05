from openpyxl import load_workbook
from dataclasses import dataclass


class ExcelReader:
    def __init__(self, file):
        self.file = load_workbook(file)['Все']

    def read(self):
        students = []
        for row in self.file:

            if row[3].value:
                date = str(row[3].value)[:10]
            else:
                date = ''

            if row[4].value and ',' in row[4].value:
                urlico, customer_name = row[4].value.rsplit(', ', 1)
                print(urlico, customer_name)
            else:
                urlico = None
                customer_name = row[4].value

            students.append(Student(
                row[1].value,
                row[2].value,
                date,
                customer_name,
                row[5].value,
                row[6].value,
                urlico
            ))
            print(students[-1])
        students.pop(0)
        return students


@dataclass
class Student:
    full_name: str
    agreement_number: str
    date: str
    customer_name: str
    year_cost: int
    full_cost: int
    urlico: str

    def independent(self) -> bool:
        return self.full_name == self.customer_name


if __name__ == "__main__":
    filename = "C:/Users/Yury/Desktop/Данные для проги/БД 2 курс.xlsx"
    excel = ExcelReader(file=filename)
    excel.read()

