from time import time

from include import Blockchain


def find_proof_of_work(blockchain, block):
    """YOUR CODE"""
    # можно менять proof вот так: block['proof'] = 123
    # можно проверить proof вот так: blockchain.block_proves_work(block)
    proof = "YOUR CODE"
    return proof


if __name__ == '__main__':
    blockchain = Blockchain(leading_zeros_amount=5)
    t1 = blockchain.new_transaction("Satoshi", "Mike", '5 BTC', "4hr2r87")
    t2 = blockchain.new_transaction("Mike", "Satoshi", '1 BTC', "osd434n")
    t3 = blockchain.new_transaction("Satoshi", "Alex", '5 BTC', "84j9ff8")
    block = blockchain.new_block()
    begin = time()
    proof = find_proof_of_work(blockchain, block)
    end = time()
    diff = end - begin
    block["proof"] = proof
    success = blockchain.add_block(block)
    assert success
    print(f"Хорошая работа! Время поиска доказательства работы - {diff}")
