from datetime import datetime
import time, win32con, win32api, win32gui
import schedule

now = datetime.now()

DOW = now.weekday() #Date Of Week 현재 요일
year = now.year
month = now.month
day = now.day
hour = now.hour
min = now.minute

# # 카톡창 이름 (열려있는 상태, 최소화 X, 창뒤에 숨어있는 비활성화 상태 가능)
kakao_opentalk_name = "송천고 2-8"

def kakao_sendtext(text):
    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    SendReturn(hwndEdit)

# # 엔터
def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

# # 핸들
hwndMain = win32gui.FindWindow( None, kakao_opentalk_name)
hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RICHEDIT50W", None)
hwndListControl = win32gui.FindWindowEx( hwndMain, None, "EVA_VH_ListControl_Dblclk", None)

def sendtext():
    if DOW == 0:
        text = (f"{year}년 {month}월 {day}일 월요일\n\n화요일 시간표\n-------------\n-문학b\n-진로\n-기하/실수\n-선택F\n-영어\n-선택E\n-선택B\n-------------\n\n준비물\n-영어 : 학습지 다 써오기\n-문학b : 노트 준비하기")
        kakao_sendtext(text)
    elif DOW == 1:
        text = (f"{year}년 {month}월 {day}일 화요일\n\n수요일 시간표\n-------------\n-선택E\n-선택C\n-수학\n-빅데이터\n-음악b\n-체육\n-------------\n\n준비물\n-수학 : 학습지 해오기\n-체육 체육복,츄리닝 준비 ")
        kakao_sendtext(text)
    elif DOW == 2:
        text = (f"{year}년 {month}월 {day}일 수요일\n\n목요일 시간표\n-------------\n-빅데이터\n-선택A\n-수학\n-문학a\n-영어\n-음악a\n-선택D\n-------------\n\n준비물\n-수학 : 학습지 해오기\n-영어 : 학습지 다 써오기")
        kakao_sendtext(text)
    elif DOW == 3:
        text = (f"{year}년 {month}월 {day}일 목요일\n\n금요일 시간표\n-------------\n-영어\n-문학a\n-선택C\n-선택B\n-창체\n-창체\n-창체\n-------------\n\n준비물\n-영어 : 학습지 다 써오기")
        kakao_sendtext(text)
    elif DOW == 4:
        text = (f"{year}년 {month}월 {day}일 금요일\n\n월요일 시간표\n-------------\n-체육\n-문학b\n-수학\n-영어\n-선택A\n-선택D\n-선택F\n-------------\n\n준비물\n-체육 : 체육시간에 입을 츄리닝or체육복 가져오기\n-수학 : 학습지 예제 해오기\n-영어 : 학습지 다 써오기\n-문학b : 노트 준비하기")
        kakao_sendtext(text)
    else : pass

# # 매일 특정 HH:MM 및 다음 HH:MM:SS에 작업 실행
# schedule.every().day.at("18:00").do(sendtext)
sendtext()

# while True:
#     schedule.run_pending()
#     time.sleep(1)