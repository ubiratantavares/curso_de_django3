from django import forms

from produto.models import Produto


class PesquisaProdutoForm(forms.Form):

    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '100'}),
                           required=False)

    # <input type="text" name="nome" id="id_nome" class="form-control form-control-sm" maxlength="100">


class ProdutoForm(forms.ModelForm):

    class Meta:

        model = Produto
        fields = ('nome', 'descricao', 'categoria', 'data_cadastro', 'preco', 'qtd_estoque', 'imagem', 'disponivel')