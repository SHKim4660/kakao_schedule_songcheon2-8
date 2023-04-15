import time, win32con, win32api, win32gui

# # # 카톡창 이름 (열려있는 상태, 최소화 X, 창뒤에 숨어있는 비활성화 상태 가능)
# kakao_opentalk_name = '.'

# def kakao_sendtext(text):
#     win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
#     SendReturn(hwndEdit)

# # # 엔터
# def SendReturn(hwnd):
#     win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
#     time.sleep(0.01)
#     win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

# # # 핸들
# hwndMain = win32gui.FindWindow( None, kakao_opentalk_name)
# hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RICHEDIT50W", None)
# hwndListControl = win32gui.FindWindowEx( hwndMain, None, "EVA_VH_ListControl_Dblclk", None)

# # # 채팅 전송
# text = "SETTEXT_test"
# kakao_sendtext(text)

# # 채팅방 목록 검색하는 Edit 핸들 (채팅방이 열려있지 않아도 전송 가능하기 위하여)
hwndkakao = win32gui.FindWindow(None, "카카오톡")
hwndkakao_edit1 = win32gui.FindWindowEx( hwndkakao, None, "EVA_ChildWindow", None)
hwndkakao_edit2_1 = win32gui.FindWindowEx( hwndkakao_edit1, None, "EVA_Window", None)
hwndkakao_edit2_2 = win32gui.FindWindowEx( hwndkakao_edit1, hwndkakao_edit2_1, "EVA_Window", None)
hwndkakao_edit3 = win32gui.FindWindowEx( hwndkakao_edit2_2, None, "Edit", None)

# # Edit에 검색 _ 입력되어있는 텍스트가 있어도 덮어쓰기됨
win32api.SendMessage(hwndkakao_edit3, win32con.WM_SETTEXT, 0, "송천고 2-8")
time.sleep(1)   # 안정성 위해 필요
SendReturn(hwndkakao_edit3)