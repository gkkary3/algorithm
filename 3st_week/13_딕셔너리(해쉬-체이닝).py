class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):  # 8개의 버킷으로 초기화
            self.items.append(LinkedTuple())

    def _hash(self, key):

        return hash(key) % len(self.items)

    def put(self, key, value):
        index = self._hash(key)
        self.items[index].add(key, value)

    def get(self, key):
        index = self._hash(key)
        return self.items[index].get(key)


class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v
        return None  # 없을 경우 None 반환
