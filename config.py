from web3 import Web3

RPC_URL = "https://ethereum-sepolia.publicnode.com"
w3 = Web3(Web3.HTTPProvider(RPC_URL))

CONTRACT_ADDRESS = Web3.to_checksum_address(
    "0x200C98F103aFb52Da6edC36419A210D630E7bD73"
)

CONTRACT_ABI = [
    {
        "inputs": [{"internalType": "string","name": "_fileHash","type": "string"}],
        "name": "addRecord",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getMyRecords",
        "outputs": [
            {
                "components": [
                    {"internalType": "string","name": "fileHash","type": "string"},
                    {"internalType": "uint256","name": "timestamp","type": "uint256"}
                ],
                "internalType": "tuple[]",
                "name": "",
                "type": "tuple[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)
