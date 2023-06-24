from pytz import timezone
from datetime import datetime
today = datetime.now(timezone('Asia/Seoul'))
print(today)