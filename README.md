# Gerador de QR Code com Logo

Projeto em Python para gerar QR Codes personalizados, com opção de inserir um logo (imagem PNG) centralizado.

## Requisitos

- Python 3.7 ou superior
- [qrcode](https://pypi.org/project/qrcode/)
- [Pillow](https://pypi.org/project/Pillow/)

Para instalar as dependências, execute:

```
pip install qrcode[pil]
```

## Como usar

1. Clone este repositório:

    ```
    git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
    cd NOME_DO_REPOSITORIO
    ```

2. Execute o script principal:

    ```
    python generate_qr.py
    ```

3. Insira o link desejado quando solicitado no terminal.

## Personalização do Logo

Se quiser inserir um logo central no QR Code:

- Abra o arquivo `generate_qr.py`.
- Remova as aspas do bloco de código indicado para o logo.
- Altere o parâmetro `logo_path` para o caminho da sua imagem PNG.

Exemplo de uso com logo via função:

```
from generate_qr import gerar_qr_com_logo

# Gerar QR sem logo
gerar_qr_com_logo("https://www.seusite.com")

# Gerar QR com logo (descomente e ajuste logo_path)
# gerar_qr_com_logo("https://www.seusite.com", logo_path="caminho/do/logo.png")
```

## Parâmetros Personalizáveis

- **logo_path:** Caminho para o arquivo PNG do logo.
- **saida:** Nome do arquivo QR gerado.
- **proporcao_logo:** Proporção do logo em relação à largura do QR (ex.: 0.25 para 25%).

## Autor: 
Ocante António - @2025

---

Projeto criado por [Seu Nome](https://github.com/SEU_USUARIO)
```

Substitua `SEU_USUARIO`, `NOME_DO_REPOSITORIO` e personalize o campo de créditos conforme preferir. Basta copiar e colar o texto acima no seu arquivo `README.md`.
