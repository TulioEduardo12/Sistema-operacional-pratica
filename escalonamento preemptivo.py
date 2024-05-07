print("========================começa aqui====================================")
print("")

#input
num_processos = int(input("Digite o número de processos: "))
processos = []

# loop input
for i in range(num_processos):
    pid = i + 1  
    prioridade = int(input(f"Digite a prioridade para o processo P{pid}: "))
    tempo_cpu = int(input(f"Digite o tempo de CPU para o processo P{pid}: "))
    processo = {"pid": pid, "prioridade": prioridade, "tempo_cpu": tempo_cpu, "tempo_cpu_original": tempo_cpu}
    processos.append(processo)

print("")
# Ordena a lista de processos com base na prioridade
processos.sort(key=lambda x: x['prioridade'])


quantum = 2
tempo_total_turnaround = 0
tempo_total_espera = 0
tempo_atual = 0

# loop de processos
while processos:
    # pop = remover da lista
    processo_atual = processos.pop(0)
    print(f"Executando P{processo_atual['pid']} - Prioridade: {processo_atual['prioridade']}, Tempo de CPU: {processo_atual['tempo_cpu']}")
    
    # calculo
    fatia_tempo = min(quantum, processo_atual['tempo_cpu'])
    processo_atual['tempo_cpu'] -= fatia_tempo
    tempo_atual += fatia_tempo

    # verifica i tempo do processo
    if processo_atual['tempo_cpu'] > 0:
        
        print(f"P{processo_atual['pid']} foi iniciado. Tempo de CPU restante: {processo_atual['tempo_cpu']}")
        print("-" * 50)  # Linha divisória
        #append = adiciona a lista
        processos.append(processo_atual)
    else:
        # se acabar o tempo
        tempo_turnaround = tempo_atual  # O tempo de turnaround é o tempo atual
        tempo_espera = tempo_turnaround - processo_atual['tempo_cpu_original']  # O tempo de espera é o tempo de turnaround menos o tempo de CPU original
        tempo_total_turnaround += tempo_turnaround
        tempo_total_espera += tempo_espera
        # Imprime informações sobre o término do processo.
        print(f"P{processo_atual['pid']} concluído. Tempo de Turnaround: {tempo_turnaround}, Tempo de Espera: {tempo_espera}")
        print("-" * 50)  # Linha divisória

# Calcula os tempos médios de turnaround e espera.
tempo_medio_turnaround = tempo_total_turnaround / num_processos if num_processos > 0 else 0
tempo_medio_espera = tempo_total_espera / num_processos if num_processos > 0 else 0

# Imprime os tempos médios de turnaround e espera.
print(f"Tempo Médio de Turnaround: {tempo_medio_turnaround}")
print(f"Tempo Médio de Espera: {tempo_medio_espera}")
print("")

# Esta linha imprime uma linha divisória indicando o fim da execução do código.
print("========================termina aqui====================================")
