class DoubleLinkedLit:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def remover_ultima_ocorrencia(self, valor):
        aux = self.head
        num_ocorrencias = 0
        while aux != None:
            if aux.data == valor:
                num_ocorrencias += 1
                if aux.next != None:
                    aux = aux.next
                else:
                    break
            else:
                if aux.next != None:
                    aux = aux.next
                else:
                    break

        if num_ocorrencias > 0:
            ocorrencia_num = 0
            aux = self.head
            while ocorrencia_num < num_ocorrencias:
                if aux.data == valor:
                    ocorrencia_num += 1
                    if aux.next != None and ocorrencia_num < num_ocorrencias:
                        aux = aux.next
                    elif ocorrencia_num == num_ocorrencias and aux.next != None:
                        aux.prev.next = aux.next
                        aux.next.prev = aux.prev
                    elif ocorrencia_num == num_ocorrencias and aux.next == None:
                        aux.prev.next = aux.next
                else:
                    if aux.next != None:
                        aux = aux.next
        else:
            print("Não existe ocorrência desse valor na lista!")
            
                


    def verificar_duplicatas(self):
        aux = self.head
        duplicata = False
        while aux != None:
            proximo_no = aux.next
            while proximo_no != None:
                if aux.data == proximo_no.data:
                    duplicata = True
                    return duplicata
                else:
                    duplicata = False
                    proximo_no = proximo_no.next
            aux = aux.next
        return duplicata


    def percorre_inversa(self):
        aux = self.tail
        nos_percorridos = []
        while aux != None:
            nos_percorridos.append(aux.data)
            aux = aux.prev
        return nos_percorridos

    def tamanho_lista(self):
        aux = self.head
        tamanho = 0
        while aux != None:
            tamanho +=1
            aux = aux.next
        print(tamanho)
    
    def retorna_maior(self):
    #nil, h20, 5, 30, 40t, nil
    #pegar o 20, verificar se é maior que o 5, se for maior que o 5, 20 continua sendo o maior, se não for, 5 será o maior!
    #5 não é maior, 20 continua sendo o valor maior
    #pegar o valor maior (20) e verificar se o 20 é maior que o 30, se for maior que o 30, 20 continua sendo o maior, se não for, 30 será o maior!
    #30 é maior que 20, 30 é o novo maior
        if self.head != None:
            aux = self.head
            proximo_no = aux.next
            valor_maior = aux
            while(proximo_no != None):
                if aux.data < proximo_no.data:
                    aux = valor_maior.next
                    valor_maior = proximo_no
                elif aux.data >= proximo_no.data:
                    proximo_no = proximo_no.next
                    valor_maior = aux
            print(valor_maior.data)
        else:
            print("Lista vazia, não existe valor maior!")

    def retorna_menor(self):
        if self.head != None: 
            aux = self.head
            proximo_no = aux.next
            valor_menor = None
            while(proximo_no != None):
                if aux.data > proximo_no.data:
                    aux = aux.next
                    valor_menor = proximo_no
                elif aux.data <= proximo_no.data:
                    proximo_no = proximo_no.next
                    valor_menor = aux
            print(valor_menor.data)
        else:
            print("Lista vazia, não existe valor menor!")
    
    


    def percorre(self):
        aux = self.head
        while aux != None:
            print(aux.data)
            aux = aux.next
        print("NIL")
    
    def busca_valor_comeco(self, valor):
        aux = self.head
        while aux != None and aux.data != valor:
            aux = aux.next
        return aux
    
    def busca_valor_final(self, valor):
        aux = self.tail
        while aux != None and aux.data != valor:
            aux = aux.prev
        return aux

    def insere_comeco(self, valor):
        novoNo = Node(data=valor)
        novoNo.next = self.head
        novoNo.prev = None
        if self.head != None:
            self.head.prev = novoNo
        else:
            self.tail = novoNo
        self.head = novoNo

    def insere_final_1(self, valor):
        novoNo = Node(data=valor)
        novoNo.prev = self.tail
        novoNo.next = None
        self.tail.next = novoNo #o que acontece quando a lista estiver vazia?
        if self.tail == None:
            self.head = novoNo
        self.tail = novoNo
    
    def insere_final_2(self, valor):
        novoNo = Node(data=valor)
        novoNo.prev = self.tail
        novoNo.next = None
        if self.tail != None:
            self.tail.next = novoNo
        else:
            self.head = novoNo
        self.tail = novoNo
    
    def remove_comeco(self):
        if self.head != None:
            self.head = self.head.next
            if self.head == None:
                self.tail = self.head
                return
            self.head.prev = None
    
    def remove_final(self):
        if self.tail != None:
            self.tail = self.tail.prev
            if self.tail == None:
                self.head = self.tail
                return
            self.tail.next = None
    def remove_valor(self, valor):
        if self.head.data == valor:
            self.remove_comeco()
        elif self.tail.data == valor:
            self.remove_final()
        else:
            aux = self.head
            while aux != None and aux.data != valor:
                aux = aux.next
            if aux != None:
                aux.prev.next = aux.next
                aux.next.prev = aux.prev

    
class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data

minhaLista = DoubleLinkedLit()
'''minhaLista.insere_comeco(5)
minhaLista.insere_comeco(10)
minhaLista.insere_final_2(30)
minhaLista.insere_final_2(40)
minhaLista.remove_valor(10)
minhaLista.insere_comeco(20)
minhaLista.insere_comeco(20)
minhaLista.insere_final_2(20)
minhaLista.insere_final_2(30)
minhaLista.insere_final_2(20)
minhaLista.insere_final_2(50)
minhaLista.percorre()
print("\n")
minhaLista.remover_ultima_ocorrencia(20)
minhaLista.percorre()'''
print("aaaa")
minhaLista.busca_valor_comeco(10)
minhaLista.insere_comeco(10)
minhaLista.busca_valor_final(10)
'''minhaLista.retorna_maior()
minhaLista.retorna_menor()
print("tamanho: ")
minhaLista.tamanho_lista()
for i in minhaLista.percorre_inversa():
    print(i)'''





