# SeedSearch.py

## This version of the tool has been customized to work with the [AnuBitux](https://anubitux.org) live system. To use it with other environments, please refer to the [main branch](https://github.com/ASeriousMister/SeedSearch.py)

A python tool that scans files in directories and subdirectories hunting BIP39 mnemonic seeds.
It is part of the bigger project Anu₿itux: more info at https://anubitux.org.


## Overview
It allows the user to provide a path and then scans all the files looking for sequencies of words that could be BIP39 mnemonic seeds. Then it checks if the found sequencies are valid mnemonic seeds and prints it in the output.
With seedsearchpro.py, when seeds are found, users can decide if they want to derive addresses and check if the seeds have been used.
At line 38 of seedsearchpro.py it is also possible to add a blockcypher API key to avoid reaching API limits
### Warning
Running issued could be encountered due to APIs limits. To check only a few seeds that could be more valuable, use [SeedCheck.py](https://github.com/ASeriousMister/SeedCheck.py)

## Tutorial
[Here](https://anubitux.org/search-for-bip39-seeds-with-anubitux/) you can see how the tool works.


## Supported derivations
The tool supports the following coins with the indicated derivation paths:
### Bitcoin
- BIP39
  * m/44'/0'/0'/0
  * m/44'/0'/0'/0' (hardened addresses)
  * m/49'/0'/0'/0
  * m/49'/0'/0'/0' (hardened addresses)
  * m/84'/0'/0'/0
  * m/84'/0'/0'/0' (hardened addresses)
  * m/84'/00/2147483645'/0'/0 (Samourai wallet Premix)
  * m/84'/00/2147483646'/0'/0 (Samourai wallet Postmix)
### Ethereum
- BIP39
  * m/44'/60'/0'/0
  * m/44'/60'/0'/0' (hardened addresses)
### Litecoin
- BIP39
  * m/44'/2'/0'/0
  * m/44'/2'/0'/0' (hardened addresses)
  * m/49'/2'/0'/0
  * m/49'/2'/0'/0' (hardened addresses)
  * m/84'/2'/0'/0
  * m/84'/2'/0'/0' (hardened addresses)
### Dash
- BIP39
  * m/44'/5'/0'/0
  * m/44'/5'/0'/0' (hardened addresses)
### ZCash
- BIP39
  * m/44'/133'/0'/0
  * m/44'/133'/0'/0' (hardened addresses)


## Read more
- [BIPs](https://github.com/bitcoin/bips)
- [HD wallet](https://pypi.org/project/hdwallet/)


## Disclaimer
SeedSearch.py aims to find seeds stored in files. Its cearch has not to be considered exhaustive, because mnemonic seeds can be easily hidden placed other words between the ones composing the mnemonic, scrambling letters, etc.

## Credits & Donations
If you appreciate this work visit https://anubitux.org and consider making a donation
- BTC: 1AnUbiYpuFsGrc1JFxFCh5K9tXFd1BXPg
- XMR: 87PTU58siKNb3WWXcP4Hq4CmCb7kMQUsEiUWFT7SvvMMUqVw9XXFGrJZqmnGvuJLGtLoRuEqovTG4SWqkPr8YLopTSxZkkL
