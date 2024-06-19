# Selection-sort
```
def ordenada(vetor):
    vet = []
    fim = len(vetor)
    for i in range(fim):
        minimo = i
        for j in range(i + 1, fim):
            if vetor[j] < vetor[minimo]:
                minimo = j
            
        vet.append(vetor[minimo])
        vetor[minimo] = vetor[i]
        
    if vet == vetor:
        return True
    else:
        return False
               
```
