# Documentação

Esta pasta descreve o experimento mantido neste repositório.

- [Objetivo](objetive.md): escopo e propósito do projeto.
- [Arquitetura](architecture.md): componentes, execução e limitações atuais.
- [Fluxo](diagrams.md): representação visual da execução do script.

## Executar o experimento

Na raiz do repositório, com Python 3 instalado, execute:

```bash
python3 src/test_cpu.py
```

O programa imprime a soma de `range(10_000_000)` e o tempo decorrido em segundos. O tempo serve apenas como observação local; não representa uma medição comparável entre máquinas ou execuções sem controles adicionais.
