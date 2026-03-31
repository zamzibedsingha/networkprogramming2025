import time

class Token:
    def __init__(self, message):
        self.message = message
        self.read = False
        self.timestamp = time.time()

    def read_token(self):
        # ถ้าเคยอ่านไปแล้ว หรือหมดอายุ (เกิน 10 วินาที) ข้อมูลจะสลายตัว
        if self.read or time.time() - self.timestamp > 10:
            return None  # Cannot read again
        self.read = True
        return self.message