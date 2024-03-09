from django.db import models

class GithubModel(models.Model):
    login = models.CharField(verbose_name='Nome do usuário', max_length=25, blank = False, null = False)
    bio = models.CharField(verbose_name='Bio do usuário', max_length=1000, blank = True, null = True)
    email = models.CharField(verbose_name='email do Usuário', max_length=25, blank = True, null = True)
    location = models.CharField(verbose_name='localização do Usuário', max_length=25, blank = True, null = True)
    public_repos = models.CharField(verbose_name='Repositórios Publicos', max_length=25, blank = True, null = True)


    def __str__(self) -> str:
        return f'Github do Usuário:{self.login}'
    






