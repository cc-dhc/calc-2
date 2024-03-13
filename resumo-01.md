# Resumo sobre integral
## Definição: $\int_{a}^{b} f(x) \, dx$

- $f(x)$ é o integrando
- $a$ é o limite inferior
- $b$ é o limite superior
- $dx$ indica é a variável a ser integrada é $x$

## Propriedades

- $\int_{a}^{b} f(x) \pm g(x) \, dx = \int_{a}^{b} f(x) \, dx \pm \int_{a}^{b} g(x) \, dx$
- $\int_{a}^{b} c \cdot f(x) \, dx = c \cdot \int_{a}^{b} f(x) dx$

*onde $c$ é uma constante*

- $\int x^n \, dx = \frac{x^{n+1}}{n+1} + C$
- $\int \frac{1}{x} \, dx = \ln{|x|} + C$
- $\int a^x \, dx = \frac{a^x}{\ln{a}} + C$
- $\int e^x \, dx = e^x + C$
- $\int \cos{(x)} \, dx = \sin{(x)} + C$
- $\int \sin{(x)} \, dx = -\cos{(x)} + C$
- $\int \sec^2{(x)} \, dx = \tan{(x)} + C$
- $\int \sec{(x)} \cdot \tan{(x)} \, dx = \sec{(x)} + C$

## Exemplos

- $\int 5 \cdot t^3 - 10 \cdot t^{-6} + 4 \, dt = 5 \cdot \frac{t^4}{4} - 10 \cdot \frac{t^{-5}}{-5} + C$
- $\int x^8 + x^{-8} \, dx = \frac{x^9}{9} + \frac{x^{-7}}{-7} + C$
- $\int \sqrt[4]{x^3} + \frac{7}{x^5} + \frac{1}{6\sqrt{x}} \, dx$
	- $\int x^{\frac{3}{4}} + 7\cdot x^{-5} + \frac{1}{6}\cdot x^{-\frac{1}{2}} \, dx$
	- $\frac{x^{\frac{7}{4}}}{\frac{7}{4}} + 7 \cdot \frac{x^{-4}}{-4} + \frac{1}{6} \cdot \frac{x^{\frac{1}{2}}}{\frac{1}{2}} + C$ 

## Regra da substituição

[Integral por substituição](https://pt.khanacademy.org/math/ap-calculus-ab/ab-integration-new/ab-6-9/a/review-applying-u-substitution)

Esse método funciona sempre que temos uma integral que possa ser escrita na forma:

$\int f(g(x))g'(x) \, dx = \int f(u) \, du$, $u=g(x)$

### Passo a Passo

1. Considere $u = g(x)$, onde $g(x)$ é parte do integrando, em geral *a função interna* da função composta $f(g(x))$
2. Calcule $du = g'(x) \, dx$
3. Use a substituição $u = g(x)$ e $du = g'(x) \, dx$ para converter a integral em uma outra envolvendo apenas $u$.
4. Calcule a integral resultante
5. Substitua $u$ por $g(x)$ para obter a solução final como função de $x$

### Exemplo

- $\int \sqrt{2x+1} \, dx$
	1. $u=g(x) = 2x+1$
	2. $du = 2x \, dx$
	3. $\int (u)^\frac{1}{2} \cdot  \, du$
	4. $\frac{u^{\frac{3}{2}}}{\frac{3}{2}} + C$


## Integral por partes

[Integral por partes](https://pt.khanacademy.org/math/ap-calculus-bc/bc-integration-new/bc-6-11/a/integration-by-parts-review)

$\int u(x) \cdot v(x) \, dx = u(x) \cdot v(x) - \int u'(x) \cdot v(x) \, dx$

$\int u \, dv = u \cdot v - \int v \, du$

Escolher o $u$ como polinômio quando possível, exceto $x^{-1}$ (verificar informação).
### Exemplo

- $\int \cos{x} \, dx$ 
	- $u=x$, $du=1\cdot dx$
	- $dv = \cos{x} \, dx$, $v = \sin{x}$
	- $u\cdot v - \int v \, du = x\cdot \sin{x} - \int \sin{x} \, dx$
	- $x\cdot \sin{x} - (-\cos{x}) + C = x\cdot \sin{x} \cdot \cos{x} + C$

