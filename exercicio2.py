#Turma 8 - Otto Bernardo Coutinho Lima

#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui

def is_anagram(string1, string2):
    string1 = string1.lower().replace(" ", "")
    string2 = string2.lower().replace(" ", "")
    return sorted(string1) == sorted(string2)

# Teste a sua função aqui (caso ache necessário)











