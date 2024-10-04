# Comparação de Valores Distintos de floor(N/i) para i=1 até N

### Descrição
Este projeto investiga a quantidade de valores distintos gerados pela função floor(N/i) à medida que i varia de 1 a N. O objetivo é identificar e analisar os padrões e a quantidade de valores únicos obtidos através dessa função.

### Metodologia
Serão implementados dois métodos para calcular a soma das divisões:

# LinearMethod: Este método itera de 1 a N, computando floor(N/i) e acumulando os resultados. A complexidade deste método é O(N), pois ele realiza uma operação em cada iteração.

# BestMethod: Este método utiliza uma abordagem mais eficiente ao identificar as repetições de valores de floor(N/i) em intervalos. A análise revela que a quantidade de iterações é significativamente reduzida, resultando em uma complexidade média de O(sqrt(N)) ou melhor, dependendo da distribuição dos valores.

### Comparação de Desempenho
A comparação entre os métodos será feita em termos de tempo de execução e a quantidade de valores distintos encontrados. Espera-se que o BestMethod apresente um desempenho superior, especialmente para valores maiores de N, demonstrando a importância de escolher algoritmos eficientes em problemas de grande escala.

Sinta-se à vontade para fazer ajustes ou adicionar informações conforme necessário!
