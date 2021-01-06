n, m = map(int, input().split()) 
plainText = input()[::-1] 
cipherText = list(input()[::-1]) 
m_i = 0 
johnsDiary = [] 
while m_i < n: 
    decrypt = ((ord(cipherText[m_i]) - ord(plainText[m_i])) % 26 + 97) 
    johnsDiary.append(decrypt) 
    cipherText[m_i] = plainText[m_i] 
    m_i += 1 
while m_i < m: 
    decrypt = ((ord(cipherText[m_i]) - johnsDiary[m_i - n]) % 26 + 97) 
    johnsDiary.append(decrypt) 
    cipherText[m_i] = chr(johnsDiary[m_i - n]) 
    m_i += 1 
print(''.join((cipherText)[::-1]))
