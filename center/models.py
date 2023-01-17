from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,AbstractUser,PermissionsMixin,BaseUserManager
class User(AbstractUser,PermissionsMixin):
    class Role(models.TextChoices):
        director = "director","director"
        manager = "manager",'manager'
        teacher = "teacher",'teacher'
    role = models.CharField(max_length=50,choices=Role.choices,null=True,blank=True)
    class Meta:
        db_table = "Users"
class DirectorManager(BaseUserManager):
    def create_user(self , username , password = None):
        if not username or len(username) <= 0 : 
            raise  ValueError("Username field is required !")
        if not password :
            raise ValueError("Password is must !")
        
        user = self.model(
            username= username
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    def get_queryset(self,*args,**kwargs):
        result =super().get_queryset(*args,**kwargs)
        return result.filter(role=User.Role.director)
class ManagerManager(BaseUserManager):
    def create_user(self , username , password = None):
        if not username or len(username) <= 0 : 
            raise  ValueError("Username field is required !")
        if not password :
            raise ValueError("Password is must !")
        
        user = self.model(
            username= username
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    def get_queryset(self,*args,**kwargs):
        result =super().get_queryset(*args,**kwargs)
        return result.filter(role=User.Role.manager)
class TeacherManager(BaseUserManager):
    def create_user(self , username , password = None):
        if not username or len(username) <= 0 : 
            raise  ValueError("Username field is required !")
        if not password :
            raise ValueError("Password is must !")
        
        user = self.model(
            username= username
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    def get_queryset(self,*args,**kwargs):
        result =super().get_queryset(*args,**kwargs)
        return result.filter(role=User.Role.teacher)
class Director(User):
    base_role = User.Role.director
    class Meta:
        proxy=True
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role=self.base_role
            super(Director, self).save(*args, **kwargs)
    objects = DirectorManager()
    
class Manager(User):
    base_role = User.Role.manager
    class Meta:
        proxy=True
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role=self.base_role
            super(Manager, self).save(*args, **kwargs)
    objects = ManagerManager()
class Teacher(User):
    base_role = User.Role.teacher
    class Meta:
        proxy=True
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role=self.base_role
            super(Teacher, self).save(*args, **kwargs)
    objects = TeacherManager()