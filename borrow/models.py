from django.db import models
from datetime import timedelta, date
from users.models import Member
from books.models import Book


# Create your models here.
class BorrowRecord(models.Model):
    book= models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrow_list')
    member= models.ForeignKey(Member, on_delete=models.CASCADE, related_name= 'borrow_list')
    
    borrow_date= models.DateField(auto_now_add=True)
    return_date= models.DateField(default= lambda:date.today()+ timedelta.days(15))

    def __str__(self):
        return f"{self.member.username} borrow {self.book.title} by {self.book.author.name}"

