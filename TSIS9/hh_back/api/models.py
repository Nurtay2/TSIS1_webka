from django.db import models

class Company(models.Model):
    name = models.CharField('название компании', max_length=250)
    description = models.TextField('описание компании', default = 0) 
    city = models.CharField('город', max_length = 250)
    address = models.TextField('адресс компании', default= 0)

    def __str__(self):
        return self.name
    
    def to_json(self):
        return{
            'id' : self.id,
            'name' : self.name,
            'description' : self.description,
            'city' : self.city,
            'address' : self.address
        }

    
class Vacancy(models.Model):
    name = models.CharField('название вакансии', max_length=250)
    description = models.TextField('описание вакансии', default = 0) 
    salary = models.FloatField('зарплата', default=0)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
    def to_json(self):
        return{
            'id' : self.id,
            'name' : self.name,
            'description' : self.description,
            'salary' : self.salary,
            'company' : self.company
        }

