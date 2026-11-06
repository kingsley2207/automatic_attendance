from random import random
import time
import pyautogui

print("Chương trình sẽ bắt đầu sau 3 giây. Hãy chuyển ngay về trang web Reward của bạn...")
time.sleep(3)

print("Đang thực hiện nhấn phím Tab 19 lần...")
# Nhấn phím 'tab' 20 lần, mỗi lần cách nhau 0.1 giây để trang web không bị nuốt phím
pyautogui.press('tab', presses=19, interval=0.1)

# Chờ một chút xíu rồi nhấn Enter để xác nhận vào ô đang chọn
time.sleep(0.5)
pyautogui.press('enter')

time.sleep(0.5)

pyautogui.hotkey('ctrl', 'tab')
time.sleep(0.5)

# 2. Nhấn Tab rồi nhấn Enter
pyautogui.press('tab')
time.sleep(0.3)
pyautogui.press('enter')
time.sleep(0.5)

# 3. Nhấn Ctrl + Tab lần nữa
pyautogui.hotkey('ctrl','shift','tab')
time.sleep(1.5)

pyautogui.press('tab')
time.sleep(0.3)
# 4. Nhấn Enter tiếp
pyautogui.press('enter')
time.sleep(1.5)

# 5. Nhấn phím "/" (thường dùng để bật ô tìm kiếm nhanh trên trang)
pyautogui.press('/')


danh_sach_tu_khoa = [
    
    "Mai VF3", "hoc bong dai hoc 179", "Tu hoc ngoai ngu", "Bi quyet song khoe",
    "Tieng anh cua nguoi viet", "Nhu mot nguoi rung", "Kinh te hoc vi mo", "Nhethuat song toi gian", "Dau tu tai chinh ca nhân",
    "Cham soc thu cung", "Kham pha dai duong", "Kien truc hien dai", "Cong thuc lam banh",
    "Nhiep anh co ban", "Yoga tai nha", "Tam ly hoc hanh vi", "Quan ly thoi gian hieu qua",
    "Xe dien thong minh", "Nang luong tai tao", "Doc sach nhanh", "Meo vat gia dinh",
    "Thien dinh giam stress", "Khoi nghiep kinh doanh", "Chien luoc marketing", "Nghe thuat giao tiep",
    "The thao mao hiem", "Phim hay cuoi tuan", "Khong gian vu tru", "Tri tue cam xuc", 
]

print("⚠️ Hãy mở sẵn trình duyệt, vào trang Bing và CLICK VÀO Ô TÌM KIẾM trong vòng 3 giây tới...")
time.sleep(3)

for index, tu_khoa in enumerate(danh_sach_tu_khoa, 1):
    print(f"[{index}/40] Đang gõ từ khóa: {tu_khoa}")
    
    # 1. Nhấn phím '/' để focus vào ô tìm kiếm (từ thứ 2 trở đi)
    if index > 1:
        pyautogui.press('/')
        time.sleep(0.3)
    
    # 2. Bôi đen từ khóa cũ và xóa
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.2)
    pyautogui.press('backspace')
    time.sleep(0.2)
    
    # 3. Gõ trực tiếp từng ký tự random thời gian nghỉ giữa mỗi chữ cái)
    pyautogui.write(tu_khoa, interval=random.uniform(0.05, 0.2))
    time.sleep(0.5)
    
    # 4. Nhấn Enter để tìm kiếm
    pyautogui.press('enter')
    
    # 5. Đợi 4 giây trước khi sang từ tiếp theo (trừ từ cuối cùng)
    if index < len(danh_sach_tu_khoa):
        time.sleep(3)

print("🎉 Hoàn thành gõ và tìm kiếm cả 40 từ khóa thành công!")

print("Đã thực hiện xong toàn bộ chuỗi phím tắt!")
print("Đã hoàn tất thao tác!")
