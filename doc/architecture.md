# Arquitetura

## Estado atual

O repositório é um experimento mínimo de desempenho em Python. O arquivo `src/test_cpu.py` executa um cálculo em memória e mede quanto tempo ele leva usando o relógio monotônico de alta precisão de `time.perf_counter()`.

```text
src/test_cpu.py
  ├─ inicia a medição
  ├─ calcula sum(range(10_000_000))
  ├─ encerra a medição
  └─ imprime o resultado e o tempo decorrido
```

Não há módulos próprios, dependências externas, configuração de build, persistência de dados nem interface de rede. O script usa apenas a biblioteca padrão do Python.

## Fluxo de execução

1. O interpretador importa `time`.
2. `perf_counter()` registra o instante inicial.
3. `sum(range(10_000_000))` soma os inteiros de 0 a 9.999.999.
4. Uma segunda chamada a `perf_counter()` fornece o instante final; a diferença é apresentada em segundos com três casas decimais.
5. O total calculado também é impresso.

O resultado esperado da soma é `49999995000000`. O tempo depende do hardware, da versão do Python, da carga do sistema e do ambiente de execução; portanto, uma execução isolada não é um benchmark controlado.

## Estrutura

| Caminho | Finalidade |
| --- | --- |
| `src/test_cpu.py` | Experimento simples de cálculo e cronometragem. |
| `README.md` | Visão geral e instruções rápidas do repositório. |
| `doc/` | Documentação detalhada do objetivo, arquitetura e fluxo. |

## Limitações conhecidas

- A medição cobre apenas a soma e não inclui inicialização do interpretador.
- Não há repetição, aquecimento, controle de carga ou comparação entre implementações.
- O nome `time` é usado para guardar a duração, ocultando o módulo importado após a medição. Isso não impede a execução atual, mas seria melhor usar um nome como `elapsed` se o script crescer.
- O arquivo é um script executável diretamente, não uma biblioteca nem uma suíte formal de testes.
