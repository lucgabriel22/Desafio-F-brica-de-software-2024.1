from django.db import models

class GithubModel(models.Model):
    login = models.CharField(verbose_name='Nome do usuário', max_length=25, blank = False, null = False)
    name = models.CharField(verbose_name='Nome', max_length=25, blank = True, null = True)
    bio = models.CharField(verbose_name='Bio do usuário', max_length=1000, blank = True, null = True)
    email = models.CharField(verbose_name='email do Usuário', max_length=25, blank = True, null = True)
    location = models.CharField(verbose_name='localização do Usuário', max_length=25, blank = True, null = True)
    public_repos = models.CharField(verbose_name='Repositórios Publicos', max_length=25, blank = True, null = True)
    followers = models.CharField(verbose_name='Seguidores', max_length=25, blank = True, null = True)
    following = models.CharField(verbose_name='Seguindo', max_length=25, blank = True, null = True)
    created_at = models.CharField(verbose_name='Data de criação', max_length=25, blank = True, null = True)
    updated_at = models.CharField(verbose_name='Data da ultíma atualização', max_length=25, blank = True, null = True)


    def __str__(self) -> str:
        return f'Github do Usuário:{self.login}'
    






