# Meu Primeiro Processador de Imagens em Python

Olá! Este é o meu primeiro projeto de processamento de imagens em Python. 
Aprendi a criar este pacote no meu curso de programação e estou muito orgulhoso do resultado!

## O que este pacote faz?

- Carrega imagens do computador
- Redimensiona imagens
- Converte para preto e branco
- Gira as imagens
- Espelha as imagens
- Recorta partes da imagem
- Salva as imagens processadas

## Como usar

1. Primeiro, instale o pacote Pillow:
```bash
pip install Pillow
```

2. Baixe este repositório ou copie os arquivos para o seu computador

3. Crie um arquivo Python (por exemplo, `meu_script.py`) e importe o processador:

```python
from image_processor.processador import ProcessadorImagens

# Cria o processador
meu_processador = ProcessadorImagens()

# Carrega uma imagem
imagem = meu_processador.carregar_imagem("foto.jpg")

# Redimensiona para 300px de largura (mantendo a proporção)
imagem_pequena = meu_processador.redimensionar(imagem, largura=300)

# Converte para preto e branco
imagem_pb = meu_processador.converter_para_preto_e_branco(imagem_pequena)

# Salva a imagem processada
meu_processador.salvar_imagem(imagem_pb, "resultado/foto_processada.jpg")
```

## Exemplo prático

Tem um arquivo chamado `exemplo_uso.py` que mostra como usar todas as funções. 
Só precisa colocar uma imagem chamada `minha_imagem.jpg` na mesma pasta e executar:

```bash
python exemplo_uso.py
```

## Estrutura do projeto

```
meu_processador_imagens/
├── image_processor/
│   ├── __init__.py
│   └── processador.py    # Aqui está o código principal
├── exemplo_uso.py        # Exemplo de como usar
├── setup.py             # Para instalar o pacote
└── README.md            # Este arquivo
```

## Coisas que aprendi fazendo este projeto

- Como criar classes em Python
- Como trabalhar com imagens usando a biblioteca Pillow
- Como criar meus próprios métodos
- Como organizar um projeto Python
- Como documentar o código

## Próximos passos

- [ ] Adicionar mais filtros
- [ ] Criar uma interface gráfica
- [ ] Fazer um programa que processa várias imagens de uma vez

---

Feito com ❤️ por um aluno iniciante em Python
