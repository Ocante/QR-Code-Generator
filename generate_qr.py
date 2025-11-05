import qrcode
from PIL import Image


def gerar_qr_com_logo(
    url: str,
    logo_path: str = "CAMINHO/DO/SEU/LOGO.png",  # <-- Altere o caminho do logo aqui quando necessário
    saida: str = "qrcode_com_logo.png",
    proporcao_logo: float = 0.25
) -> None:
    """
    Gera um QR Code com um logo central (opcional).
    
    Parâmetros:
    - url (str): Conteúdo para o QR Code.
    - logo_path (str): Caminho do arquivo do logo (PNG), se desejar inserir o logo.
    - saida (str): Caminho/nome do arquivo de saída.
    - proporcao_logo (float): Tamanho relativo do logo em relação ao QR Code (0.25 = 25%).

    Observação:
    - Para incluir um logo, descomente o bloco de código indicado abaixo e ajuste o caminho do logo.
    """
    # Essa parte é para Gerar QR Code com alto nível de correção de erro
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Aqui, criu imagem base do QR Code (RGBA para suportar transparência)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

    # --- BLOCO DO LOGO NO CENTRO (opcional) ---
    # Aqui comentei, porque para inserir um logo, é necessário remover as três aspas abaixo e configure o caminho do seu logo.
    """
    # 3) Abrir imagem do logo em RGBA
    logo = Image.open(logo_path).convert("RGBA")

    # 4) Redimensionar logo mantendo proporção
    qr_w, qr_h = qr_img.size
    tamanho_alvo = int(qr_w * proporcao_logo)
    logo.thumbnail((tamanho_alvo, tamanho_alvo), Image.ANTIALIAS)

    # 5) Centralizar e colar o logo com máscara de alfa (preserva transparência)
    pos_x = (qr_w - logo.width) // 2
    pos_y = (qr_h - logo.height) // 2
    qr_img.paste(logo, (pos_x, pos_y), logo)
    """

    # Agora é só Salvar imagem final
    qr_img.save(saida)
    print(f" QR Code gerado: {saida}")


if __name__ == "__main__":
    url_usuario = input("Cole o link do site aqui: ")
    # A parte de gerar SEM LOGO:
    gerar_qr_com_logo(url_usuario)
    
    # Para gerar COM LOGO, descomente a linha abaixo e ajuste o caminho do logo:
    # gerar_qr_com_logo(url_usuario, logo_path="CAMINHO/DO/SEU/LOGO.png")
