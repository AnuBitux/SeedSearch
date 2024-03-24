#!/bin/bash
echo ' '
figlet SeedSearch
echo ' '
echo seedsearch.py is a python tool that scans all the files in a directory,
echo including subdirectories, looking for BIP39 mnemonic seeds
echo ''
echo seedsearchpro.py is also available: if users agree, it will also try to derive addresses with the found seeds
echo and check online if the addresses were used, trying to guess the right derivation path
echo ''
echo note that deriving lots of addresses could overload APIs
echo users that have a blockcypher API key can provide it editing the proper line in the file in /Tools/Recovery/SeesSearch.py/seedsearchpro.py
echo ''
echo example: seedsearch.py -d /home/anubitux/Documents
echo example: seedsearchpro.py -d /home/anubitux/Documents
echo ''

$SHELL
