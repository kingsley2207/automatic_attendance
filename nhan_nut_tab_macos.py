import sys
import time
import random
import pyautogui

# ---------------------------------------------------------------
# Cấu hình cho macOS
# - Phím chọn tất cả / copy / ... trên Mac dùng 'command' thay cho 'ctrl'
# - Chuyển tab trình duyệt (Chrome/Edge/Firefox) vẫn dùng 'ctrl' + 'tab'
# - Cần cấp quyền: System Settings -> Privacy & Security -> Accessibility
#   (bật cho Terminal / VS Code / PyCharm... tuỳ nơi bạn chạy script)
# ---------------------------------------------------------------
if sys.platform != "darwin":
    print("Lưu ý: script này được viết cho macOS, nhưng vẫn sẽ thử chạy.")

MOD = "command" if sys.platform == "darwin" else "ctrl"

# Kéo chuột vào góc trên cùng bên trái màn hình để dừng khẩn cấp
pyautogui.FAILSAFE = True

danh_sach_tu_khoa = [
    "Lich su cac nen van minh co dai", "Cach trong rau sach tai nha", "Thiet ke noi that nho gon", "Am nhac jazz thu gian",
    "Meo chup anh bang dien thoai", "Du lich vung cao Viet Nam", "Cac loai ca nuoc ngot", "Mon chay de lam",
    "Bao ve moi truong bien", "Hoc lap trinh Python co ban", "Thoi trang ben vung", "Cach cham soc cay sen da",
    "Van hoa ca phe Viet Nam", "Bi an kim tu thap Ai Cap", "Khoa hoc ve giac ngu", "Lam vuon tren ban cong",
    "Phuong phap ghi nho hieu qua", "Cac hanh tinh trong he mat troi", "Loi ich cua viec di bo", "Lich su dien anh",
    "Mon an dac san mien Tay", "Kinh nghiem nuoi meo trong nha", "Nghe thuat lam gom", "Cong nghe pin mat troi",
    "Cach lap ke hoach du lich", "Truyen thuyet Son Tinh Thuy Tinh", "Kham pha rung nhiet doi", "Thoi quen song xanh",
]

# ---------------------------------------------------------------
# PHẦN 1: Chuỗi thao tác phím tắt trên trang web
# ---------------------------------------------------------------
print("Chương trình sẽ bắt đầu sau 3 giây. Hãy chuyển ngay về trang web của bạn...")
time.sleep(3)

print("Đang nhấn phím Tab 19 lần...")
# Mỗi lần cách nhau 0.1 giây để trang web không bị nuốt phím
pyautogui.press("tab", presses=19, interval=0.1)

time.sleep(0.5)
pyautogui.press("enter")
time.sleep(0.5)

# Chuyển sang tab kế tiếp (trên Mac vẫn dùng Control, không phải Command)
pyautogui.hotkey("ctrl", "tab")
time.sleep(0.5)

# Nhấn Tab rồi Enter
pyautogui.press("tab")
time.sleep(0.3)
pyautogui.press("enter")
time.sleep(0.5)

# Quay lại tab trước
pyautogui.hotkey("ctrl", "shift", "tab")
time.sleep(1.5)

pyautogui.press("tab")
time.sleep(0.3)
pyautogui.press("enter")
time.sleep(1.5)

# Nhấn "/" để bật ô tìm kiếm nhanh trên trang
pyautogui.press("/")

# ---------------------------------------------------------------
# PHẦN 2: Gõ và tìm kiếm lần lượt các từ khóa
# ---------------------------------------------------------------
print("⚠️ Hãy mở sẵn trình duyệt, vào trang Bing và CLICK VÀO Ô TÌM KIẾM trong vòng 3 giây tới...")
time.sleep(3)

tong = len(danh_sach_tu_khoa)

for index, tu_khoa in enumerate(danh_sach_tu_khoa, 1):
    print(f"[{index}/{tong}] Đang gõ từ khóa: {tu_khoa}")

    # 1. Từ thứ 2 trở đi: nhấn '/' để focus vào ô tìm kiếm
    if index > 1:
        pyautogui.press("/")
        time.sleep(0.3)

    # 2. Chọn hết nội dung cũ (Command + A trên Mac) rồi xóa
    pyautogui.hotkey(MOD, "a")
    time.sleep(0.2)
    pyautogui.press("backspace")
    time.sleep(0.2)

    # 3. Gõ từng ký tự (nên tắt bộ gõ tiếng Việt, chuyển về ABC/US)
    pyautogui.write(tu_khoa, interval=random.uniform(0.05, 0.2))
    time.sleep(0.5)

    # 4. Nhấn Enter để tìm kiếm
    pyautogui.press("enter")

    # 5. Đợi 3 giây trước khi sang từ tiếp theo (trừ từ cuối)
    if index < tong:
        time.sleep(3)

print(f"🎉 Hoàn thành gõ và tìm kiếm cả {tong} từ khóa!")
