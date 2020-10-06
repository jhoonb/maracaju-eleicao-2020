Eleição 2020 - Maracaju, Mato Grosso do Sul
=

[*em desenvolvimento...*]


Dados sobre os candidatos
==

**Fonte dos dados:** [Repositório de dados eleitorais - TSE](http://www.tse.jus.br/hotsites/pesquisas-eleitorais/candidatos.html).


Análise (SQL - banco de dados SQLITE)
===


**Candidatos por cargo**


```sql
select c.CARGO, count(*) as QUANTIDADE from candidato c
GROUP by c.CARGO 
order by quantidade desc
```

---- 


**Candidatos por sexo**

```sql
select c.SEXO, count(*) as QUANTIDADE from candidato c
GROUP by c.SEXO 
order by QUANTIDADE desc
```

----


**Candidatos por partido (TODOS)**

```sql
select c.sigla_partido, count(*) as quantidade from candidato c 
group by c.sigla_partido
order by quantidade DESC
```

**Candidatos por partido (MASCULINO)**

```sql
select c.sigla_partido, count(*) as quantidade from candidato c 
where c.sexo like 'MASCULINO'
group by c.sigla_partido
order by quantidade DESC
```


**Candidatos por partido (FEMININO)**

```sql
select c.sigla_partido, count(*) as quantidade from candidato c 
where c.sexo like 'FEMININO'
group by c.sigla_partido
order by quantidade DESC
```

----


**Candidatos por ocupação (todos e no mínimo 2 candidatos por ocupação)** 
as ocupações com apenas 1 candidato serão agrupados e somados a ocupação "outros".

```sql
select c.OCUPACAO, count(*) as quantidade from candidato c
group by c.OCUPACAO
HAVING COUNT(*) >= 2
order by quantidade desc
```

**Candidatos por ocupação (MASCULINO e no mínimo 2 candidatos por ocupação)** 
as ocupações com apenas 1 candidato serão agrupados e somados a ocupação "outros".

```sql
select c.OCUPACAO, count(*) as quantidade from candidato c
group by c.OCUPACAO
HAVING COUNT(*) >= 2
order by quantidade desc
```

**Candidatos por ocupação (FEMININO e no mínimo 2 candidatos por ocupação)** 
as ocupações com apenas 1 candidato serão agrupados e somados a ocupação "outros".

```sql
select c.OCUPACAO, count(*) as quantidade from candidato c
where c.sexo like "FEMININO"
group by c.OCUPACAO
HAVING COUNT(*) >= 2
order by quantidade desc
```

----


**Candidatos por Grau de instrução (todos)**

```sql
select c.GRAU_INSTRUCAO, count(*) as quantidade from candidato c 
group by c.GRAU_INSTRUCAO
order by quantidade desc
```

**Candidatos por Grau de instrução (masculino)**

```sql
select c.GRAU_INSTRUCAO, count(*) as quantidade from candidato c 
where c.sexo like 'MASCULINO'
group by c.GRAU_INSTRUCAO
order by quantidade desc
```

**Candidatos por Grau de instrução (feminino)**

```sql
select c.GRAU_INSTRUCAO, count(*) as quantidade from candidato c 
where c.sexo like 'FEMININO'
group by c.GRAU_INSTRUCAO
order by quantidade desc
```

----

**Candidatos por Estado Civil (todos)**

```sql
select c.
select c.ESTADO_CIVIL, count(*) as quantidade from candidato c 
group by c.ESTADO_CIVIL
order by quantidade desc
```


**Candidatos por Estado Civil (masculino)**

```sql
select c.
select c.ESTADO_CIVIL, count(*) as quantidade from candidato c 
where c.sexo like "MASCULINO"
group by c.ESTADO_CIVIL
order by quantidade desc
```

**Candidatos por Estado Civil (masculino)**

```sql
select c.
select c.ESTADO_CIVIL, count(*) as quantidade from candidato c 
where c.sexo like "FEMININO"
group by c.ESTADO_CIVIL
order by quantidade desc
``` 

----

**Candidatos por COR/RAÇA (todos)**

```sql
select c.COR_RACA, count(*) as quantidade from candidato c 
group by c.COR_RACA
order by quantidade desc
```

**Candidatos por COR/RAÇA (masculino)**

```sql
select c.COR_RACA, count(*) as quantidade from candidato c 
where c.sexo like "MASCULINO"
group by c.COR_RACA
order by quantidade desc
```

**Candidatos por COR/RAÇA (feminino)**

```sql
select c.COR_RACA, count(*) as quantidade from candidato c 
where c.sexo like "FEMININO"
group by c.COR_RACA
order by quantidade desc
```

----

**Candidatos por composição da coligação (todos)**

```sql
select c.COMPOSICAO_COLIGACAO, count(*) as quantidade from candidato c 
group by c.COMPOSICAO_COLIGACAO
order by quantidade desc
```

**Candidatos por composição da coligação (masculino)**

```sql
select c.COMPOSICAO_COLIGACAO, count(*) as quantidade from candidato c 
where c.SEXO like "MASCULINO"
group by c.COMPOSICAO_COLIGACAO
order by quantidade desc
```

**Candidatos por composição da coligação (feminino)**

```sql
select c.COMPOSICAO_COLIGACAO, count(*) as quantidade from candidato c 
where c.SEXO like "FEMININO"
group by c.COMPOSICAO_COLIGACAO
order by quantidade desc
```

## TODO


- [ ] adicionar e relacionar as fotos (no index.html)

- [ ] tabela com filtro dos dados (json / js frontend)

- [ ] adicionar ao banco sqlite os bens dos candidatos

- [ ] organizar os gráficos