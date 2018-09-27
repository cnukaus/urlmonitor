import difflib
#from difflib_data import *


text1_lines="['SOPBTC', 'VITEBCH', 'TRXETH', 'SEERBTC', 'CETBTC', 'DOGEBTC', 'LFTBTC', 'KANETH', 'LTCBTC', 'VITEETH', 'QTUMBTC', 'ETHBCH', 'MGDBTC', 'LFTBCH', 'EOSUSDT', 'WINGSBTC', 'THPCETH', 'VETETH', 'ETHBTC', 'LTCBCH', 'BBNBTC', 'OLTETH', 'XMVBCH'"
text2_lines="['TRXETH', 'SEERBTC', 'CETBTC', 'DOGEBTC', 'LFTBTC', 'KANETH', 'LTCBTC', 'VITEETH', 'QTUMBTC', 'ETHBCH', 'MGDBTC', 'LFTBCH', 'EOSUSDT', 'WINGSBTC', 'THPCETH', 'VETETH', 'ETHBTC', 'LTCBCH', 'BBNBTC', 'OLTETH', 'XMVBCH'"
d = difflib.Differ()
#diff = d.compare(text1_lines, text2_lines)
diff = difflib.unified_diff(
    text1_lines,
    text2_lines,
    #lineterm='',
)
#print(diff)
print(''.join(diff))