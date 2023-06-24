from pytz import timezone
from datetime import datetime
import time, win32con, win32api, win32gui
import schedule

now = datetime.now(timezone('Asia/Seoul'))

day_of_week = now.weekday() #Date Of Week 현재 요일
year = now.year
month = now.month
day = now.day
hour = now.hour
min = now.minute

# # 카톡창 이름, (활성화 상태의 열려있는 창)
chatroom_name = '송천고 2-8'


# # 채팅방에 메시지 전송
def kakao_sendtext(chatroom_name, text):
    time.sleep(1)
    # # 핸들 _ 채팅방
    hwndMain = win32gui.FindWindow( None, chatroom_name)
    hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RICHEDIT50W", None)
    # hwndListControl = win32gui.FindWindowEx( hwndMain, None, "EVA_VH_ListControl_Dblclk", None)

    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    SendReturn(hwndEdit)


# # 엔터
def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(1)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


# # 채팅방 열기
def open_chatroom(chatroom_name):
    # # 채팅방 목록 검색하는 Edit (채팅방이 열려있지 않아도 전송 가능하기 위하여)
    hwndkakao = win32gui.FindWindow(None, "카카오톡")
    hwndkakao_edit1 = win32gui.FindWindowEx( hwndkakao, None, "EVA_ChildWindow", None)
    hwndkakao_edit2_1 = win32gui.FindWindowEx( hwndkakao_edit1, None, "EVA_Window", None)
    hwndkakao_edit2_2 = win32gui.FindWindowEx( hwndkakao_edit1, hwndkakao_edit2_1, "EVA_Window", None)
    hwndkakao_edit3 = win32gui.FindWindowEx( hwndkakao_edit2_2, None, "Edit", None)

    # # Edit에 검색 _ 입력되어있는 텍스트가 있어도 덮어쓰기됨
    win32api.SendMessage(hwndkakao_edit3, win32con.WM_SETTEXT, 0, chatroom_name)
    time.sleep(1)   # 안정성 위해 필요
    SendReturn(hwndkakao_edit3)
    time.sleep(1)

def sendtext(day_of_week,chatroom_name,year,month,day):
    if day_of_week == 0:
        text = (f"{year}년 {month}월 {day}일 월요일\n\n화요일 시간표\n-------------\n-문학b\n-진로\n-기하/실수\n-선택F\n-영어\n-선택E\n-선택B\n-------------\n\n준비물\n-영어 : 학습지 다 써오기\n-문학b : 노트 준비하기")
        kakao_sendtext(chatroom_name,text)
    elif day_of_week == 1:
        text = (f"{year}년 {month}월 {day}일 화요일\n\n수요일 시간표\n-------------\n-선택E\n-선택C\n-수학\n-빅데이터\n-음악b\n-체육\n-------------\n\n준비물\n-수학 : 학습지 해오기\n-체육 체육복,츄리닝 준비 ")
        kakao_sendtext(chatroom_name,text)
    elif day_of_week == 2:
        text = (f"{year}년 {month}월 {day}일 수요일\n\n목요일 시간표\n-------------\n-빅데이터\n-선택A\n-수학\n-문학a\n-영어\n-음악a\n-선택D\n-------------\n\n준비물\n-수학 : 학습지 해오기\n-영어 : 학습지 다 써오기")
        kakao_sendtext(chatroom_name,text)
    elif day_of_week == 3:
        text = (f"{year}년 {month}월 {day}일 목요일\n\n금요일 시간표\n-------------\n-영어\n-문학a\n-선택C\n-선택B\n-창체\n-창체\n-창체\n-------------\n\n준비물\n-영어 : 학습지 다 써오기")
        kakao_sendtext(chatroom_name,text)
    elif day_of_week == 4:
        text = (f"{year}년 {month}월 {day}일 금요일\n\n월요일 시간표\n-------------\n-체육\n-문학b\n-수학\n-영어\n-선택A\n-선택D\n-선택F\n-------------\n\n준비물\n-체육 : 체육시간에 입을 츄리닝or체육복 가져오기\n-수학 : 학습지 예제 해오기\n-영어 : 학습지 다 써오기\n-문학b : 노트 준비하기")
        kakao_sendtext(chatroom_name,text)
    else : pass

# sendtext()

def main():
    now = datetime.now()
    day_of_week = now.weekday()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    min = now.minute
    open_chatroom(chatroom_name)  # 채팅방 열기
    time.sleep(5)
    sendtext(day_of_week,chatroom_name,year,month,day)    # 메시지 전송

schedule.every().day.at("14:49").do(main)

while True:
    schedule.run_pending()
    time.sleep(1)