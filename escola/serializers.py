from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validators import cpf_invalido, nome_invalido, celular_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular'] #Definindo explicitamente quais campos devem ser serializados

    def validate(self, dados):
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf': 'O CPF deve ter um valor válido!'})
        
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome': 'O nome só pode ser letras'})
        
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({'celular': 'O celular deve ter o formato 86 99999-9999!'})
        
        return dados


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__' # Define que todos os campos devem ser serializados

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = [] # Define quais os campos vamos excluir da serialização

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    # get_periodo_display() é um método padrão do Django para campos que possuem choices
    # então obj.get_periodo_display() retorna a label correspondente ao valor armazenado no campo.
    def get_periodo(self, obj):
        #get_periodo_display() é um método padrão do Django para campos que possuem choices
        return obj.get_periodo_display()
    
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')

    class Meta:
        model = Matricula
        fields = ['estudante_nome']

class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'celular']