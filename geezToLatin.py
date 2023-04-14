def convert(s):
    mapping = {'ሀ': 'Hä', 'ሁ': 'Hu', 'ሂ': 'Hi', 'ሃ': 'Ha', 'ሄ': 'He', 'ህ': 'H', 'ሆ': 'Ho',
               'ለ': 'Lä', 'ሉ': 'Lu', 'ሊ': 'Li', 'ላ': 'La', 'ሌ': 'Le', 'ል': 'L', 'ሎ': 'Lo',
               'ሐ': 'Hä', 'ሑ': 'Hu', 'ሒ': 'Hi', 'ሓ': 'Hā', 'ሔ': 'He', 'ሕ': 'H', 'ሖ': 'Ho',
               'መ': 'Mä', 'ሙ': 'Mu', 'ሚ': 'Mi', 'ማ': 'Ma', 'ሜ': 'Me', 'ም': 'M', 'ሞ': 'Mo',
               'ሠ': 'Sä', 'ሡ': 'Su', 'ሢ': 'Si', 'ሣ': 'Sa', 'ሤ': 'Se', 'ሥ': 'S', 'ሦ': 'So',
               'ረ': 'Rä', 'ሩ': 'Ru', 'ሪ': 'Ri', 'ራ': 'Ra', 'ሬ': 'Re', 'ር': 'R', 'ሮ': 'Ro',
               'ሰ': 'Sä', 'ሱ': 'Su', 'ሲ': 'Si', 'ሳ': 'Sa', 'ሴ': 'Se', 'ስ': 'S', 'ሶ': 'So',
               'ሸ': 'Ŝä', 'ሹ': 'Ŝu', 'ሺ': 'Ŝi', 'ሻ': 'Ŝa', 'ሼ': 'Ŝe', 'ሽ': 'Ŝ', 'ሾ': 'Ŝo',
               'ቀ': 'Qä', 'ቁ': 'Qu', 'ቂ': 'Qi', 'ቃ': 'Qa', 'ቄ': 'Qe', 'ቅ': 'Q', 'ቆ': 'Qo',
               'በ': 'Bä', 'ቡ': 'Bu', 'ቢ': 'Bi', 'ባ': 'Ba', 'ቤ': 'Be', 'ብ': 'B', 'ቦ': 'Bo',
               'ተ': 'Tä', 'ቱ': 'Tu', 'ቲ': 'Ti', 'ታ': 'Ta', 'ቴ': 'Te', 'ት': 'T', 'ቶ': 'To',
               'ቸ': 'Čä', 'ቹ': 'Ču', 'ቺ': 'Či', 'ቻ': 'Ča', 'ቼ': 'Če', 'ች': 'Č', 'ቾ': 'Čo',
               'ኀ': 'Hä', 'ኁ': 'Hu', 'ኂ': 'hi', 'ኃ': 'Ha', 'ኄ': 'He', 'ኅ': 'H', 'ኆ': 'ho',
               'ነ': 'Nä', 'ኑ': 'Nu', 'ኒ': 'Ni', 'ና': 'Na', 'ኔ': 'Ne', 'ን': 'N', 'ኖ': 'No',
               'ኘ': 'Ñä', 'ኙ': 'Ñu', 'ኚ': 'Ñi', 'ኛ': 'Ña', 'ኜ': 'Ñe', 'ኝ': 'Ñ', 'ኞ': 'Ño',
               'አ': 'ä', 'ኡ': 'u', 'ኢ': 'i', 'ኣ': 'a', 'ኤ': 'é', 'እ': 'e', 'ኦ': 'o',
               'ከ': 'Kä', 'ኩ': 'Ku', 'ኪ': 'Ki', 'ካ': 'Ka', 'ኬ': 'Ke', 'ክ': 'K', 'ኮ': 'Ko',
               'ኸ': 'Xä', 'ኹ': 'Xu', 'ኺ': 'Xi', 'ኻ': 'Xa', 'ኼ': 'Xe', 'ኽ': 'X', 'ኾ': 'Xo',
               'ወ': 'Wä', 'ዉ': 'Wu', 'ዊ': 'Wi', 'ዋ': 'Wa', 'ዌ': 'We', 'ው': 'W', 'ዎ': 'Wo',
               'ዐ': 'Aä', 'ዑ': 'Au', 'ዒ': 'Ai', 'ዓ': 'Aā', 'ዔ': 'Aé', 'ዕ': 'A', 'ዖ': 'Ao',
               'ዘ': 'Zä', 'ዙ': 'Zu', 'ዚ': 'Zi', 'ዛ': 'Za', 'ዜ': 'Ze', 'ዝ': 'Z', 'ዞ': 'Zo',
               'ዠ': 'Žä', 'ዡ': 'Žu', 'ዢ': 'Ži', 'ዣ': 'Ža', 'ዤ': 'Žw', 'ዥ': 'Ž', 'ዦ': 'Žo',
               'የ': 'Yä', 'ዩ': 'Yu', 'ዪ': 'Yi', 'ያ': 'Ya', 'ዬ': 'Ye', 'ይ': 'Y', 'ዮ': 'Yo',
               'ደ': 'Dä', 'ዱ': 'Du', 'ዲ': 'Di', 'ዳ': 'Da', 'ዴ': 'De', 'ድ': 'D', 'ዶ': 'Do',
               'ጀ': 'Ğä', 'ጁ': 'Ğu', 'ጂ': 'Ği', 'ጃ': 'Ğa', 'ጄ': 'Ğe', 'ጅ': 'Ğ', 'ጆ': 'Ğo',
               'ገ': 'Gä', 'ጉ': 'Gu', 'ጊ': 'Gi', 'ጋ': 'Ga', 'ጌ': 'Ge', 'ግ': 'G', 'ጎ': 'Go',
               'ጠ': 'Ṭä', 'ጡ': 'Ṭu', 'ጢ': 'Ṭi', 'ጣ': 'Ṭa', 'ጤ': 'Ṭe', 'ጥ': 'Ṭ', 'ጦ': 'Ṭo',
               'ጨ': 'Ċä', 'ጩ': 'Ċu', 'ጪ': 'Ċi', 'ጫ': 'Ċa', 'ጬ': 'Ċe', 'ጭ': 'Ċ', 'ጮ': 'Ċo',
               'ጰ': 'P̣ä', 'ጱ': 'P̣u', 'ጲ': 'P̣i', 'ጳ': 'P̣a', 'ጴ': 'P̣a', 'ጵ': 'P̣', 'ጶ': 'P̣o',
               'ጸ': 'Ṣä', 'ጹ': 'Ṣu', 'ጺ': 'Ṣi', 'ጻ': 'Ṣa', 'ጼ': 'Ṣe', 'ጽ': 'Ṣ', 'ጾ': 'Ṣo',
               'ፀ': 'Ṡä', 'ፁ': 'Ṡu', 'ፂ': 'Ṡi', 'ፃ': 'Ṡa', 'ፄ': 'Ṡe', 'ፅ': 'Ṡ', 'ፆ': 'Ṡo',
               'ፈ': 'Fä', 'ፉ': 'Fu', 'ፊ': 'Fi', 'ፋ': 'Fa', 'ፌ': 'Fe', 'ፍ': 'F', 'ፎ': 'Fo',
               'ፐ': 'Pä', 'ፑ': 'Pu', 'ፒ': 'Pi', 'ፓ': 'Pa', 'ፔ': 'Pe', 'ፕ': 'P', 'ፖ': 'Po',
               'ቨ': 'Vä', 'ቩ': 'Vu', 'ቪ': 'Vi', 'ቫ': 'Va', 'ቬ': 'Ve', 'ቭ': 'V', 'ቮ': 'Vo'
               }
    return ''.join(mapping.get(x, x) for x in s)