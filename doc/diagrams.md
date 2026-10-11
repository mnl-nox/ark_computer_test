# Fluxo de execução

O diagrama mostra o caminho percorrido por `src/test_cpu.py` ao ser executado:

```mermaid
flowchart TD
    A[Iniciar test_cpu.py] --> B[Registrar instante inicial com perf_counter]
    B --> C[Somar os inteiros de 0 a 9.999.999]
    C --> D[Calcular duração com perf_counter]
    D --> E[Imprimir soma]
    E --> F[Imprimir duração em segundos]
```

Não há entrada do usuário ou saída em arquivo: ambos os valores são escritos na saída padrão do processo.
