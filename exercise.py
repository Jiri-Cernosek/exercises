SourceStr = str(input("Zadej řetězec znaků ke spočítání: "))
pocet = 0
nejdelsi_znak = 0
predchozi = ""
for znak in SourceStr:
    if znak in predchozi:
        pocet += 1
    else:
        predchozi = znak
        if pocet > nejdelsi_znak:
            nejdelsi_znak = pocet
            pocet = 1
if pocet > nejdelsi_znak:
    nejdelsi_znak = pocet
Result = nejdelsi_znak
print("V zadaném řetězci je maximálně {} stejných znaků ihned za sebou" .format(Result))
                  
  
s = list(input("Zadej čísla k seřazení: "))
for i in range(len(s)):
    for a in range(0, len(s) - i - 1):
        if s[a] > s[a + 1]:
            s[a], s[a + 1] = s[a + 1], s[a]
print(s)