# 🗺 Web3 Roadmap

A roadmap for [Web3](https://en.wikipedia.org/wiki/Web3) development, divided into three steps.

## 🖋 Step 1 - Solidity Smart Contract

In this first step, we will implement a basic [Solidity](https://soliditylang.org/) smart contract.

`Motivation`: Centralized identity systems often suffer from vulnerabilities such as single points of failure (SPOF), lack of transparency in data handling, limited user control, high operational costs, inefficiencies, and risks of censorship.

`Proposal`: Suppose you want to create a decentralized application (DApp) to securely and transparently manage user identities on the blockchain, thereby avoiding these vulnerabilities.

So, we created the [Identity Manager](https://github.com/MiguelHenri/Web3-Roadmap/blob/main/code/IdentityManager.sol) smart contract to store these decentralized identifiers (DIDs). 
> You can try it out on [Remix ETH](https://remix.ethereum.org/).

## 🔗 Step 2 - Hyperledger Besu Private Blockchain

In the second step, we will run a private blockchain using [Hyperledger Besu](https://besu.hyperledger.org/private-networks). We will also deploy our smart contract on this new network.

## ⚙ Step 3 - Transactions using Web3.py

In the final step, we will interact with our smart contract using the [Web3.py](https://web3py.readthedocs.io/en/stable/) library. 