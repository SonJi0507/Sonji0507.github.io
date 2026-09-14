import qrcode
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer

def make_qrcode():
    url: str = "https://sonji0507.github.io/"
    # QR코드 생성
    qr = qrcode.QRCode(version=1, box_size=10, border=1, error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(url)
    qr.make(fit=True)
    # 이미지로 저장
    img = qr.make_image(fill="black", back_color="white", module_drawer=RoundedModuleDrawer())
    img.save("qrcode.png")

if __name__ == "__main__":
    make_qrcode()
