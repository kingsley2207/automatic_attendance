import json
import random
import time
import unicodedata
import urllib.parse
import urllib.request

import pyautogui


def lay_tu_khoa_wikipedia(so_luong=33):
    danh_sach_tu_khoa = []
    tu_khoa_da_co = set()
    so_lan_thu_toi_da = 10

    for _ in range(so_lan_thu_toi_da):
        if len(danh_sach_tu_khoa) >= so_luong:
            break

        tham_so = urllib.parse.urlencode({
            "action": "query",
            "format": "json",
            "list": "random",
            "rnnamespace": 0,
            "rnlimit": 50,
        })
        yeu_cau = urllib.request.Request(
            f"https://vi.wikipedia.org/w/api.php?{tham_so}",
            headers={"User-Agent": "AutomaticAttendance/1.0"},
        )
        with urllib.request.urlopen(yeu_cau, timeout=15) as phan_hoi:
            du_lieu = json.load(phan_hoi)

        for trang in du_lieu["query"]["random"]:
            tieu_de = trang["title"].replace("_", " ")
            tu_khoa = unicodedata.normalize("NFKD", tieu_de)
            tu_khoa = tu_khoa.encode("ascii", "ignore").decode("ascii")
            tu_khoa = " ".join(tu_khoa.split())

            if tu_khoa and tu_khoa.casefold() not in tu_khoa_da_co:
                danh_sach_tu_khoa.append(tu_khoa)
                tu_khoa_da_co.add(tu_khoa.casefold())

            if len(danh_sach_tu_khoa) == so_luong:
                break

    if len(danh_sach_tu_khoa) != so_luong:
        raise RuntimeError(
            f"Chi lay duoc {len(danh_sach_tu_khoa)}/{so_luong} tu khoa tu Wikipedia."
        )

    return danh_sach_tu_khoa


danh_sach_tu_khoa = lay_tu_khoa_wikipedia()
random.shuffle(danh_sach_tu_khoa)

print("Chương trình sẽ bắt đầu sau 3 giây. Hãy chuyển ngay về trang web Reward của bạn...")
time.sleep(3)

print("Đang thực hiện nhấn phím Tab 19 lần...")
# Nhấn phím 'tab' 19 lần, mỗi lần cách nhau 0.1 giây để trang web không bị nuốt phím
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
    
print("⚠️ Hãy mở sẵn trình duyệt, vào trang Bing và CLICK VÀO Ô TÌM KIẾM trong vòng 3 giây tới...")
time.sleep(3)

for index, tu_khoa in enumerate(danh_sach_tu_khoa, 1):
    print(f"[{index}/{len(danh_sach_tu_khoa)}] Đang gõ từ khóa: {tu_khoa}")
    
    # 1. Nhấn phím '/' để focus vào ô tìm kiếm (từ thứ 2 trở đi)
    if index > 1:
        time.sleep(0.5)
        pyautogui.press('/')
        time.sleep(0.5)
        pyautogui.press('/')
    # 2. Bôi đen từ khóa cũ và xóa
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.3)
    pyautogui.press('backspace')
    time.sleep(0.3)
    
    # 3. Gõ trực tiếp từng ký tự random thời gian nghỉ giữa mỗi chữ cái)
    pyautogui.write(tu_khoa, interval=random.uniform(0.05, 0.1))
    time.sleep(0.5)
    
    # 4. Nhấn Enter để tìm kiếm
    pyautogui.press('enter')
    
    # 5. Đợi 4 giây trước khi sang từ tiếp theo (trừ từ cuối cùng)
    if index < len(danh_sach_tu_khoa):
        time.sleep(3)

print(f"Hoàn thành gõ và tìm kiếm cả {len(danh_sach_tu_khoa)} từ khóa thành công!")
print("Đã hoàn tất thao tác!")
