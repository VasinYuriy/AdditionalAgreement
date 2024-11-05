from docxtpl import DocxTemplate
import os
from num2txt import num2text
from datetime import datetime
import sys
import pathlib
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    os.environ["PYMORPHY2_DICT_PATH"] = str(pathlib.Path(sys._MEIPASS).joinpath('pymorphy2_dicts_ru/data'))

import pymorphy2


class FillTemplate:
    def __init__(self, students):
        self.students = students
        self.out_path = 'output'
        self.date = str(datetime.now()).replace(':', '.')
        self.unindependent_template = DocxTemplate('template_unindependent.docx')
        self.independent_template = DocxTemplate('template_independent.docx')
        self.urlico_template = DocxTemplate('template_urlico.docx')

    def fill_words(self):
        morph = pymorphy2.MorphAnalyzer()
        date_dict = {
            "01": "января",
            "02": "февраля",
            "03": "марта",
            "04": "апреля",
            "05": "мая",
            "06": "июня",
            "07": "июля",
            "08": "августа",
            "09": "сентября",
            "10": "октября",
            "11": "ноября",
            "12": "декабря",
        }

        try:
            os.mkdir(self.out_path)
        except Exception as e:
            print(e)
        try:
            os.mkdir('{}/{}'.format(self.out_path, self.date))
        except FileExistsError:
            pass

        for student in self.students:

            try:
                splitted_customer_name = student.customer_name.split(' ')
                customer_initials = splitted_customer_name[1][0] + '.' + splitted_customer_name[2][0] + '. ' + splitted_customer_name[0]
            except:
                customer_initials = student.customer_name
            try:
                splitted_full_name = student.full_name.split(' ')
                full_name_initials = splitted_full_name[1][0] + '.' + splitted_full_name[2][0] + '. ' + splitted_full_name[0]
            except:
                full_name_initials = student.full_name

            if isinstance(student.year_cost, int):
                year_cost_text = num2text(student.year_cost)
            else:
                year_cost_text = ''

            if isinstance(student.full_cost, int):
                full_cost_text = num2text(student.full_cost)
            else:
                full_cost_text = ''

            if student.date:
                date = student.date[8:10] + " " + date_dict[student.date[5:7]] + " " + student.date[0:4]
            else:
                date = ''

            context = {
                'date': date,
                'agreement_number': student.agreement_number,
                'customer_name': student.customer_name,
                'full_name': student.full_name,
                'all_cost': student.full_cost,
                'all_cost_text': full_cost_text,
                'year_cost': student.year_cost,
                'year_cost_text': year_cost_text,
                'customer_initials': customer_initials,
                'full_name_initials': full_name_initials,
                'urlico': student.urlico
            }
            print(context)

            if student.urlico:
                customer_second_name, customer_first_name, customer_third_name = student.customer_name.split(' ')
                word1 = morph.parse(customer_second_name)[0]
                gent1 = word1.inflect({'gent'})
                word2 = morph.parse(customer_first_name)[0]
                gent2 = word2.inflect({'gent'})
                word3 = morph.parse(customer_third_name)[0]
                gent3 = word3.inflect({'gent'})
                context['customer_name'] = gent1.word.title() + ' ' + gent2.word.title() + ' ' + gent3.word.title()
                self.urlico_template.render(context)
                save_path = os.path.join(self.out_path, self.date, '111{}.docx'.format(student.full_name))
                self.urlico_template.save(save_path)

            elif student.independent():
                self.independent_template.render(context)
                save_path = os.path.join(self.out_path, self.date, '222{}.docx'.format(student.full_name))
                self.independent_template.save(save_path)

            else:
                self.unindependent_template.render(context)
                save_path = os.path.join(self.out_path, self.date, '333{}.docx'.format(student.full_name))
                self.unindependent_template.save(save_path)


