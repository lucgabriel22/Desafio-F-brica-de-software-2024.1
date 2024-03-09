from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from apiapp.models import GithubModel
from .serializers import GithubSerializer
from rest_framework.permissions import IsAuthenticated
from . import viewsets
import requests

class GithubViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = GithubSerializer
    queryset = GithubModel.objects.all()


    class GithubViewSet(viewsets.ModelViewSet):
        queryset = GithubModel.objects.all()
        serializer_class = GithubSerializer
        pagination_class = 2


    def create(self, request):
        login = request.data.get('login', '')
        if not login:
            return Response({'aviso': 'O campo nome do usuário é obrigatório'}, status=400)

        # criar um usuário no GitHub
        
        site = f'https://api.github.com/users/{login}'
        requisicao = requests.get(site)

        if requisicao.status_codigo != 200:
            return Response({'aviso': 'Erro ao pesquisar o usuário no GitHub'}, status=requisicao.status_codigo)
        
        json_data = requisicao.json()

        login = json_data.get('login', '')
        bio = json_data.get('bio', '')
        email = json_data.get('email', '')
        location = json_data.get('location', '')
        public_repos = json_data.get('public_repos', '')

        dados_usuario = {
            'login': login,
            'email': email,
            'location': location,
            'public_repos': public_repos,
            'bio': bio
        }

        serializer = GithubSerializer(data=dados_usuario)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = GithubSerializer(queryset, many=True)
        return Response(serializer.data)

    def recuperar(self, request, pk=None):
        login = pk
        if not login:
            return Response({'aviso': 'O campo nome do usuário é obrigatório'}, status=400)

        site = f'https://api.github.com/users/{login}'
        requisicao = requests.get(site)

        if requisicao.status_codigo != 200:
            return Response({'aviso': 'Usuário do GitHub não encontrado'}, status=requisicao.status_codigo)

        json_data = requisicao.json()
        serializer = GithubSerializer(data=json_data)

        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def up(self, request, pk=None):
        login = pk
        if not login:
            return Response({'aviso': 'O campo nome do usuário é obrigatório'}, status=400)

        site = f'https://api.github.com/users/{login}'
        requisicao = requests.put(site)

        if requisicao.status_codigo != 200:
            return Response({'aviso': 'Erro ao atualizar o usuário no GitHub'}, status=requisicao.status_codigo)

        json_data = requisicao.json()
        serializer = GithubSerializer(instance=self.get_object(), data=json_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
    def partial_update(self, request, pk=None):
        login = pk
        if not login:
            return Response({'aviso': 'O campo nome do usuário é obrigatório'}, status=400)

        site = f'https://api.github.com/users/{login}'
        requisicao = requests.patch(site)

        if requisicao.status_codigo != 200:
            return Response({'aviso': 'Erro ao atualizar parcialmente o usuário no GitHub'}, status=requisicao.status_codigo)

        json_data = requisicao.json()
        serializer = GithubSerializer(instance=self.get_object(), data=json_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        

    def destroy(self, request, pk=None):
        if not pk:
            return Response({'aviso': 'É necessário fornecer o ID do usuário'}, status=400)

        user = self.get_object()

        site = f'https://api.github.com/users/{user.login}'
        requisicao = requests.delete(site)

        if requisicao.status_codigo == 204:
            user.delete()
            return Response({'aviso': 'Usuário excluído com sucesso'}, status=204)
        else:
            return Response({'aviso': 'Erro ao excluir o usuário do GitHub'}, status=requisicao.status_codigo)
