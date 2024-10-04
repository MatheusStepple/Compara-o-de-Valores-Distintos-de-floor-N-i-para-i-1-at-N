# Comparação de Valores Distintos de `floor(N/i)` para `i=1` até `N`

### Descrição
Este projeto investiga a quantidade de valores distintos gerados pela função `floor(N/i)` à medida que `i` varia de 1 a `N`. O foco é identificar padrões na distribuição desses valores e quantificar a singularidade dos resultados. Essa análise é fundamental para o estudo de **algoritmos e estruturas de dados**, pois ajuda a entender a eficiência de diferentes abordagens para a resolução de problemas computacionais. Para mais detalhes, consulte a [questão no Math Stack Exchange](https://math.stackexchange.com/questions/1069460/how-many-distinct-values-of-floorn-i-exists-for-i-1-to-n).


### Metodologia
Para abordar a questão, serão implementados dois métodos distintos que calculam os valores de `floor(N/i)`:

#### 1. **LinearMethod**
- **Descrição**: Este método adota uma abordagem direta, iterando de 1 a `N` e computando `floor(N/i)` em cada iteração. Os resultados são acumulados em uma variável total.
- **Complexidade**: O tempo de execução deste método é O(N), pois realiza uma operação de divisão e uma operação de armazenamento em cada iteração. Este método é simples, mas pode ser ineficiente para valores elevados de `N`.

#### 2. **BestMethod**
- **Descrição**: Este método é mais sofisticado e otimizado. Em vez de iterar por todos os valores de `i`, ele identifica as repetições de `floor(N/i)` em intervalos. Ao agrupar os valores repetidos, o número de iterações é reduzido significativamente.
- **Complexidade**: A complexidade média deste método é O(sqrt(N)) ou melhor, dependendo da distribuição dos valores. Isso é alcançado ao explorar a natureza dos resultados de `floor(N/i)`, que se tornam menos variados à medida que `i` aumenta.

### Comparação de Desempenho
A avaliação do desempenho entre os dois métodos será baseada em dois critérios principais:
1. **Tempo de Execução**: Mediremos o tempo que cada método leva para processar valores crescentes de `N`.
2. **Quantidade de Valores Distintos**: Contabilizaremos quantos valores distintos são gerados por cada método.

### Expectativas
Espera-se que o **BestMethod** demonstre um desempenho significativamente superior em comparação ao **LinearMethod**, especialmente em escalas maiores de `N`. Este projeto destaca a importância de algoritmos eficientes e otimizações em cenários onde a complexidade computacional pode ser um fator limitante.

### Conclusão
Através deste projeto, buscamos não apenas calcular os valores de `floor(N/i)`, mas também oferecer uma compreensão mais profunda sobre a eficiência dos algoritmos e a análise de complexidade. Os resultados poderão servir como referência para futuros trabalhos em otimização de algoritmos e análise de desempenho.

### Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou um pull request para sugestões de melhorias, correções ou novas funcionalidades.
