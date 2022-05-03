import hashlib
import json
from time import time


class Blockchain(object):
    def __init__(self, leading_zeros_amount=5):
        self.leading_zeros_amount = leading_zeros_amount
        self.chain = []
        self.pending_transactions = []
        # добавляем первый блок для инициализации цепи
        init_block = self.new_block(
            previous_hash=
            "00000fee7780abb1aac28be835275675038b476eb592f8ec15caa6b3d65255b7",
            proof=0)
        self.add_block(init_block)


    def new_block(self, proof=0, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'transactions': self.pending_transactions,  # записываем транзакции которые этот блок подтверждает
            'proof': proof,  # записываем доказательство работы, которое считают майнеры
            'previous_hash': previous_hash or self.hash(self.chain[-1])  # записываем хэш предыдущего блока, чтобы соблюдать последовательность в цепи
        }
        return block

    def add_block(self, block):
        if self.block_proves_work(block):  # если проделанная работа доказана,
            # добавляем блок с доказательством в цепь
            self.pending_transactions = []  # ожидающие транзакции подтверждены, очищаем список
            self.chain.append(block)  # добавляем блок в цепь
            return True  # значит всё успешно
        return False  # доказательство работы поддельное - не записываем блок в цепь и говорим об отказе
          
    def block_proves_work(self, block):
        return self.hash(block).startswith("0" * self.leading_zeros_amount)  # проверяем что шеснадцатиричная запись содержит нужное количество нулей
        # майнеру нужно будет угадать число, при котором условие выше выполняется, это и считается доказательством работы. 

    @property
    def last_block(self):
        # вернет крайний в цепи блок
        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount, signature):
        transaction = {
            'sender': sender,  # отправитель денег
            'recipient': recipient,  # получатель денег
            'amount': amount,  # количество денег
            'signature': signature,  # цифровая подпись отправителя
            'timestamp': time()  # записываем время транзакции
        }
        self.pending_transactions.append(transaction)  # добавляем транзакцию в очередь
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        сериализуем блок, берем байтовое представление и хешируем его, 
        полученный хэш переводим в шестнадцатиричное представление
        """
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash
